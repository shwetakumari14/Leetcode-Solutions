package com.example.cscihw9;

import java.util.ArrayList;

public class Common {

    static public ArrayList<EventData> eventlistingData;
    static public ArrayList<DetailsData> detailsData;
    static public ArrayList<ArtistsData> artistsData;
    static public ArrayList<VenueData> venueData;

    public Common() {
        eventlistingData = new ArrayList<>();
    }
    static public ArrayList<EventData> getEventData() {
        return eventlistingData;
    }

    static public void clearArtists() {
        artistsData = new ArrayList<ArtistsData>();
    }

    static public ArrayList<DetailsData> getDetailsData() {return detailsData;}
    static public ArrayList<ArtistsData> getArtistsData() {return artistsData;}
    static public ArrayList<VenueData> getVenueData() {return venueData;}
}
