from django import forms
from .models import Log


class IssueLogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ["client_name", "issue_description"]