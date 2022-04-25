from rest_framework import serializers
from ..models.Nhaxuatban import Nhaxuatban

class NhaxuatbanSerializer(serializers.ModelSerializer):
  tennhaxuatban = serializers.CharField(max_length=200, required=True)
  class Meta:
    model = Nhaxuatban
    fields = ('__all__')