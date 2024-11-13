from django.shortcuts import redirect, render
from teacher.models import SchoolClass, Teacher
from teacher.forms import TeacherForm, ClassForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.

@login_required(login_url='/admin/login')

def teacher(request):
    # data = Teacher.objects.filter(is_active=True)
    data = Teacher.objects.all()
    data_dict = {
        "teacher": data
    }
    return render(request,'teacher/index.html',data_dict)

@login_required(login_url='/admin/login')

def teacher_create(request):
    if not request.user.is_authenticated:
        return HttpResponse("User is not login")
    if request.method =="POST":
        print("======?",request.POST)
        Teacher.objects.create(
            name = request.POST['name'],
            address = request.POST['address'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            website = request.POST['link'],
            salary = request.POST['salary'],
            # is_active = request.POST.get['is_active',False],
            date_joined = request.POST['date_joined'],
            
        )
        return redirect('teacher/test')
    return render(request,'teacher/create.html')

@login_required(login_url='/admin/login')

def modelform(request):
    form = TeacherForm()
    if request.method =="POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/test')
        
    data_dict = {
        "form":form
    }
    return render(request,'teacher/modelform.html',data_dict)

@login_required(login_url='/admin/login')

def teacher_update(request,id):
    data = Teacher.object.get(id=id)
    form = TeacherForm(instance=data)
    if request.method =="POST":
        form = TeacherForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/teacher/test')
        
    data_dict = {
        "form":form
    }
    return render(request,'teacher/modelform.html',data_dict)

@login_required(login_url='/admin/login')

def delete_teacher(request,id):
    data = Teacher.objects.get(id=id).delete()
    return redirect('/teacher/test')


def list_class(request):
    data = SchoolClass.objects.all()
    context = {
        "data": data 
    }
    return render(request,'schoolclass/index.html',context)

def create_class(request):
    form = ClassForm()
    if request.method == 'POST':
        form = ClassForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/teacher/class')
        
    content = {
        'form': form
    }
    return render(request,'schoolclass/create.html',content)

class TeacherView(ListView):
    model = Teacher
    queryset = Teacher.objects.filter(is_active = False)
    template_name = 'teacher/teacher.html'
    context_object_name = 'teacher'
    
class TeacherCreate(CreateView):
    model = Teacher
    fields= '__all__'
    success_url = '/'

class UpdateTeacher(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = '/'

class DeleteTeacher(DeleteView):
    model = Teacher
    fields = '__all__'
    success_url = '/'
    
class DetailTeacher(DetailView):
    model = Teacher
    fields = '__all__'
    