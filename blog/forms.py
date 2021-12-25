from django import forms
from django.forms import ModelForm

from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import CharField, Form, PasswordInput



# Create your forms here.

class PostForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(PostForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class PostForm1(UserCreationForm):
	class Meta:
		model=User
		fields = ("username", "password")




class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


