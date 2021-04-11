# Documentation of why and what


1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
The original intention of the start up makes totally sense as insights from the data can gain interaction between user and start-up to bring worthfull features. The db will enable the start-.up to get better and quick analysis on the users. Furthermore the database can show up difficulties and missing data in the logs. 

2. State and justify your database schema design and ETL pipeline.
For stating the schema please see QuickDBD-Free%20Diagram%20(1).png

To make the songplays table happen you need to extracct different data from logs and song data.

The songplays facttable includes all primary keys from the dimension tables(users, songs, time and artists)

To create the songs and artists table you need to process the songs log files.
For the rest of the tables you use the process log data

For the different tables you need to organize data insert in several ways to meet the postgres requirements.


3. [Optional] Provide example queries and results for song play analysis.

sparkifydb=# select * from songplays;
 songplay_id |       start_time        | user_id | level | song_id | artist_id | session_id |                   location                   |                                                                 user_agent                                                                  
-------------+-------------------------+---------+-------+---------+-----------+------------+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------
           0 | 2018-11-30 00:22:07.796 | 91      | free  |         |           |        829 | Dallas-Fort Worth-Arlington, TX              | Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)
           1 | 2018-11-30 01:08:41.796 | 73      | paid  |         |           |       1049 | Tampa-St. Petersburg-Clearwater, FL          | "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"
           2 | 2018-11-30 01:12:48.796 | 73      | paid  |         |           |       1049 | Tampa-St. Petersburg-Clearwater, FL          | "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"
           
As we see in the example dataset, there were no matches for the song_id and artist_id

4. What was difficult?
T ohave no matching data made me irritationg and braought up the notebooklength issue. In this notebook you can see that i tried to match several songs.druration woith the length logdata. But there was no successful match.