from django.urls import path
from . import views

#순서1-
# localhost:8000/members라는 요청이 들어오면 views.py의 members라는 뷰 함수 호출 
urlpatterns = [
  path('', views.home, name='home'),  # 빈문자열로 기본 경로url에 home 함수 연결
  path('members/', views.members, name='members'),
  path('members/details/<int:id>', views.details, name='details')
]