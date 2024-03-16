from django.shortcuts import render

def start(request):
    #тут прописывается весь бекэнд
    return render(request, 'info/start.html')