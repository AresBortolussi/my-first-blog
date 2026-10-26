from django.contrib.syndication.views import Feed
from .models import visible_notes
class LatestNotes(Feed):
    title='Technical Journal'
    link='/'
    description='Note di progettazione software, dati e sistemi.'
    def items(self):return visible_notes()[:20]
    def item_title(self,item):return item.title
    def item_description(self,item):return item.summary
    def item_pubdate(self,item):return item.published_at
