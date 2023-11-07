import sqlite3


# Function to create the music database
def create_music_db():
    # create music db if it does not exist and connect to it.
    conn = sqlite3.connect("music.db")
    # create a cursor to the music db
    cursor = conn.cursor()
    # create tables if they don't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS artists (
            artist_id INTEGER PRIMARY KEY,
            artist_name TEXT
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS albums (
            album_id INTEGER PRIMARY KEY,
            album_name TEXT,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS songs (
            song_id INTEGER PRIMARY KEY,
            song_name TEXT,
            artist_id INTEGER,
            album_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
            FOREIGN KEY (album_id) REFERENCES albums(album_id)
        );
        """
    )
    # commit the changes to db
    conn.commit()
    # close the connection
    conn.close()


# Function to load sample data in music database
def load_data():
    # setup database and tables
    create_music_db()
    # connect to music db
    conn = sqlite3.connect("music.db")
    # create a cursor to the pets db
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO artists (artist_name) VALUES
            ('Eminem'),
            ('Jay-Z'),
            ('Rihanna'),
            ('Drake');
        """
    )
    cursor.execute(
        """
        INSERT INTO albums (album_name, artist_id) VALUES
            ('The Eminem Show', 1),
            ('The Blueprint', 2),
            ('Good Girl Gone Bad', 3),
            ('Take Care', 4);
        """
    )
    cursor.execute(
        """
        INSERT INTO songs (song_name, artist_id, album_id) VALUES
            ('Lose Yourself', 1, 1),
            ('99 Problems', 2, 2),
            ('Umbrella', 3, 3),
            ('Hotline Bling', 4, 4),
            ('Stan', 1, 1),
            ('Empire State of Mind', 2, 2),
            ('We Found Love', 3, 3),
            ('In My Feelings', 4, 4);
        """
    )
    # commit changes
    conn.commit()
    # close the connection
    conn.close()


if __name__ == "__main__":
    load_data()