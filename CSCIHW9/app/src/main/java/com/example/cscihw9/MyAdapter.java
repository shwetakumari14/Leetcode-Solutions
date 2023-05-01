package com.example.cscihw9;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;


public class MyAdapter extends RecyclerView.Adapter<MyAdapter.ViewHolder> {

    private ArrayList<MyObject> myObjects;
    private OnItemClickListener listener;

    public MyAdapter(ArrayList<MyObject> myObjects, OnItemClickListener listener) {
        this.myObjects = myObjects;
        this.listener = listener;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.listing_data_layout, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        MyObject myObject = myObjects.get(position);
        holder.textViewName.setText(myObject.getName());
        holder.textViewDescription.setText(myObject.getDescription());

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (listener != null) {
                    listener.onItemClick(myObject);
                }
            }
        });
    }

    @Override
    public int getItemCount() {
        return myObjects.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        TextView textViewName;
        TextView textViewDescription;

        public ViewHolder(View itemView) {
            super(itemView);
            textViewName = itemView.findViewById(R.id.eventName);
            textViewDescription = itemView.findViewById(R.id.genreName);
        }
    }

    public interface OnItemClickListener {
        void onItemClick(MyObject myObject);
    }
}

