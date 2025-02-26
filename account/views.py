from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request=request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("home")
            
            else:
                print("로그인 실패")
                return render(request, 'login.html', {'form': form, 'error_message': '로그인에 실패했습니다'})
        else:
            return render(request, 'login.html', {'form': form, 'error_message': '폼이 유효하지 않습니다'})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})
