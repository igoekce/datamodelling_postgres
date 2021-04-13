import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

#reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.

def process_song_file(cur, filepath):
    """
    - The procedure reads in one song file and extracts needed data for song and artist table
    - It extracts the relevant coumns 
    - and writes it to the respective tables in the database
    
    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the song file
    * column labels
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data =  df[['artist_id', 'artist_name','artist_location','artist_longitude','artist_latitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This procedure processes the json logfiles. It filters for "next song" as this is the relevant songs. 
    After setting datetime object several columns for time differentaition are created.
    User dataframe is generated for database insert
    songplay iterates over dataframe and writes the new mixed information to the databse
    
    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the log file
    * column labels
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms') 
    
    # insert time data records
    time_data = [t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday]
    column_labels = ['ts', 'hour', 'day', 'week', 'month', 'year', 'dayofweek']
    time_df = pd.DataFrame({c: d for c,d in zip (column_labels, time_data)}).dropna()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))


    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]
    user_not_null_df=user_df[user_df["userId"].notnull()]

    # insert user records
    for i, row in user_not_null_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist,row.length))
        results = cur.fetchone()
        
        if results:
            print(results)
            songid, artistid = results
            print(songid,artistid)
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'),row.userId, row.level,songid,artistid,
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    '''
    - walks through the folder and gives the full path back for further processing
    '''
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
    - establishes a connection 
    - starts the function defined before
    '''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()