from django import forms

from .models import Person , Ad


class PostForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('name', 'price', 'img')

