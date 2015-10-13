package com.example.testfakelocationprovider;


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
		
		if(Utils.IsGps() && mLocationManager.isProviderEnabled(LocationManager.GPS_PROVIDER))
		{
			m_strProvider = LocationManager.GPS_PROVIDER;
			this.btSetTestProviderLocation.setEnabled(false);
		}
		else{
			// --- mock
			m_strProvider = Constants.m_strMyMockProviderName;
			
			
			 if(mLocationManager.getProvider(m_strProvider) == null)
			{
				 mLocationManager.addTestProvider(m_strProvider,
                     false, false, false, false, false, false, false, 0,
                     m_nMyMockProviderAccuracy);
			}
			 
			 mLocationManager.setTestProviderEnabled(m_strProvider, true);
		}

		
		Toast.makeText(getApplicationContext(),
				String.format("Location Provider : %s", m_strProvider), 
				Toast.LENGTH_LONG).show();
		
		mLocationManager.requestLocationUpdates(m_strProvider,
		        10000,          // 10-second interval.
		        10,             // 10 meters.
		        m_listener);
		
		
		if(Utils.IsMock())
		{
			 Location loc = getLocationObject(1,11);
			 mLocationManager.setTestProviderLocation(m_strProvider, loc);
		}
		
		oLocation = mLocationManager.getLastKnownLocation(m_strProvider);
		updateGuiLocation(oLocation);

	}

	public void ClickSetTestProviderLocation(View v)
	{
		Location loc = getLocationObject(11,22);
		 mLocationManager.setTestProviderLocation(m_strProvider, loc);
	}

	private Location getLocationObject(double fLatitude,double fLongitude) {
		Location loc = new Location("");
		loc.setLatitude(fLatitude);
		loc.setLongitude(fLongitude);
		loc.setProvider(Constants.m_strMyMockProviderName);
		Date dt = new Date();
		loc.setTime(dt.getTime());
		return loc;
	}
	
	@Override
	protected void onStop() {
		super.onStop();
		
		if(Utils.IsMock())
		{
			mLocationManager.removeTestProvider(m_strProvider);
		}
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_location);
		
		m_tvLongitude = (TextView)findViewById(R.id.tvLongitude);
		m_tvLatitude  = (TextView)findViewById(R.id.tvLatitude);
		btSetTestProviderLocation = (Button)findViewById(R.id.btSetTestProviderLocation);
		
		mLocationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
	}
	
	private void updateGuiLocation(Location oLocation) {
		if(oLocation != null)
		{
			m_tvLongitude.setText(Double.toString(oLocation.getLongitude()));
			m_tvLatitude.setText(Double.toString(oLocation.getLatitude()));
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
	private  Button btSetTestProviderLocation;
	private  String m_strProvider;
	private final int m_nMyMockProviderAccuracy = 10;
}
