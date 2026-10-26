from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import visible_notes

def index(request):
    query=request.GET.get('q','')[:200].strip()
    topic=request.GET.get('topic','')[:60].strip()
    notes=visible_notes()
    topics=notes.order_by('topic').exclude(topic='').values_list('topic',flat=True).distinct()
    if query:notes=notes.filter(Q(title__icontains=query)|Q(summary__icontains=query)|Q(body__icontains=query))
    if topic:notes=notes.filter(topic=topic)
    return render(request,'notes/index.html',{'page':Paginator(notes,10).get_page(request.GET.get('page')),'query':query,'topic':topic,'topics':topics})

def detail(request,slug):
    return render(request,'notes/detail.html',{'note':get_object_or_404(visible_notes(),slug=slug)})
