<!-- lists all the users, if you click on a user, you can see all the information about that user -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<div id="user_info">
<h1 align="center">Admin Panel - All Users</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<%

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT User_ID, User_Name FROM User;"

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset
     user_id = rsUserInfo("User_ID")
     user_name = rsUserInfo("User_Name")
     Response.Write "<p>"
     Response.Write "<a href=""user.asp?user_id=" & user_id & """>"&user_name&"</a>"
     Response.Write "</p>"

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