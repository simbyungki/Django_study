from django.db import models

# Create your models here.
class board(models.Model) : 
    category = models.CharField(max_length=64,
                                verbose_name='카테고리')
    subject = models.CharField(max_length=256,
                                verbose_name='제목')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록시간')
    class Meta : 
        db_table = 'bk_board'