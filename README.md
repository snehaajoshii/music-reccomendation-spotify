# music-reccomendation-spotify
 Music Recommendation System to discovere new and relevant musical content based on preferences and listening behaviour.

#### Before running the application, make sure you have the following:

- Spotify Developer Account
- Client ID and Client Secret obtained from Spotify Developer Dashboard

### Usage
The main.py script demonstrates the usage of the recommendation system. It fetches data from a specified playlist, displays the playlist information, and provides hybrid recommendations for a selected song.

Adjust the CLIENT_ID and CLIENT_SECRET in main.py with your Spotify Developer credentials.

### Files
main.py: Entry point for testing the recommendation system.
client_credentials.py: Helper module to obtain Spotify access token.
get_playlist_data.py: Retrieves trending playlist data using the Spotify API.
recommendations.py: Contains functions for content-based and hybrid recommendations.

### Functionality
Content-Based Filtering: Recommends songs based on the similarity of music features (e.g., danceability, energy) to a given input song.
Hybrid Recommendations: Combines content-based recommendations with a weighted popularity score, considering the release date of the song.

### Notes
This project assumes access to the Spotify API. Ensure you have the required permissions and API access.
Adjust the playlist ID and access token in main.py for testing with different playlists.


