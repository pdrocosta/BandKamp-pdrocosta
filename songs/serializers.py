from django.shortcuts import get_object_or_404
from rest_framework import serializers
from albums.models import Album

from albums.serializers import AlbumSerializer

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['album']
    
    def create(self, validated_data):
        album = get_object_or_404(Album, id = validated_data.album.id)
        return Song.objects.create(**validated_data, album = album)
