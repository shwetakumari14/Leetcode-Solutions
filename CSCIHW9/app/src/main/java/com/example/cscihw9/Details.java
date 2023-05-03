package com.example.cscihw9;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class Details extends Fragment {
    private TextView artistName;
    private TextView venueName;
    private TextView artistDate;
    private TextView artistTime;
    private TextView artistGenre;
    private TextView artistPrice;
    private TextView ticketStatus;
    private TextView ticketURL;
    private ImageView stadiumPic;
    private ArrayList<DetailsData> detailsData;

    public Details() {
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
        View view = inflater.inflate(R.layout.fragment_details, container, false);
        artistName = view.findViewById(R.id.artistName);
        venueName = view.findViewById(R.id.venueName);
        artistDate = view.findViewById(R.id.artistDate);
        artistTime = view.findViewById(R.id.artistTime);
        artistGenre = view.findViewById(R.id.artistGenre);
        artistPrice = view.findViewById(R.id.artistPrice);
        ticketStatus = view.findViewById(R.id.ticketStatus);
        ticketURL = view.findViewById(R.id.ticketURL);
        stadiumPic = view.findViewById(R.id.stadiumPic);

        detailsData = Common.getDetailsData();

        if (!detailsData.isEmpty()) {
            DetailsData details = detailsData.get(0);

            String date = details.getDate();
            if (date.isEmpty()) {
                artistDate.setVisibility(View.GONE);
            } else {
                artistDate.setText(date);
            }

            String time = details.getTime();
            if (time.isEmpty()) {
                artistTime.setVisibility(View.GONE);
            } else {
                artistTime.setText(time);
            }

            String artist = details.getArtist();
            if (artist.isEmpty()) {
                artistName.setVisibility(View.GONE);
            } else {
                artistName.setText(artist);
                artistName.setSelected(true);
            }

            String venue = details.getVenue();
            if (venue.isEmpty()) {
                venueName.setVisibility(View.GONE);
            } else {
                venueName.setText(venue);
                venueName.setSelected(true);
            }

            String genre = details.getGenre();
            if (genre.isEmpty()) {
                artistGenre.setVisibility(View.GONE);
            } else {
                artistGenre.setText(genre);
                artistGenre.setSelected(true);
            }

            String price = details.getPrice_range();
            if (price.isEmpty()) {
                artistPrice.setVisibility(View.GONE);
            } else {
                artistPrice.setText(price);
            }

            String ticketText = details.getTicket_text();
            if (ticketText.isEmpty()) {
                ticketStatus.setVisibility(View.GONE);
            } else {
                ticketStatus.setText(ticketText);
                if (ticketText.equals("On Sale")){
                    ticketStatus.setBackgroundColor(getResources().getColor(R.color.green_100));
                }
                if (ticketText.equals("Off Sale")){
                    ticketStatus.setBackgroundColor(getResources().getColor(R.color.red));
                }
                if (ticketText.equals("Canceled")){
                    ticketStatus.setBackgroundColor(getResources().getColor(R.color.black));
                }
                if (ticketText.equals("Postponed")){
                    ticketStatus.setBackgroundColor(getResources().getColor(R.color.orange));
                }
                if (ticketText.equals("Rescheduled")){
                    ticketStatus.setBackgroundColor(getResources().getColor(R.color.orange));
                }
            }

            String ticketUrl = details.getTicket_location();
            if (ticketUrl.isEmpty()) {
                ticketURL.setVisibility(View.GONE);
            } else {
                ticketURL.setText(ticketUrl);
                ticketURL.setSelected(true);

                ticketURL.setOnClickListener(new View.OnClickListener() {
                    boolean isFav = false;
                    @Override
                    public void onClick(View view) {
                        // Handle click event
                        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(ticketUrl));
                        view.getContext().startActivity(intent);

                    }
                });
            }

            String stadium_pic = details.getStadium_img();
            if (stadium_pic.isEmpty()) {
                stadiumPic.setVisibility(View.GONE);
            } else {
                Picasso.get().load(stadium_pic).into(stadiumPic);
            }
        }
        return view;
    }
}