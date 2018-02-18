<!-- This page allows new user to register for the system -->

<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<div id="user_info">
<h2 align="center">Register a new account</h2>

<%
REM The register_process.asp pager check for three things before allowing the user to register.
REM     First, both instances of the email must be the same. Next, both instances of the password
REM     must be the same. Finally, the email address must be a Stern email address. If any of these
REM     tests fail, the user is sent back to this page, with an appropriate error code. The following
REM     statements test to see if there is an error code, and then prints the matching error statement.

name = Request.QueryString("name")
err_id = Request.QueryString("error_id")

if err_id = 1 then
Response.Write ("<p class=""error"">Email was not entered correctly!</p>")
End if
if err_id = 2 then
Response.Write ("<p class=""error"">Password was not entered correctly!</p>")
End if
if err_id = 3 then
Response.Write ("<p class=""error"">You must enter a valid Stern Email Address!</p>")
End if
%>

</div>

<br />
<br />
<br />
<div id="content_text_of_page">


<!-- Begin form code -->
<form name="form" method="post" action="register_process.asp">
     Name: <input type="text" name="name" maxlength="20" value="<%=name%>" >
     <br />
     Email Address (Must be a valid Stern Email Address): <input type="text" name="email" maxlength="50">
     <br />
     Repeat Email Address: <input type="text" name="email1" maxlength="50">
     <br />
     Show email address to other users?
     <input type="checkbox" name="show_email" checked value="1"><br />
     Password: <input type="password" name="password" maxlength="10"><br />
     Repeat Password: <input type="password" name="password1" maxlength="10"><br />
     <input type="submit" name="Submit" value="Submit">
</form>
<!-- End form code -->
</div>
<div id="menu">
</div>

<!--#include file="incas/footer.asp"-->
