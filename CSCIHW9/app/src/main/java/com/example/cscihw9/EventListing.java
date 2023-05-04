package com.example.cscihw9;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.fragment.app.Fragment;
import androidx.navigation.NavController;
import androidx.navigation.fragment.NavHostFragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class EventListing extends Fragment implements EventListingAdapter.OnItemClickListener {
    ArrayList<EventData> listingData;
    private RecyclerView recyclerView;
    private ImageView backBtn;
    private TextView backBtnText;
    private ProgressBar detailsProgress;
    private NavController navController;
    private EventListingAdapter eventListingAdapter;
    private ArrayList<EventData> eventData = new ArrayList<>();
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public void onResume() {
        recyclerView = this.getView().findViewById(R.id.recyclerView);
        eventListingAdapter = new EventListingAdapter(eventData, this, getContext());
        recyclerView.setAdapter(eventListingAdapter);
        super.onResume();
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.listing_layout, container, false);
        navController = NavHostFragment.findNavController(this);
        backBtn = view.findViewById(R.id.backBtn);
        backBtnText = view.findViewById(R.id.backBtnText);
        TextView noResults = view.findViewById(R.id.noResult);
        detailsProgress = view.findViewById(R.id.detailsProgress);
        recyclerView = view.findViewById(R.id.recyclerView);

        backBtn.setVisibility(View.VISIBLE);
        backBtnText.setVisibility(View.VISIBLE);
        recyclerView.setVisibility(View.VISIBLE);
        detailsProgress.setVisibility(View.GONE);



        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        eventListingAdapter = new EventListingAdapter(eventData, this, getContext());
        recyclerView.setAdapter(eventListingAdapter);

        listingData = Common.getEventData();
        if (!listingData.isEmpty()) {
            noResults.setVisibility(View.GONE);
            for (int i = 0; i < listingData.size(); i++) {
                EventData event = listingData.get(i);
                eventData.add(new EventData(event.getDate(), event.getTime(), event.getIcons(), event.getEvents(), event.getGenres(), event.getVenues(), event.getIds(), false));
            }
            eventData.sort((eventNew, val) -> {
                if(eventNew.getDate().equals(val.getDate())) {
                    return eventNew.getTime().compareTo(val.getTime());
                }
                return eventNew.getTime().compareTo(val.getDate());
            });
        }else {
            noResults.setVisibility(View.VISIBLE);
        }
        eventListingAdapter.notifyDataSetChanged();



        backBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                navController.navigate(R.id.action_eventListing2_to_search23);
            }
        });

        return view;
    }

    @Override
    public void onItemClick(EventData eventData) {
        // handle the item click here

//        Bundle eventID = new Bundle();
//        eventID.putString("eventID", eventData.getIds());
        Log.d("----- item clicked ----- ", eventData.getIds());
//        backBtn.setVisibility(View.GONE);
//        backBtnText.setVisibility(View.GONE);
//        recyclerView.setVisibility(View.GONE);
//        detailsProgress.setVisibility(View.VISIBLE);
        getEventDetails(eventData.getIds(), eventData.getGenres());
    }

    public void  getEventDetails(String eventID, String eventGenres){
        //Details Data
        RequestQueue queue = Volley.newRequestQueue(getContext());
        String url = "https://web-sh-hw8.uc.r.appspot.com/events_details/" + eventID;
        Log.d("--- event listing url ---- ", url);
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Handle the API response
                        try {
                            JSONArray finalData = response.getJSONArray("finalData");
                            ArrayList<DetailsData> detailsData = new ArrayList<DetailsData>();

                                JSONObject data = finalData.getJSONObject(0);
                                JSONArray dates  = data.getJSONArray("dates");
                                String inputDate = dates.getString(0);
                                LocalDate dateTemp = null;
                                if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                                    dateTemp = LocalDate.parse(inputDate);
                                }
                                String date = null;
                                if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                                    date = dateTemp.format(DateTimeFormatter.ofPattern("MMM d, yyyy", Locale.ENGLISH));
                                }
//                                String date = dates.getString(0);
                                String inputTime = dates.getString(1);
                                SimpleDateFormat inputFormat = new SimpleDateFormat("HH:mm:ss");
                                Date dateFormat = inputFormat.parse(inputTime);
                                SimpleDateFormat outputFormat = new SimpleDateFormat("hh:mm a");
                                String time = outputFormat.format(dateFormat);
                                String artist = data.getString("artist");
                                String venue = data.getString("venue");
                                String genre = data.getString("genre");
                                String price_range = data.getString("price_range");
                                String ticket_style = data.getString("ticket_style");
                                String ticket_text = data.getString("ticket_text");
                                String ticket_location = data.getString("ticket_location");
                                String stadium_img = data.getString("stadium_img");
                                String event_name = data.getString("event_name");
                                String id = data.getString("id");

                                Log.d("---- date ------ ", date);
                                Log.d("---- time ------ ", time);
                                Log.d("---- venue ------ ", venue);
                                Log.d("---- genre ------ ", genre);
                                Log.d("---- price_range ------ ", price_range);
                                Log.d("---- ticket_style ------ ", ticket_style);
                                Log.d("---- ticket_text ------ ", ticket_text);
                                Log.d("---- ticket_location ------ ", ticket_location);
                                Log.d("---- stadium_img ------ ", stadium_img);
                                Log.d("---- event_name ------ ", event_name);
                                Log.d("---- id ------ ", id);

                                DetailsData obj = new DetailsData(date, time, artist, venue, genre, price_range, ticket_style, ticket_text, ticket_location, stadium_img, event_name, id);
                                detailsData.add(obj);
                                Common.detailsData = detailsData;
                                navController.navigate(R.id.action_eventListing2_to_eventDetails);

                            Log.d("---- ************************************* ------ ", " ---- ************************************* ------ ");

                                //Artists Data
                                if(eventGenres.equals("Music")) {
                                    Log.d("---- calling ------ ", " Music ");
                                    getArtists(artist, venue);
                                }else{
                                    Log.d("---- calling ------ ", " No Music ");
                                    getVenue(venue);
                                }


                        } catch (JSONException e) {
                            throw new RuntimeException(e);
                        } catch (ParseException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("--- error ---- ", error.toString());
                // Handle errors
            }
        });
        queue.add(jsonObjectRequest);
    }

    public void getArtists(String artist, String venue){
        RequestQueue queue2 = Volley.newRequestQueue(getContext());
        String url2 = "https://web-sh-hw8.uc.r.appspot.com/artists_details/?keyword=" + artist;
        Log.d("--- artist url ---- ", url2);
        JsonObjectRequest jsonObjectRequest2 = new JsonObjectRequest(Request.Method.GET, url2, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Handle the API response
                        try {
                            JSONArray finalData2 = response.getJSONArray("finalData");
                            ArrayList<ArtistsData> artistsData = new ArrayList<ArtistsData>();

                            for (int i = 0; i < finalData2.length(); i++) {
                                JSONObject data = finalData2.getJSONObject(i);
                                JSONArray albums  = data.getJSONArray("artist_albums");
                                String albumOne = albums.getString(0);
                                String albumTwo = albums.getString(1);
                                String albumThree = albums.getString(2);
                                String artist_name = data.getString("artist_name");
                                int popular = data.getInt("popularity");
                                String popularity = String.valueOf(popular);
                                String numberStr = data.getString("followers");
                                double number = Double.parseDouble(numberStr.replaceAll(",", ""));
                                String followers;
                                if (number >= 1000000) {
                                    followers = String.format("%.0fM", number / 1000000);
                                } else if (number >= 1000) {
                                    followers = String.format("%.0fK", number / 1000);
                                } else {
                                    followers = numberStr;
                                }
                                String spotify_link = data.getString("spotify_link");
                                String artist_img = data.getString("artist_img");

                                Log.d("---- artist_name ------ ", artist_name);
                                Log.d("---- popularity ------ ", popularity);
                                Log.d("---- followers ------ ", followers);
                                Log.d("---- spotify_link ------ ", spotify_link);
                                Log.d("---- artist_img ------ ", artist_img);
                                Log.d("---- albumOne ------ ", albumOne);
                                Log.d("---- albumTwo ------ ", albumTwo);
                                Log.d("---- albumThree ------ ", albumThree);


                                ArtistsData obj = new ArtistsData(artist_name, popularity, followers, spotify_link, artist_img, albumOne, albumTwo, albumThree);
                                artistsData.add(obj);
                            }
                            Common.artistsData = artistsData;

                            Log.d("---- ************** Before Venue *********************** ------ ", " ---- ************************************* ------ ");

                            //Venue Data


                            RequestQueue queue3 = Volley.newRequestQueue(getContext());
                            String url3 = "https://web-sh-hw8.uc.r.appspot.com/venue_details/?venue=" + venue;
                            Log.d("--- venue url ---- ", url3);
                            JsonObjectRequest jsonObjectRequest3 = new JsonObjectRequest(Request.Method.GET, url3, null,
                                    new Response.Listener<JSONObject>() {
                                        @Override
                                        public void onResponse(JSONObject response) {
                                            // Handle the API response
                                            try {
                                                JSONArray finalData3 = response.getJSONArray("finalData");
                                                ArrayList<VenueData> venueData = new ArrayList<VenueData>();

                                                JSONObject data = finalData3.getJSONObject(0);
                                                String venue_name = data.getString("name");
                                                String addressTemp = data.getString("address");
                                                String[] parts = addressTemp.split(", ");
                                                String address = parts[0];
                                                String city = parts[1] + ", " + parts[2];
                                                String phone_number = data.getString("phone_number");
                                                String upcoming_events = data.getString("upcoming_events");
                                                String venue_img = data.getString("venue_img");
                                                String open_hours_detail = data.getString("open_hours_detail");
                                                String general_rule = data.getString("general_rule");
                                                String child_rule = data.getString("child_rule");
                                                double lat = data.getDouble("lat");
                                                double lng = data.getDouble("long");
//                                                                            String venueLat = String.valueOf(lat);
//                                                                            String venueLong =String.valueOf(lng);

                                                Log.d("---- venue_name ------ ", venue_name);
                                                Log.d("---- address ------ ", address);
                                                Log.d("---- phone_number ------ ", phone_number);
                                                Log.d("---- city ------ ", city);
                                                Log.d("---- upcoming_events ------ ", upcoming_events);
                                                Log.d("---- venue_img ------ ", venue_img);
                                                Log.d("---- open_hours_detail ------ ", open_hours_detail);
                                                Log.d("---- general_rule ------ ", general_rule);
                                                Log.d("---- child_rule ------ ", child_rule);
                                                Log.d("---- venueLat ------ ", String.valueOf(lat));
                                                Log.d("---- venueLong ------ ", String.valueOf(lng));


                                                VenueData obj = new VenueData(venue_name, address, phone_number, city, upcoming_events, venue_img, open_hours_detail, general_rule, child_rule, lat, lng);
                                                venueData.add(obj);

                                                Common.venueData = venueData;

                                                //Venue Data

                                            } catch (JSONException e) {
                                                throw new RuntimeException(e);
                                            }
                                        }
                                    }, new Response.ErrorListener() {
                                @Override
                                public void onErrorResponse(VolleyError error) {
                                    Log.d("--- error ---- ", error.toString());
                                    // Handle errors
                                }
                            });
                            queue3.add(jsonObjectRequest3);

                        } catch (JSONException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("--- error ---- ", error.toString());
                // Handle errors
            }
        });
        queue2.add(jsonObjectRequest2);
    }

    public void getVenue(String venue){
        Common.clearArtists();
        RequestQueue queue3 = Volley.newRequestQueue(getContext());
        String url3 = "https://web-sh-hw8.uc.r.appspot.com/venue_details/?venue=" + venue;
        Log.d("--- venue url ---- ", url3);
        JsonObjectRequest jsonObjectRequest3 = new JsonObjectRequest(Request.Method.GET, url3, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Handle the API response
                        try {
                            JSONArray finalData3 = response.getJSONArray("finalData");
                            ArrayList<VenueData> venueData = new ArrayList<VenueData>();

                            JSONObject data = finalData3.getJSONObject(0);
                            String venue_name = data.getString("name");
                            String addressTemp = data.getString("address");
                            String[] parts = addressTemp.split(", ");
                            String address = parts[0];
                            String city = parts[1] + ", " + parts[2];
                            String phone_number = data.getString("phone_number");
                            String upcoming_events = data.getString("upcoming_events");
                            String venue_img = data.getString("venue_img");
                            String open_hours_detail = data.getString("open_hours_detail");
                            String general_rule = data.getString("general_rule");
                            String child_rule = data.getString("child_rule");
                            double lat = data.getDouble("lat");
                            double lng = data.getDouble("long");
//                                                                            String venueLat = String.valueOf(lat);
//                                                                            String venueLong =String.valueOf(lng);

                            Log.d("---- venue_name ------ ", venue_name);
                            Log.d("---- address ------ ", address);
                            Log.d("---- phone_number ------ ", phone_number);
                            Log.d("---- city ------ ", city);
                            Log.d("---- upcoming_events ------ ", upcoming_events);
                            Log.d("---- venue_img ------ ", venue_img);
                            Log.d("---- open_hours_detail ------ ", open_hours_detail);
                            Log.d("---- general_rule ------ ", general_rule);
                            Log.d("---- child_rule ------ ", child_rule);
                            Log.d("---- venueLat ------ ", String.valueOf(lat));
                            Log.d("---- venueLong ------ ", String.valueOf(lng));


                            VenueData obj = new VenueData(venue_name, address, phone_number, city, upcoming_events, venue_img, open_hours_detail, general_rule, child_rule, lat, lng);
                            venueData.add(obj);

                            Common.venueData = venueData;

                            //Venue Data

                        } catch (JSONException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("--- error ---- ", error.toString());
                // Handle errors
            }
        });
        queue3.add(jsonObjectRequest3);
    }

}
