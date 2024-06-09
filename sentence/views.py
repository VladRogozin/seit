from django.shortcuts import render, redirect, get_object_or_404
from .forms import SentenceAddForm, SubjectAddForm
from .models import Sentence, Subject
from django.core.serializers import serialize
import random


def index(request, sentence_id=None):
    data = Sentence.objects.all()
    subjects = Subject.objects.all()


    if request.method == 'POST':
        sentence = get_object_or_404(Sentence, id=sentence_id)
        subject_form = SubjectAddForm(request.POST)
        if subject_form.is_valid():
            subject = subject_form.save()
            sentence.subject = subject
            sentence.save()
            return redirect('index')
    else:
        subject_form = SubjectAddForm()
    subject_form = SubjectAddForm()
    return render(request, 'sentence/index.html', {'data': data, 'subjects': subjects, 'subject_form':subject_form})

def play_subject(request, id):
    sentence = Sentence.objects.filter(subject=id)
    sentence_json = serialize('json', sentence)
    return render(request, 'sentence/play_subject.html', {'sentence_json': sentence_json})

def random_sentence(request):
    data = Sentence.objects.all()
    sentence = random.choice(data)
    return render(request, 'sentence/random_sentence.html', {'sentence': sentence})


def add_sentences(request):
    if request.method == 'POST':
        sentence_form = SentenceAddForm(request.POST, request.FILES)
        subject_form = SubjectAddForm(request.POST)
        if sentence_form.is_valid():
            sentence_form.save()
        elif subject_form.is_valid():
            subject_form.save()
    else:
        sentence_form = SentenceAddForm()
        subject_form = SubjectAddForm()
    return render(request, 'sentence/add_sentences.html', {'sentence_form': sentence_form,'subject_form': subject_form, })


def edit_sentence(request, sentence_id):
    sentence = get_object_or_404(Sentence, id=sentence_id)

    if request.method == 'POST':
        sentence_form = SentenceAddForm(request.POST, request.FILES, instance=sentence)
        if sentence_form.is_valid():
            sentence_form.save()
            return HttpResponseRedirect('/sentences/')  # перенаправление после сохранения
    else:
        sentence_form = SentenceAddForm(instance=sentence)

    return render(request, 'sentence/edit_sentence.html', {'sentence_form': sentence_form, 'sentence': sentence})

def delete(request, id_obj, obj):
    if obj == 'sentence':
        sentence = Sentence.objects.get(id=id_obj)
        sentence.delete()

    elif obj == 'subject':
        subject = Subject.objects.get(id=id_obj)
        subject.delete()

    return redirect('app:index')
