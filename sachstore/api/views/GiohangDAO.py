from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.Giohang import Giohang
from ..models.Sanphamtronggio import Sanphamtronggio
from ..models.Nguoidung import Khachhang, Nguoidung
from ..models.Sach import Sach
from ..serializers.SanphamtronggioSerializer import SanphamtronggioSerializer
from ..utils import dictfetchall


class GiohangViews(APIView):
  def get(self, request, idKhachhang=None):
    with connection.cursor() as cursor:
      if idKhachhang:
        existedUser = Khachhang.objects.filter(api_nguoidung_id=idKhachhang)
        if existedUser:
          cursor.execute("select api_giohang.api_khachhang_id as khachhangid, api_giohang.id as giohangid, (api_sanphamtronggio.soluong * api_sach.giasach) as tongtien, api_sanphamtronggio.soluong as soluong, api_sach.id as sachid, tensach, giasach, hinhanh, api_sach.soluong as soluongStock from api_giohang join api_khachhang on api_giohang.api_khachhang_id = api_khachhang.api_nguoidung_id join api_nguoidung on api_nguoidung.id = api_khachhang.api_nguoidung_id join api_sanphamtronggio on api_giohang.id = api_sanphamtronggio.api_giohang_id join api_sach on api_sach.id = api_sanphamtronggio.api_sach_id where api_giohang.api_khachhang_id =%s", [idKhachhang])
          data = cursor.fetchall()

          for book in data:
            if book[8] == 0:
              sanphamtronggio = Sanphamtronggio.objects.get(api_giohang=book[1], api_sach=book[4])
              sanphamtronggio.soluong = 0
              sanphamtronggio.save()
            elif book[8] != 0 and book[3] > book[8]:
              sanphamtronggio = Sanphamtronggio.objects.get(api_giohang=book[1], api_sach=book[4])
              sanphamtronggio.soluong = book[8]
              sanphamtronggio.save()
            elif book[8] != 0 and book[3] == 0: 
              sanphamtronggio = Sanphamtronggio.objects.get(api_giohang=book[1], api_sach=book[4])
              sanphamtronggio.soluong = 1
              sanphamtronggio.save()

          cursor.execute("select api_giohang.api_khachhang_id as khachhangid, api_giohang.id as giohangid, (api_sanphamtronggio.soluong * api_sach.giasach) as tongtien, api_sanphamtronggio.soluong as soluong, api_sach.id as sachid, tensach, giasach, hinhanh, api_sach.soluong as soluongStock from api_giohang join api_khachhang on api_giohang.api_khachhang_id = api_khachhang.api_nguoidung_id join api_nguoidung on api_nguoidung.id = api_khachhang.api_nguoidung_id join api_sanphamtronggio on api_giohang.id = api_sanphamtronggio.api_giohang_id join api_sach on api_sach.id = api_sanphamtronggio.api_sach_id where api_giohang.api_khachhang_id =%s", [idKhachhang])
          data = dictfetchall(cursor)
          return Response(data,status=status.HTTP_200_OK)
        else:
          return Response("Ch??? t??i kho???n kh??ch h??ng m???i ???????c ph??p mua h??ng!", status=status.HTTP_404_NOT_FOUND)
      else:
        return Response("Nh???p th??ng tin kh??ch h??ng!", status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, idKhachhang=None):
    with connection.cursor() as cursor:
      if idKhachhang:
           
        serializer = SanphamtronggioSerializer(data=request.data)
        if serializer.is_valid():
          existedUser = Nguoidung.objects.filter(id=idKhachhang)
          book = Sach.objects.filter(id=request.data.get('api_sach'))
          if not existedUser or not book:
            return Response("Kh??ng t??m th???y th??ng tin id (s???n ph???m/kh??ch h??ng) n??y!", status=status.HTTP_404_NOT_FOUND)
          else:
            cursor.execute("select * from api_giohang where api_khachhang_id=%s", [idKhachhang])
            giohang = dictfetchall(cursor)
            if giohang:
              giohangID = Giohang.objects.get(api_khachhang_id=idKhachhang).id
              sanphamtronggio = Sanphamtronggio.objects.filter(api_giohang_id=giohangID, api_sach_id=request.data.get('api_sach'))
              if(sanphamtronggio): 
                return Response("B???n ???? c?? s???n ph???m n??y trong gi???", status=status.HTTP_406_NOT_ACCEPTABLE)
              else:
                cursor.execute("INSERT INTO api_sanphamtronggio(`api_giohang_id`, `api_sach_id`, `soluong`) VALUES (%s, %s, %s)", [giohangID, request.data.get('api_sach'), request.data.get('soluong')])
                connection.commit()
                return Response("Th??m s???n ph???m v??o gi??? th??nh c??ng!", status=status.HTTP_201_CREATED)

            else:
              return Response("Ch??? t??i kho???n kh??ch h??ng m???i ???????c ph??p mua h??ng!", status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
          return Response("Ki???m tra l???i th??ng tin ?????u v??o!", status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response("Nh???p th??ng tin kh??ch h??ng!", status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, idKhachhang=None):
    serializer = SanphamtronggioSerializer(data=request.data)
    if serializer.is_valid():
      existedUser = Nguoidung.objects.filter(id=idKhachhang)
      book = Sach.objects.filter(id=request.data.get('api_sach'))
      if not existedUser or not book:
        return Response("Kh??ng t??m th???y th??ng tin id (s???n ph???m/kh??ch h??ng) n??y!", status=status.HTTP_404_NOT_FOUND)
      else:
        giohangID = Giohang.objects.get(api_khachhang_id=idKhachhang).id
        sanphamtronggio = Sanphamtronggio.objects.get(api_giohang=giohangID, api_sach=request.data.get('api_sach'))
        sanphamtronggio.soluong = request.data.get('soluong')
        sanphamtronggio.save()
        return Response("C???p nh???t s??? l?????ng th??nh c??ng!", status=status.HTTP_201_CREATED)
    else:
      return Response("Ki???m tra l???i!", status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, idKhachhang=None, idSach=None):
    existedUser = Nguoidung.objects.filter(id=idKhachhang)
    book = Sach.objects.filter(id=idSach)
    if not existedUser or not book:
      return Response("Kh??ng t??m th???y th??ng tin id (s???n ph???m/kh??ch h??ng) n??y!", status=status.HTTP_404_NOT_FOUND)
    else:
      giohangID = Giohang.objects.get(api_khachhang_id=idKhachhang).id
      Sanphamtronggio.objects.filter(api_giohang=giohangID, api_sach=idSach).delete()
      return Response("Xo?? kh???i gi??? h??ng th??nh c??ng!", status=status.HTTP_201_CREATED)
  