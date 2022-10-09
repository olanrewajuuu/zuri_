from importlib.resources import path

from django.urls import path

from . import views

urlpatterns = [
    path('song/',views.list_create_song_view),
    path('song/<int:pk>',views.song_detail_view),
    path('artist/',views.list_create_artist_view),
]
