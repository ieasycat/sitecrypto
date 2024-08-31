from django import forms
from .models import Crypto


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Crypto
        fields = '__all__'
