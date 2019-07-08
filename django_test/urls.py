"""django_test URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib import admin
import rest_framework.authtoken.views
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from DemoApp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='动力环境监控系统')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sys_user/',include('sys_user.urls',namespace='sys_user',app_name='sys_user')),#r表示不转义
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_token_auth/',obtain_jwt_token),
    url(r'^access_app/', include('AccessApp.urls', namespace='access_app', app_name='access_app')),
    url(r'^scene_app/', include('SceneApp.urls', namespace='scene_app', app_name='scene_app')),
    url(r'^demo_app/', include('DemoApp.urls', namespace='demo_app', app_name='demo_app')),
    url(r'^device_app/', include('DeviceApp.urls', namespace='device_app', app_name='device_app')),
    url( r'^$', schema_view),

]
