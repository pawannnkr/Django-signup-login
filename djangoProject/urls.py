from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', views.login, name='login'),
    re_path('signup', views.signup, name='signup'),
    re_path('test_token', views.test_token, name='test_token'),
    re_path(r'^delete_user/(?P<id>\d+)/$', views.delete_user, name='delete_user/<int:id>'),
]
