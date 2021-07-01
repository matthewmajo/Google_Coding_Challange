"""A video player class."""
import random

from .video_library import VideoLibrary
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)



    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        requested_video = self._video_library.get_video(video_id)
        if self._video_library.Video_Playing == 'None':
            if requested_video == None:
                print('Cannot play video: Video does not exist')
            else:
                print(f'Playing video: {requested_video.title}')
                self._video_library.isPlaying = True
                self._video_library.Video_Playing = requested_video
        else:
            if requested_video == None:
                print('Cannot play video: Video does not exist')
            else:
                print(f'Stopping video: {self._video_library.Video_Playing.title}')
                print(f'Playing video: {requested_video.title}')
                self._video_library.isPlaying = True
                self._video_library.Video_Playing = requested_video





    def stop_video(self):
        """Stops the current video."""
        if self._video_library.isPlaying == True:
            current_video = self._video_library.Video_Playing
            print(f'Stopping video: {current_video.title}')
            self._video_library.Video_Playing = 'None'
            self._video_library.isPlaying = False
        else:
            print('Cannot stop video: No video is currently playing')


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        random_video = random.choice(all_videos)
        if self._video_library.isPlaying == False:
            print(f'Playing video: {random_video.title}')
            self._video_library.Video_Playing = random_video
            self._video_library.isPlaying = True
        else:
            print(f'Stopping video: {self._video_library.Video_Playing.title}')
            print(f'Playing video: {random_video.title}')
            self._video_library.Video_Playing = random_video



    def pause_video(self):
        """Pauses the current video."""
        if self._video_library.Video_Playing == 'None':
            print('Cannot pause video: No video is currently playing')
        elif self._video_library.isPlaying == False:
            print(f'Video already paused: {self._video_library.Video_Playing.title}')
        else:
            print(f'Pausing video: {self._video_library.Video_Playing.title}')
            self._video_library.isPlaying = False

    def continue_video(self):
        """Resumes playing the current video."""
        if self._video_library.Video_Playing == 'None':
            print('Cannot continue video: No video is currently playing')
        elif self._video_library.isPlaying == True:
            print('Cannot continue video: Video is not paused')
        else:
            print(f'Continuing video: {self._video_library.Video_Playing.title}')
            self._video_library.isPlaying = True

    def show_playing(self):
        """Displays video currently playing."""
        current_video = self._video_library.Video_Playing

        if self._video_library.Video_Playing == 'None':
            print('No video is currently playing')
        else:

            tags = "["
            for tag in current_video.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            if self._video_library.isPlaying == False:
                print(f'Currently playing: {current_video.title} ({current_video.video_id}) {tags} - PAUSED')
            else:
                print(f'Currently playing: {current_video.title} ({current_video.video_id}) {tags}')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        new_playlist_lower = str(playlist_name).lower()

        playlist_list = self._playlist.playlist_name
        for i in range(len(playlist_list)):
            playlist_list[i] = playlist_list[i].lower()
        playlist_list_lower = playlist_list

        if new_playlist_lower in playlist_list_lower:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            self._playlist.playlist_name.append(playlist_name)
            self._playlist.in_playlist.append([])
            print(f'Successfully created new playlist: {playlist_name}')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_name_lower = str(playlist_name).lower()
        playlist_list = self._playlist.playlist_name
        for i in range(len(playlist_list)):
            playlist_list[i] = playlist_list[i].lower()
        playlist_list_lower = playlist_list

        if playlist_name_lower in playlist_list_lower:
            if self._video_library.get_video(video_id) == None:
                print(f'Cannot add video to {playlist_name}: Video does not exist')
            elif video_id == self._playlist.in_playlist(playlist_name):
                print(f'Cannot add video to {playlist_name}: Video already added')
            else:
                index = self._playlist.playlist_name.index(playlist_name)
                self._playlist.in_playlist.append[index](video_id)
                video_title = self._video_library.get_video(video_id).title
                print(f'Added video to {playlist_name}: {video_title}')
        else:
            print(f'Cannot add video to {playlist_name}: Playlist does not exist')

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
