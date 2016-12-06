package br.ufc.great.service;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/GreatDataCenterNotification")
public class GreatDataCenterNotification extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public GreatDataCenterNotification() {
        super();
    }

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String token = request.getParameter("regID");
		System.out.println(token);
	}

}
