from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import util


class NewPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data.lower() in [entry.lower() for entry in util.list_entries()]:
            raise ValidationError(
                _("Encyclopedia page for '%(value)s' has already existed"),
                params={"value": data},
            )
        return data


class EditPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
