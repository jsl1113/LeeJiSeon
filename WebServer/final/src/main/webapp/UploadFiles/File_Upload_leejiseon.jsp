<%@ page language="java" contentType="text/html; charset=UTF-8"  pageEncoding="UTF-8"%>
<%@ page import="com.oreilly.servlet.MultipartRequest,
                 com.oreilly.servlet.multipart.DefaultFileRenamePolicy,
                 java.io.File, java.util.*" %>
    
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>

<% 
    MultipartRequest multi = new MultipartRequest(
            request,                    // POST 로 전달된 내용을 담은 객체
            application.getRealPath("/UploadFiles"),   // 파일을 저장할 경로
            100 * 1024 * 1024,                   // 최대 파일 크기 (100MB)
            "utf-8",                             // 인코딩
            new DefaultFileRenamePolicy()        // 동일 파일명 처리 방법
    );

    Enumeration fileNames = multi.getFileNames();
    
    String file1 = (String) fileNames.nextElement();
    String filename1 = multi.getFilesystemName(file1);
    String file2 = (String) fileNames.nextElement();
    String filename2 = multi.getFilesystemName(file2);
    String file3 = (String) fileNames.nextElement();
    String filename3 = multi.getFilesystemName(file3);
    
    if(filename1 == null | filename2 == null | filename3 == null){
    	out.print("파일 업로드 오류");
    }
%>

</body>
</html>