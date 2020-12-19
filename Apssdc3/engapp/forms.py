from django import forms
from engapp.models import Register


class regform(forms.ModelForm):

    class Meta:
        model = Register
        fields = '__all__'
