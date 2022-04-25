from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.NhaxuatbanSerializer import NhaxuatbanSerializer
from ..utils import dictfetchall


class NhaxuatbanViews(APIView):
  def get(self, request):
    with connection.cursor() as cursor:
      cursor.execute("select * from api_nhaxuatban")
      data = dictfetchall(cursor)
      return Response(data,status=status.HTTP_200_OK)

  def post(self, request):
    with connection.cursor() as cursor:
      serializer = NhaxuatbanSerializer(data=request.data)
      if serializer.is_valid():
        cursor.execute("INSERT INTO api_nhaxuatban(`tennhaxuatban`) VALUES (%s)", [request.data.get('tennhaxuatban')])
        connection.commit()
        return Response("Thêm nhà xuất bản thàng công!", status=status.HTTP_201_CREATED)
      else:
        return Response("Kiểm tra lại thông tin nhập vào!", status=status.HTTP_400_BAD_RENUEST)

