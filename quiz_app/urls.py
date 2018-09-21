"""quiz_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from quiz import views as q_views
from player import views as p_views

urlpatterns = [
    url(r'^$', p_views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/', q_views.quiz, name='quiz'),
    url(r'^home/', p_views.home, name='home'),
    url(r'^signup/', p_views.signup, name='signup'),
    url(r'^login/', p_views.signin, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
]