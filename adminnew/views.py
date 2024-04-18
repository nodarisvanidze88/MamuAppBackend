from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    if request.method=="POST":
        print('hellos')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Welcome')
        else:
            return HttpResponse('wrongs')
    return render(request,'adminnew/login.html')