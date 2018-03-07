"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from polls import views as poll_views
from django.conf.urls import url
app_name = 'polls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.indexView.as_view()),
    path('detail/<int:pk>', poll_views.DetailView.as_view(), name='detail'),    
    path('detail/<int:pk>/results/', poll_views.ResultsView.as_view(), name='results'),
    path('detail/<int:question_id>/vote', poll_views.vote, name='vote'),
]
