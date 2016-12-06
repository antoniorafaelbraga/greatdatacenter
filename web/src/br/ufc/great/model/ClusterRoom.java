package br.ufc.great.model;

public class ClusterRoom {

	private String date;
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
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
	
	@Override
	public String toString() {
		return "{\"temperature\" : \""+temperature+"\", \"humidity\" : \""+humidity+"\", \"date\" : \""+date+"\"}";
	}
}
