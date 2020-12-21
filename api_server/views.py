from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

class NoteViewSet(viewsets.ModelViewSet):
    ''' ViewSet for NoteSerializer '''
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        """Overrides LIST request
        
        Returns:
            All the titles of Notes
        """        
        notes = self.get_queryset()
        serializer = self.get_serializer_class()(notes, many=True)
        return Response(serializer.data)
