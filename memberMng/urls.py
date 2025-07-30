from django.urls import path
from . import views

app_name = 'memberMng'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('members/', views.MemberListView.as_view(), name='members'),  # メンバー管理ページへのURL
]






