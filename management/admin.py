from django.contrib import admin
from .models import Language , Genre , Book
from .forms import BookForm

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['b_name' , 'b_author' , 'b_genre' ]
    form = BookForm
    list_filter = ['b_name' , 'b_author' , 'b_genre' , 'b_language']
#    search_fields = ['b_name' , 'b_author' , 'b_genre' , 'b_language']

admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Book , BookAdmin)



