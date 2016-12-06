package br.ufc.great.servlets;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import br.ufc.great.persistence.ConnectionDB;

@WebServlet("/GDCLastStatus")
public class GDCLastStatus extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public GDCLastStatus() {
        super();
    }

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		ConnectionDB conn = new ConnectionDB();
        out.println(conn.getLastStatus().toString());
        conn.closeConnection();
	}
}
