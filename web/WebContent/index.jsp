<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Great Data Center</title>
</head>
<body>
	
	<form action="/GreatDataCenter/GreatDataCenterGateway">
	<center>GREat Data Center</center>

		ClusterRoom <br><br>
	
		Temperature <input type="text" name="temperature" id="temperature"> <br>
		Humidity <input type="text" name="humidity" id="humidity"><br>
		
		<hr align="left" width="300" size="1" color="black">
		
		PowerGeneratorRoom <br><br>
		
		Noise <input type="text" name="noise" id="noise"> <br>
		Hourmeter <input type="text" name="hourmeter" id="hourmeter"><br>
		Fuel level <input type="text" name="fuel_level" id="fuel_level"><br>
		
		<hr align="left" width="300" size="1" color="black">
		
		<input type="submit" name="asdf" value="Enviar">
	
	</form>


</body>
</html>