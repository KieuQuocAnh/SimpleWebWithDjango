"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from users.views import PasswordChangeView,UserLoginView
from users import views


# URL đa ngôn ngữ
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),


    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),


     path('login/', UserLoginView.as_view(), name='login'),  # Đường dẫn cho login
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/',views.logout_user, name='logout'),
    
    # path('password_change/',auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"),name="password_change"),



    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confoirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'), 
             name='password_reset_confirm'),


    path('password_change/',PasswordChangeView.as_view(template_name="users/password_change.html"),name="password_change"),
    path('password_success',views.password_success,name="password_success"),
    path('', include('users.urls')),  # Đảm bảo 'users.urls' đã hỗ trợ ngôn ngữ
    path('', include('blog.urls')),
)

# Thêm URL xử lý đổi ngôn ngữ
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # Đường dẫn này quan trọng!
]



if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)