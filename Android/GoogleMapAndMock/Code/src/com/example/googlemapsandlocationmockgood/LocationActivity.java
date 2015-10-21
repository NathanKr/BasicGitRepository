package com.example.googlemapsandlocationmockgood;


import java.util.ArrayList;
import java.util.Date;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.nynkmobile.utils.MockLocationProvider;
import com.nynkmobile.utils.MockUtils;


import android.app.Activity;
import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

/*
 * 
 * i want this activity to run the location listening for as long as it exist 
 * even when it is not in the forground so i put Init in OnCreate
 * 
 * no need for Finish , app will be killed by system or user and 
 * no location listening will happen
 * 
 * i see no reason to use Service
 */
public class LocationActivity extends FragmentActivity implements OnMapReadyCallback {
	
	private void initLogic() {
		m_map = null;
		PACKAGE_NAME = getApplicationContext().getPackageName();
		mLocationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);

		
		Location oLocation;
		
		m_strProvider = Constants.m_strMyMockProviderName;
			
		m_MockLocation.Init(mLocationManager, m_strProvider);

		
		Toast.makeText(getApplicationContext(),
				String.format("Location Provider : %s", m_strProvider), 
				Toast.LENGTH_LONG).show();
		
		mLocationManager.requestLocationUpdates(m_strProvider,
		        1000,          // 1-second interval.
		        10,             // 10 meters.
		        m_listener);
		
		
		//if(Utils.IsMock())
		//{
			ArrayList<Location> listLocations = new  ArrayList<Location>();
			boolean bLoop = true,bUpdateTimeToCurrent=true;
			int delayMs = 0,// -- start immidiately so i will get LastKnowLocation 
					periodMs = 5000;
			
			Date dtDummy = new Date();
			// --- מרכז הכרמל -> דה וינצי 12
			listLocations.add( MockUtils.GetValidLocationObject(32.803,34.987,
					Constants.m_strMyMockProviderName,dtDummy));
			listLocations.add(MockUtils.GetValidLocationObject(32.809,34.985,
					Constants.m_strMyMockProviderName,dtDummy));
			listLocations.add(MockUtils.GetValidLocationObject(32.813,34.981,
					Constants.m_strMyMockProviderName,dtDummy));
			listLocations.add(MockUtils.GetValidLocationObject(32.811,34.981,
					Constants.m_strMyMockProviderName,dtDummy));
			m_MockLocation.Start(listLocations, delayMs, periodMs,bLoop,bUpdateTimeToCurrent);
			
		//}
		
		oLocation = mLocationManager.getLastKnownLocation(m_strProvider);
		updateGuiLocation(oLocation);
	}




	/**
	 * no need to call because init is @ OnCreate
	 */
	private void finishXXX() {
		this.m_MockLocation.Stop();
		this.m_MockLocation.Finish();
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		initGui();
		initLogic();
	}




	private void initGui() {
		setContentView(R.layout.activity_location);
		
		 SupportMapFragment mapFragment =
	                (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map_location);
	        mapFragment.getMapAsync(this);
		
		
		// --- keep on front as much as you can
		getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
	}
	
	@SuppressWarnings("deprecation")
	private void updateGuiLocation(Location oLocation) {
		if(oLocation != null)
		{
			if(m_map != null)
			{
				LatLng oLatLng = new LatLng(oLocation.getLatitude(), oLocation.getLongitude());
				m_Marker.setPosition(oLatLng);
				m_map.moveCamera(CameraUpdateFactory.newLatLngZoom(oLatLng, 13));
			}
			
			Log.i(getTag(), "updateGuiLocation is called");
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

	String getTag()
	{
		return PACKAGE_NAME;
	}
	
	@Override
	public void onMapReady(GoogleMap map) {
		//LatLng Haifa = new LatLng(32.811,34.981);
		m_map = map;
		m_map.setMyLocationEnabled(true);
        //map.moveCamera(CameraUpdateFactory.newLatLngZoom(Haifa, 13));

       /* map.addMarker(new MarkerOptions()
                .title("Haifa")
                .snippet("Home Town")
                .position(Haifa));*/
        m_Marker =  m_map.addMarker(new MarkerOptions().position(new LatLng(0, 0)).title("Marker"));
	}
	
	
	private  LocationManager mLocationManager;
	private  String m_strProvider;
	private final MockLocationProvider m_MockLocation = new MockLocationProvider();
	private String PACKAGE_NAME;
	private GoogleMap m_map;
	Marker m_Marker;
}
