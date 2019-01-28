from django.urls import re_path,path
from hello import views

urlpatterns = [
    path('<int:year>', views.HelloWorldView.as_view()),
    
    re_path(r'^', views.HelloWorldView.as_view()),
]
