from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


# Create your views here.
def register_page(request):
    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('home-page')
    else:
        reg_form = UserRegistrationForm()
        context = {'reg_form': reg_form}
        return render(request, 'usersapp/register.html', context=context)
