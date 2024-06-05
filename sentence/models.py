from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Sentence(models.Model):
    text = models.TextField(max_length=500)
    text_translate = models.TextField(max_length=500)
    audio = models.FileField(upload_to='audio/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sentences', null=True)

    def __str__(self):
        return self.text
