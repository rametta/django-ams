from django import forms
from gallery.models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = (
            'title',
            'description',
            'image',
        )