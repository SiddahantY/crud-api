from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class meta:
        model=Note
        fields=('id','title','text')

#'''Serializers: In a Django REST Framework-based project, serializers are
# used to convert complex data types, such as Django model instances, into Python data types that can be easily rendered into JSON 
# and sent to the client.'''