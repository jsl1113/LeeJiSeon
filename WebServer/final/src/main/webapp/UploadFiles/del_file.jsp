<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@ page import="java.io.File" %>
    
<% 
    int num = Integer.parseInt(request.getParameter("num"));

    Connection conn = null;
    Statement stmt = null;

// 데이터베이스 연결관련정보를 문자열로 선언
	String jdbc_driver = "com.mysql.jdbc.Driver";
	String jdbc_url = "jdbc:mysql://127.0.0.1/jspdb";
    try { 
    	Class.forName(jdbc_driver);
    	conn = DriverManager.getConnection(jdbc_url,"jspbook","qweasdzxc0309!");
        stmt = conn.createStatement();           
        
        // 삭제할 파일의 정보를 읽어오는 쿼리 (파일명을 알기 위해)
        ResultSet rs = stmt.executeQuery(
                "select * from webhard where num=" + num);
     {
        if (rs.next()) {

            // 지정된 파일 삭제
            File file = new File(application.getRealPath("/UploadFiles/") +
                                 rs.getString("fname"));
            if (file.exists()) {
                file.delete();
            }
            
            // DB에서 파일 정보를 삭제
            stmt.executeUpdate(
                    "delete from webhard where num=" + num);
        }

    } 
    }
     catch(Exception e) {
        e.printStackTrace();
    }
    
    response.sendRedirect("webhard.jsp");
%>