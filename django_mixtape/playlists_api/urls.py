from django.urls import path
from . import views

urlpatterns = [
    path('api/playlists', views.PlaylistList.as_view(), name='playlist_list'), # api/playlists will be routed to the PlaylistList view for handling
    path('api/playlists/<int:pk>', views.PlaylistDetail.as_view(), name='playlist_detail'), # api/playlists will be routed to the PlaylistDetail view for handling
]
