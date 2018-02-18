<%
REM This checks for an Administrative login in the session variable
If Session("Super_Auth") = 0 Then
  Response.Redirect ("Login.asp")
End If
%>