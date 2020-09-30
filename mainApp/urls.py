
from django.urls import path,include
from mainApp import views

app_name='mainApp'
urlpatterns = [
    path(r'', views.index , name='index' ),
    path(r'/leave_coment', views.leave_email , name='leave_email' ),
]
