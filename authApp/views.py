from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})