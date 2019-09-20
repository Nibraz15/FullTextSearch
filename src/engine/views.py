from django.shortcuts import render
from django.db.models import F
from django.contrib.postgres.search import SearchQuery, SearchRank ,TrigramSimilarity
from django.shortcuts import render
from django.views.generic import ListView
from itertools import chain
from engine.models import  Meagazines , Books , Thesis 






class MeagazinesListView(ListView):
    template_name = 'engine/books_list.html'
    paginate_by = 20
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        
        if query is not None:
            book_title_result         = Books.objects.annotate(similarity=TrigramSimilarity('Title', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            book_keywor_result        = Books.objects.annotate(similarity=TrigramSimilarity('Keywords', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            book_author_result        = Books.objects.annotate(similarity=TrigramSimilarity('Author', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            book_descrip_result       = Books.objects.annotate(similarity=TrigramSimilarity('Description', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            book_feos_result          = Books.objects.annotate(similarity=TrigramSimilarity('FiledOfStudies', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            thesis_title_result       = Thesis.objects.annotate(similarity=TrigramSimilarity('Title', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            thesis_keywor_result      = Thesis.objects.annotate(similarity=TrigramSimilarity('Keywords', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            thesis_author_result      = Thesis.objects.annotate(similarity=TrigramSimilarity('Author', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            thesis_descrip_result     = Thesis.objects.annotate(similarity=TrigramSimilarity('Description', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            thesis_feos_result        = Thesis.objects.annotate(similarity=TrigramSimilarity('FiledOfStudies', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            magazi_title_result       = Meagazines.objects.annotate(similarity=TrigramSimilarity('Title', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            magazi_keywor_result      = Meagazines.objects.annotate(similarity=TrigramSimilarity('Keywords', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            magazi_author_result      = Meagazines.objects.annotate(similarity=TrigramSimilarity('Author', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            magazi_descrip_result     = Meagazines.objects.annotate(similarity=TrigramSimilarity('Description', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            magazi_feos_result        = Meagazines.objects.annotate(similarity=TrigramSimilarity('FiledOfStudies', query),).filter(similarity__gt=0.1).order_by('-similarity') 
            
            # combine querysets 
            queryset_chain = chain(
                    book_title_result,
                    book_keywor_result,
                    book_author_result,
                    book_descrip_result,
                    book_feos_result,
                    thesis_title_result,
                    thesis_keywor_result,
                    thesis_author_result,
                    thesis_descrip_result,
                    thesis_feos_result,
                    magazi_title_result,
                    magazi_keywor_result,
                    magazi_author_result,
                    magazi_descrip_result,
                    magazi_feos_result

            )
                    
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            qs = list(dict.fromkeys(qs))
            self.count = len(qs) # since qs is actually a list
            return qs
        return Books.objects.none() # just an empty queryset as default

    


