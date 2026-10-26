from django.contrib import admin
from django.urls import path
from notes.views import index, detail
from notes.feeds import LatestNotes
urlpatterns = [path('admin/', admin.site.urls),path('',index,name='index'),path('feed/',LatestNotes(),name='feed'),path('notes/<slug:slug>/',detail,name='detail')]
