package com.example.cscihw9;

import android.support.annotation.NonNull;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;
import androidx.viewpager2.adapter.FragmentStateAdapter;


public class EventAdapter extends FragmentStateAdapter {

    public EventAdapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        switch (position) {
            case 0:
                return new Details();
            case 1:
                return new Artists();
            case 2:
                return new Venue();
            default:
                return null;
        }
    }

    @Override
    public int getItemCount() {
        return 3;
    }
}

//FragmentStateAdapter
//public class EventAdapter extends FragmentPagerAdapter {
//
//    public EventAdapter(FragmentManager fm) {
//        super(fm);
//    }
//
//    @Override
//    public Fragment getItem(int position) {
//        switch (position) {
//            case 0:
//                return new Details();
//            case 1:
//                return new Artists();
//            case 2:
//                return new Venue();
//            default:
//                return null;
//        }
//    }
//
//    @Override
//    public int getCount() {
//        return 3; // two tabs
//    }
//
////    @Override
////    public CharSequence getPageTitle(int position) {
////        switch (position) {
////            case 0:
////                return "DETAILS";
////            case 1:
////                return "ARTIST(S)";
////            case 2:
////                return "VENUE";
////            default:
////                return null;
////        }
////    }
//
//
//}