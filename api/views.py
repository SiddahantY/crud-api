from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# now here we will create a view of api window

class Notelist(generics.ListCreateAPIView):
    queryset= Note.objects.all() # this will get all the records present in the database
    serializer_class= NoteSerializer

class Notedetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Note.objects.all() 
    serializer_class= NoteSerializer
