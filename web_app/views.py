from django.shortcuts import render, redirect
from . models import student, result

# Create your views here.


def index(request):
    f = student.objects.all()

    return render(request, 'index.html', {"f":f})

def student_save(request):
    s_n = request.POST.get('student_name')
    s_r = request.POST.get('student_roll')

    f = student(name= s_n, roll = s_r)
    f.save()

    return redirect('index')

def result_save(request):

    o = request.POST.get('student_info')
    f = student.objects.get(id=o)

    h = request.POST.get('result_Status')

    k = result(student_info=f, Status=h)
    k.save()
    return redirect('index')

def show_data_of_result(request):
    t = request.POST.get('result_of_stu')

    g = result.objects.filter(Status = t)
    print(t +" " + "student are : ")
    dd={"g":g

    }

    #
    # for i in g:
    #     p = i.id
    #     y = student.objects.get(id = p)
    #     dd={
    #         "y":y
    #     }



    return render(request, 'index.html', dd)
