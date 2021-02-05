from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [path("", HomePage.as_view(), name="index"),
                path("register/", Register.as_view(), name="register"),
               path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
               path("logout/", LogoutView.as_view(), name="logout"),
               path("list/", UserList.as_view(), name="user_list"),
               path("detail/<int:pk>/", UserDetail.as_view(), name="user_detail"),
               path("update/<int:pk>/", UpdateProfile.as_view(), name="update_profile"),
               path("delete/<int:pk>/", DeleteUser.as_view(), name="delete_user"),]