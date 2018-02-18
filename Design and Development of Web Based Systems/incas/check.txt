<%
REM This checks for a log in in the session variable
If Session("Authenticated") = 0 Then
  Response.Redirect ("Login.asp")
End If
%>