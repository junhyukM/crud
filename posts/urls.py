from django.urls import path
from . import views

# 현재 내가 있는 앱의 이름 path함수의 name 속성과 같이 사용할 예정
app_name = 'posts'

urlpatterns = [
    # Read
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    # Create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # Delete
    path('delete/<int:id>/', views.delete, name='delete'),
    # Update
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
]