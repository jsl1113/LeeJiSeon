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
 Home > 관리자 화면 <br><HR>
새로운 세션이 생성되었습니다!<br>
<%String adminId = (String) session.getAttribute("adminid"); %>
관리자 [<% out.print(adminId); %>] 님이 입장하였습니다. <br>
<button onclick="'membershipList.jsp'">등록 회원 관리 화면으로</button>
<button onclick="'logout.jsp'">로그 아웃하기</button>

</body>
</html>