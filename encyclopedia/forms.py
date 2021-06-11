from django import forms
from django.core.exceptions import ValidationError
from . import util


class NewPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data.lower() in [entry.lower() for entry in util.list_entries()]:
            raise ValidationError("This entry has already existed")
        return data
