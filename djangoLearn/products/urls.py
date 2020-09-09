from django.urls import path
from .views import (
product_detail_view,
product_create_view,
product_detail_view,
product_delete_view,
product_query_all_view,
product_update_view
) 

app_name='products'
urlpatterns = [
    path('', product_query_all_view),
    path('create/', product_create_view),
    path('<int:id>/', product_detail_view, name='product-detail'), 
    path('delete/<int:id>/', product_delete_view, name='product-delete'),
    path('update/<int:id>/', product_update_view, name='product-update'),

]
