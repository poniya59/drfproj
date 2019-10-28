from .models import Essay, Album, Files
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')


class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'desc', 'image', 'author_name')

class FilesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)
    
    class Meta:
        model = Album
        fields = ('pk','author', 'myfile', 'desc')

