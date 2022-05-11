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

<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
</head>
<body>
 Home > 회원 가입 <br><HR>
<H2>회원 가입 화면</H2>
<form method=post action=signupSeccess.jsp>
아이디 : <input type="text" name="id"><br>
비밀번호 : <input type="password" name="passwd"><br>
이메일 : <input type="text" name="email"><br>
<input type=reset value="다시 작성">
<input type=submit value="가입하기">
</form>
</body>
</html>