from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from albums.models import Album
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics

class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer


    def get_queryset(self):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))
        songs = Song.objects.filter(album_id=album.pk)
        return songs

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        serializer.save(album_id=album.pk)
