from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import BKUser
from .forms import LoginForm

# 홈
def home(request) : 
	user_id = request.session.get('user')
	if user_id : 
		user = BKUser.objects.get(id = user_id)
		res_data = {}
		res_data['user_name'] = user.name
		return render(request, 'mypage.html', res_data)
		
	return HttpResponse('Home!')

# 마이페이지
def mypage(request) : 
	user_id = request.session.get('user')
	if user_id : 
		user = BKUser.objects.get(id = user_id)
		res_data = {}
		res_data['user_name'] = user.name
		return render(request, 'mypage.html', res_data)

	return HttpResponse('Home!')

# 회원가입
def register(request) : 
	# templates 폴더를 보고 있기 때문에 html파일명만 기재
	if request.method == 'GET' : 
		return render(request, 'register.html')
	elif request.method == 'POST' : 
		input_name = request.POST.get('name', None)
		input_email = request.POST.get('email', None)
		input_password = request.POST.get('password', None)
		input_re_password = request.POST.get('re-password', None)

		res_data = {}

		if not (input_name and input_email and input_password and input_re_password) : 
			res_data['error'] = '모든 값을 입력해주세요!'
		elif input_password != input_re_password : 
			res_data['error'] = '비밀번호가 다릅니다!'
		else :
			users = BKUser(
				name = input_name,
				email = input_email,
				password = make_password(input_password)
			)
			users.save()

		return render(request, 'register.html', res_data)

# 로그인
def login(request) : 
	if request.method == 'POST' : 
		form = LoginForm(request.POST)
		if form.is_valid() : 
			return redirect('/')
	else : 
		form = LoginForm()
	

	return render(request, 'login.html', {'form': form})

# 로그아웃
def logout(request) : 
	if request.session.get('user') : 
		del(request.session['user'])

	return redirect('/')