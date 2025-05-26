from django.shortcuts import render
from .forms import ProjectForm
# Create your views here.
def projects(request):
    if request.method =="POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ProjectForm()
    return render(request, 'projform.html', {'form': form})