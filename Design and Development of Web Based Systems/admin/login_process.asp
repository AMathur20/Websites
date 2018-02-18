<!-- makes sure the admin logs in with the correct password -->

<!--#include file="../incas/MD5.asp"--> <!-- needed to calculate the MD5 checksums -->

<!--#include file="../incas/header.asp"--> <!-- contains the header information -->


<!--#include file="../incas/db_connect.asp"-->

<%

password_work = Request.Form("password")
password_MD5 = MD5(password_work)

user = Request.Form("name")
user_md5 = MD5(user)



'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT User_Name, Password FROM Admin WHERE User_Name = '"&user_md5&"';"

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

user_db = rsUserInfo("User_Name")
pass_db = rsUserInfo("Password")

if user_MD5 = User_Db Then
	if password_MD5 = pass_db Then
		Response.Write ("Welcome: "&user_db)
		Session("Super_Auth") = 1
		Response.Redirect ("index.asp")
	Else
		Response.Write ("SORRY!")
		Session("Super_Auth") = 0
		Response.Redirect ("login.asp")
	End if
Else
    Response.Redirect("login.asp")
End if

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing


%>


<!--#include file="../incas/footer.asp"-->