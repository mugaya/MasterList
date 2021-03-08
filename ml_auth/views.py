from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import LoginForm


def log_in(request):
    """Method to handle log out to system."""
    try:
        url = '/'
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.data['username'].strip()
                password = form.data['password'].strip()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        msg = 'You have successfully logged in.'
                        messages.add_message(request, messages.INFO, msg)
                        return HttpResponseRedirect(url)
                    else:
                        msg = "Account is inactive."
                        messages.add_message(request, messages.ERROR, msg)
                        return render(request, 'login.html', {'form': form})
                else:
                    msg = "Invalid credentials. Check username and password"
                    messages.add_message(request, messages.ERROR, msg)
                    return render(request, 'login.html', {'form': form})
        else:
            form = LoginForm()
            logout(request)
        return render(request, 'login.html', {'form': form})
    except Exception as e:
        raise e


def log_out(request):
    """Method to handle log out to system."""
    try:
        url = '/'
        logout(request)
        msg = 'You have successfully logged out.'
        messages.add_message(request, messages.INFO, msg)
        return HttpResponseRedirect(url)
    except Exception as e:
        raise e
