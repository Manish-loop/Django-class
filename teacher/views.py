from django.shortcuts import redirect, render
from teacher.models import SchoolClass, Teacher
from teacher.forms import TeacherForm, ClassForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

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
        return redirect('teacher/test') # successful message ki arko page ma lai janko lagi redirect use garne, ani yesma chai url hit garne ho
    return render(request,'teacher/create.html')   # get request le render matra garcha yesma logic khasai lagdaina

@login_required(login_url='/admin/login')
def modelform(request):
    form = TeacherForm()  # yesma form dekhako matra ho
    if request.method =="POST":
        form = TeacherForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('/teacher/test')
        
    data_dict = {
        "form":form
    }
    return render(request,'teacher/modelform.html',data_dict)



#submit button click gare pachi if request.method =="POST":

# yesma actual data pass garne ho , rah yesma compare garcha form ko model= Teacher ma 
# TeacherForm forms.py ma jancha ani forms.py ko model = Teacher ma Teacher model ma jancha ra yesma bhako fields lai compare gardai jancha kun kun milyo bhanera

# form valid cha bhane form save garcha rah url '/teacher/test' ma redirect gardincha

# modelform ko key modelform.html ma pathaune {{form}} yesto khalko huncha modelform.html ma herda

@login_required(login_url='/admin/login')

def teacher_update(request,id):
    data = Teacher.object.get(id=id)
    form = TeacherForm(instance=data) #get garda ko data, hyaha instance=data bhaneko hamro lagi bhayo
    if request.method =="POST":
        form = TeacherForm(request.POST, instance=data) # POST garda dekhna ko lagi pani instance=data lekhnu parcha, natra naya data bancha
        if form.is_valid():
            form.save()
            return redirect('/teacher/test')
        
    data_dict = {
        "form":form
    }
    return render(request,'teacher/modelform.html',data_dict)

# instance 
# yesma key ko aadhar ma page render garne ho key "form" ho yesma 
# data_dict dictionary variable ho
# form = TeacherForm(instance=data) hyaha form le 


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
    
def user_list(request):
    user = User.objects.all().first()
    