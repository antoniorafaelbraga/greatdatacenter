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

	public void destroy() {
	}

	public ServletConfig getServletConfig() {
		return null;
	}

	public String getServletInfo() {
		return null; 
	}

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		GreatDataCenter gdc = new GreatDataCenter();
		ClusterRoom cr = new ClusterRoom();
		PowerGeneratorRoom pgr = new PowerGeneratorRoom();
		
		
		String temperature = request.getParameter("temperatura");
		String humidity = request.getParameter("temperatura");
		String noise = request.getParameter("temperatura");
		String hourmeter = request.getParameter("temperatura");
		String fuel_level = request.getParameter("temperatura");
		
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		cr.setTemperature(temperature!=null?Float.parseFloat(temperature):0);
		
		
		
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

	protected void doPut(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	}

}
