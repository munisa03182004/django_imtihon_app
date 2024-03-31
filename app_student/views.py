from django.shortcuts import render, redirect ,get_object_or_404
from app_student.models import Student

def student_list(request):
    if 'name' not in request.GET:
        student = Student.objects.all()
        return render(request,template_name='students/students_list.html',context={'student':student})
    else:
        student = Student.objects.filter(name__contains = request.GET['name'])
        return render(request,template_name='students/students_list.html',context={'student':student})
    

def students_detail(request,pk):
    students = Student.objects.get(id=pk)
    return render(request,template_name ='students/student_info.html', context={'students':students})


def student_create(request):
    if request.method =="POST":
        name = request.POST['name'] 
        age = request.POST['age']
        mark_1 = request.POST['mark_1']
        mark_2 = request.POST['mark_2']
        mark_3 = request.POST['mark_3']
        mark_4 = request.POST['mark_4']
        mark_5 = request.POST['mark_5']
        mark_6 = request.POST['mark_6']
        mark_7 = request.POST['mark_7']
        image = request.FILES['image']
        if image:
            new_student = Student(name=name,age=age,mark_1 = mark_1,mark_2 = mark_2,mark_3 = mark_3,mark_4=mark_4,mark_5=mark_5,mark_6=mark_6,mark_7 = mark_7,image = image)
        else:
            new_student = Student(name=name,age=age,mark_1 = mark_1,mark_2 = mark_2,mark_3 = mark_3,mark_4=mark_4,mark_5=mark_5,mark_6=mark_6,mark_7 = mark_7)

        new_student.save()
        return redirect(to='student_info', pk = new_student.pk)
    else:
        return render(request,template_name='students/add_student.html')



def students_edit(request,pk):
    this_student = get_object_or_404(Student,id=pk)
    if request.method =="POST":
    
        this_student.name = request.POST['name']
        this_student.age = request.POST['age']
        this_student.mark_1 = request.POST['mark_1']
        this_student.mark_2 = request.POST['mark_2']
        this_student.mark_3 = request.POST['mark_3']
        this_student.mark_4 = request.POST['mark_4']
        this_student.mark_5 = request.POST['mark_5']
        this_student.mark_6 = request.POST['mark_6']
        this_student.mark_7 = request.POST['mark_7']
        image = request.FILES.get['image']
        if image:
            this_student.image = image
        this_student.save()
        return redirect(to='student_info',pk=this_student.pk)
    else:
        return redirect(request,template_name='students/edit_student.html',context={'students':this_student})

            

