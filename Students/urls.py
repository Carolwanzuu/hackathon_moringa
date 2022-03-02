from os import name
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('all_groups/', views.group, name='group'),
    path('register/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('new-group/', views.create_group, name='new-group'),
    path('group/<int:id>/', views.groupdiscussions, name = 'groupdiscussions'),
    path('reply/<int:id>/', views.reply, name = 'reply'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
