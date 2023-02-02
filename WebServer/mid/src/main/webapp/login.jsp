<%/********************************/
/* 학번 : 2018305056             */
/* 성명 : 이지선                    */
/* 작성일 : 2021.           */
/* 파일명 : Assign_이지선.jsp    */
/* 내용 : Assignment #          */
/********************************/%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<% request.setCharacterEncoding("utf-8"); %>
<%
session.setAttribute("adminid", "jiseon");
session.setAttribute("adminpasswd", "1234");
%>

<html> 
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
<script>
</script>
</head>
<body>
 Home > 관리자 로그인 <br><HR>
<H2>관리자 로그인 화면</H2>
<form action="./loginCheck.jsp">
아이디 : <input type="text" name="id"><br>
비밀번호 : <input type="password" name="passwd"><br>
<input type="submit" value="로그인"></button>
</form>


</body>
</html>