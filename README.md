# Project-Group-5
Project Name: Trending Music Attributes


Category: Music

Questions: 
The duration songs are in the top 40?
What genres are more frequently in the top 40?
What musical attributes might affect this?

Data Files:
https://data.world/kcmillersean/billboard-hot-100-1958-2017


18 July 2020:
Music genres were too specific and we had to simpfily them. 
We used the explode command to get a more broad genre.
- genre_df = genre_df.set_index(['Performer', 'Song'])
- new_df = genre_df['spotify_genre'].str.split(pat=",", expand=True)
- new_df.head()

Data Organization: 

-	Merged two data sets that were pulled from two different csv files Both csv files were derived from a Spotify API Hot 100 Audio Features (song attributes and components) Hot Stuff (chart topper placements) Merged the two data sets on columns: Song, Performer, Song ID 
-	Clean up columns and removing unnecessary columns of data that won’t be used and making the remaining columns uniform. 
-	Reduce data to ‘Top 40 songs’ Locked onto items who’s “Week Position” was ever 40 or more Used loc on “Week Position” for those >= 40 When sorted in ascending order, Imagine Dragons, Radioactive took first place with 84 weeks in the Top 40 
-	Reduce columns down to what each individual will use Created a new dataframe specific to each person’s designated attribute to research primarily, designated song attributes and duration songs are in top 40 
-	Used dropna on ONLY columns that each person was actually using Using dropna on the whole dataframe left us with 5 rows of data Using dropna ONLY on the columns used left each person with ~120,000 rows
- Remove outlires for more efficient data
-	Use final data sets to organize, compare, and create visualizations to show the impact each attribute has on a song’s placement in the top 40


<div align="center">
<img src="Energy Data/Visuals/energy-weeks bar.png" width="400"> <img src="Energy Data/Visuals/energy heatmap2.png" width="400">
<img src="Energy Data/Visuals/energy final box.png" width="400">
</div>


Members:

[Laura Rice](https://github.com/LRiceBall)

[Gianni Adamo](https://github.com/gianx1)

[Adam McVey](https://github.com/adamemcvey)

[Matthew Berkley](https://github.com/mberkley25)
