from django.urls import path, include
from . import views

urlpatterns = [
    path('prof/add',views.add),
    path('course/add',views.add_course),
    path('student/add',views.add_student),
    path('set_grade',views.set_grade),
    path('get_student_summary',views.get_student_summary),
    path('assign_course_to_prof',views.assign_course_to_prof),
    path('assign_student_to_course',views.assign_student_to_course)

]