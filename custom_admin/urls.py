from django.urls import path
from . import views
urlpatterns = [
    path('',views.adminLogin,name="adminLogin"),
    path('Dashboard/',views.Dashboard,name="Dashboard"),
    path('category/',views.category,name="category"),
    path('add_category',views.add_category,name="add_category"),
    path('category/update_category/<int:myid>',views.update_category,name="update_category"),
    path('category/delete_category/<int:id>',views.delete_category,name="delete_category"),
    path('orders/',views.orders,name="orders"),
    path('orders/delete_order/<int:id>',views.delete_order,name="delete_order"),
    path('searchProduct/',views.searchProduct,name="searchProduct"),
    path('productList/',views.productList,name="productList"),
    path('add_product/',views.add_product,name="add_product"),
    path('productList/update_product/<int:id>',views.update_product,name="update_product"),
    path('productList/delete_product/<int:id>',views.delete_product,name="delete_product"),
    path('contactList',views.contactList,name="contactList"),
    path('adminLogout/',views.adminLogout,name="adminLogout")
]
