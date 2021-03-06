from django.urls import path, include, re_path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('base/', views.base, name='base'),
	path('sing_up/', views.sing_up, name='sing_up'),
	path('log_out/', auth_views.LogoutView.as_view(), name='log_out'),
	path('', views.index, name='index'),
	path('log_in/', views.log_in, name='log_in'),
	path('index/', views.index, name='index'),
	path('list_post/', views.list_post, name='list_post'),
	path('tag/<tag_slug>/', views.list_post, name='list_post_by_tag'),
	path('about_blog/', views.about_blog, name='about_blog'),
	path('new_post/', views.new_post, name='new_post'),
	path('news_blog/', views.news_blog, name='news_blog'),
	path('<slug>/', views.read_post, name='read_post'),
]

