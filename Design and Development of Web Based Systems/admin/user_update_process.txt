<!-- processes the user upadte page -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<%

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

user = Request.Form("user_ID")

show = Request.Form("Show_email")
verify = Request.Form("Verify_email")



if show ="0" then
Show_email_enter = "True"
Else
Show_email_enter = "False"
End if


if Verify_email ="0" then
Verify_email_enter = "False"
Else
Verify_email_enter = "True"
End if

Response.write (Verify_email_enter)

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User WHERE User_ID=" & user & " ; "

'Set the cursor type we are using so we can navigate through the recordset
rsUserInfo.CursorType = 2

'Set the lock type so that the record is locked by ADO when it is updated
rsUserInfo.LockType = 3

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Update the record in the recordset
rsUserInfo.Fields("User_Name") = Request.Form("User_Name")
rsUserInfo.Fields("Email_address") = Request.Form("Email_address")
rsUserInfo.Fields("Show_email") = Show_email_enter
rsUserInfo.Fields("Verify") = Verify_email_enter


'Write the updated recordset to the database
rsUserInfo.Update

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

'Return to the update select page in case another record needs deleting
Response.Redirect "all_users.asp"
%>

 <!--#include file="../incas/footer.asp"-->
