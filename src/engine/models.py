

from django.db import models

from django.db.models import Q

# Create your models here.

class BooksManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(Title__icontains=query) |
                         Q(Keywords__icontains=query)|
                         Q(Author__icontains=query) |
                         Q(Description__icontains=query) | 
                         Q(FiledOfStudies__icontains=query)
                        
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class ThesisManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(Title__icontains=query) | 
                         Q(Keywords__icontains=query)|
                         Q(Author__icontains=query) |
                         Q(Description__icontains=query) | 
                         Q(FiledOfStudies__icontains=query)
                        
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class MeagazinesManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(Title__icontains=query) | 
                         Q(Keywords__icontains=query)|
                         Q(Author__icontains=query) |
                         Q(Description__icontains=query) | 
                         Q(FiledOfStudies__icontains=query)
                        
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Books(models.Model):
    Title                   = models.TextField()
    Keywords                = models.TextField()
    Author                  = models.TextField()
    Description             = models.TextField()
    FiledOfStudies          = models.TextField()
    
    objects                 = BooksManager()


    def __unicode__(self):
        return self.Title


class Thesis(models.Model):
    Title                   = models.TextField()
    Keywords                = models.TextField()
    Author                  = models.TextField()
    Description             = models.TextField()
    FiledOfStudies          = models.TextField()
   
    objects                 = ThesisManager()


    def __unicode__(self):
        return self.Title


class Meagazines(models.Model):
    Title                   = models.TextField()
    Keywords                = models.TextField()
    Author                  = models.TextField()
    Description             = models.TextField()
    FiledOfStudies          = models.TextField()

    objects                 = MeagazinesManager()


    def __unicode__(self):
        return self.Title

