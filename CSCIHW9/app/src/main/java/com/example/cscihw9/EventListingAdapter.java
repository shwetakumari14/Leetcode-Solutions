package com.example.cscihw9;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import jp.wasabeef.picasso.transformations.RoundedCornersTransformation;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class EventListingAdapter extends RecyclerView.Adapter<EventListingAdapter.ViewHolder> {

    private ArrayList<EventData> listingsData;
    private OnItemClickListener listener;

    public EventListingAdapter(ArrayList<EventData> listingsData, OnItemClickListener listener) {
        this.listingsData = listingsData;
        this.listener = listener;
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
        Picasso.get().load(eventData.getIcons()).transform(new RoundedCornersTransformation(20, 0)).into(holder.iconImg);

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (listener != null) {
                    listener.onItemClick(eventData);
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

            fav.setOnClickListener(new View.OnClickListener() {
                boolean isFav = false;
                @Override
                public void onClick(View view) {
                    // Handle click event
                    if (isFav) {
                        fav.setImageResource(R.drawable.favourite);
                    } else {
                        fav.setImageResource(R.drawable.favourite_fill);
                    }
                    isFav = !isFav;
                }
            });
        }
    }

    public interface OnItemClickListener {
        void onItemClick(EventData eventData);
    }
}