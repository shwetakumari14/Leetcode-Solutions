package com.example.cscihw9;

import android.content.SharedPreferences;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.content.Context;
import android.widget.TextView;
//import jp.wasabeef.picasso.transformations.RoundedCornersTransformation;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.resource.bitmap.RoundedCorners;
import com.google.android.material.snackbar.Snackbar;
import com.google.gson.Gson;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class EventListingAdapter extends RecyclerView.Adapter<EventListingAdapter.ViewHolder> {

    private ArrayList<EventData> listingsData;
    private Context mContext;
    private OnItemClickListener listener;

    private EventListingAdapter self_adapter;
    private SharedPreferences sharedPreferences;

    public EventListingAdapter(ArrayList<EventData> listingsData, OnItemClickListener listener, Context context) {
        this.listingsData = listingsData;
        this.listener = listener;
        mContext = context;
        this.self_adapter = this;
        sharedPreferences = mContext.getSharedPreferences("fav_pref", Context.MODE_PRIVATE);

    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.listing_data_layout, parent, false);
        TextView eventName = view.findViewById(R.id.eventName);
//        eventName.setSelected(true);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        EventData eventData = listingsData.get(position);
        holder.eventName.setText(eventData.getEvents());
        holder.eventDate.setText(eventData.getDate());
        holder.eventTime.setText(eventData.getTime());
        holder.venueName.setText(eventData.getVenues());
        holder.genreName.setText(eventData.getGenres());
        Glide.with(holder.itemView.getContext())
                .load(eventData.getIcons())
                .transform(new RoundedCorners(20))
                .into(holder.iconImg);

        if (sharedPreferences.getAll().keySet().contains(eventData.getIds())) {
            // ID is present in SharedPreferences
            holder.fav.setImageResource(R.drawable.favourite_fill);
        } else {
            // ID is not present in SharedPreferences
            holder.fav.setImageResource(R.drawable.favourite);
        }

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (listener != null) {
                    listener.onItemClick(eventData);
                }
            }
        });

        holder.fav.setOnClickListener(new View.OnClickListener() {
//            boolean isFav = eventData.getIsFav();
            @Override
            public void onClick(View view) {
//                String id = eventData.getIds();
                if (sharedPreferences.getAll().keySet().contains(eventData.getIds())) {
                    eventData.setIsFav(false);
                    holder.fav.setImageResource(R.drawable.favourite);
                    Snackbar.make(view, "Removed from favourites", Snackbar.LENGTH_SHORT).show();
                    SharedPreferences.Editor editor = sharedPreferences.edit();
                    editor.remove(eventData.getIds());
                    editor.apply();
                } else {
                    eventData.setIsFav(true);
                    holder.fav.setImageResource(R.drawable.favourite_fill);
                    Gson gson = new Gson();
                    String eventDataJsonString = gson.toJson(eventData);
                    sharedPreferences.edit().putString(eventData.getIds(), eventDataJsonString).apply();
                    Log.d("------ pref ------ ",  sharedPreferences.getAll().toString());
                    String  test = sharedPreferences.getString(eventData.getIds(), "");
                    Snackbar.make(view, eventData.getEvents() +" Added to favourites", Snackbar.LENGTH_SHORT).show();
                }
            }
        });
    }

    @Override
    public int getItemCount() {
        return listingsData.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView eventName;
        TextView eventDate;
        TextView eventTime;
        TextView venueName;
        TextView genreName;

        ImageView iconImg;

        ImageView fav;


        public ViewHolder(View itemView) {
            super(itemView);
            eventName = itemView.findViewById(R.id.eventName);
            eventName.setSelected(true);
            eventDate = itemView.findViewById(R.id.eventDate);
            eventTime = itemView.findViewById(R.id.eventTime);
            venueName = itemView.findViewById(R.id.venueName);
            venueName.setSelected(true);
            genreName = itemView.findViewById(R.id.genreName);
            iconImg = itemView.findViewById(R.id.stadiumImg);
            fav = itemView.findViewById(R.id.favourite);
        }
    }

    public interface OnItemClickListener {
        void onItemClick(EventData eventData);
    }
}