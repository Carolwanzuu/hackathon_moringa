from django.shortcuts import render
from .models import chamaGroup
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
