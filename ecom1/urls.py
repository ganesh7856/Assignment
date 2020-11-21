"""ecom1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

from search_indexes import urls as search_index_urls

from rest_framework.authtoken import views

#from productsapi.views import ProductsDetailView

schema_view = get_swagger_view(title='Nested_Serialization')

urlpatterns = [
    path('api/', include('productsapi.urls')),
    path('admin/', admin.site.urls),
    #path('mostviewed/',ProductsDetailView.as_view()),
    url(r'^swagger', schema_view),
    url(r'^search/', include(search_index_urls)),
    url(r'^token/', views.obtain_auth_token,name='token'),

]