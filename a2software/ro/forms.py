from django import forms
from .models import Emails


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = Emails

        fields = [
            "form_subject",
            "form_name",
            "form_email",
            "form_phone",
            "form_message",
        ]
