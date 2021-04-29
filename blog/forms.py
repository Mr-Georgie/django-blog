from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Post, Comment

class AddNewPostForm(ModelForm):
	title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

	class Meta:
		model = Post
		fields = ("title", "author", "body",)
  
  
# Create comment views here.
class CommentForm(ModelForm):
	comment_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
 
	class Meta:
		model = Comment
		fields = ('name', 'comment_text',)


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "password")

