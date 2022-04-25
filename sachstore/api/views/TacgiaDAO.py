from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.TacgiaSerializer import TacgiaSerializer
from ..utils import dictfetchall


class TacgiaViews(APIView):
  def get(self, request):
    with connection.cursor() as cursor:
      cursor.execute("select * from api_tacgia")
      data = dictfetchall(cursor)
      return Response(data,status=status.HTTP_200_OK)

  def post(self, request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO api_tacgia(`tentacgia`, `diachi`,`namsinh`) VALUES (%s, %s, %s)", [request.data.get('tentacgia'),request.data.get('diachi') or None,request.data.get('namsinh') or None])
        connection.commit()

        return Response("Thêm tác giả thàng công!", status=status.HTTP_201_CREATED)

