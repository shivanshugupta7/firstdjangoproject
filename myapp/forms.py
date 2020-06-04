from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.core.validators import validate_email
# all the fields

class EmployeeForm(forms.ModelForm):
    # ename=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['eid','ename','eemail','econtact','profile_image']
    def clean_eid(self):  # Validates the Computer Name Field
        eid = self.cleaned_data.get('eid')
        if (eid == ""):
            raise forms.ValidationError('This field cannot be left blank')
        return self.cleaned_data['eid']

