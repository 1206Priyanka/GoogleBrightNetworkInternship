"""A video player class."""

# python3 -m src.run
# python3 -m pytest


import random
from .video_library import VideoLibrary
class VideoPlayer:
    """A class used to represent a Video Player."""


    def __init__(self):
        self._video_library = VideoLibrary()
        self.moreInfo = {}

        # this will be a list of all the playlists, where every item will be a Playlist object
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        #gets video information from library
        videoList = self._video_library.get_all_videos()
        #empty list
        sortedVideos = []

        #for every video data is appened in the required format
        for videos in videoList:
            dataFormat = f"{videos.title} ({videos.video_id}) [{' '.join(videos.tags)}]"
            sortedVideos.append (dataFormat)

        #sorts video in the sortedVideo list
        sortedVideos.sort()
        print("Here's a list of all available videos:")

        #printing each video information
        for videos in sortedVideos:
            print (f'\t {videos}')
 


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        selection = self._video_library.get_video(video_id)
        if not selection:
            print("Cannot play video: Video does not exist")
            return

        nowPLayingId = self.moreInfo.get("nowPLayingId")
        if nowPLayingId:
            self.stop_video()
            self.moreInfo["nowPLayingId"] = selection.video_id
            self.moreInfo["isPlaying"] = True
            print(f"Playing video: {selection.title}")
        else:
            self.moreInfo["nowPLayingId"] = selection.video_id
            self.moreInfo["isPlaying"] = True
            print(f"Playing video: {selection.title}")




    def stop_video(self):
        """Stops the current video."""

        nowPLayingId = self.moreInfo.get("nowPLayingId")
        if not nowPLayingId:
            print("Cannot stop video: No video is currently playing")
            return
        PlayingVideo = self._video_library.get_video(nowPLayingId)
        self.moreInfo["nowPLayingId"] = None
        self.moreInfo["currentlyPlaying"] = None
        print(f"Stopping video: {PlayingVideo.title}")



    def play_random_video(self):
        """Plays a random video from the video library."""

        videoList = self._video_library.get_all_videos()

        randomSelected = random.choice(videoList)
        self.play_video(randomSelected.video_id)

    def pause_video(self):
        nowPLayingId = self.moreInfo.get("nowPLayingId")
        if not nowPLayingId:
            print("Cannot pause video: No video is currently playing")
            return
        selection = self._video_library.get_video(nowPLayingId)
        if self.moreInfo["is_current_video_playing"]:
            self.moreInfo["is_current_video_playing"] = False
            print(f"Pausing video: {selection.title}")
        else:
            print(f"Video already paused: {selection.title}")

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
