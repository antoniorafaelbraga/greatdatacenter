package br.ufc.great.model;

public class ClusterRoom {
	private float temperature;
	private float humidity;

	
	public float getTemperature() {
		return temperature;
	}
	public void setTemperature(float temperature) {
		this.temperature = temperature;
	}
	public float getHumidity() {
		return humidity;
	}
	public void setHumidity(float humidity) {
		this.humidity = humidity;
	}
	
	@Override
	public String toString() {
		return "{\"temperature\" : \""+temperature+"\", \"humidity\" : \""+humidity+"\"}";
	}
}
