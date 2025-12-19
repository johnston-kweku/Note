from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.index, name='index' ),
    path('show_notes/', views.show_notes, name='show_notes'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('add_notes/', views.add_notes, name='add_notes'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note')
]