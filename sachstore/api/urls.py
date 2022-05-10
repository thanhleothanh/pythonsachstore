from django.urls import path
from rest_framework.response import Response


from .views.NguoidungDAO import NguoidungViews, SigninViews
from .views.TacgiaDAO import TacgiaViews
from .views.NhaxuatbanDAO import NhaxuatbanViews
from .views.TheloaiDAO import TheloaiViews
from .views.SachDAO import SachViews
from .views.GiohangDAO import GiohangViews
from .views.DonhangDAO import DonhangViews, DonhangcuatoiViews, SanphamdadatViews, ThongtinthanhtoanViews

def apiOverview(request):
  return Response("api endpoint", safe=False)

urlpatterns = [
  # users related
  path('users/', NguoidungViews.as_view()),
  path('users/<int:id>', NguoidungViews.as_view()),
  path('users/signin', SigninViews.as_view()),
  # sach related
  path('books/', SachViews.as_view()),
  path('books/authors', TacgiaViews.as_view(http_method_names=['get', 'post'])),
  path('books/categories', TheloaiViews.as_view(http_method_names=['get', 'post'])),
  path('books/publishers', NhaxuatbanViews.as_view(http_method_names=['get', 'post'])),
  path('books/<int:id>', SachViews.as_view()),
  # cart related
  path('cart/<int:idKhachhang>', GiohangViews.as_view(http_method_names=['get', 'post', 'patch'])),
  path('cart/<int:idKhachhang>/<int:idSach>', GiohangViews.as_view(http_method_names=['delete'])),
  # order related
  path('orders/', DonhangViews.as_view(http_method_names=['post', 'get'])),
  path('orders/myorders/<int:idKhachhang>', DonhangcuatoiViews.as_view(http_method_names=['get'])),
  path('orders/<int:idDonhang>', DonhangViews.as_view(http_method_names=['get', 'patch', 'delete'])),
  
  path('orders/<int:idDonhang>/pay', ThongtinthanhtoanViews.as_view(http_method_names=[ 'post'])),

  path('orders/<int:idDonhang>/items', SanphamdadatViews.as_view(http_method_names=['get', 'post'])),

  path('', apiOverview, name='api-overview'),
]