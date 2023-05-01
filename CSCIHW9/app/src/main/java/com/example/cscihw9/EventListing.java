package com.example.cscihw9;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
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

import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class EventListing extends Fragment implements EventListingAdapter.OnItemClickListener {
    private RecyclerView recyclerView;
    private EventListingAdapter eventListingAdapter;
    private ArrayList<EventData> eventData = new ArrayList<>();
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.listing_layout, container, false);
        NavController navController = NavHostFragment.findNavController(this);
        ImageView imageView = view.findViewById(R.id.backBtn);
        TextView noResults = view.findViewById(R.id.noResult);

        recyclerView = view.findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        eventListingAdapter = new EventListingAdapter(eventData, this);
        recyclerView.setAdapter(eventListingAdapter);

        Log.d("---- listingData before ----- ", " false ");
        ArrayList<EventData> listingData = Common.getEventData();
        if (!listingData.isEmpty()) {
            Log.d("---- listingData ----- ", " true ");
            noResults.setVisibility(View.GONE);
            for (int i = 0; i < listingData.size(); i++) {
                EventData event = listingData.get(i);
                eventData.add(new EventData(event.getDate(), event.getTime(), event.getIcons(), event.getEvents(), event.getGenres(), event.getVenues(), event.getIds()));
//                Log.d("---- date ----- ", event.getDate());
//                Log.d("---- time ----- ", event.getTime());
//                Log.d("---- icons ----- ", event.getIcons());
//                Log.d("---- events ----- ", event.getEvents());
//                Log.d("---- genres ----- ", event.getGenres());
//                Log.d("---- venues ----- ", event.getVenues());
//                Log.d("---- ids ----- ", event.getIds());
            }
        }else {
            Log.d("---- visibility ----- ", noResults.toString());
            noResults.setVisibility(View.VISIBLE);
        }
        eventListingAdapter.notifyDataSetChanged();



        imageView.setOnClickListener(new View.OnClickListener() {
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
        Log.d("----- item clicked ----- ", "yayy");
    }

}
