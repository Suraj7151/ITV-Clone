from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
import requests
import razorpay
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponseBadRequest,HttpResponse
# Create your views here.

# Home View Starts#
@login_required
def home(request):
    modules=module.objects.all()
    openings1 = openings.objects.all()
    # profiles=profile.objects.all()
    # progress_percentage = 0.0
    try:
        f = profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        f = None
    module_progress={}
    if request.user.is_authenticated:
        for mod in modules:
            total_topics = StudyTopic.objects.filter(module=mod).count()
            if total_topics > 0:
                completed_topics = SubtopicProgress.objects.filter(user=request.user, completed=True, topic__module=mod).count()
                progress_percentage = (completed_topics / total_topics) * 100
            else:
                progress_percentage=0.0
            module_progress[mod] = progress_percentage
    context={'modules':modules,'openings':openings1,'profile':f,'progress_percentage':progress_percentage,'module_progress':module_progress}
    return render(request,"home.html",context)

# Home View Ends#

def openingDetail(request,cid):
    return render(request,'jobDetail.html'),

# Profile View Starts #

# @login_required
def profile_view(request):
    if request.method=="POST":
        user = request.user
        # uid=request.session.get('uid')
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
        img =request.FILES.get('img')
        fileUpload =request.FILES.get('fileUpload')
        f, created = profile.objects.get_or_create(user=user)
        f.firstname=firstname
        f.middlename=middlename
        f.lastname=lastname
        f.email=email
        f.mobile=mobile
        f.dob=dob
        f.gender=gender
        f.address=address
        f.guardian=guardian
        f.contact=contact
        
        if img:
            f.img=img

        if fileUpload:
            f.fileUpload = fileUpload
        f.save()
        
        messages.info(request,"Profile Updated Successfully.")
        return redirect('/profile')
    else:
        # user = request.user
        # f=profile.objects.get_or_create(user=user)
        try:
            f = profile.objects.get(user=request.user)
        except profile.DoesNotExist:
            f = None
        context={'profile':f}
        return render(request,'profile.html',context)

# Profile View Ends #

# Interview Questions View Starts#

def interview_view(request):
    # int_id = get_object_or_404(Interview,id=id)
    interviews=Interview.objects.all()
    f = profile.objects.get(user=request.user)
    context={'interviews':interviews,'profile':f}
    return render(request,'interview.html',context)

# Interview Questions View Ends#
# Registration View Starts#

# def register_view(request):
#     if request.method=="POST":
#         f=UserCreationForm(request.POST)
#         f.save()
#         return redirect('/profile')
#     else:
#         f=UserCreationForm
#         context={'form':f}
#         return render(request,'register.html',context)

# def register_view(request):
#     if request.method == "POST":
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             user = f.save()
#             # Authenticate the user
#             username = f.cleaned_data.get('username')
#             raw_password = f.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 # Log the user in
#                 login(request, user)
#                 # Redirect to the profile page
#                 return redirect('/profile')
#     else:
#         f = UserCreationForm()
#         context = {'form': f}
#         return render(request, 'register.html', context)

def register_view(request):
    # logic
    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        # print(uname,email,fname,lname,pass1,cpass)

# check wheater user exists or not
        if(pass1 != cpass):
            messages.warning(request,"Password is'nt Matching")
            return redirect("/register")

        try:
            if User.objects.get(username=email):
                messages.info(request,"Username is taken..")
                return redirect("/register")
        except:
            pass

        myuser = User.objects.create_user(username=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        user = authenticate(request, username=email, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Signup and Login Success")
            return redirect("/profile")  # Redirect to profile page

        messages.error(request,"Something went wrong")
        return redirect("/register")

    return render(request, "register.html")

    
# Registration View Ends#

# Login View Starts #

def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')

        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            messages.info(request,"Login Successful")
            return redirect('/dashboard')
        else:
            f=LoginForm
            context={'form':f}
            messages.error(request,"Invalid Credentials, Please Enter correct email and password.")
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,'login.html',context)
    
# Login View Ends #

# Logout View Starts #
def logout_view(request):
    logout(request)
    messages.success(request,'Logout successful')
    return redirect('/login_view')
# Logout View Ends #

def wd(request,id):
    int_id = get_object_or_404(Interview,id=id)
    f=InterviewQuestions.objects.filter(moduleName=int_id)
    p = profile.objects.get(user=request.user)
    context={'f':f,'profile':p}
    return render(request,'wd.html',context)


from django.db.models import Q
def searchView(request):
    srch=request.POST.get('src')
    inte=InterviewQuestions.objects.filter(Q(ans__contains=srch) | Q(ques__contains=srch))
    context={'f':inte}

    context = {'f': inte}

    if srch=="": 
        return redirect('/wd-interview') 
    
    # elif srch != query:
    #     messages.info(request,'No results found')
    #     return redirect('/wd-interview')
    else:
        messages.success(request,'Your Search Results:')
        return render(request,'wd.html',context)
    

def sqlStudy(request,id):
    main_topics = StudyTopic.objects.filter(module=id)
    f = profile.objects.get(user=request.user)
    modul = get_object_or_404(module, id=id)
    topics_with_materials = [(topic, StudyMaterial.objects.filter(studytopic=topic)) for topic in main_topics]
    return render(request,'sqlStudy.html',{'modul':modul,'topics_with_materials':topics_with_materials,'profile':f})

def study_material_view(request,id):
    # Getting material
    material = get_object_or_404(StudyMaterial, id=id)

    # Getting All Subtopics
    all_subtopics = StudyMaterial.objects.filter(studytopic=material.studytopic).order_by('id')

    # Getting Next Material
    next_material = StudyMaterial.objects.filter(id__gt=material.id,studytopic=material.studytopic).order_by('id').first()

    # Checking If it is last Subtopic
    is_last_subtopic = next_material is None

    # Getting profile data of logged in user

    f = profile.objects.get(user=request.user)

    if request.method=="POST" and is_last_subtopic:

        SubtopicProgress.objects.update_or_create(user=request.user, topic=material.studytopic, defaults={'completed': True})
        next_topic = StudyMaterial.objects.filter(studytopic__module=material.studytopic.module,studytopic__id__gt=material.studytopic.id).order_by('studytopic__id').first()
        if next_topic:
            next_subtopic = StudyMaterial.objects.filter(studytopic=next_topic.studytopic).order_by('id').first()
            return redirect('student:study_material', id=next_subtopic.id)
        else:
            return redirect('/dashboard')
    
    return render(request, 'study_material.html',{'material': material, 'next_material': next_material,'profile':f})

def course(request):
    uid=request.session.get('uid')
    f = profile.objects.get(user=request.user)
    courses = Course.objects.all()
    courseSort=set()
    for i in courses:
        courseSort.add(i.category)
    return render(request,'course.html',{'courses':courses,'courseSort':courseSort,'profile':f})


def sort(request,category):
    # uid=request.objects.filter(user=uid)
    courses = Course.objects.all()
    f = profile.objects.get(user=request.user)
    filtered_courses = Course.objects.filter(category__name=category)
    context={'courses':filtered_courses,'profile':f}
    return render(request,'course.html',context)


API_KEY= '742c401aaf2a40d1bf59b0da2e96c656'
def news(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    sort_by = request.GET.get('sort', 'publishedAt')
    if query:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()

    # Handle potential errors in the API response
    articles = data.get('articles', [])
    if not articles:
        articles = []  # Ensure articles is always a list

    # Filter articles based on the search query in both title and content
    if query:
        query_lower = query.lower()
        articles = [article for article in articles if query_lower in (article.get('title', '').lower() + article.get('content', '').lower())]


    f = get_object_or_404(profile, user=request.user)
    context = {'articles': articles, 'profile': f, 'query': query}
    return render(request, 'news.html', context)


def news_search(request):
    pass

from django.conf import settings
from django.contrib.auth.decorators import login_required



    

# @login_required
# def cart_list(request):
#     user = request.user
#     f = profile.objects.get(user=request.user)
#     cl = Cart.objects.filter(user=user)
#     total_price = sum(
#         (item.course.price) * item.quantity for item in cl)
#     final_price=total_price*100
    
#     context = {'cl': cl, 'total_price': total_price,'final_price':final_price,'profile':f,}
#     context['razorpay_key_id'] = settings.RAZORPAY_KEY_ID
#     return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, cid=None):
    user = request.user
    courses = get_object_or_404(Course, id=cid)
    cl = Cart.objects.filter(user=user)
    cart_item, created = Cart.objects.get_or_create(user=user, course=courses)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/cartlist',{'cl':cl})

@login_required
def cart_list(request):
    user = request.user
    f = profile.objects.get(user=request.user)
    cl = Cart.objects.filter(user=user)
    total_price = sum((item.course.price) * item.quantity for item in cl)
    final_price = total_price * 100

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount': final_price, 'currency': 'INR','payment_capture': '1'})
    print(payment)

    context = {
        'cl': cl,
        'total_price': total_price,
        'final_price': final_price,
        'profile': f,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'razorpay_order_id': payment['id']
    }

    return render(request, 'cart.html', context)

@csrf_exempt
def payment_success(request):
    return render(request, 'success.html')

@login_required
def update_cart(request, item_id, action):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        cart_item.quantity -= 1
        if cart_item.quantity < 1:
            cart_item.delete()
            return redirect('/cartlist')

    cart_item.save()
    return redirect('/cartlist')




@login_required
def delete_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('/cartlist')


import pyttsx3 # type: ignore

@csrf_exempt
def recognize_speech(request):
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    user = request.user

    Profile = profile.objects.get(user=user)  
    first_name = Profile.firstname
    print(first_name)

    engine.say(f"Hello{first_name}, How can I assist you today?")
    try:
        engine.runAndWait()  # Ensure the event loop runs and completes before proceeding
    except RuntimeError:
        pass
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language='en-IN')
        print("Recognized Text: " + query)
        response_text = f"Sure, Just press search button to search for: {query}"
    except sr.UnknownValueError:
        response_text = "Could not understand the audio"
    except sr.RequestError:
        response_text = "Could not request results; check your network connection"

    # Speaking the response
    engine.say(response_text)
    try:
        engine.runAndWait()  # Ensure the event loop runs and completes before proceeding
    except RuntimeError:
        pass

    print(response_text)
    return JsonResponse({'query': query, 'first_name': first_name})


# from .form import *
# from django.contrib.auth.views import *


# from django.urls import reverse_lazy
# class MyPasswordResetView(PasswordResetView):
#     template_name = 'password_reset.html'
#     form_class = MyPasswordResetForm
#     success_url = reverse_lazy('password_reset_done')


# class MyPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'password_reset_confirm.html'
#     form_class = MySetPasswordForm
#     success_url = reverse_lazy('password_reset_complete')




    # srch = request.POST.get('src', '')
    # # Split the search query into individual words
    # search_words = srch.split()

    # # Start with an empty Q object
    # query = Q()

    # # Loop over each word and add it to the query
    # for word in search_words:
    #     query |= Q(ans__icontains=word) | Q(ques__icontains=word)

    # # Filter the InterviewQuestions based on the constructed query
    # inte = InterviewQuestions.objects.filter(query)