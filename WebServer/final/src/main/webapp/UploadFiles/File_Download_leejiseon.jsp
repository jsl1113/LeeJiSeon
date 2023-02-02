<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.io.*, java.text.*, java.lang.*, java.util.*, java.net.*" %>

<%
request.setCharacterEncoding("UTF-8");

String root = application.getRealPath("/");
String savePath = root + "UploadFiles";

String filename = request.getParameter("fileName");
String orgfilename = request.getParameter("fileName");

InputStream in = null;
OutputStream os = null;
File file = null;
String client = "";

try {
	file = new File(savePath, filename);
	in = new FileInputStream(file);
	client = request.getHeader("User-Agent");
	
	response.reset();
	response.setContentType("application/octet-stream");
	response.setHeader("Content-Description", "JSP Generated Data");
	
	if(client.indexOf("MSIE") != -1) {
		response.setHeader("Content-Disposition", "attachmnet; filename=" 
				+ new String(orgfilename.getBytes("KSC5601"), "ISO8859_1"));
	} else {
		orgfilename = new String(orgfilename.getBytes("UTF-8"), "ISO-8859-1");
		
		response.setHeader("Content-Disposition", "attachment; filename=\"" + orgfilename + "\"");
		response.setHeader("Content-Type", "application/octet-stream; charset=utf-8");
	}
	response.setHeader("Content-Length", ""+file.length());
	out.clear();
	out = pageContext.pushBody();
	
	os = response.getOutputStream();
	byte b[] = new byte[(int) file.length()];
	
	int l = 0;
	while((l = in.read(b)) > 0) {
		os.write(b, 0, l);
	}
	in.close();
	os.close();
} catch(Exception e){
	e.printStackTrace();
}

%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type"  content="text/html; charset=UTF-8">
<title> </title>
</head>
<body>

</body>
</html>