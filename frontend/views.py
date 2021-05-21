from django.shortcuts import render, redirect

import servises


def index(request):
    relocate, template, params = servises.clicker_services.main_page(request)
    if relocate:
        return redirect(template)
    else:
        return render(request, template, params)


def user_login(request):
    relocate, template, params = servises.auth_services.user_login(request)
    if relocate:
        return redirect(template)
    else:
        return render(request, template, params)


def user_logout(request):
    template = servises.auth_services.user_logout(request)
    return redirect(template)


def user_registration(request):
    relocate, template, params = servises.auth_services.user_registration(request)
    if relocate:
        return redirect(template)
    else:
        return render(request, template, params)
