from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductsList.as_view(), name='products_list'),
    # path('<slug:slug>/', views.post_detail, name="post_detail"),

]
