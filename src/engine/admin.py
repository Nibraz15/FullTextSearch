from django.contrib import admin

# Register your models here.
from .models import Books , Thesis , Meagazines

admin.site.register(Books)
admin.site.register(Thesis)
admin.site.register(Meagazines)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author')
    readonly_fields = ('search_vector',)

class ThesisAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author')
    readonly_fields = ('search_vector',)

class MeagazinesAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author')
    readonly_fields = ('search_vector',)