from django.shortcuts import get_object_or_404
from rest_framework import serializers
from albums.models import Album

from albums.serializers import AlbumSerializer

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ["id", 'title', 'duration', 'album_id']
    
   