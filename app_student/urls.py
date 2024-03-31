from django.urls import path
from .views import student_list,students_detail,student_create,students_edit

urlpatterns = [
    path('',student_list,name='student_list'),
    path('<int:pk>/',students_detail,name = 'student_info'),
    path('edit/<int:pk>/',students_edit,name = 'etid_student'),
    path('add/',student_create,name='add_student'),

    
]