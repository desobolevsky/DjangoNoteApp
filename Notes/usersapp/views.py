from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


def register_page(request):
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()

            # login user after registration
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home-page')
    else:
        reg_form = UserRegistrationForm()
    context = {'reg_form': reg_form}
    return render(request, 'usersapp/register.html', context=context)
