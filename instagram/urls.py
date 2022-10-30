from django.urls import path, re_path, register_converter

from . import views


app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),

]