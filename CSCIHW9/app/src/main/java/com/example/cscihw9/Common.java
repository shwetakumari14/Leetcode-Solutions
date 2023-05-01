package com.example.cscihw9;

import java.util.ArrayList;

public class Common {

    static public ArrayList<EventData> eventlistingData;

    public Common() {
        eventlistingData = new ArrayList<>();
    }

    public void setEventData(ArrayList<EventData> myObjects) {
        this.eventlistingData = myObjects;
    }

    static public ArrayList<EventData> getEventData() {
        return eventlistingData;
    }
}
