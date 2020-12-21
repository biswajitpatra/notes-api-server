from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    '''
        Serializer for Note model
    '''
    class Meta:
        model = Note
        fields = ('id','title','content')