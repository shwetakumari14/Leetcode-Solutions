package com.example.cscihw9;

import java.lang.reflect.Array;

public class ArtistsData {
    private String  artist_name;
    private String popularity;
    private String followers;
    private String spotify_link;
    private String artist_img;
    private String albumsOne;
    private String albumsTwo;
    private String albumsThree;


    public ArtistsData(String artist_name, String popularity, String followers, String spotify_link, String artist_img, String albumsOne, String albumsTwo, String albumsThree) {
        this.artist_name = artist_name;
        this.popularity = popularity;
        this.followers = followers;
        this.spotify_link = spotify_link;
        this.artist_img = artist_img;
        this.albumsOne = albumsOne;
        this.albumsTwo = albumsTwo;
        this.albumsThree = albumsThree;
    }


    public String getArtist_name() {return artist_name;}
    public String getPopularity() {return popularity;}
    public String getFollowers() {
        return followers;
    }
    public String getSpotify_link() {
        return spotify_link;
    }
    public String getArtist_img() {
        return artist_img;
    }
    public String getAlbumsOne() {
        return albumsOne;
    }
    public String getAlbumsTwo() {
        return albumsTwo;
    }
    public String getAlbumsThree() {
        return albumsThree;
    }
}
