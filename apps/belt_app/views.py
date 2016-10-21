from django.shortcuts import render
from .models import Book,Author,Review
from ..user_app .models import User
# Create your views here.
def index(request):
    return render(request,"belt_app/index.html")
def addbook(request):
    if request.method =="POST":
        user=User.objects.get(id=request.session['userid'])
        if request.POST["Author"] == "add":
            Author.objects.create(author=request.POST['author_name'],user=user)
            Book.objects.create(title=request.POST['book'],user=user)
            this_book=Book.objects.filter(title=request.POST['book'])[:1]
            this_author=Author.objects.filter(author=request.POST['author_name'])[:1]
            # this_book.author.add(this_author)
            # Review.objects.create(review=request.POST['review'],user=user,book=this_book['book'])
        else:
            Author.objects.create(author=request.POST['Author'],user=user)
            Book.objects.create(title=request.POST['book'],user=user)
            this_book=Book.objects.filter(title=request.POST['book'])[:1]
            this_author=Author.objects.filter(author=request.POST['Author'])[:1]
            # this_book.author.add(this_author)
            # Review.objects.create(review=request.POST['review'],user=user,book=request.POST['book'])

        context={
        'books':Book.objects.filter(title=request.POST['book'])
        }
        return render(request,"belt_app/book.html",context)

    return render(request,"belt_app/add.html")
