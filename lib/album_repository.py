from lib.album import Album

"""
ArtistRepository makes the queries to pass through database connection
for execution
"""

class AlbumRepository:
    
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        """retreive all albums"""

        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'],
                         row['release_year'], row['artist_id'])
            albums.append(item)
        return albums
    
    def find(self, id):
        """Retrieve specified album using id"""
        rows = self._connection.execute(
            "select * from albums where id = %s", [id])
        row = rows[0]
        return Album(row['id'], row['title'],
                         row['release_year'], row['artist_id'])