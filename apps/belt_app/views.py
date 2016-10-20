from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"belt_app/index.html")
def register(request):
    if request.method =="POST":
        User.objects.register(request.POST)
        
