package com.example.cscihw9;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;
import androidx.viewpager2.widget.ViewPager2;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.android.material.tabs.TabLayout;
import com.google.android.material.tabs.TabLayoutMediator;

import java.util.ArrayList;

public class EventDetails extends AppCompatActivity {
    private ImageView backFlowBtn;
    private TextView backFlowText;
    private ImageView facebookBtn;
    private ImageView twitterBtn;
    private ImageView favIcon2;
    private String[] detailsTabs = new String[]{"DETAILS", "ARTIST(S)", "VENUE"};
    private int[] detailsIcons = new int[]{R.drawable.detail, R.drawable.artist, R.drawable.venue};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_event_details);

        ViewPager2 viewPager = findViewById(R.id.viewPager2);
        EventAdapter adapter = new EventAdapter(this);
        viewPager.setAdapter(adapter);

        TabLayout tabLayout = findViewById(R.id.tabLayout2);
//        tabLayout.setupWithViewPager(viewPager);
        new TabLayoutMediator(tabLayout, viewPager, (tab, position) -> {
            tab.setIcon(detailsIcons[position]);
            tab.setText(detailsTabs[position]);
        }).attach();

        backFlowBtn = findViewById(R.id.backFlowBtn);
        backFlowText = findViewById(R.id.backFlowText);
        facebookBtn = findViewById(R.id.facebookBtn);
        twitterBtn = findViewById(R.id.twitterBtn);
        favIcon2 = findViewById(R.id.favIcon2);

        backFlowBtn.setOnClickListener(new View.OnClickListener() {
            boolean isFav = false;
            @Override
            public void onClick(View view) {
                // Handle click event
                onBackPressed();
            }
        });

        ArrayList<DetailsData> detailsData = Common.getDetailsData();

        if (!detailsData.isEmpty()) {
            DetailsData details = detailsData.get(0);
            backFlowText.setText(details.getArtist());
            backFlowText.setSelected(true);

            String ticketUrl = details.getTicket_location();
            String eventName = details.getEvent_name();

            facebookBtn.setOnClickListener(new View.OnClickListener() {
                boolean isFav = false;
                @Override
                public void onClick(View view) {
                    // Handle click event
                    String fbUrl = "https://www.facebook.com/sharer/sharer.php?u=" +  ticketUrl;
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(fbUrl));
                    view.getContext().startActivity(intent);

                }
            });


            twitterBtn.setOnClickListener(new View.OnClickListener() {
                boolean isFav = false;
                @Override
                public void onClick(View view) {
                    // Handle click event
                    String twitterUrl =  "https://twitter.com/intent/tweet?url=" + ticketUrl + "&text=Check%20" +  eventName + "%20on%20Ticketmaster!";
                    Intent intent2 = new Intent(Intent.ACTION_VIEW, Uri.parse(twitterUrl));
                    view.getContext().startActivity(intent2);

                }
            });
        }

    }
}