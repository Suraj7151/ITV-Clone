from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.


def home(request):
    # articles=Article.objects.all()
    # tags=Tag.objects.all()
    # topics=Topic.objects.all()
    # subtopics=SubTopic.objects.all()
    modules=module.objects.all()
    openings1 = openings.objects.all()
    profiles=profile.objects.all()
    context={'modules':modules,'openings':openings1,'profiles':profiles,}
    return render(request,"home.html",context)


def profile_view(request):
    if request.method=="POST":
        uid=request.session.get('uid')
        firstname=request.POST.get('firstname')
        middlename=request.POST.get('middlename')
        lastname=request.POST.get('lastname')
        email=request.POST.get('myemail')
        mobile=request.POST.get('mobile')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        guardian=request.POST.get('guardian')
        contact=request.POST.get('contact')
        f=profile()
        f.firstname=firstname
        f.middlename=middlename
        f.lastname=lastname
        f.email=email
        f.mobile=mobile
        f.dob=dob
        f.gender=gender
        f.address=address
        f.guardian=guardian
        f.emergency=contact
        f.user=User.objects.get(id=uid)
        f.save()
        return redirect('/profile')
    else:
        f=profile.objects.all()
        context={'form':f}
        return render(request,'profile.html',context)


def interview_view(request):
    interviews=Interview.objects.all()
    context={'interviews':interviews}
    return render(request,'interview.html',context)

def aws(request):
    return render(request,'aws.html')

def register_view(request):
    if request.method=="POST":
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'register.html',context)
    

def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')

        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/dashboard')
        else:
            f=LoginForm
            context={'form':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,'login.html',context)
    
def logout_view(request):
    logout(request)
    return redirect('/login')

def sqlStudy(request):
    return render(request,'sqlStudy.html')

def wd(request):
    f=InterviewQuestions.objects.all()
    context={'f':f}
    return render(request,'wd.html',context)


from django.db.models import Q
def searchView(request):
    # uid=request.session.get('uid')
    srch=request.POST.get('src')
    inte=InterviewQuestions.objects.filter(Q(ans__contains=srch) | Q(ques__contains=srch))
    # inter=InterviewQuestions.objects.filter(ques__contains=srch)    
    context={'f':inte}
    return render(request,'wd.html',context)