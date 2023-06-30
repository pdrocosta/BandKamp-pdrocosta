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


    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs.get('album_id'))
        serializer.save(album=album)

    def get_queryset(self):
        queryset = super().get_queryset()
        album = get_object_or_404(Album, id=self.kwargs.get("album_id"))

        return queryset.filter(album=album)