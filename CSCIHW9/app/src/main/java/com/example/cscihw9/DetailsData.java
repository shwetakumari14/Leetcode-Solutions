package com.example.cscihw9;

public class DetailsData {
    private String  date;
    private String time;
    private String artist;
    private String venue;
    private String genre;
    private String price_range;
    private String ticket_style;
    private String ticket_text;
    private String ticket_location;
    private String stadium_img;
    private String event_name;
    private String event_ID;


    public DetailsData(String date, String time, String artist, String venue, String genre, String price_range, String ticket_style, String ticket_text, String ticket_location, String stadium_img, String event_name, String event_ID) {
        this.date = date;
        this.time = time;
        this.artist = artist;
        this.venue = venue;
        this.genre = genre;
        this.price_range = price_range;
        this.ticket_style = ticket_style;
        this.ticket_text = ticket_text;
        this.ticket_location = ticket_location;
        this.stadium_img = stadium_img;
        this.event_name = event_name;
        this.event_ID = event_ID;
    }


    public String getDate() {return date;}
    public String getTime() {return time;}
    public String getArtist() {
        return artist;
    }
    public String getVenue() {
        return venue;
    }
    public String getGenre() {
        return genre;
    }
    public String getPrice_range() {
        return price_range;
    }
    public String getTicket_style() {
        return ticket_style;
    }
    public String getTicket_text() {
        return ticket_text;
    }
    public String getTicket_location() {
        return ticket_location;
    }
    public String getStadium_img() {
        return stadium_img;
    }
    public String getEvent_name() {
        return event_name;
    }
    public String getEvent_ID() {
        return event_ID;
    }

}
