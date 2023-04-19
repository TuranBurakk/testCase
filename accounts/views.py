from django.shortcuts import render ,redirect
from . forms import LoginForm , RegisterForm
from django.contrib.auth import authenticate, login,logout


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    else:
        form = RegisterForm()
    return render(request,'pages/register.html',{'form':form})
        


def user_logout(request):
    logout(request)
    return redirect('index')
