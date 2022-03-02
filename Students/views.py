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


def profile(request,username):
    
    return render(request, 'profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})

def Discussion(request, id):
# Start a discussion.

    current_user = request.user
    group = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        form = DiscussionForm(request.POST, request.FILES)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.creator = current_user
            discussion.group = group
            discussion.save()

        return redirect('cohortdiscussions',group.id)

    else:
        form = DiscussionForm()
    return render(request, 'new_discussion.html', {"form": form ,'group':group})
@login_required(login_url= 'login')  
def groupdiscussions(request, id):
    group = get_object_or_404(Group, pk=id)
    messages = Message.objects.filter(group = group)
    members = UserProfile.objects.filter(group=group)

    return render(request, 'singlegroup.html', {'group':group , 'messages':messages,"members":members})
            

@login_required(login_url= 'login')                   
def reply(request, id):
    user = request.user
    message = get_object_or_404(Message, pk=id)
    all_responses = Response.get_response(message.id)
    if request.method == 'POST':
        form = ResponseForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.creator = user
            reply.message = message
            reply.save()

        return  HttpResponseRedirect(request.path_info)
        

    else:
        form = ResponseForm()
    return render(request, 'reply.html', {'all_responses':all_responses,"form": form, 'message':message})


    discussion.user = current_user