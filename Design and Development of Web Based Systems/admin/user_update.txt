<!-- this page has a form with is populated from the database, with all the info of a specific user, which the admin can update -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<div id="user_info">
<h1 align="center">Admin Panel - Update User Information</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<%

intURL = Request.Form("user_id")

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User WHERE User_ID = " & intURL & " ; "

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset

     Response.Write "<Form method=""post"" action=""user_update_process.asp"">"
     Response.Write "<p>User Name: <input type=""text"" name=""User_Name"" value=""" & rsUserInfo("User_Name") & """><br/>"
     Response.Write "Email Address: <input type=""text"" name=""Email_address"" value=""" & rsUserInfo("Email_address")  & """><br/>"


     if rsUserInfo("Show_email") = "True" Then
     show = "1"
     Response.Write "Show Email Address: <input type=""checkbox"" checked name=""Show_email"" value=""" & show  & """><br/>"
     Else
     show = "0"
     Response.Write "Show Email Address: <input type=""checkbox""  name=""Show_email"" value=""" & show  & """><br/>"
     End if

     if rsUserInfo("Verify") = "True" Then
     Verify = "1"
     Response.Write "Email Verified: <input type=""checkbox"" checked name=""Verify_email"" value=""" & Verify  & """><br/>"
     Else
     Verify = "0"
     Response.Write "Email Verified: <input type=""checkbox""  name=""Verify_email"" value=""" & Verify  & """><br/>"
     End if


     Response.Write "<input type=""hidden"" name=""user_ID"" value=" & rsUserInfo("User_ID") & ">"
     Response.Write "<input type=""submit"" name=""submit"" value=""Update User Information"">"
     Response.Write "</form>"

     'Move to the next record in the recordset
     rsUserInfo.MoveNext

Loop


'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
%>
</div>
<div id="menu">
<a href="add_new_song.asp">Add a new song</a><br />
<a href="all_songs.asp">List all songs</a><br />
<a href="all_users.asp">List all users<a><br />
<a href="logout.asp">Logout</a><br />

</div>

<!--#include file="../incas/footer.asp"-->


