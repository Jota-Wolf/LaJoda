from core.models import Galeria
from rest_framework import serializers

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galeria
        fields = ('url','titulo', 'imagen',)
