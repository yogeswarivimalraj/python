class PlaylistIterator:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Play next song (loops automatically)"""
        song = self.songs[self.index]
        self.index = (self.index + 1) % len(self.songs) 
        return song

    def previous(self):
        """Play previous song (loops automatically)"""
        self.index = (self.index - 1) % len(self.songs)
        return self.songs[self.index]

    def current_song(self):
        """Display currently playing song"""
        return self.songs[self.index]
playlist = PlaylistIterator(["Song A", "Song B", "Song C", "Song D"])


print(next(playlist)) 
print(next(playlist))  
print(next(playlist))  


print(playlist.previous())  
print(next(playlist))  
print(next(playlist)) 
print(next(playlist))  
