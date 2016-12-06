package br.ufc.great.servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import br.ufc.great.model.ClusterRoom;
import br.ufc.great.persistence.ConnectionDB;

@WebServlet("/GDCHistoryLast12hours")
public class GDCHistoryLast12hours extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public GDCHistoryLast12hours() {
        super();
    }

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		ConnectionDB conn = new ConnectionDB();
		
		StringBuffer sbBuffer = new StringBuffer();
		ArrayList<ClusterRoom> al = conn.getLast12HoursClusterRoom();
		for (Iterator<ClusterRoom> iterator = al.iterator(); iterator.hasNext();) {
			ClusterRoom clusterRoom = (ClusterRoom) iterator.next();
			sbBuffer.append(clusterRoom.toString()+"\n");
		}
        out.println(sbBuffer.toString());
        conn.closeConnection();
	}
}