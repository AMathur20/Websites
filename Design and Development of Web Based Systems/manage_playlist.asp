<!-- This page allows the user to manage their playlist, delete a single song, or delete the entire list. -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<div id="user_info">
<%


user_id = Session("user")

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = " SELECT Playlist.Song_ID, Playlist.User_ID, Songs.Song_Name FROM Songs INNER JOIN Playlist ON Songs.Song_ID = Playlist.Song_ID WHERE (((Playlist.User_ID)= " & user_id & " ));"

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

Response.Write ("<h2 align=""center"">Manage Playlist</h2> <br />")
Response.Write ("<a href=""delete_playlist.asp"">Delete Entire List</a>")
%>


</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<p>
<%

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset

     song =  rsUserInfo("Song_ID")
     Response.Write (rsUserInfo("Song_Name")& " - <a href=""delete_song_from_list.asp?song_id=" & song & """>Delete</a><br />")
     Response.Write ("")

     'Move to the next record in the recordset
     rsUserInfo.MoveNext

Loop

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

%>
</p>
</div>
<div id="menu">
<a href="search.asp">Search for a new song</a><br />
<%

u_file="lists/"&user&"_"&user_id&"_list.smil"


set fso = createobject("scripting.filesystemobject")


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
