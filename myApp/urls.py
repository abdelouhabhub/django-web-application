"""myApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_Views, Stuff_Views, Student_Views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login/', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('Hod/Home', Hod_Views.HOME, name='hod_home'),
    path("profile", views.PROFILE , name="profile"),
    path("Eprofile", views.EDITED_PROFILE, name="Eprofile"),
    path('doLogout', views.doLOGOUT, name='doLogout'),
    path('forms', views.FORMS, name='forms'),
    path('addStudent', Hod_Views.addStudent, name='addStudent'),
    path('viewStudents', Hod_Views.viewStudents, name='viewStudents'),
    path('timeTable', Hod_Views.timeTable, name='timeTable'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    #path('accounts/', include('django.contrib.auth.urls'))
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
                      template_name='templates/password/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                      template_name='templates/password/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                      template_name='templates/password/password_reset_complete.html'), name="password_reset_complete"),


    path('password_reset', views.password_reset_request, name='password_reset'),
    #path('', include('app.urls')),
    path('', views.LOGIN, name='LOGIN'),
    #path('users/', include('users.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

