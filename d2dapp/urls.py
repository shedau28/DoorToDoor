
from django.urls import path
from .views import *

urlpatterns = [
    path("", login_page),
    path("index/", index, name='index'),
    path("shop/", shop, name='shop'),
    path("shop/<str:query>", product_detail, name='product_detail'),
    path("detail/", detail, name='detail'),
    path("login_page/", login_page, name='login_page'),
    path("login/", login, name='login'),
    path("logout/", logout, name='logout'),
    path("register_page/", register_page, name='register_page'),
    path("register/", register, name='register'),
    path("profile_page/", profile_page, name='profile_page'),
    path("update_data/", update_data, name='update_data'),
    path("change_password/", change_password, name='change_password'),
    path("upload_image/", upload_image, name='upload_image'),
    path("product_upload/", product_upload, name='product_upload'),
    path("update_product_upload/", update_product_upload, name='update_product_upload'),
]