from django import forms
from .models import Professor,Course,Student,Student_Course

class ProfessorForm(forms.ModelForm):
    class Meta:
        model  = Professor
        fields = ['name','designation','degree']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'credits', 'hours_needed', 'professor']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'degree']

class Student_CourseForm(forms.ModelForm):
    class Meta:
        model = Student_Course
        fields = ['course','student','semester_year','semester_number','grade']
