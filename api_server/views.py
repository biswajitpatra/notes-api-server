from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

class NoteViewSet(viewsets.ModelViewSet):
    ''' ViewSet for NoteSerializer '''
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(methods=['GET'], name='Get Titles', detail=False)
    def list_titles(self,request):
        """Custom action for returing only titles

        Returns:
            List of titles
        """       
        notes = self.get_queryset()
        serializer = self.get_serializer_class()(notes, fields={'title'},many=True)
        return Response(serializer.data) 

    def list(self, request):
        """Overrides LIST request

        Returns:
            All the titles of Notes with ids hiding the content
        """        
        notes = self.get_queryset()
        serializer = self.get_serializer_class()(notes, fields={'id','title'},many=True)
        return Response(serializer.data)
