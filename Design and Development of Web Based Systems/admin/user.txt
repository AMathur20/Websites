<!-- has all the info about the user, and has a button which will take the admin to a page to update the user info -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<div id="user_info">
<h1 align="center">Admin Panel - User Information</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<%

intURL = CInt(Request.QueryString("user_id"))

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User WHERE User_ID = " & intURL & " ; "

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset
     Response.Write ("<br>")
     
     if rsUserInfo("Show_email") = "True" Then
     show="Yes"
     Else
     show="No"
     End if
     
     
     
     Response.Write "<p>User Name: " & rsUserInfo("User_Name") & "<br/>"
     Response.Write "Email Address: " & rsUserInfo("Email_address") & "<br/>"
     Response.Write "Show Email: " & show & "<br/>"
     Response.Write "Email Verified: " & rsUserInfo("Verify") & "<br/>"
     Response.Write "Check Sum: " & rsUserInfo("Check") & "<br/>"
     
     Response.Write "<form method=""post"" action=""user_update.asp"">"
     Response.Write "<input type=""hidden"" name=""user_id"" value=" & rsUserInfo("User_ID") & ">"
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


