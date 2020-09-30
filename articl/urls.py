
from django.urls import path,include
from articl import views
app_name='articl'
urlpatterns = [
    path(r'<int:articl_id>/', views.index , name='index' ),
    path(r'<int:articl_id>/leave_coment', views.leave_coment , name='leave_coment' ),
]
