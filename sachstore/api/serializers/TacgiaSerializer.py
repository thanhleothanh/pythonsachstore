from rest_framework import serializers
from ..models.Tacgia import Tacgia

class TacgiaSerializer(serializers.ModelSerializer):
  tentacgia = serializers.CharField(max_length=200,required=True)
  diachi = serializers.CharField(required=False)
  namsinh = serializers.IntegerField(required=False)
  class Meta:
    model = Tacgia
    fields = ('__all__')