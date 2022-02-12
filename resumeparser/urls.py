"""resumeparser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('index/', include('home.urls')),
    path('signup/', include('home.urls')),
    path('otp_verify/', include('home.urls')),
    path('reload/', include('home.urls')),
    path('userside/', include('home.urls')),
    path('candidate/', include('home.urls')),
    path('landingpage/', include('home.urls')),
    path('forgetpassword', include('home.urls')),
    path('forget/', include('home.urls')),
    path('forget1/', include('home.urls')),
    path('database/', include('home.urls')),
    path('upload/', include('home.urls')),
    path('database/index', include('home.urls')),
    path('upload/index', include('home.urls')),
    path('editprofile/', include('home.urls')),
    path('resume/', include('home.urls')),
    path('demoupload/', include('home.urls')),
    path('filter', include('home.urls')),
    path('complete', include('home.urls')),
    path('partial', include('home.urls')),
    path('notmatched', include('home.urls')),


]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)