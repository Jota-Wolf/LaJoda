from core.models import Galeria
from rest_framework import viewsets
from core.quickstart.serializers import GaleriaSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Galeria.objects.all().order_by('-created_date')
    serializer_class = GaleriaSerializer
