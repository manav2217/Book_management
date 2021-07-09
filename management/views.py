from django.shortcuts import render,redirect
from .models import Book , Language , Genre
from .forms import BookForm
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self , request):
        books = None
        language = Language.objects.all()
        genre = Genre.objects.all()
        print(genre)
        genre_id = request.GET.get('genre')
        print(genre_id)
        language_id = request.GET.get('language')
        if genre_id:
            books = Book.get_books_by_genre_id(genre_id)
        elif language_id:
            books = Book.get_books_by_language_id(language_id)
        else:
            books = Book.objects.all()
        return render(request , "index.html" , {"all_books":books , 'lan':language , 'gen':genre} )


def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request , "Add_book.html" , {'form':form})
    
