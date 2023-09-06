from WebApp.models import ClassModel
from django import forms

class StudForm(forms.ModelForm):
    class Meta:
        model=ClassModel
        fields='__all__'