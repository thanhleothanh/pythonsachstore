from xmlrpc.client import Boolean
from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.Donhang import Donhang
from ..models.Thongtinthanhtoan import Thongtinthanhtoan
from ..serializers.DonhangSerializer import DonhangSerializer
from ..utils import dictfetchall

class DonhangViews(APIView):
  def get(self, request, idDonhang=None):
    with connection.cursor() as cursor:
      if idDonhang:
        existedOrder = Donhang.objects.filter(id=idDonhang)
        if existedOrder:
          cursor.execute("select api_donhang.id as donhangid, api_donhang.diachi as donhangdiachi, api_donhang.ngaydat as donhangngaydat, api_donhang.tongtien as donhangtongtien, api_donhang.isThanhtoan as donhangisthanhtoan, api_donhang.isHoanthanh as donhangishoanthanh, api_thongtinthanhtoan.thoigianthanhtoan as thoigianthanhtoan, api_donhang.ngaydat as donhangngaydat, api_khachhang.api_nguoidung_id as khachhangid, api_donhang.hoten as donhanghoten, api_nguoidung.email as khachhangemail, api_donhang.sodienthoai as donhangsodienthoai from api_donhang join api_khachhang on api_donhang.api_khachhang_id = api_khachhang.api_nguoidung_id join api_nguoidung on api_nguoidung.id = api_khachhang.api_nguoidung_id left join api_thongtinthanhtoan on api_donhang.thongtinthanhtoan_id = api_thongtinthanhtoan.id where api_donhang.id = %s", [idDonhang])
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)
        else:
          return Response("Không có đơn hàng nào với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
          cursor.execute("select api_donhang.id as donhangid, api_donhang.diachi as donhangdiachi, api_donhang.ngaydat as donhangngaydat, api_donhang.tongtien as donhangtongtien, api_donhang.isThanhtoan as donhangisthanhtoan, api_donhang.isHoanthanh as donhangishoanthanh, api_thongtinthanhtoan.thoigianthanhtoan as thoigianthanhtoan, api_donhang.ngaydat as donhangngaydat, api_khachhang.api_nguoidung_id as khachhangid, api_donhang.hoten as donhanghoten, api_nguoidung.email as khachhangemail, api_donhang.sodienthoai as donhangsodienthoai from api_donhang join api_khachhang on api_donhang.api_khachhang_id = api_khachhang.api_nguoidung_id join api_nguoidung on api_nguoidung.id = api_khachhang.api_nguoidung_id left join api_thongtinthanhtoan on api_donhang.thongtinthanhtoan_id = api_thongtinthanhtoan.id")
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)

  def post(self, request):
    with connection.cursor() as cursor:
      serializer = DonhangSerializer(data=request.data)
      if serializer.is_valid():
          cursor.execute("INSERT INTO api_donhang(`ngaydat`,`diachi`, `hoten`, `sodienthoai`, `tongtien`, `isThanhtoan`, `isHoanthanh`,  `api_khachhang_id`) VALUES (CURRENT_TIMESTAMP,%s, %s, %s, %s, %s, %s, %s)", [request.data.get('diachi'),request.data.get('hoten'),request.data.get('sodienthoai'), request.data.get('tongtien'), False, False,  request.data.get('api_khachhang')])
          connection.commit()

          newOrderID = Donhang.objects.last().id
          cursor.execute("select * from api_donhang where id=%s", [newOrderID])
          data = dictfetchall(cursor)
          return Response(data[0], status=status.HTTP_201_CREATED)
      else:
        return Response("Kiểm tra lại thông tin đầu vào!", status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, idDonhang=None):
      order = Donhang.objects.filter(id=idDonhang)
      if not order:
        return Response("Không tìm thấy thông tin id (đơn hàng) này!", status=status.HTTP_404_NOT_FOUND)
      else:
        donhang = Donhang.objects.get(id=idDonhang)
        if request.data.get('diachi') is not None and len(request.data.get('diachi')) != 0:
          donhang.diachi = request.data.get('diachi') 
        if request.data.get('hoten') is not None and len(request.data.get('hoten')) != 0:
          donhang.hoten = request.data.get('hoten') 
        if request.data.get('sodienthoai') is not None and len(request.data.get('sodienthoai')) != 0:
          donhang.sodienthoai = request.data.get('sodienthoai') 
        if request.data.get('isThanhtoan') is not None:
          donhang.isThanhtoan = Boolean(request.data.get('isThanhtoan'))
        if request.data.get('isHoanthanh') is not None:
          donhang.isHoanthanh = Boolean(request.data.get('isHoanthanh'))
        if request.data.get('thongtinthanhtoan_id') is not None:
          donhang.thongtinthanhtoan_id = int(request.data.get('thongtinthanhtoan_id'))
        donhang.save()
        return Response("Cập nhật đơn hàng thành công!", status=status.HTTP_202_ACCEPTED)

  def delete(self, request, idDonhang=None):
    order = Donhang.objects.filter(id=idDonhang)
    if not order:
      return Response("Không tìm thấy thông tin id (đơn hàng) này!", status=status.HTTP_404_NOT_FOUND)
    else:
      Donhang.objects.filter(id=idDonhang).delete()
      return Response("Xoá đơn hàng thành công!", status=status.HTTP_202_ACCEPTED)
  
class SanphamdadatViews(APIView):
  def get(self, request, idDonhang=None):
    with connection.cursor() as cursor:
      if idDonhang:
        existedOrder = Donhang.objects.filter(id=idDonhang)
        if existedOrder:
          cursor.execute("select api_donhang.id as donhangid, api_donhang.diachi as donhangdiachi, api_donhang.ngaydat as donhangngaydat, api_donhang.tongtien as donhangtongtien, api_donhang.isThanhtoan as donhangisthanhtoan, api_donhang.isHoanthanh as donhangishoanthanh, api_thongtinthanhtoan.thoigianthanhtoan as thoigianthanhtoan, api_donhang.ngaydat as donhangngaydat, api_donhang.hoten as donhanghoten, api_donhang.sodienthoai as donhangsodienthoai, api_sach.id as sachid, api_sanphamdadat.soluong as soluongdadat, api_sanphamdadat.giaban as giabandadat, api_sach.tensach as tensachdadat, api_sach.hinhanh as hinhanh from api_donhang join api_sanphamdadat on api_sanphamdadat.api_donhang_id = api_donhang.id join api_sach on api_sach.id = api_sanphamdadat.api_sach_id left join api_thongtinthanhtoan on api_thongtinthanhtoan.id = api_donhang.thongtinthanhtoan_id where api_donhang.id =%s", [idDonhang])
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)
        else:
          return Response("Không có giỏ hàng nào với id này!", status=status.HTTP_404_NOT_FOUND)
      else:
          cursor.execute("select api_donhang.id as donhangid, api_donhang.diachi as donhangdiachi, api_donhang.ngaydat as donhangngaydat, api_donhang.tongtien as donhangtongtien, api_donhang.isThanhtoan as donhangisthanhtoan, api_donhang.isHoanthanh as donhangishoanthanh, api_thongtinthanhtoan.thoigianthanhtoan as thoigianthanhtoan, api_donhang.ngaydat as donhangngaydat, api_donhang.hoten as donhanghoten, api_donhang.sodienthoai as donhangsodienthoai, api_sach.id as sachid, api_sanphamdadat.soluong as soluongdadat, api_sanphamdadat.giaban as giabandadat, api_sach.tensach as tensachdadat, api_sach.hinhanh as hinhanh from api_donhang join api_sanphamdadat on api_sanphamdadat.api_donhang_id = api_donhang.id join api_sach on api_sach.id = api_sanphamdadat.api_sach_id left join api_thongtinthanhtoan on api_thongtinthanhtoan.id = api_donhang.thongtinthanhtoan_id")
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)

  def post(self, request, idDonhang=None):
    with connection.cursor() as cursor:
      if idDonhang:
          cursor.execute("INSERT INTO api_sanphamdadat(`api_donhang_id`,`api_sach_id`, `soluong`, `giaban`) VALUES (%s, %s, %s, %s)", [idDonhang, request.data.get('api_sach'),request.data.get('soluong'), request.data.get('giaban')])
          connection.commit()

          return Response("Thêm sản phẩm đã đặt thành công!", status=status.HTTP_201_CREATED)
      else:
        return Response("Kiểm tra lại thông tin đầu vào!", status=status.HTTP_400_BAD_REQUEST)
        
class DonhangcuatoiViews(APIView):
  def get(self, request, idKhachhang=None):
    with connection.cursor() as cursor:
      if idKhachhang:
          cursor.execute("select api_donhang.id as donhangid, api_donhang.diachi as donhangdiachi, api_donhang.ngaydat as donhangngaydat, api_donhang.tongtien as donhangtongtien, api_donhang.isThanhtoan as donhangisthanhtoan, api_donhang.isHoanthanh as donhangishoanthanh, api_thongtinthanhtoan.thoigianthanhtoan as thoigianthanhtoan, api_donhang.ngaydat as donhangngaydat, api_khachhang.api_nguoidung_id as khachhangid, api_donhang.hoten as donhanghoten, api_nguoidung.email as khachhangemail, api_donhang.sodienthoai as donhangsodienthoai from api_donhang join api_khachhang on api_donhang.api_khachhang_id = api_khachhang.api_nguoidung_id join api_nguoidung on api_nguoidung.id = api_khachhang.api_nguoidung_id left join api_thongtinthanhtoan on api_donhang.thongtinthanhtoan_id = api_thongtinthanhtoan.id where api_donhang.api_khachhang_id = %s", [idKhachhang])
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)
      else:
          return Response("Không tìm thấy khách hàng với id này",status=status.HTTP_404_NOT_FOUND)


class ThongtinthanhtoanViews(APIView):
  def post(self, request, idDonhang=None):
    with connection.cursor() as cursor:
      if idDonhang:
          order = Donhang.objects.filter(id=idDonhang)
          if not order:
            return Response("Không tìm thấy thông tin id (đơn hàng) này!", status=status.HTTP_404_NOT_FOUND)
          else:
            donhang = Donhang.objects.get(id=idDonhang)
            print(donhang)
            if donhang.thongtinthanhtoan_id is not None:
              return Response("Đơn hàng đã được thanh toán!", status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
              cursor.execute("INSERT INTO api_thongtinthanhtoan(`thoigianthanhtoan`) VALUES (CURRENT_TIMESTAMP)")
              connection.commit()
              thongtinthanhtoanID = (Thongtinthanhtoan.objects.last().id)

              donhang.thongtinthanhtoan_id = thongtinthanhtoanID;
              donhang.isThanhtoan = 1;
              donhang.save()
              return Response("Thanh toán đơn hàng thành công!", status=status.HTTP_201_CREATED)
      else:
        return Response("Kiểm tra lại thông tin đầu vào!", status=status.HTTP_400_BAD_REQUEST)