from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()


artist_1 = Artist("Radiohead")
artist_2 = Artist("Blur")
album_1 = Album("The Bends","Rock",artist_1)
album_2 = Album("Ok Computer","rock",artist_1)
album_3 = Album("blur","rock",artist_2)
album_4 = Album("13","rock",artist_2)


artist_repository.save(artist_1)
artist_repository.save(artist_2)
album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_4)


result = artist_repository.select_all()

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict__)    

# artist_albums =artist_repository.albums(artist_1)
# for album in artist_albums:
#     print(album.artist.name)    