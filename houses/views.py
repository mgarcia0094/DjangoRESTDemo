from django.contrib.auth.models import User,Group
from rest_framework import viewsets, permissions
from houses.serializers import HouseSerializer
from houses.models import House

# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('id')
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]