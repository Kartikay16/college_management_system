from django.db import models

class Professor(models.Model):
    name = models.TextField(max_length=200)
    designation = models.TextField(max_length=200)
    degree = models.TextField(max_length=200)


class Course(models.Model):
    name = models.TextField(max_length=200)
    code = models.IntegerField()
    credits = models.IntegerField()
    hours_needed = models.IntegerField()
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE, null=True, blank=True)

class Student(models.Model):
    name = models.TextField(max_length=200)
    degree = models.TextField(max_length=200)
    course = models.ManyToManyField(Course,through= 'Student_Course',related_name='students')

class Student_Course(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    semester_year = models.IntegerField()
    semester_number = models.IntegerField()
    grade = models.CharField(max_length=1,blank=True,null=True)
    
    class Meta:
        unique_together = ('student','course','semester_year','semester_number')


