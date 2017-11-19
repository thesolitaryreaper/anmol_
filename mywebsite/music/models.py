from django.db import models

class Album(models.Model):
    artist= models.CharField(max_length=250)
    album_title = models.CharField(max_length=300)
    lyrics_by = models.CharField(max_length=250)
    produced_by = models.CharField(max_length=250)

    def __str__(self):
        return self.album_title + ' _ ' + self.artist

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    file_type = models.CharField(max_length=25)
    song_title = models.CharField(max_length=230)


