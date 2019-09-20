import datetime
from haystack import indexes
from engine.models import Books , Thesis , Meagazines


class BooksIndex(indexes.SearchIndex, indexes.Indexable):
    text            = indexes.CharField(document=True, use_template=True)
    Title           = indexes.CharField(model_attr='Title')
    Keywords        = indexes.CharField(model_attr='Keywords') 
    Author          = indexes.CharField(model_attr='Author') 
    Description     = indexes.CharField(model_attr='Description') 
    FiledOfStudies  = indexes.CharField(model_attr='FiledOfStudies') 

    content_auto_1    = indexes.EdgeNgramField(model_attr='Title')
    content_auto_2    = indexes.EdgeNgramField(model_attr='Keywords')
    content_auto_3    = indexes.EdgeNgramField(model_attr='Author')
    content_auto_4    = indexes.EdgeNgramField(model_attr='Description')
    content_auto_5    = indexes.EdgeNgramField(model_attr='FiledOfStudies')
   

    def get_model(self):
        return Books

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

class ThesisIndex(indexes.SearchIndex, indexes.Indexable):
    text            = indexes.CharField(document=True, use_template=True)
    Title           = indexes.CharField(model_attr='Title')
    Keywords        = indexes.CharField(model_attr='Keywords') 
    Author          = indexes.CharField(model_attr='Author') 
    Description     = indexes.CharField(model_attr='Description') 
    FiledOfStudies  = indexes.CharField(model_attr='FiledOfStudies') 

    content_auto_1    = indexes.EdgeNgramField(model_attr='Title')
    content_auto_2    = indexes.EdgeNgramField(model_attr='Keywords')
    content_auto_3    = indexes.EdgeNgramField(model_attr='Author')
    content_auto_4    = indexes.EdgeNgramField(model_attr='Description')
    content_auto_5    = indexes.EdgeNgramField(model_attr='FiledOfStudies')
   
    def get_model(self):
        return Thesis

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

class MeagazinesIndex(indexes.SearchIndex, indexes.Indexable):
    text            = indexes.CharField(document=True, use_template=True)
    Title           = indexes.CharField(model_attr='Title')
    Keywords        = indexes.CharField(model_attr='Keywords') 
    Author          = indexes.CharField(model_attr='Author') 
    Description     = indexes.CharField(model_attr='Description') 
    FiledOfStudies  = indexes.CharField(model_attr='FiledOfStudies') 

    content_auto_1    = indexes.EdgeNgramField(model_attr='Title')
    content_auto_2    = indexes.EdgeNgramField(model_attr='Keywords')
    content_auto_3    = indexes.EdgeNgramField(model_attr='Author')
    content_auto_4    = indexes.EdgeNgramField(model_attr='Description')
    content_auto_5    = indexes.EdgeNgramField(model_attr='FiledOfStudies')

    suggestions = indexes.FacetCharField()

    def prepare(self, obj):
        prepared_data = super(MeagazinesIndex, self).prepare(obj)
        prepared_data['suggestions'] = prepared_data['text']
        return prepared_data
   
    def get_model(self):
        return Meagazines

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
