package com.example.testfakelocationprovider;


import java.util.Date;



import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		m_rbGpsProvider = (RadioButton)findViewById(R.id.rbGPS);
		m_rbMockProvider= (RadioButton)findViewById(R.id.rbMock);
		m_rbMockProvider.setChecked(true);
	}
	
	public void Clicked(View v)
	{
		if(this.m_rbGpsProvider.isChecked())
		{
			Globals.m_strProvider = LocationManager.GPS_PROVIDER;
		}
		else{
			// --- mock
			Globals.m_strProvider = Constants.m_strMyMockProviderName;
		}
		
		Intent intent = new Intent(this, LocationActivity.class);

		this.startActivity(intent);
	}
	
	private  RadioButton m_rbGpsProvider;
	private  RadioButton m_rbMockProvider;

}
