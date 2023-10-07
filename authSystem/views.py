from django.forms import ValidationError
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
from .utils import check_email
from django.contrib.auth.password_validation import validate_password


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': RegisterForm()})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            username_taken = User.objects.filter(username=username).exists()
            email_taken = User.objects.filter(email=email).exists()

            if username_taken:
                error = 'This username is taken. Try again!'
            elif email_taken:
                error = 'This e-mail is taken. Try again!' 
            else:
                email_valid = check_email(email)  
                if email_valid:
                    try:
                        validate_password(password1)
                    except ValidationError as e:
                        return render(request, 'register.html', {'password_errors': e.messages, 'form': RegisterForm()})
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password1)
                        return redirect('home')

                else:
                    error = 'Invalid e-mail. try again!'  
        else:
            error = 'Passwors must match. Try again!'

    return render(request, 'register.html',{'form':RegisterForm(), 'error': error})
        
