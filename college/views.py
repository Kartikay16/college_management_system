from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProfessorForm,CourseForm, StudentForm, Student_CourseForm
from .models import Student, Course, Professor, Student_Course
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"Success..Professor added sucesfully"})

@csrf_exempt
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"Success..Course added successfully"})
        
@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"Success..Student added successfully"})  
        
@csrf_exempt        
def set_grade(request):
    course_id = request.POST.get("course_id")
    student_id = request.POST.get("student_id")
    semester_year = request.POST.get("semester_year")
    semester_number = request.POST.get("semester_number")

    course = Course.objects.filter(id = course_id).first()
    student = Student.objects.filter(id = student_id).first()

    if not course or not student:
        return JsonResponse({"error": "Invalid course or student ID"}, status=400)

    grade = request.POST.get("grade")
    enrollment = Student_Course.objects.filter(course=course, student=student,semester_year = semester_year, semester_number = semester_number).first()
    if not enrollment:
        return JsonResponse({"error": "Student is not enrolled in this course"}, status=400)
 
    enrollment.grade = grade
    enrollment.save()

    return JsonResponse({"message": "Success..Grade set successfully"})

@csrf_exempt
def get_student_summary(request):
    student_id = request.POST.get('student_id')
    students = Student.objects.filter(id = student_id)
    students = students.prefetch_related('student_course_set').first()
    enrollments = students.student_course_set.all()
    summary = {
        "id": students.id,
        "name": students.name,
        "degree": students.degree,
        "courses": []
    }

    for enrollment in enrollments:
        summary["courses"].append({
            "course_name": enrollment.course.name,
            "course_code": enrollment.course.code,
            "semester_year": enrollment.semester_year,
            "semester_number": enrollment.semester_number,
            "grade": enrollment.grade
        })

    return JsonResponse(summary, safe=False)


@csrf_exempt
def assign_course_to_prof(request):
    course_id = request.POST.get("course_id")
    professor_id = request.POST.get("professor_id")

    course = Course.objects.filter(id = course_id).first()
    professor = Professor.objects.filter(id = professor_id).first()
    if not course or not professor:
        return JsonResponse({"error": "Invalid course or professor ID"}, status=400)

    course.professor = professor
    course.save()

    return JsonResponse({"mssg":"Course assigned to professor successfully"})


@csrf_exempt
def assign_student_to_course(request):
     if request.method == 'POST':
        form = Student_CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"Success..Student assigned to course successfully"})
        else:
            return JsonResponse({"error": "Invalid data"}, status=400)
