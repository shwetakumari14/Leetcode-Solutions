package com.example.cscihw9;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TableRow;
import android.widget.TextView;

import java.util.ArrayList;

public class Venue extends Fragment {

    private TextView venueCardName;
    private TextView address;
    private TextView city;
    private TextView phoneNum;
    private TextView openHoursText;
    private TextView generalRulesText;
    private TextView childRulesText;

    private TableRow phoneNumRow;

    private ArrayList<VenueData> venueData;
    public Venue() {
        // Required empty public constructor
    }



    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_venue, container, false);
        venueCardName = view.findViewById(R.id.venueCardName);
        address = view.findViewById(R.id.address);
        city = view.findViewById(R.id.city);
        phoneNum = view.findViewById(R.id.phoneNum);
        openHoursText = view.findViewById(R.id.openHoursText);
        generalRulesText = view.findViewById(R.id.generalRulesText);
        childRulesText = view.findViewById(R.id.childRulesText);
        phoneNumRow = view.findViewById(R.id.phoneNumRow);

        venueData = Common.getVenueData();

        if (!venueData.isEmpty()) {
            VenueData venues = venueData.get(0);

            String venueName = venues.getVenueName();
            if (venueName.isEmpty()) {
                venueCardName.setVisibility(View.GONE);
            } else {
                venueCardName.setText(venueName);
            }

            String addressName = venues.getAddress();
            if (addressName.isEmpty()) {
                address.setVisibility(View.GONE);
            } else {
                address.setText(addressName);
            }

            String input = venues.getPhone_number();
            String phone = input.trim();
            if (phone.isEmpty()) {
                phoneNumRow.setVisibility(View.GONE);
            } else {
                phoneNum.setText(phone);
            }

            String cityName = venues.getCity();
            if (cityName.isEmpty()) {
                city.setVisibility(View.GONE);
            } else {
                city.setText(cityName);
            }

            String open = venues.getOpen_hours_detail();
            if (open.isEmpty()) {
                openHoursText.setVisibility(View.GONE);
            } else {
                openHoursText.setText(open);

                openHoursText.setOnClickListener(new View.OnClickListener() {
                    boolean isFav = false;
                    @Override
                    public void onClick(View view) {
                        // Handle click event
                        if(openHoursText.getMaxLines() == 3) {
                            openHoursText.setMaxLines(Integer.MAX_VALUE);
                        }else {
                            openHoursText.setMaxLines(3);
                        }
                    }
                });
            }

            String general = venues.getGeneral_rule();
            if (general.isEmpty()) {
                generalRulesText.setVisibility(View.GONE);
            } else {
                generalRulesText.setText(general);

                generalRulesText.setOnClickListener(new View.OnClickListener() {
                    boolean isFav = false;
                    @Override
                    public void onClick(View view) {
                        // Handle click event
                        if(generalRulesText.getMaxLines() == 3) {
                            generalRulesText.setMaxLines(Integer.MAX_VALUE);
                        }else {
                            generalRulesText.setMaxLines(3);
                        }
                    }
                });
            }

            String child = venues.getChild_rule();
            if (child.isEmpty()) {
                childRulesText.setVisibility(View.GONE);
            } else {
                childRulesText.setText(child);

                childRulesText.setOnClickListener(new View.OnClickListener() {
                    boolean isFav = false;
                    @Override
                    public void onClick(View view) {
                        // Handle click event
                        if(childRulesText.getMaxLines() == 3) {
                            childRulesText.setMaxLines(Integer.MAX_VALUE);
                        }else {
                            childRulesText.setMaxLines(3);
                        }
                    }
                });
            }

            Double lat = venues.getVenueLat();
            float latFloat = lat.floatValue();
            Double lng = venues.getVenueLong();
            float lngFloat = lng.floatValue();
            MapsFragment googleMapsFragment = new MapsFragment();
            googleMapsFragment.setLatLon(latFloat, lngFloat);
            getChildFragmentManager().beginTransaction()
                    .replace(R.id.venueMap, googleMapsFragment)
                    .commit();
        }

        return view;
    }
}