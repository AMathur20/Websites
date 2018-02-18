<!-- This page process the log in, and if a valid user allows them into the system -->
<!--#include file="incas/MD5.asp"--> <!-- Needed to encrypt the password -->
<!--#include file="incas/regheader.asp"-->
<!--#include file="incas/db_connect.asp"-->
<div id="user_info">

<%


REM The passwords are stored in the database as MD5 checksum, they are encrypted, so no one can take the database and get passwords
REM So the next 2 lines get the password via Post, and creates the MD5 sum using the file incas/MD5.asp
password_work = Request.Form("password")
final_password = MD5(password_work)

user = Request.Form("name")

REM Connect to the DB and check to see if the user information is valid
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")
strSQL = "SELECT User_Name, User_id, Password, Verify FROM User WHERE User_Name = '"&user&"';"
rsUserInfo.Open strSQL, adoCon

user_db = rsUserInfo("User_name")
pass_db = rsUserInfo("Password")
verified = rsUserInfo("Verify")

REM This first checks to make sure that the user has verified their email address that they registered with.
if verified = "False" then
   Response.Write "<h2>You have not verified you email, please do that first</h1>"
Else
		  REM If they have verified their email, then check if the password is correct or not
	if final_password = pass_db Then
			  REM If the password is correct, then set the Session Varaible with Authenticated = 1, and the User ID
		Session("Authenticated") = 1
		Session("user") = rsUserInfo("User_id")
		Response.Redirect ("index.asp")
	Else
			  REM if the password is wrong, then set Authenticated = 0, and send the user back to the log in page
		Session("Authenticated") = 0
		Response.Redirect ("login.asp")
End if

End if

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
%>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
</div>
<div id="menu">
</div>

<!--#include file="incas/footer.asp"-->