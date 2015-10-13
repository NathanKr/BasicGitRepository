package com.example.testfakelocationprovider;

import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import android.location.Location;
import android.location.LocationManager;
import android.util.Log;

public class MockLocation {
	/**
	 * 
	 * @param oLocationManager - ready to use LocationManager
	 * @param strMockProviderName - unique location provider name on this android machine
	 */
	public  void Init(LocationManager oLocationManager,String strMockProviderName)
	{
		m_LocationManager = oLocationManager;
		m_strMockProviderName = strMockProviderName;
		
		 if(m_LocationManager.getProvider(m_strMockProviderName) == null)
			{
			 m_LocationManager.addTestProvider(m_strMockProviderName,
                  false, false, false, false, false, false, false, 0,5);
			}
			 
		 m_LocationManager.setTestProviderEnabled(m_strMockProviderName, true);
		 m_TimerInjectLocation = new Timer();
		
	}
	
	
	/**
	 * 
	 * @param list Locations - location to be injected to the Mock Location adapter.
	 * 						   Location->provider must be m_strMockProviderName
	 * @param bLoop - loop on list once its over
	 * @param delay - delay in milliseconds before task is to be executed.
	 * @param period - time in milliseconds between successive task start executions.
	 * @param bUpdateTimeToCurrent - update the Location time to the time it is 
	 * 								 injected to the LocationService
	 */
	public void Start(	List<Location> listLocations,
						long delayMs, long periodMs,
						final boolean bLoop,
						final boolean bUpdateTimeToCurrent)
	{
		m_ListLocations = listLocations;
		if(m_ListLocations != null)
		{
			TimerTask task = new TimerTask()
			{
				@Override
				public void run() {
					if(m_ListLocationsIterator.hasNext())
					{
						Location loc = m_ListLocationsIterator.next();
						Log.i("Tag", String.format("Longitude : %f , Latitude : %f",
								loc.getLongitude(),loc.getLatitude()));
						
						if(bUpdateTimeToCurrent)
						{
							Date dt = new Date();
							loc.setTime(dt.getTime());
						}
						m_LocationManager.setTestProviderLocation(m_strMockProviderName, loc);
					}
					else if(bLoop)
					{
						m_ListLocationsIterator = m_ListLocations.iterator();
					}
				}
				
			};
			
			m_ListLocationsIterator = m_ListLocations.iterator();
			m_TimerInjectLocation.scheduleAtFixedRate(task, delayMs, periodMs);
		}

	}
	
	
	public void Stop()
	{
		m_TimerInjectLocation.cancel();
		m_TimerInjectLocation.purge();
	}
	
	
	public void Finish()
	{
		Stop(); // -- make sure
		m_LocationManager.removeTestProvider(m_strMockProviderName);
	}
	
	LocationManager m_LocationManager;
	// -- this is global so we can use two of this on same machine
	String m_strMockProviderName;
	List<Location> m_ListLocations;
	Iterator<Location> m_ListLocationsIterator;
	Timer m_TimerInjectLocation;
}
