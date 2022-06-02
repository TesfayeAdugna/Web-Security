from django.shortcuts import render

# Create your views here.
def render_login(request):
    return render(request, "login.html")

def render_register(request):
    return render(request, "register.html")