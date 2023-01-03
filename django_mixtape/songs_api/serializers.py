from .serializers_base import SongSerializerBase
from playlists_api.serializers_base import PlaylistSerializerBase

class SongSerializer(SongSerializerBase):
    playlist = SongSerializerBase()
    class Meta(SongSerializerBase.Meta):
        fields = SongSerializerBase.Meta.fields + ('playlist',)