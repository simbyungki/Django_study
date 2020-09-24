from django.db import models

# Create your models here.
class BKUser(models.Model) :
	name = models.CharField(max_length=64, 
								verbose_name='사용자명')
	email = models.EmailField(max_length=128,
                                null=True,
								verbose_name='이메일')
	save_info = models.CharField(max_length=8,
								verbose_name='아이디 저장')
	password = models.CharField(max_length=128, 
								verbose_name='비밀번호')
	registered_dttm = models.DateTimeField(auto_now_add=True, 
											verbose_name='등록일시')

	def __str__(self) : 
		return self.name

	class Meta :
		db_table = 'bk_users'
		verbose_name = 'BK 커뮤니티 사용자'
		verbose_name_plural = 'BK 커뮤니티 사용자'

