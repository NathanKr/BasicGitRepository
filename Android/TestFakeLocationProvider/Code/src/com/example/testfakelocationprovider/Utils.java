package com.example.testfakelocationprovider;

import android.location.LocationManager;

public class Utils {
	public static boolean IsGps()
	{
		return (Globals.m_strProvider.equals(LocationManager.GPS_PROVIDER));
	}
	
	public static boolean IsMock()
	{
		return (Globals.m_strProvider.equals(Constants.m_strMyMockProviderName));
	}
}
