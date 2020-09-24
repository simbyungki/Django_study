from django import forms
from .models import BKUser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form) : 
	name = forms.CharField(max_length=32, label='사용자 이름')
	password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')

	def clean(self) : 
		cleaned_data = super().clean()
		input_name = cleaned_data.get('name')
		input_password = cleaned_data.get('password')

		if input_name and input_password : 
			user = BKUser.objects.get(name=input_name)
			if not check_password(input_password, user.password) : 
				self.add_error('password', '비밀번호를 확인해주세요.')

