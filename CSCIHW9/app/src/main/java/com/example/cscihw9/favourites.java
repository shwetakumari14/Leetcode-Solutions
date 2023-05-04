package com.example.cscihw9;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.Map;

public class favourites extends Fragment {

    private SharedPreferences sharedPreferences;
    private RecyclerView recyclerView;
    private ArrayList<EventData> eventData = new ArrayList<>();

    private FavouritesAdapter favouritesAdapter;

    public favourites() {
        // Required empty public constructor
    }

    @Override
    public void onResume(){
        setFavView(new View[]{this.getView()});
        super.onResume();
    }


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View[] view = {inflater.inflate(R.layout.fragment_favourites, container, false)};
        setFavView(view);
        return view[0];
    }

    public void setFavView(View[] view){
        SharedPreferences sharedPreferences = requireContext().getApplicationContext().getSharedPreferences("fav_pref", Context.MODE_PRIVATE);

        eventData = new ArrayList<>();
        Map<String, ?> allEntries = sharedPreferences.getAll();
        for (Map.Entry<String, ?> entry : allEntries.entrySet()) {
            String eventDataJsonString = (String) entry.getValue();
            EventData favEvents = new Gson().fromJson(eventDataJsonString, EventData.class);
            eventData.add(favEvents);
        }
        TextView noFav = view[0].findViewById(R.id.noFav);
        recyclerView = view[0].findViewById(R.id.recyclerView3);

        recyclerView.setVisibility(View.VISIBLE);

        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        favouritesAdapter = new FavouritesAdapter(eventData, getContext());
        favouritesAdapter.registerAdapterDataObserver(new RecyclerView.AdapterDataObserver() {
            @Override
            public void onChanged() {
                super.onChanged();
                if(eventData.isEmpty()) {
                    noFav.setVisibility(View.VISIBLE);
                }
            }
        });
        recyclerView.setAdapter(favouritesAdapter);

        if (eventData.isEmpty()) {
            noFav.setVisibility(View.VISIBLE);
        }else {
            noFav.setVisibility(View.GONE);
        }
    }
}