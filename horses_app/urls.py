from . import views
from django.urls import path

urlpatterns = [
    path('', views.HorseList.as_view(), name='horses_list'),
    # path('<slug:slug>/', views.post_detail, name="post_detail"),

]