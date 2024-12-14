from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('logout/',views.signout,name="logout"),
    path('profile/<int:id>',views.profile,name="profile"),
    path('register/',views.register,name="register"),
    path('after_register/',views.afterregister,name="afterregister"),
    path('passwordinc/',views.passwordinc,name="passwordinc"),
    path('loginfailed/',views.loginfailed,name="loginfailed"),


]