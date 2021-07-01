"""A video playlist class."""

class Playlist:

    """A class used to represent a Playlist."""
    def __init__(self):
        '''The playlist class is initialized'''
        self._playlist = Playlist
        self.playlist_name = []
        self.in_playlist = []

    def get_playlist_name(self):
        return self.playlist_name

    def in_playlist(self, playlist_name):
        index = self.playlist_name.index(playlist_name)
        playlist = self.in_playlist[index]
        return playlist
    def playlist_name_lower(self):
        playlist_list = self.playlist_name
        for i in range(len(playlist_list)):
            playlist_list[i] = playlist_list[i].lower()
        playlist_list_lower = playlist_list
        return playlist_list_lower

