import sqlite3


# Function to query the music database
def query_music():
    # connect to music database
    conn = sqlite3.connect("music.db")
    # create a cursor to the music db
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT artists.artist_name AS Artist, songs.song_name AS Song
            FROM artists
            INNER JOIN songs ON artists.artist_id = songs.artist_id
            ORDER BY artists.artist_name;
        """
    )
    artist_songs = cursor.fetchall()
    cursor.execute(
        """
            SELECT albums.album_name AS Album, songs.song_name AS Song
            FROM albums
            INNER JOIN songs ON albums.album_id = songs.album_id
            ORDER BY albums.album_name;
        """
    )
    album_songs = cursor.fetchall()
    # close db connection
    conn.close()

    if artist_songs:
        print("Artist\t:\tSong")
        for a_s in artist_songs:
            print(f"{a_s[0]}\t=>\t{a_s[1]}")
    else:
        print("The database is empty, run the initialization script first.")
    print()
    if album_songs:
        print("Album\t:\tSong")
        for a_s in album_songs:
            print(f"{a_s[0]}\t=>\t{a_s[1]}")
    else:
        print("The database is empty, run the initialization script first.")


if __name__ == "__main__":
    query_music()