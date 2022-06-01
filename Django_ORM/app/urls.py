from django.urls import path
from . import views
app_name = 'app'

urlpatterns=[
    path('',views.student_list,name='student_data'),
    path('filter/',views.student_list_filter,name='filter'),
    path('and/',views.student_list_and,name='and'),
    path('union/',views.student_and_teacher_union,name='union'),    
    path('exclude/',views.exclude_stu,name='exclude'),
    path('exclude2/',views.exclude_stu2,name='exclude2'),
    path('individual/',views.individual_field,name='individual'),
    path('raw/',views.raw_qry,name='raw'),
    path('raw2/',views.raw2,name='raw2'),
]