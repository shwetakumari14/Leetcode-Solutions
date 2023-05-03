package com.example.cscihw9;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import java.util.ArrayList;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.viewpager2.adapter.FragmentStateAdapter;

public class Adapter extends FragmentStateAdapter {

    public Adapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
    }

    @Override
    public Fragment createFragment(int position) {
        switch (position) {
            case 0:
                return new NavHost();
            case 1:
                return new favourites();
            default:
                return null;
        }
    }

    @Override
    public int getItemCount() {
        return 2; // two tabs
    }

    @Override
    public long getItemId(int position) {
        // If you have stable IDs, return them here.
        // This can help optimize your adapter.
        return super.getItemId(position);
    }
}




