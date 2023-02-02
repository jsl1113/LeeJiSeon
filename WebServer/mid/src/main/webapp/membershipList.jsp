<%/********************************/
/* 학번 : 2018305056             */
/* 성명 : 이지선                    */
/* 작성일 : 2021.           */
/* 파일명 : Assign_이지선.jsp    */
/* 내용 : Assignment #          */
/********************************/%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ page import="java.sql.*" %>
<% request.setCharacterEncoding("utf-8"); %>

<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
</head>
<body>
 Home > 관리자 등록 회원 관리 <br><HR>
 <%
 int i = 1;
 Connection conn = null;
 PreparedStatement pstmt = null;
 String jdbc_driver = "com.mysql.jdbc.Driver";
 String jdbc_url = "jdbc:mysql://127.0.0.1/jspdb";
 
 try {
	 Class.forName(jdbc_driver);
	conn = DriverManager.getConnection(jdbc_url,"jspbook","qweasdzxc0309!");	
	 String sql = "select id, email from midtest";
	 pstmt = conn.prepareStatement(sql);
	 ResultSet rs = pstmt.executeQuery();
	 
	 while(rs.next()){
		 out.println(i + ", " + rs.getString("id") + " / / " + rs.getString("email"));
		 i++;
	 }
	 rs.close();
	 pstmt.close();
	 conn.close();
 } catch(Exception e){
	 
 } 
 %><HR>
 <button onclick="'withdraw.jsp'">회원 탈퇴시키기</button>
<button onclick="'logout.jsp'">로그 아웃하기</button>
</body>
</html>