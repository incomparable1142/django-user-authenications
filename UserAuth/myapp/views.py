from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TutorForm, SchoolForm, CoachingForm
from .models import Tutor, School, Coaching
# Create your views here.


@login_required(login_url='login')
def home(request):
    dictionary = {'tutorForm': TutorForm(),
                  'schoolForm': SchoolForm(),
                  'coachingForm': CoachingForm()}
    return render(request, 'home.html', dictionary)


@login_required(login_url='login')
def tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.current_user = request.user.id
            fs.save()
            return redirect(show_tutor)
    else:
        return redirect(home)


@login_required(login_url='login')
def coaching(request):
    if request.method == 'POST':
        form = CoachingForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.current_user = request.user.id
            fs.save()
            return redirect(show_coaching)
    else:
        return redirect(home)


@login_required(login_url='login')
def school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.current_user = request.user.id
            fs.save()
            return redirect(show_school)
    else:
        return redirect(home)


@login_required(login_url='login')
def show_school(request):
    school_obj = School.objects.filter(current_user=request.user.id)
    return render(request, 'school.html', {'data': school_obj})


@login_required(login_url='login')
def show_tutor(request):
    tutor_obj = Tutor.objects.filter(current_user=request.user.id)
    return render(request, 'tutor.html', {'data': tutor_obj})


@login_required(login_url='login')
def show_coaching(request):
    coaching_obj = Coaching.objects.filter(current_user=request.user.id)
    return render(request, 'coaching.html', {'data': coaching_obj})




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.add_message(request, messages.INFO, 'Successfully User registered.')
        return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, 'The username and/or password you specified are not correct.')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')
