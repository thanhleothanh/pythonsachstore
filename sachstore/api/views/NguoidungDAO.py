from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.NguoidungSerializer import NguoidungSerializer 
from ..models.Nguoidung import Nguoidung
from ..utils import dictfetchall


# Nguoi dung views
class NguoidungViews(APIView):
  def get(self, request, id=None):
    with connection.cursor() as cursor:
      if id:
        cursor.execute("select * from api_nguoidung where id=%s", [id])
        data = dictfetchall(cursor)
        if data:
          return Response(data,status=status.HTTP_200_OK)
        else:
          return Response("Không có user nào với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
        cursor.execute("select * from api_nguoidung")
        data = dictfetchall(cursor)
        return Response(data,status=status.HTTP_200_OK)

  def post(self, request):
    with connection.cursor() as cursor:
      # serializer = NguoidungSerializer(data=request.data)
      # if serializer.is_valid():
        cursor.execute("select * from api_nguoidung where taikhoan=%s" , [request.data.get('taikhoan')])
        existedUser = dictfetchall(cursor)
        if existedUser:
          return Response("Tài khoản đã tồn tại!", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
          cursor.execute("insert into api_nguoidung (`taikhoan`, `matkhau`, `hoten`,`diachi`,`sodienthoai`, `vaitro`) values (%s, %s, %s, %s, %s, %s)", [request.data.get('taikhoan'),request.data.get('matkhau'), request.data.get('hoten'),request.data.get('diachi') or 'Địa chỉ mặc định', request.data.get('sodienthoai') or '00000000000', request.data.get('vaitro')] )
          connection.commit()

          newID = (Nguoidung.objects.last().id)
          if request.data.get('vaitro') == 'khachhang':
            cursor.execute("insert into api_khachhang (`api_nguoidung_id`) values (%s)", [newID])
            connection.commit()
            cursor.execute("insert into api_giohang (`api_khachhang_id`, `tongtien`) values (%s, 0)", [newID])
            connection.commit()
          elif request.data.get('vaitro') == 'nhanvien':
            cursor.execute("insert into api_nhanvien (`api_nguoidung_id`) values (%s)", [newID])
            connection.commit()
          elif request.data.get('vaitro') == 'admin':
            cursor.execute("insert into api_admin (`api_nguoidung_id`) values (%s)", [newID])
            connection.commit()

          newUser = Nguoidung.objects.get(id=newID)
          return Response(NguoidungSerializer(newUser).data, status=status.HTTP_201_CREATED)
      # else:
      #   return Response("Kiểm tra lại các thông tin!", status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, id=None):
    with connection.cursor() as cursor:
      cursor.execute("select * from api_nguoidung where id=%s",[id])
      existedUser = dictfetchall(cursor)
      if not existedUser:
        return Response("Không tìm thấy người dùng", status=status.HTTP_404_NOT_FOUND)
      else:
        user = Nguoidung.objects.get(id=id)
        if request.data.get('matkhau') is not None and len(request.data.get('matkhau')) != 0:
          user.matkhau = request.data.get('matkhau') 
        if request.data.get('hoten') is not None and len(request.data.get('hoten')) != 0:
          user.hoten = request.data.get('hoten') 
        if request.data.get('diachi') is not None and len(request.data.get('diachi')) != 0:
          user.diachi = request.data.get('diachi') 
        if request.data.get('sodienthoai') is not None and len(request.data.get('sodienthoai')) != 0:
          user.sodienthoai = request.data.get('sodienthoai') 
        if request.data.get('email') is not None and len(request.data.get('email')) != 0:
          user.email = request.data.get('email') 
        user.save()
        newUser = Nguoidung.objects.get(id=id)
        return Response(NguoidungSerializer(newUser).data, status=status.HTTP_201_CREATED)

  def delete(self, request, id=None):
    existedUser = Nguoidung.objects.filter(id=id)
    if not existedUser:
      return Response("Không tìm thấy người dùng với id này!", status=status.HTTP_404_NOT_FOUND)
    else:
      Nguoidung.objects.filter(id=id).delete()
      return Response("Xoá người dùng thành công!", status=status.HTTP_202_ACCEPTED)


# Signin views
class SigninViews(APIView):
  def post(self, request):
    with connection.cursor() as cursor:
      if request.data.get('taikhoan') is not None and request.data.get('matkhau') is not None:
        cursor.execute("select * from api_nguoidung where taikhoan=%s" , [request.data.get('taikhoan')])
        existedUser = dictfetchall(cursor)
        if not existedUser:
          return Response("Sai tài khoản hoặc mật khẩu!", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
          if request.data.get('matkhau') == existedUser[0].get('matkhau'):
            return Response(existedUser[0], status=status.HTTP_200_OK)
          else:
            return Response("Sai tài khoản hoặc mật khẩu!", status=status.HTTP_406_NOT_ACCEPTABLE)
      else:
        return Response("Sai tài khoản hoặc mật khẩu!", status=status.HTTP_400_BAD_REQUEST)
