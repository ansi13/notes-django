from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note

# Create your views here.

from .forms.login_form import UserLoginForm
from .forms.notes_form import NotesForm


class UserLoginView(View):
    """
     Logs author into dashboard.
    """
    template_name = 'login.html'
    context_object = {"login_form": UserLoginForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = UserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('user_home')

            else:
                return render(request, self.template_name, self.context_object)

        else:
            messages.error(request, f"Invalid username and password")
            return render(request, self.template_name, self.context_object)


class UserLogoutView(View):
    """
     Logs user out of the dashboard.
    """
    template_name = 'logout.html'

    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return render(request, self.template_name)


def index(request):
    return render(request, 'index.html')


class NotesView(LoginRequiredMixin, View):
    login_url = '/notes/login'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            query_set = Note.objects.filter(author=request.user)
            return render(request, template_name='home.html', context={'notes': query_set})
        else:
            return redirect('login')


class NotesCreateView(LoginRequiredMixin, View):
    login_url = '/notes/login'
    context_object = {"notes_form": NotesView}

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, template_name='create.html', context={"notes_form": NotesForm})

    def post(self, request):
        notes_form = NotesForm(data=request.POST)

        if notes_form.is_valid():
            title = notes_form.cleaned_data['title']
            text = notes_form.cleaned_data['text']

            if request.user.is_authenticated:
                new_note = Note(title=title,
                                text=text,
                                author=request.user)
                new_note.save()
                return redirect('user_home')

            else:
                messages.error(request,
                               f"Invalid Login details. Please "
                               f"enter a valid username and password.")
                return render(request, self.template_name, self.context_object)

        else:
            messages.error(request, f"Invalid username and password")
            return render(request, self.template_name, self.context_object)
