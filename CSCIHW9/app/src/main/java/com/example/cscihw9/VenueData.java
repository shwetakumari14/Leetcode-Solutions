package com.example.cscihw9;

public class VenueData {
    private String  venueName;
    private String address;
    private String phone_number;
    private String city;
    private String upcoming_events;
    private String venue_img;
    private String open_hours_detail;
    private String general_rule;
    private String child_rule;
    private Double venueLat;
    private Double venueLong;


    public VenueData(String venueName, String address, String phone_number, String city, String upcoming_events, String venue_img, String open_hours_detail, String general_rule, String child_rule, Double venueLat, Double venueLong) {
        this.venueName = venueName;
        this.address = address;
        this.phone_number = phone_number;
        this.city = city;
        this.upcoming_events = upcoming_events;
        this.venue_img = venue_img;
        this.open_hours_detail = open_hours_detail;
        this.general_rule = general_rule;
        this.child_rule = child_rule;
        this.venueLat = venueLat;
        this.venueLong = venueLong;
    }


    public String getVenueName() {return venueName;}
    public String getAddress() {return address;}
    public String getPhone_number() {
        return phone_number;
    }
    public String getCity() {
        return city;
    }
    public String getUpcoming_events() {
        return upcoming_events;
    }
    public String getVenue_img() {
        return venue_img;
    }
    public String getOpen_hours_detail() {
        return open_hours_detail;
    }
    public String getGeneral_rule() {
        return general_rule;
    }
    public String getChild_rule() {
        return child_rule;
    }
    public Double getVenueLat() {
        return venueLat;
    }
    public Double getVenueLong() {
        return venueLong;
    }

}
