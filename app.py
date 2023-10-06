# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

    print("\nWelcome to the music library manager!")
    print("\nWhat would you like to do?\n"
          "  1 - List all albums\n"
          "  2 - List all artists\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        print("\nHere is the list of albums:")
        for album in albums:
           print(f" * {album.id} - {album.title}")

    if choice == '2':
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        print("\nHere is the list of artists:")
        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()