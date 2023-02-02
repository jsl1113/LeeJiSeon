<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="java.sql.*"%>   
 <%@ page import="java.net.URLEncoder, java.util.*" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        table  { width: 700px; text-align: center; }
        th     { background-color: cyan; }
        
        .left  { text-align: left;  }        
        .right { text-align: right; }

        a:link  { text-decoration: none; color: blue; }
        a:hover { text-decoration: none; color: red;  }
    </style>    
</head>
<body>

<form action="add_file.jsp" enctype="multipart/form-data" method="post">
    업로드할 파일을 선택하세요.<br>
    <input type="file" name="upload"><br>
    <input type="file" name="upload2"><br>
    <input type="file" name="upload3"><br>
    <input type="submit" value="업로드">
</form>
<br>

<table>
    <tr>
        <th>파일명     </th>
        <th>업로드 시간</th>
        <th>크기       </th>
        <th>삭제       </th>
    </tr>
    
<%  
   Connection conn = null;
   Statement stmt = null;

// 데이터베이스 연결관련정보를 문자열로 선언
	String jdbc_driver = "com.mysql.jdbc.Driver";
	String jdbc_url = "jdbc:mysql://127.0.0.1/jspdb";
    
    
    try { 
        Class.forName(jdbc_driver);
        conn = DriverManager.getConnection(jdbc_url,"jspbook","qweasdzxc0309!");
        stmt = conn.createStatement();
            
        ResultSet rs = stmt.executeQuery("select * from webhard");
        {
            while (rs.next()) {
%>    
            <tr>
                <td class="left">
                    <a href="File_Download_leejiseon.jsp?fileName=<%=URLEncoder.encode(rs.getString("fname"), "UTF-8") %>">
                        <%=rs.getString("fname")%>
                    </a>
                </td>
                <td><%=rs.getString("ftime")%></td>
                <td class="right"><%=rs.getInt("fsize")%>&nbsp;&nbsp;</td>
                <td><a href="del_file.jsp?num=<%=rs.getInt("num")%>">X</a></td>
            </tr>
<%  
            }
        
    } 
        }
    catch(Exception e) {
    e.printStackTrace();
    }
    
%>    
</table>

</body>
</html>
