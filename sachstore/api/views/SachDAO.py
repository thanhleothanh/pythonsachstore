from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.SachSerializer import SachSerializer
from ..models.Sach import Sach
from ..utils import dictfetchall


class SachViews(APIView):
  def get(self, request, id=None):
    with connection.cursor() as cursor:
      if id:
        cursor.execute("select api_sach.id as id, hinhanh, tensach, giasach, namphathanh, soluong, tentacgia, api_tacgia.diachi as diachitacgia, api_tacgia.namsinh as namsinhtacgia, tennhaxuatban, tentheloai from api_sach left join api_tacgia on api_sach.api_tacgia_id = api_tacgia.id left join api_nhaxuatban on api_sach.api_nhaxuatban_id = api_nhaxuatban.id left join api_theloai on api_sach.api_theloai_id = api_theloai.id where api_sach.id=%s", [id])
        data = dictfetchall(cursor)

        if data:
          return Response(data,status=status.HTTP_200_OK)
        else:
          return Response("Không có sách nào với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
        cursor.execute("select api_sach.id as id, hinhanh, tensach, giasach, namphathanh, soluong, tentacgia, api_tacgia.diachi as diachitacgia, api_tacgia.namsinh as namsinhtacgia, tennhaxuatban, tentheloai from api_sach left join api_tacgia on api_sach.api_tacgia_id = api_tacgia.id left join api_nhaxuatban on api_sach.api_nhaxuatban_id = api_nhaxuatban.id left join api_theloai on api_sach.api_theloai_id = api_theloai.id")
        data = dictfetchall(cursor)
        return Response(data,status=status.HTTP_200_OK)

  def post(self, request):
    with connection.cursor() as cursor:
      serializer = SachSerializer(data=request.data)
      if serializer.is_valid():
        cursor.execute("select * from api_nhanvien where api_nguoidung_id=%s" , [request.data.get('api_nguoidung_id')])
        user = dictfetchall(cursor)
        if not user:
          return Response("Chỉ nhân viên mới được uỷ quyền!", status=status.HTTP_403_FORBIDDEN)
        else:
          cursor.execute("INSERT INTO api_sach(`hinhanh`, `mota`,`tensach`, `giasach`, `soluong`, `api_tacgia_id`, `api_theloai_id`, `api_nhaxuatban_id`, `namphathanh`) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)", [request.data.get('hinhanh'), request.data.get('mota') or None , request.data.get('tensach'), round(float(request.data.get('giasach')),2), (request.data.get('soluong')), (request.data.get('api_tacgia')) or None, (request.data.get('api_theloai')) or None, (request.data.get('api_nhaxuatban')) or None, (request.data.get('namphathanh')) or None])
          connection.commit()

          return Response("Thêm sách thàng công!", status=status.HTTP_201_CREATED)
      else:
        return Response("Kiểm tra lại thông tin nhập vào!", status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, id=None):
    with connection.cursor() as cursor:
      cursor.execute("select * from api_sach where id=%s",[id])
      existedBook = dictfetchall(cursor)
      if not existedBook:
        return Response("Không tìm thấy sách với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
        sach = Sach.objects.get(id=id)
        if request.data.get('giasach') is not None:
          if(float(request.data.get('giasach')) <= 0):
            return Response("Giá sách không hợp lệ", status=status.HTTP_400_BAD_REQUEST)
          else:
            sach.giasach = round(float(request.data.get('giasach')),2)
        if request.data.get('soluong') is not None:
          if(int(request.data.get('soluong')) <= 0):
            return Response("Số lượng stock không hợp lệ", status=status.HTTP_400_BAD_REQUEST)
          else:
            sach.soluong = int(request.data.get('soluong')) 
        if request.data.get('namphathanh') is not None:
          sach.namphathanh = request.data.get('namphathanh') 
        sach.save()
        return Response("Cập nhật sách thành công", status=status.HTTP_201_CREATED)

  def delete(self, request, id=None):
    with connection.cursor() as cursor:
      cursor.execute("select * from api_sach where id=%s",[id])
      sach = dictfetchall(cursor)
      if not sach:
        return Response("Không tìm thấy sách với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
        cursor.execute("delete from api_sach where id=%s", [id])
        connection.commit()
        return Response("Xoá sách thành công!", status=status.HTTP_201_CREATED)

