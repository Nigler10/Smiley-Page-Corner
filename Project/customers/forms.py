from django import forms
from .models import CustomerPreference

class CustomerPreferenceForm(forms.ModelForm):
    class Meta:
        model = CustomerPreference
        fields = [
            "name",
            "favorite_flavor",
            "preferred_size",
            "notes",
        ]
