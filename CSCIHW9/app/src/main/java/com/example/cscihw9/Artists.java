package com.example.cscihw9;

import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

public class Artists extends Fragment implements ArtistAdapter.OnItemClickListener {

    private RecyclerView recyclerView2;

    private ArtistAdapter artistAdapter;
    private ArrayList<ArtistsData> artistsData = new ArrayList<>();
    public Artists() {
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
        View view =  inflater.inflate(R.layout.artist_layout, container, false);

        TextView noMusic = view.findViewById(R.id.noMusicResult);
        recyclerView2 = view.findViewById(R.id.recyclerView2);
        recyclerView2.setVisibility(View.VISIBLE);

        recyclerView2.setLayoutManager(new LinearLayoutManager(getContext()));
        artistAdapter = new ArtistAdapter(artistsData, this);
        recyclerView2.setAdapter(artistAdapter);



        ArrayList<ArtistsData> artistsData1 = Common.getArtistsData();
        if (!artistsData1.isEmpty()) {
            Log.d("---- listingData ----- ", " true ");
            noMusic.setVisibility(View.GONE);
            for (int i = 0; i < artistsData1.size(); i++) {
                ArtistsData art = artistsData1.get(i);
                artistsData.add(new ArtistsData(art.getArtist_name(), art.getPopularity(), art.getFollowers(), art.getSpotify_link(), art.getArtist_img(), art.getAlbumsOne(), art.getAlbumsTwo(), art.getAlbumsThree()));
            }
        }else {
            Log.d("---- visibility ----- ", noMusic.toString());
            noMusic.setVisibility(View.VISIBLE);
        }
        artistAdapter.notifyDataSetChanged();
        return view;
    }

    @Override
    public void onItemClick(ArtistsData artistsData) {

    }
}