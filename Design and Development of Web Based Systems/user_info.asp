<!-- This file shows the user information of any user. Basically it shows the User ID, -->
<!-- 	the user name, and the user's email address if they have made it visable. -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->
<div id="user_info">
<h2 align="center">User Info</h2>
<%

user = CInt(Request.QueryString("user_id"))

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User WHERE User_ID = " & user & " ; "

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset


     Response.Write "<p>User ID: " & rsUserInfo("User_ID") & "<br/>"
     Response.Write "User Name: " &rsUserInfo("User_Name") & "<br/>"

     show_email = rsUserInfo("Show_email")

     if show_email = "True" Then
          Response.Write "Email: " & rsUserInfo("Email_address") & "<br/>"
     Else
          Response.Write "Email: Hidden<br/>"
     End if

     'Move to the next record in the recordset
     rsUserInfo.MoveNext

Loop

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
<a href="search.asp">Search for a new song</a><br />
<%

u_file="lists/"&user&"_"&user_id&"_list.smil"


set fso = createobject("scripting.filesystemobject")

' This will check to see if the parent directory has an index.asp page in its directory
' if so it will hyper-link it
if fso.FileExists (server.mappath(u_file)) then
Response.Write "<a href='"& u_file &"'>Listen to your playlist</a><br />"
Response.Write "<a href=""playlist_generator.asp"">Regenerate your playlist</a><br />"
else
Response.Write "<a href=""playlist_generator.asp"">Generate your playlist</a><br />"
end if
%>


<a href="manage_playlist.asp">Manage Playlist</a><br />
<a href="logout.asp">Logout</a>
</div>

<!--#include file="incas/footer.asp"-->