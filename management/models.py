from django.db import models


# Create your models here.

class Genre(models.Model):
    book_genre = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.book_genre
    
    @staticmethod
    def get_all_genre():
        return Genre.objects.all()

class Language(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    b_name = models.CharField(max_length=150)
    b_author = models.CharField(max_length=150)
    b_genre = models.ForeignKey(Genre ,on_delete=models.CASCADE)
    b_language = models.ManyToManyField(Language)
    
    @staticmethod
    def get_books_by_genre_id(genre_id):
        if genre_id:
            return Book.objects.filter(b_genre = genre_id)
        else:
            return Book.objects.all()
        
    @staticmethod
    def get_books_by_language_id(language_id):
        if language_id:
            return Book.objects.filter(b_language = language_id)
        else:
            return Book.objects.all()
        
    

    

