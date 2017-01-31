from rest_framework import generics
from serializers import RequestSerializer, PricingSerializer
from models import Pricing, Request

class AddRequest(generics.CreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

class PricingList(generics.ListAPIView):
    serializer_class = PricingSerializer
    queryset = Pricing.objects.all()