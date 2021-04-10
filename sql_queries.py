#ontains all your sql queries, and is imported into the last three files above.
# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table_drop"
user_table_drop = "DROP TABLE IF EXISTS user_table_drop"
song_table_drop = "DROP TABLE IF EXISTS song_table_drop"
artist_table_drop = "DROP TABLE IF EXISTS artist_table_drop"
time_table_drop = "DROP TABLE IF EXISTS time_table_drop"

# CREATE TABLES


songplay_table_create = ("""

CREATE TABLE "songplays" (
    "songplay_id" varchar   ,
    "start_time" varchar   ,
    "user_id" varchar   ,
    "level" varchar   ,
    "song_id" int   ,
    "artist_id" int   ,
    "session_id" int   ,
    "location" varchar   ,
    "user_agent" varchar   ,
    CONSTRAINT "pk_songplays" PRIMARY KEY (
        "songplay_id"
     )
);
""")


user_table_create = ("""
CREATE TABLE "users" (
    "user_id" varchar   ,
    "first_name" varchar   ,
    "last_name" varchar   ,
    "gender" varchar   ,
    "level" varchar   
    
);
""")

song_table_create = ("""
CREATE TABLE "songs" (
    "song_id" varchar   ,
    "title" varchar   ,
    "artist_id" varchar   ,
    "year" int   ,
    "duration" varchar   ,
    CONSTRAINT "pk_songs" PRIMARY KEY (
        "song_id"
     )
);
""")



artist_table_create = ("""

CREATE TABLE "artists" (
    "artist_id" varchar   ,
    "name" varchar   ,
    "location" varchar   ,
    "latitude" varchar   ,
    "longtitude" varchar   ,    
    CONSTRAINT "pk_artists" PRIMARY KEY (
        "artist_id"
     )
);
""")

time_table_create = ("""

CREATE TABLE "time" (
    "start_time" varchar   ,
    "hour" int   ,
    "dayint" int   ,
    "week" int   ,
    "month" int   ,
    "year" int   ,
    "weekday" varchar   
);
""")




# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
                    INSERT INTO users (user_id, first_name, last_name, gender, level) \
                     VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
                    INSERT INTO songs (song_id, title, artist_id, year, duration) \
                     VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
                    INSERT INTO artists (artist_id, name, location, latitude, longtitude) \
                     VALUES (%s, %s, %s, %s, %s)
""") 

'artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude'



time_table_insert = ("""
                    INSERT INTO time (start_time, hour, dayint, week, month, year, weekday) \
                     VALUES (%s, %s, %s, %s, %s, %s, %s)

""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id \
                FROM (songs s INNER JOIN artists a ON s.artist_id = a.artist_id) \
                WHERE s.title = %s AND a.name = %s AND s.duration = %s
                
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]