import django.forms as forms
from .models import PractitionerModel


class PractitionerForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PractitionerModel
        fields = ('identifier', 'name', 'birthdate', 'gender', 'home_address', 'telecom', 'practitioner_role', 'qualification')
        
        
