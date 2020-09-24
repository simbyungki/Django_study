from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import BKUser
from bs4 import BeautifulSoup
import requests

# 웹툰 랭크뷰
def rank_view(request) : 
	url = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=sun'
	res = requests.get(url)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	cartoons = soup.find_all('td', attrs={'class':'title'})

	result_list = []
	for cartoon in cartoons :
		title = cartoon.a.get_text()
		link = 'https://comic.naver.com' + cartoon.a.get('href')
		result_list.append({'title': title, 'url': link})

	return render(request, 'rank_view.html', {'result_list': result_list})

	# 로그인 처리
	# user_id = request.session.get('user')
	# if user_id : 
	# 	user = BKUser.objects.get(id = user_id)
	# 	res_data = {}
	# 	res_data['user_name'] = user.name
	# 	return render(request, 'webtoon.html', res_data)

	#return render(request, '/users/login')
