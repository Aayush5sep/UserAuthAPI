"""
URL configuration for youseai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from api.views import UserLoginView,UserRegisterView,UserLogoutView,UserProfileView,flushexpired

urlpatterns = [
    path('user/register/',UserRegisterView.as_view(), name='register_new_user'),
    path('user/login/',UserLoginView.as_view(), name='login_user'),
    path('user/logout/',UserLogoutView.as_view(), name='logout_user'),
    path('user/refresh/',TokenRefreshView.as_view(), name='obtain_access_token'),
    path('user/profile/',UserProfileView.as_view(), name='user_profile_get_post_put'),
    path('manage/flush/tokens/',flushexpired, name='flush_expired_tokens'),
]
