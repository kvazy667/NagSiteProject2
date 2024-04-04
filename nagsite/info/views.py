from django.shortcuts import render, redirect
from .forms import projectForm

def start(request):
    #тут прописывается весь бекэнд
    return render(request, 'info/start.html')

def forms(request):
    if request.method == 'POST':
        data = projectForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("/admin/info/project/")
    form = projectForm()
    print(form)
    context = {
        'form':form
    }
    return render(request, 'info/forms.html', context)


