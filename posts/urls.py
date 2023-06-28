from django.urls import path
from . import views

# 현재 내가 있는 앱의 이름 path함수의 name 속성과 같이 사용할 예정
app_name = 'posts'

urlpatterns = [
    # Read
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    # Create

    # Delete

    # Update
]