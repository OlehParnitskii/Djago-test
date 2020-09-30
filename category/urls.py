
from django.urls import path,include
from category import views
app_name='category'
urlpatterns = [
    path('', views.index , name='index' ),
    path(r'<int:category_id>/', views.category_detal , name='category_detal' ),
]
