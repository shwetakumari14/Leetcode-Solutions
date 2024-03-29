package com.example.cscihw9;

public class EventData {
    private String  date;
    private String time;
    private String icons;
    private String events;
    private String genres;
    private String venues;
    private String ids;

    private Boolean isFav;


    public EventData(String date, String time, String icons, String events, String genres, String venues, String ids, Boolean isFav) {
        this.date = date;
        this.time = time;
        this.icons = icons;
        this.events = events;
        this.genres = genres;
        this.venues = venues;
        this.ids = ids;
        this.isFav = isFav;
    }


    public void setIsFav(Boolean isFav) {
        this.isFav = isFav;
    }
    public String getDate() {return date;}
    public String getTime() {return time;}
    public String getIcons() {
        return icons;
    }
    public String getEvents() {
        return events;
    }
    public String getGenres() {
        return genres;
    }
    public String getVenues() {
        return venues;
    }
    public String getIds() {
        return ids;
    }

    public Boolean getIsFav(){return isFav;}

}
