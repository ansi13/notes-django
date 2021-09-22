from django import forms


class NotesForm(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={
            "name": "title",
            "placeholder": "Title"
        }))

    text = forms.CharField(widget=forms.Textarea(attrs={
            "name": "text",
            "placeholder": "Text"
        }))
