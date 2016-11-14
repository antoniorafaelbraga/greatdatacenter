package br.ufc.great.servlets;

import java.io.IOException;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import br.ufc.great.model.ClusterRoom;
import br.ufc.great.model.GreatDataCenter;
import br.ufc.great.model.PowerGeneratorRoom;

/**
 * Servlet implementation class GreatDataCenterGateway
 */
@WebServlet("/GreatDataCenterGateway")
public class GreatDataCenterGateway extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public GreatDataCenterGateway() {
        super();
    }

	public void init(ServletConfig config) throws ServletException {

	}

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		GreatDataCenter gdc = new GreatDataCenter();
		ClusterRoom cr = new ClusterRoom();
		PowerGeneratorRoom pgr = new PowerGeneratorRoom();
		
		
		String temperature = request.getParameter("temperatura");
		String humidity = request.getParameter("humidity");
		String noise = request.getParameter("noise");
		String hourmeter = request.getParameter("hourmeter");
		String fuel_level = request.getParameter("fuel_level");
		
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		cr.setHumidity(humidity!=null?Float.parseFloat(humidity):0);
		pgr.setNoise(noise!=null?Float.parseFloat(noise):0);
		pgr.setHourmeter(hourmeter!=null?Float.parseFloat(hourmeter):0);
		pgr.setFuelLevel(fuel_level!=null?Float.parseFloat(fuel_level):0);
		
		gdc.setCr(cr);
		gdc.setPgr(pgr);
		
		
	}
}
