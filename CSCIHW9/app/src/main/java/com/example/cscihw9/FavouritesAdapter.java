package com.example.cscihw9;

import android.annotation.SuppressLint;
import android.content.SharedPreferences;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.content.Context;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.load.resource.bitmap.RoundedCorners;
import com.google.android.material.snackbar.Snackbar;
import com.google.gson.Gson;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class FavouritesAdapter extends RecyclerView.Adapter<FavouritesAdapter.ViewHolder> {

    private ArrayList<EventData> listingsData;
    private FavouritesAdapter self_adapter;
    private Context mContext;
    private SharedPreferences sharedPreferences;

    public FavouritesAdapter(ArrayList<EventData> listingsData, Context context) {
        this.listingsData = listingsData;
        mContext = context;
        this.self_adapter = this;
        sharedPreferences = mContext.getSharedPreferences("fav_pref", Context.MODE_PRIVATE);
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.favorites_layout, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, @SuppressLint("RecyclerView") int position) {
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

        holder.fav.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (sharedPreferences.getAll().keySet().contains(eventData.getIds())) {
                    eventData.setIsFav(false);
                    Snackbar.make(view, "Removed from favourites", Snackbar.LENGTH_SHORT).show();
                    SharedPreferences.Editor editor = sharedPreferences.edit();
                    editor.remove(eventData.getIds());
                    editor.apply();
                    listingsData.remove(position);
                    notifyDataSetChanged();
                } else {
                }
                notifyDataSetChanged();
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
            fav = itemView.findViewById(R.id.favouriteImg);
        }
    }
}