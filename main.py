from client_credentials import get_access_token
from get_playlist_data import get_trending_playlist_data
from recommendations import hybrid_recommendations

# add your Client ID and Client Secret to get spotify access token 
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

if access_token:
    # Test with a playlist ID (any playlist of your choice)
    playlist_id = '1pyxHenAhYqXGrDrzZqJay'

    # Get playlist data
    music_df = get_trending_playlist_data(playlist_id, access_token)

    # Display the DataFrame
    print(music_df)

    # Test recommendations
    input_song_name = "tolerate it"
    recommendations = hybrid_recommendations(input_song_name, num_recommendations=10)
    print(f"Hybrid recommended songs for '{input_song_name}':")
    print(recommendations)
