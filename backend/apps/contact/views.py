from rest_framework import generics
from serializers import ContactSerializer

class AddMessage(generics.CreateAPIView):
    serializer_class = ContactSerializer