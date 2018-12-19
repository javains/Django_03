from django.shortcuts import render, redirect
from .models import *
from .forms import FeedbackForm
 
def add(request):
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm()
 
    return render(request, 'feedback.html', {'form': form})

def list(request):
    #return render(request, 'list.html')
    feedbacks = Feedback.objects.all()
    return render(request, 'list.html', {'feedbacks': feedbacks})

def edit(request,id):
    #return "update"
    fb = Feedback.objects.get(pk=id)
    if request.method=='POST':
        form = FeedbackForm(request.POST, instance=fb)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = FeedbackForm(instance=fb)
 
    return render(request, 'feedback.html', {'form': form})