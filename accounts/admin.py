from django.contrib import admin
from .models import *
# Register your models here
class PhraseAdmin(admin.ModelAdmin):
  list_display = ( 'private_phrase', 'date_created')
  list_display_links = ('private_phrase',)
  search_fields = ('id','private_phrase', 'date_created')
  list_per_page = 25

admin.site.register(Phrase,PhraseAdmin)