<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@ page import="com.oreilly.servlet.MultipartRequest,
                 com.oreilly.servlet.multipart.DefaultFileRenamePolicy,
                 java.io.File, java.util.*" %>
<%@ page import="java.time.*" %>

<%
    MultipartRequest multi = new MultipartRequest(
            request,
            application.getRealPath("/UploadFiles"),   // 파일을 저장할 경로
            100 * 1024 * 1024,                   // 최대 파일 크기 (100MB)
            "utf-8",                             // 인코딩
            new DefaultFileRenamePolicy()        // 동일 파일명 처리 방법
    );
	Enumeration fileNames = multi.getFileNames();
	
	ArrayList<String> arr1 = new ArrayList<>();  // 파일 
	ArrayList<String> arr2 = new ArrayList<>(); // 파일 이름
	
	while(fileNames.hasMoreElements()){
		String parameter = (String) fileNames.nextElement();
		String file_name = multi.getFilesystemName(parameter);
		
		if(file_name != null){
			arr1.add(parameter);
			arr2.add(file_name);
		}
	}
	
    Connection conn = null;
    Statement stmt = null;

 // 데이터베이스 연결관련정보를 문자열로 선언
	String jdbc_driver = "com.mysql.jdbc.Driver";
	String jdbc_url = "jdbc:mysql://127.0.0.1/jspdb";
	
    if (arr2.size() != 0) {
        try {
        Class.forName(jdbc_driver);
        conn = DriverManager.getConnection(jdbc_url,"jspbook","qweasdzxc0309!");
                stmt = conn.createStatement();
         {
        	 File file = null;
        	 for(int i = 0; i < arr2.size(); i++){
        		 file = multi.getFile(arr1.get(i));
        		 
                 String curTime = LocalDate.now() + " " +
                                  LocalTime.now().toString().substring(0, 8);  // 현재 시간 얻기
        		
                 stmt.executeUpdate(String.format(
                         "insert into webhard (fname, ftime, fsize) " +
                         "values ('%s', '%s', %d)",
                         file.getName(), curTime, (int)file.length()));  // 쿼리 실행
				
        	 }
        	 
             response.sendRedirect("webhard.jsp");   // 메인 페이지로 돌아가기
             return;

         } 
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>

<script>
    alert('업로드 실패 !');
    history.back();
</script>

</body>
</html>