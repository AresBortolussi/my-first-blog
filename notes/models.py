from django.db import models
from django.urls import reverse
from django.utils import timezone

class Note(models.Model):
    class State(models.TextChoices):
        DRAFT='draft','Bozza'
        PUBLISHED='published','Pubblicata'
    title=models.CharField(max_length=180)
    slug=models.SlugField(unique=True,max_length=180)
    summary=models.CharField(max_length=350)
    body=models.TextField()
    topic=models.CharField(max_length=60,blank=True,db_index=True)
    state=models.CharField(max_length=12,choices=State.choices,default=State.DRAFT)
    published_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-published_at','-pk']
        indexes=[models.Index(fields=['state','published_at'],name='notes_visibility_idx')]
        constraints=[models.CheckConstraint(condition=models.Q(state__in=['draft','published']),name='valid_note_state')]
    def __str__(self):return self.title
    def get_absolute_url(self):return reverse('detail',args=[self.slug])

def visible_notes():
    return Note.objects.filter(state=Note.State.PUBLISHED,published_at__lte=timezone.now())
