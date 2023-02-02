<%/********************************/
/* 학번 : 2018305056             */
/* 성명 : 이지선                    */
/* 작성일 : 2021.           */
/* 파일명 : Assign_이지선.jsp    */
/* 내용 : Assignment #          */
/********************************/%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" errorPage="loginErr.jsp" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<% request.setCharacterEncoding("utf-8"); %>

<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
</head>
<body>
<%
String adminId = (String) session.getAttribute("adminid");
String adminPasswd = (String) session.getAttribute("adminpasswd");

String id = request.getParameter("id");
String passwd = request.getParameter("passwd");
String i = "jiseon";
String p = "1234";
if(id.equals(i) && passwd.equals(p)){ 
	response.sendRedirect("./loginSuccess.jsp");
} else {
	out.print(adminId + id);
	//response.sendRedirect("./loginErr.jsp");
}
%>
</body>
</html>