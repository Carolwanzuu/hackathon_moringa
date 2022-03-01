from django.shortcuts import render
from .models import chamaGroup

# Create your views here.
def index(request):
    return render(request, 'index.html')

def group(request):
    all_groups = chamaGroup.objects.all()
    params = {
        'all_groups': all_groups,
    }
    return render(request, 'all_groups.html', params)
