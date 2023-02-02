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
<title>회원 공간 </title>
</head>
<body>
 Home > 회원 공간 <br><HR>
여기는 회원 공간 입니다. <br>
회원을 탈퇴하려면 "탈퇴하기" 버튼을 눌러주세요. <br>
<form name="form1" method="POST" action="withdraw.jsp">
	<input type=submit value="탈퇴하기">
</form>
</body>
</html>