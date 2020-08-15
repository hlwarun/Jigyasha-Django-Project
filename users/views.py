from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['name'].split(' ')[0]
        last_name = request.POST['name'].split(' ')[1]
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']

        if password == passwordConfirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User with this Username already exists.')
                return redirect('users:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'User with this Email already exists.')
                return redirect('users:register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, f'Congratulations! {first_name}, Your account has been created successfully!')
                return redirect('root:home')
        else:
            messages.info(request, 'Password do not match.')
            return redirect('users:register')

    else:
        return render(request, 'signup.html')
