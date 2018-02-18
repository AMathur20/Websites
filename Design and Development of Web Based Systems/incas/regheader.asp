<!-- This file has the header information for all pages. -->

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

	<head>
<%
REM I originally created, and tested the whole system in Firefox. So all of the
REM     stylesheets worked in FireFox. When I tested it in Internet Explorer,
REM     I found that the styles were messed up. So I created another stylesheet
REM     just for Internet Explorer. I then needed a way to switch between the
REM     two stylesheets. The following code test to see what browser the user
REM     is using, and then gives the appropriate style sheet to user.

'Detect Client Browser Environment
Dim strUserAgent ' browser type capture
Dim IE5Plus, IE55Plus, css2compatible ' general purpose capabilities
Dim NS, NS4, NS6, IE, IE4, IE5, IE6 ' Browser Boolean Constants
Dim Opera, Opera5                   ' Browser Boolean Constants
Dim OtherBrowser ' obsolete browser flags

strUserAgent = UCase(CStr(Request.ServerVariables("HTTP_USER_AGENT")))

'Explorer
IE = FALSE
IE4 = FALSE
IE5 = FALSE
IE6 = FALSE
If InStr(strUserAgent, "MSIE") Then
    IE = TRUE
End If
If InStr(strUserAgent, "MSIE 4") Then
    IE4 = TRUE
ElseIf InStr(strUserAgent, "MSIE 5") Then
    IE5 = TRUE
ElseIf InStr(strUserAgent, "MSIE 6") Then
    IE6 = TRUE
End If

'Opera
Opera = FALSE
Opera5 = FALSE
If InStr(strUserAgent, "Opera") Then
    Opera = TRUE
End If
If InStr(strUserAgent, "Opera 5") _
Or InStr(strUserAgent, "Opera/5") Then
    Opera5 = TRUE
End If

'Netscape
NS = FALSE
NS4 = FALSE
NS6 = FALSE
If InStr(strUserAgent, "Netscape6") Then
    NS6 = TRUE
ElseIf InStr(strUserAgent, "Mozilla/4") AND Not (IE OR Opera) Then
    NS4 = TRUE
End If
'This may not be 100% accurate; there are a lot of browsers
'based on the Mozilla core
If NS6 OR NS4 OR (InStr(strUserAgent, "Mozilla") _
   AND Not (IE OR Opera)) Then
    NS = TRUE
End If

'If the document looses the Loose DTD instead of Transitional or
'Strict then set css2compatible to FALSE for IE6 instead
If Opera5 Or IE6 Or NS6 Then
    css2compatible = TRUE
Else
    css2compatible = FALSE
End If

OtherBrowser = FALSE
If Not (IE OR NS4 OR NS6 OR Opera) Then
    OtherBrowser = TRUE
End If
If InStr(strUserAgent, "MSIE 5") _
Or InStr(strUserAgent, "MSIE 6") Then
    IE5Plus = TRUE
Else
    IE5Plus = FALSE
End If

If IE Then
   response.write(" <link href=""incas/ie_style.css"" type=""text/css"" rel=""Stylesheet"" />")
Else
    response.write(" <link href=""incas/firefox_style.css"" type=""text/css"" rel=""Stylesheet"" />")
End if
%>
		<title>Anks329 Music Database</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	</head>

	<body>
<div id="container">