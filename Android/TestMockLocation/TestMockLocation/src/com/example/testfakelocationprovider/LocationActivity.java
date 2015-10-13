package com.example.testfakelocationprovider;


import java.util.ArrayList;
import java.util.Date;


import android.app.Activity;
import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

public class LocationActivity extends Activity {

	@Override
	protected void onStart() {
		super.onStart();
		
		Location oLocation;
		
		m_strProvider = Constants.m_strMyMockProviderName;
			
		m_MockLocation.Init(mLocationManager, m_strProvider);

		
		Toast.makeText(getApplicationContext(),
				String.format("Location Provider : %s", m_strProvider), 
				Toast.LENGTH_LONG).show();
		
		mLocationManager.requestLocationUpdates(m_strProvider,
		        1000,          // 1-second interval.
		        10,             // 1 meters.
		        m_listener);
		
		
		//if(Utils.IsMock())
		//{
			ArrayList<Location> listLocations = new  ArrayList<Location>();
			boolean bLoop = true,bUpdateTimeToCurrent=true;
			int delayMs = 0,// -- start immidiately so i will get LastKnowLocation 
					periodMs = 5000;
			
			// --- מרכז הכרמל -> דה וינצי 12
			listLocations.add(getLocationObject(32.803,34.987,Constants.m_strMyMockProviderName));
			listLocations.add(getLocationObject(32.809,34.985,Constants.m_strMyMockProviderName));
			listLocations.add(getLocationObject(32.813,34.981,Constants.m_strMyMockProviderName));
			listLocations.add(getLocationObject(32.811,34.981,Constants.m_strMyMockProviderName));
			m_MockLocation.Start(listLocations, delayMs, periodMs,bLoop,bUpdateTimeToCurrent);
			
		//}
		
		oLocation = mLocationManager.getLastKnownLocation(m_strProvider);
		updateGuiLocation(oLocation);

	}

	

	private Location getLocationObject(double fLatitude,double fLongitude,
			String strMyMockProviderName) {
		Location loc = new Location("");
		loc.setLatitude(fLatitude);
		loc.setLongitude(fLongitude);
		loc.setProvider(strMyMockProviderName);
		Date dt = new Date();
		loc.setTime(dt.getTime());
		return loc;
	}
	
	@Override
	protected void onStop() {
		super.onStop();
		
		//if(Utils.IsMock())
		//{
			this.m_MockLocation.Stop();
			this.m_MockLocation.Finish();
		//}
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_location);
		
		m_tvLongitude = (TextView)findViewById(R.id.tvLongitude);
		m_tvLatitude  = (TextView)findViewById(R.id.tvLatitude);
		m_tvLocationTime = (TextView)findViewById(R.id.tvLocationTime);
		
		mLocationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
	}
	
	@SuppressWarnings("deprecation")
	private void updateGuiLocation(Location oLocation) {
		if(oLocation != null)
		{
			m_tvLongitude.setText(Double.toString(oLocation.getLongitude()));
			m_tvLatitude.setText(Double.toString(oLocation.getLatitude()));
			Date oDate = new Date(oLocation.getTime());
			m_tvLocationTime.setText(oDate.toLocaleString());
		}
	}
	
	private final LocationListener m_listener = new LocationListener() {

		@Override
		public void onLocationChanged(final Location arg0) {
			final Runnable oRunnableAction = new Runnable() {
				
				@Override
				public void run() {
					updateGuiLocation(arg0);
				}
			};
			runOnUiThread(oRunnableAction);
		}

		@Override
		public void onProviderDisabled(String arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void onProviderEnabled(String arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void onStatusChanged(String arg0, int arg1, Bundle arg2) {
			// TODO Auto-generated method stub
			
		}
	};

	private  LocationManager mLocationManager;
	private  TextView m_tvLongitude;
	private  TextView m_tvLatitude;
	private  TextView m_tvLocationTime;
	private  Button btSetTestProviderLocation;
	private  String m_strProvider;
	private final int m_nMyMockProviderAccuracy = 10;
	private final MockLocation m_MockLocation = new MockLocation();
}
