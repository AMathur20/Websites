<!-- This page verifies the user's email address and with then allow them to log into the system>

<!--#include file="incas/MD5.asp"--> <!-- This is needed to create the MD5 checksums -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<div id="user_info">


<h2 align="center">User Verification</h2>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">


<%
REM The link that the user followed from their email, contains two pieces of
REM     information: the user name, and the MD5 checksum. The next 2 statements
REM     grab this information
user = Request.QueryString("user")
check_MD5 = Request.QueryString("check")


REM Connect to the database and get the database version of the MD5 checksum for this user.
'Create an ADO recordset object
Set rsUserGet = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT User_Name, Check FROM User WHERE User_Name = '"& user & "'"

rsUserGet.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserGet.EOF

     'Write the HTML to display the current record in the recordset
     db_check = rsUserGet("Check")
     'Move to the next record in the recordset
     rsUserGet.MoveNext

Loop
'Reset server objects
rsUserGet.Close
Set rsSongInfo = Nothing
Set adoCon = Nothing


REM The If statement checks to make sure that the database MD5 checksum is the
REM     same as the one the user has. If they are the same, then update the
REM     database field "Verify" in table User to True, and empty the database
REM     MD5 checksum.
if db_check = check_MD5 then
	'Create an ADO connection object
	Set adoCon = Server.CreateObject("ADODB.Connection")

	'Set an active connection to the Connection object using DSN connection
	adoCon.Open "DSN=ankur"


	'Create an ADO recordset object
	Set rsUserUpdate = Server.CreateObject("ADODB.Recordset")

	'Initialise the strSQL variable with an SQL statement to query the database
	strSQL = "SELECT * FROM User WHERE User_Name = '"& user & "'"

	'Set the cursor type we are using so we can navigate through the recordset
	rsUserUpdate.CursorType = 2

	'Set the lock type so that the record is locked by ADO when it is updated
	rsUserUpdate.LockType = 3

	'Open the recordset with the SQL query
	rsUserUpdate.Open strSQL, adoCon

	'Update the record in the recordset
	rsUserUpdate.Fields("Verify") = "True"
	rsUserUpdate.Fields("Check") = ""
	'Write the updated recordset to the database
	rsUserUpdate.Update

	'Reset server objects
	rsUserUpdate.Close
	Set rsSongInfo = Nothing
	Set adoCon = Nothing
	Response.Write "Email Verified. You can now <a href=""login.asp"">Log in.</a>"

Else    REM Otherwise, if the two MD5 checksums are not the same, then print an error
    response.write "Email not verified, please try again."
End if

%>
</div>
<div id="menu">

</div>

<!--#include file="incas/footer.asp"-->

