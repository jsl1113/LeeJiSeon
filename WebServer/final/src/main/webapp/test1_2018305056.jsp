<%/********************************/
/* 학번 : 2018305056             */
/* 성명 : 이지선                    */
/* 작성일 : 2021.  06. 14         */
/* 파일명 : test1_2018305056.jsp    */
/* 내용 : Final Test        */
/********************************/%>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@ page import = "finaltest.BookBean" %>

<%
	ArrayList <BookBean> bookList = new ArrayList<BookBean>();
	BookBean b1 = new BookBean("미드나잇 라이브러리", "매크 헤이그", "인플루엔셜");
	BookBean b2 = new BookBean("자바 웹 프로그래밍", "황희정", "한빛아카데미");
	bookList.add(b1);
	bookList.add(b2);
	
	request.setAttribute("bookList", bookList);
	
	String[] bookCode = {"소설", "역사", "인문", "정치", "미술", "종교", "여행", "과학", "만화", "건강"};
	request.setAttribute ("bookCode", bookCode);
	
	String[] Color = {"Red", "Green", "Blue", "Black"};
	request.setAttribute ("Color", Color);
	
	String bookCode1 = "소설/역사/인문/정치/미술/종교/여행/과학/만화/건강";
	request.setAttribute("bookCode1", bookCode1);
%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
</head>
<body>
<!--  Step 2  -->
<c:forEach var="book" items="${bookList }">
	<c:out value="${book }"></c:out><br>
</c:forEach><hr>

<c:forEach var="code" items="${bookCode }">
	<c:out value="${code }"></c:out>
</c:forEach><hr>

<!--  Step 3  -->
<h2>JSTL를 이용한 출력</h2><br>

<c:forEach var="color" items="${Color }">
	<font color="${color }">${color }</font>
</c:forEach><br>

<h2>varStatus 속성 살펴보기</h2>
<c:set var="index" value="index : " />
<c:set var="count" value="count : " />

<table border="1" >
<c:forEach begin="3" end="5" varStatus="status">
<tr>
<td><c:out value="${count } ${status.count }"></c:out></td>
<td><c:out value="${index } ${status.index }"></c:out></td>
</tr>
</c:forEach>
</table>

<h2>1에서 100까지 정수 중 홀수의 합(Step 사용 금지)</h2><br>
1~100사이의 정수 중 홀수의 합은? 

<c:set var="sum" value="0" />
<c:forEach var="i" begin="1" end="100" >
<c:if test="${i%2 != 0 }">
<c:set var="sum" value="${sum+i }" />
</c:if>
</c:forEach>
<c:out value="${sum }" ></c:out><br>

<!--  Step 4  -->
<c:set var="bookCode1" value="${bookCode1 }" />

<c:set var="bookCode1" value="${fn:split(bookCode1, '/')}"  />
<c:out value="${bookCode1 }" ></c:out>
</body>
</html>