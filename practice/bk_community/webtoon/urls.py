from django.urls import path
from . import views 

urlpatterns = [
    path('rank_view/', views.rank_view)
]
