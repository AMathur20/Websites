<!-- lists all the songs, if you click on a song, you will be able to see all the information of that song -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<div id="user_info">
<h1 align="center">Admin Panel - All Songs</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">

<%

'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT Song_ID, Song_Name FROM Songs ORDER BY Song_Name ASC;"

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsSongInfo.EOF

     'Write the HTML to display the current record in the recordset
     song_id = rsSongInfo("Song_ID")
     song_name = rsSongInfo("Song_Name")
     Response.Write "<p>"
     Response.Write "<a href=""song.asp?song_id=" & song_id & """>"&song_name&"</a>"
     Response.Write "</p>"

     'Move to the next record in the recordset
     rsSongInfo.MoveNext

Loop


'Reset server objects
rsSongInfo.Close
Set rsSongInfo = Nothing
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
