package com.example.cscihw9;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import java.util.ArrayList;

public class Adapter extends FragmentPagerAdapter {

    public Adapter(FragmentManager fm) {
        super(fm);
    }

    @Override
    public Fragment getItem(int position) {
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
    public int getCount() {
        return 2; // two tabs
    }

    @Override
    public CharSequence getPageTitle(int position) {
        switch (position) {
            case 0:
                return "SEARCH";
            case 1:
                return "FAVORITES";
            default:
                return null;
        }
    }
}


//public class Adapter extends FragmentPagerAdapter {
//
//    private final ArrayList<Fragment> fragmentList = new ArrayList<>();
//    private final ArrayList<String> titleList = new ArrayList<>();
//
//    public Adapter(@NonNull FragmentManager fm, int behavior) {
//        super(fm, behavior);
//    }
//
//    @NonNull
//    @Override
//    public Fragment getItem(int position) {
//        return fragmentList.get(position);
//    }
//
//    @Override
//    public int getCount() {
//        return fragmentList.size();
//    }
//
//    public void addFragment(Fragment fragment, String title) {
//        fragmentList.add(fragment);
//        titleList.add(title);
//    }
//
//    @Nullable
//    @Override
//    public CharSequence getPageTitle(int position) {
//        return titleList.get(position);
//    }
//}
