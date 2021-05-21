from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

from user_profile.forms import UserForm
from user_profile.models import MainCycle


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True, 'index', {}
        else:
            return False, 'login.html', {'invalid': True}
    else:
        return False, 'login.html', {'invalid': False}


def user_logout(request):
    logout(request)
    return 'login'


def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                main_cycle = MainCycle()
                main_cycle.user = user
                main_cycle.save()
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return True, 'index', {}
            except ValidationError as error:
                return (False, 'registration.html',
                        {'invalid': True, 'form': form, 'message': error.messages[0]})
        else:
            return False, 'registration.html', {'invalid': True, 'form': form, 'message': 'Incorrect Data'}
    else:
        return False, 'registration.html', {'invalid': False, 'form': UserForm(), }
