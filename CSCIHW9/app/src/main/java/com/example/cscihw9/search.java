package com.example.cscihw9;

import android.content.res.ColorStateList;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.fragment.NavHostFragment;

import android.os.Parcelable;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.CompoundButton;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.snackbar.Snackbar;

import android.widget.EditText;
import android.widget.Spinner;
import android.widget.ArrayAdapter;
import android.widget.AdapterView;
import android.widget.Switch;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.lang.reflect.Array;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class search extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private AutoCompleteTextView autoCompleteTextView;
    private ArrayAdapter<String> adapter;

    private String lat;
    private String lng;
    private Boolean AutoDetect = false;

    private String category;
    public search() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_search, container, false);
        //Spinner filling
        Spinner mySpinner = view.findViewById(R.id.category);
        ArrayAdapter<String> myAdapter = new ArrayAdapter<String>(getContext(), R.layout.spinner_design, new String[]{"All", "Music", "Sports", "Arts & Theatre", "Film", "Miscellaneous"});
        myAdapter.setDropDownViewResource(R.layout.spinner_background);
        mySpinner.setAdapter(myAdapter);
        // Set up the OnItemSelectedListener to get the selected item
        mySpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                category = parent.getItemAtPosition(position).toString();
                // Do something with the selected item
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                // Do nothing
            }
        });

        EditText keyword = view.findViewById(R.id.keyword);

        //Auto Detect Check
        Switch autoDetectSwitch = view.findViewById(R.id.autoDetect);
        EditText location = view.findViewById(R.id.location);
        autoDetectSwitch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    if (location.getVisibility() == View.VISIBLE) {
                        location.setVisibility(View.GONE);
                    }
                    AutoDetect = true;
                } else {
                    location.setVisibility(View.VISIBLE);
                    AutoDetect = false;
                }
            }
        });

        //Auto complete
        autoCompleteTextView = view.findViewById(R.id.keyword);
        adapter = new ArrayAdapter<>(getContext(), android.R.layout.simple_dropdown_item_1line);
        autoCompleteTextView.setAdapter(adapter);
        autoCompleteTextView.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                adapter.getFilter().filter(s);
                String text = autoCompleteTextView.getText().toString();
                getAutoComplete(text, autoCompleteTextView);
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });

        NavController navController = NavHostFragment.findNavController(this);

        //Clear Button
        Button clearButton = view.findViewById(R.id.clear);
        clearButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Set the switch value to default
                clear_data(view);
                //navController.navigate(R.id.action_search2_to_eventListing2);
            }
        });

        //Submit Button
        Button submitButton = view.findViewById(R.id.submit);
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Set the switch value to default
                EditText distance = view.findViewById(R.id.distance);
                if(distance.equals("")){
                    distance.setText("10");
                }
//                if (keyword.getText().toString().trim().isEmpty()) {
//                    Snackbar.make(view, "Please enter the keyword", Snackbar.LENGTH_SHORT).show();
//                }

                if (AutoDetect == true) {
                    RequestQueue queue = Volley.newRequestQueue(getContext());
                    String url = "https://ipinfo.io/json?token=697fc234a1cb06";
                    JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                            new Response.Listener<JSONObject>() {
                                @Override
                                public void onResponse(JSONObject response) {
                                    // Handle the API response
                                    try {
                                        String temp = response.getString("loc");
                                        String[] coordinates = temp.split(",");
                                        lat = coordinates[0];
                                        lng = coordinates[1];
                                        RequestQueue queue = Volley.newRequestQueue(getContext());
                                        String url = "https://web-sh-hw8.uc.r.appspot.com/events_listing/?keyword=" + keyword.getText().toString() + "&radius=" + distance.getText().toString() + "&category=" + category + "&latitude=" + lat + "&longitude=" + lng;
                                        Log.d("--- event listing url ---- ", url);
                                        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                                                new Response.Listener<JSONObject>() {
                                                    @Override
                                                    public void onResponse(JSONObject response) {
                                                        // Handle the API response
                                                        try {
                                                            JSONArray finalData = response.getJSONArray("finalData");
                                                            ArrayList<EventData> listingData = new ArrayList<EventData>();

                                                            for (int i = 0; i < finalData.length(); i++) {
                                                                JSONObject data = finalData.getJSONObject(i);
                                                                // Do something with the dataObject, such as accessing its properties
                                                                JSONArray dates  = data.getJSONArray("date");
                                                                String date = dates.getString(0);
                                                                String inputTime = dates.getString(1);
                                                                SimpleDateFormat inputFormat = new SimpleDateFormat("HH:mm:ss");
                                                                Date dateFormat = inputFormat.parse(inputTime);
                                                                SimpleDateFormat outputFormat = new SimpleDateFormat("hh:mm a");
                                                                String time = outputFormat.format(dateFormat);
                                                                String icons = data.getString("icons");
                                                                String events = data.getString("events");
                                                                String genres = data.getString("genres");
                                                                String venues = data.getString("venues");
                                                                String ids = data.getString("ids");
                                                                EventData obj = new EventData(date, time, icons, events, genres, venues, ids);
                                                                listingData.add(obj);
                                                            }
                                                            Common.eventlistingData = listingData;
                                                            navController.navigate(R.id.action_search2_to_eventListing2);
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
                                    } catch (JSONException e) {
                                        throw new RuntimeException(e);
                                    }

                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // Handle errors
                        }
                    });
                    queue.add(jsonObjectRequest);
                } else {
                        RequestQueue queue = Volley.newRequestQueue(getContext());
                        String url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location.getText().toString() + "&key=AIzaSyA-rLDdLR91LXyvPjJqBS7YE2o2kR__Mlw";
                        Log.d("---- url ----- ", url);
                        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                                new Response.Listener<JSONObject>() {
                                    @Override
                                    public void onResponse(JSONObject response) {
                                        // Handle the API response
                                        try {
                                            String status = response.getString("status");
                                            if (status.equals("OK")) {
                                                JSONArray result = response.getJSONArray("results");
                                                JSONObject resultFirst = result.getJSONObject(0);
                                                JSONObject geometry = resultFirst.getJSONObject("geometry");
                                                JSONObject geoLoc = geometry.getJSONObject("location");
                                                Double x = geoLoc.getDouble("lat");
                                                Double y = geoLoc.getDouble("lng");
                                                lat = Double.toString(x);
                                                lng = Double.toString(y);

                                                RequestQueue queue = Volley.newRequestQueue(getContext());
                                                String url = "https://web-sh-hw8.uc.r.appspot.com/events_listing/?keyword=" + keyword.getText().toString() + "&radius=" + distance.getText().toString() + "&category=" + category + "&latitude=" + lat + "&longitude=" + lng;
                                                Log.d("--- event listing url ---- ", url);
                                                JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                                                        new Response.Listener<JSONObject>() {
                                                            @Override
                                                            public void onResponse(JSONObject response) {
                                                                // Handle the API response
                                                                try {
                                                                    JSONArray finalData = response.getJSONArray("finalData");
                                                                    ArrayList<EventData> listingData = new ArrayList<EventData>();

                                                                    for (int i = 0; i < finalData.length(); i++) {
                                                                        JSONObject data = finalData.getJSONObject(i);
                                                                        // Do something with the dataObject, such as accessing its properties
                                                                        JSONArray dates  = data.getJSONArray("date");
                                                                        String date = dates.getString(0);
                                                                        String time = dates.getString(1);
                                                                        String icons = data.getString("icons");
                                                                        String events = data.getString("events");
                                                                        String genres = data.getString("genres");
                                                                        String venues = data.getString("venues");
                                                                        String ids = data.getString("ids");
                                                                        EventData obj = new EventData(date, time, icons, events, genres, venues, ids);
                                                                        listingData.add(obj);
                                                                    }
                                                                    Common.eventlistingData = listingData;
                                                                    navController.navigate(R.id.action_search2_to_eventListing2);
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
                                                queue.add(jsonObjectRequest);

                                            }
                                        } catch (JSONException e) {
                                            Log.d("---- errror ----- ", e.toString());
                                            throw new RuntimeException(e);
                                        }
                                    }
                                }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // Handle errors
                            }
                        });
                        queue.add(jsonObjectRequest);
                }
            }
        });

        return view;
    }

//    private FragmentManager getChildFragmentManager() {
//        return null;
//    }

    public void getAutoComplete(String text, AutoCompleteTextView keyword_auto)
    {

        RequestQueue queue_autoCom = Volley.newRequestQueue(getContext());
        String url = "http://10.0.2.2:3001/autocomplete/?keyword=" + text;
        ArrayList<String> suggestions = new ArrayList<String>();

        JsonObjectRequest request_autoCom = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try
                        {
                            JSONArray keywords = response.getJSONArray("keywords");
                            for (int i = 0; i < keywords.length(); i++) {
                                suggestions.add(keywords.getString(i));
                            }

                            adapter.clear();
                            adapter.addAll(suggestions);
                            adapter.notifyDataSetChanged();
                        }
                        catch(Throwable t){
                            Log.e("getAutoCom" , "Not JSONify");
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("getAutoCom" ,error.toString());
            }
        });

        queue_autoCom.add(request_autoCom);
        return;
    }
    public void clear_data(View view){
        EditText keyword = view.findViewById(R.id.keyword);
        keyword.setText("");
        EditText distance = view.findViewById(R.id.distance);
        distance.setText("10");
        EditText location = view.findViewById(R.id.location);
        location.setText("");
        Switch autoDetect = view.findViewById(R.id.autoDetect);
        autoDetect.setChecked(false);
        Spinner spinner = view.findViewById(R.id.category);
        ArrayAdapter<String> myAdapter = new ArrayAdapter<String>(getContext(), R.layout.spinner_design, new String[]{"All", "Music", "Sports", "Arts & Theatre", "Film", "Miscellaneous"});
        myAdapter.setDropDownViewResource(R.layout.spinner_background);
        spinner.setAdapter(myAdapter);
    }
    public void fetch_lat_long_from_ip(){

        RequestQueue queue = Volley.newRequestQueue(getContext());
        String url = "https://ipinfo.io/json?token=697fc234a1cb06";
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Handle the API response
                        try {
                            String temp = response.getString("loc");
                            String[] coordinates = temp.split(",");
                            lat = coordinates[0];
                            lng = coordinates[1];
                        } catch (JSONException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // Handle errors
            }
        });
        queue.add(jsonObjectRequest);
    }
    public void fetch_lat_long_from_location(String location){
        RequestQueue queue = Volley.newRequestQueue(getContext());
        String url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyA-rLDdLR91LXyvPjJqBS7YE2o2kR__Mlw";
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Handle the API response
                        try {
                            String status = response.getString("status");
                            if (status.equals("OK")) {
                                JSONArray result = response.getJSONArray("results");
                                JSONObject resultFirst = result.getJSONObject(0);
                                JSONObject geometry = resultFirst.getJSONObject("geometry");
                                JSONObject geoLoc = geometry.getJSONObject("location");
                                Double x = geoLoc.getDouble("lat");
                                Double y = geoLoc.getDouble("lng");
                                lat = Double.toString(x);
                                lng = Double.toString(y);
                            }
                        } catch (JSONException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // Handle errors
            }
        });
        queue.add(jsonObjectRequest);
    }

//    public void get_event_listing_data(String keyword, String distance){
//
//        RequestQueue queue = Volley.newRequestQueue(getContext());
//        String url = "https://web-sh-hw8.uc.r.appspot.com/events_listing/?keyword=" + keyword + "&radius=" + distance + "&category=" + category + "&latitude=" + lat + "&longitude=" + lng;
//        Log.d("--- event listing url ---- ", url);
//        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Request.Method.GET, url, null,
//                new Response.Listener<JSONObject>() {
//                    @Override
//                    public void onResponse(JSONObject response) {
//                        // Handle the API response
//                        Log.d("--- result ---- ", response.toString());
//                        try {
//                            JSONArray finalData = response.getJSONArray("finalData");
//                            ArrayList<EventData> listingData = new ArrayList<EventData>();
//
//                            for (int i = 0; i < finalData.length(); i++) {
//                                JSONObject data = finalData.getJSONObject(i);
//                                // Do something with the dataObject, such as accessing its properties
//                                JSONArray dates  = data.getJSONArray("date");
//                                String date = dates.getString(0);
//                                String time = dates.getString(1);
//                                String icons = data.getString("icons");
//                                String events = data.getString("events");
//                                String genres = data.getString("genres");
//                                String venues = data.getString("venues");
//                                String ids = data.getString("ids");
//                                EventData obj = new EventData(date, time, icons, events, genres, venues, ids);
//                                listingData.add(obj);
//                                Log.d("---- date ----- ", date);
//                                Log.d("---- time ----- ", time);
//                                Log.d("---- icons ----- ", icons);
//                                Log.d("---- events ----- ", events);
//                                Log.d("---- genres ----- ", genres);
//                                Log.d("---- venues ----- ", venues);
//                                Log.d("---- ids ----- ", ids);
//                            }
//
//                        } catch (JSONException e) {
//                            throw new RuntimeException(e);
//                        }
//                    }
//                }, new Response.ErrorListener() {
//            @Override
//            public void onErrorResponse(VolleyError error) {
//                Log.d("--- error ---- ", error.toString());
//                // Handle errors
//            }
//        });
//        queue.add(jsonObjectRequest);
//    }
}