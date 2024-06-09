from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<int:sentence_id>/', views.index, name='index_add'),
    path('add_sentences/', views.add_sentences, name='add_sentences'),
    path('random_sentence/', views.random_sentence, name='random_sentence'),
    path('play_subject/<int:id>/', views.play_subject, name='play_subject'),
    path('delete/<int:id_obj>/<str:obj>', views.delete, name='delete'),
    path('sentences/edit/<int:sentence_id>/', views.edit_sentence, name='edit_sentence'),

]
