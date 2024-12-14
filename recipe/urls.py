from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.recipe_list,name="home"),
    path('createpost/',views.createpost,name="createpost"),
    path('postsuccess/',views.postsuccess,name="postsuccess"),
    path('recipe_detail/<int:id>',views.recipe_detail,name="recipe_detail"),
    path('recipe_delete/<int:id>',views.recipe_delete,name="recipe_delete"),
    path('recipe_edit/<int:id>',views.recipe_edit,name="recipe_edit"),
    path('comment/<int:recipe_id>',views.comment,name="comment"),
]

