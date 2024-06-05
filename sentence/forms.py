from django import forms
from .models import Sentence, Subject

class SentenceAddForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ['text', 'text_translate', 'audio', 'subject']

    def __init__(self, *args, **kwargs):
        super(SentenceAddForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.all()


class SubjectAddForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title']