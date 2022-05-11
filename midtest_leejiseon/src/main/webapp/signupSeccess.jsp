<%/********************************/
/* 학번 : 2018305056             */
/* 성명 : 이지선                    */
/* 작성일 : 2021.           */
/* 파일명 : Assign_이지선.jsp    */
/* 내용 : Assignment #          */
/********************************/%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<% request.setCharacterEncoding("utf-8"); %>

<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title>회원 가입 성공 </title>
<% 
Connection conn = null;
PreparedStatement pstmt = null;
String jdbc_driver = "com.mysql.jdbc.Driver";
String jdbc_url = "jdbc:mysql://127.0.0.1/jspdb";

try {
	Class.forName(jdbc_driver);
	conn = DriverManager.getConnection(jdbc_url,"jspbook","qweasdzxc0309!");	
	String sql = "insert into midtest(id, passwd, email) values(?,?,?)";
	pstmt = conn.prepareStatement(sql);
	pstmt.setString(1, request.getParameter("id"));
	pstmt.setString(2, request.getParameter("passwd"));
	pstmt.setString(3, request.getParameter("email"));
	pstmt.executeUpdate();
} catch(Exception e){
	System.out.println(e);
}

%>
</head>
<body>
 Home > 회원 가입 성공 <br><HR>

축하합니다! <br>
관리자만 로그인이 가능합니다. <br>
<form name="form1" method="POST" action="membership.jsp">
	<input type=submit value="사용자 공간 이동">
</form>
	
</body>
</html>