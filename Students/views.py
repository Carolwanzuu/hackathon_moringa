from django.shortcuts import render
from .models import chamaGroup
from django.shortcuts import get_object_or_404, render,redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('group')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def group(request):
    all_groups = chamaGroup.objects.all()
    params = {
        'all_groups': all_groups,
    }
    return render(request, 'all_groups.html', params)

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            
            group.save()
            return redirect('group')
    else:
        form = GroupForm()
    return render(request, 'newgroup.html', {'form': form})
