from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_album',views.AlbumCreate.as_view(),name='album_create'),
    path('album_detail/<int:pk>',views.AlbumDetail.as_view(),name='album_detail'),
    path('band_detail/<int:pk>',views.BandDetail.as_view(),name='band_detail'),
    path('list_album',views.AlbumListView.as_view(),name='list_album'),
    path('list_band',views.BandListView.as_view(),name='list_band'),
    path('my_view/',views.my_view,name='my_view'),
]
