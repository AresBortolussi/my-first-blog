from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from .models import Note

class JournalTest(TestCase):
    def make(self,slug,**extra):
        return Note.objects.create(title='Nota '+slug,slug=slug,summary='Sintesi tecnica',body='Contenuto originale',**extra)
    def test_drafts_and_future_notes_are_private_everywhere(self):
        self.make('draft')
        self.make('future',state='published',published_at=timezone.now()+timedelta(days=1))
        for slug in ['draft','future']:
            self.assertEqual(self.client.get('/notes/'+slug+'/').status_code,404)
            self.assertNotContains(self.client.get('/'), 'Nota '+slug)
            self.assertNotContains(self.client.get('/feed/'), 'Nota '+slug)
    def test_public_search_and_topic(self):
        self.make('one',state='published',topic='AI')
        self.make('two',state='published',topic='Hardware')
        response=self.client.get('/?q=tecnica&topic=AI')
        self.assertContains(response,'Nota one');self.assertNotContains(response,'Nota two')
    def test_content_is_escaped(self):
        note=self.make('safe',state='published');note.body='<script>alert(1)</script>';note.save()
        response=self.client.get(note.get_absolute_url())
        self.assertNotContains(response,'<script>');self.assertContains(response,'&lt;script&gt;')
    def test_admin_requires_auth_and_csrf(self):
        response=self.client.get('/admin/')
        self.assertEqual(response.status_code,302)
        from django.test import Client
        self.assertEqual(Client(enforce_csrf_checks=True).post('/admin/login/',{}).status_code,403)
    def test_pagination_and_rss(self):
        for i in range(12):self.make('note-'+str(i),state='published')
        self.assertEqual(len(self.client.get('/').context['page']),10)
        self.assertEqual(len(self.client.get('/?page=2').context['page']),2)
        response=self.client.get('/feed/');self.assertEqual(response.status_code,200)
        self.assertContains(response,'<rss')
