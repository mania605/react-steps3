
from django.contrib import admin
from django.urls import path, include

urlpatterns = [   #해당 urls는 해당 프로젝트 안쪽에 있는 개별적인 앱의 url정보값을 불러와서 연결해주는 역할
    path('admin/', admin.site.urls),
    path('', include('member_app.urls'))#path로 2개 경로를 이어붙임: 기본url뒤에 member_app에 등록된 urls가져와서 연결
    #Include의 장점: 여러번 일하게 할 필요없이 한번만 연결하면 다 연결해줌.
] 