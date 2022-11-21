"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from capstone import views
from .views import Kscholarlistapi,CartView


app_name = 'capstone'
urlpatterns = [
    path('admin/',admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('capstone/', views.index, name="index"),
    path('common/', include('common.urls')),
    path('capstone/<int:question_id>/', views.detail, name='detail'),
    path('capstone/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('', views.scholar_list, name='index1'),
    path('/<int:scholars_id>/',views.scholar_content,name ='scholar'),# '/' 에 해당되는 path
    path('api/scholar',Kscholarlistapi.as_view()),
    path('scholar', CartView.as_view()),

        

]
