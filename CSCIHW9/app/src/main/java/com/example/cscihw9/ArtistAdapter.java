package com.example.cscihw9;

import android.content.Intent;
import android.net.Uri;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.progressindicator.CircularProgressIndicator;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class ArtistAdapter extends RecyclerView.Adapter<ArtistAdapter.ViewHolder> {

    private ArrayList<ArtistsData> artistsData;
    private OnItemClickListener listener;

    public ArtistAdapter(ArrayList<ArtistsData> artistsData, OnItemClickListener listener) {
        this.artistsData = artistsData;
        this.listener = listener;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.fragment_artists, parent, false);
//        TextView eventName = view.findViewById(R.id.eventName);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        ArtistsData artistData = artistsData.get(position);
        Picasso.get().load(artistData.getArtist_img()).into(holder.artistImg);
        holder.artistName.setText(artistData.getArtist_name());
        holder.popularityProgressText.setText(artistData.getPopularity());
        holder.followers.setText(artistData.getFollowers());
//        holder.spotify.setText(artistData.getSpotify_link());
        String str = artistData.getPopularity();
        int num = Integer.parseInt(str);
        holder.popularityProgress.setProgress(num);
        Picasso.get().load(artistData.getAlbumsOne()).into(holder.album1);
        Picasso.get().load(artistData.getAlbumsTwo()).into(holder.album2);
        Picasso.get().load(artistData.getAlbumsThree()).into(holder.album3);


        holder.spotify.setOnClickListener(new View.OnClickListener() {
            boolean isFav = false;
            @Override
            public void onClick(View view) {
                // Handle click event

                String spotifyURL = artistData.getSpotify_link();
                Intent spotifyIn = new Intent(Intent.ACTION_VIEW, Uri.parse(spotifyURL));
                view.getContext().startActivity(spotifyIn);

            }
        });


        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (listener != null) {
                    listener.onItemClick(artistData);
                }
            }
        });
    }

    @Override
    public int getItemCount() {
        return artistsData.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        private ImageView artistImg;
        private TextView artistName;
        private TextView popularityProgressText;

        private CircularProgressIndicator popularityProgress;
        private TextView followers;
        private TextView spotify;
        private ImageView album1;
        private ImageView album2;
        private ImageView album3;


        public ViewHolder(View itemView) {
            super(itemView);
            artistImg = itemView.findViewById(R.id.artistImg);
            artistName = itemView.findViewById(R.id.artistName);
            popularityProgressText = itemView.findViewById(R.id.popularityProgressText);
            popularityProgress = itemView.findViewById(R.id.popularityProgress);
            followers = itemView.findViewById(R.id.followers);
            spotify = itemView.findViewById(R.id.spotify);
            album1 = itemView.findViewById(R.id.album1);
            album2 = itemView.findViewById(R.id.album2);
            album3 = itemView.findViewById(R.id.album3);
        }
    }

    public interface OnItemClickListener {
        void onItemClick(ArtistsData artistData);
    }
}