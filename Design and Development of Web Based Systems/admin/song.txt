<!-- shows all the information of a specific song, and has a button which will let the admin change the information -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<div id="user_info">
<h1 align="center">Admin Panel - Song Information</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">

<%

intURL = CInt(Request.QueryString("song_id"))

'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM Songs WHERE Song_ID = " & intURL & " ; "

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsSongInfo.EOF

     'Write the HTML to display the current record in the recordset
     Response.Write ("<br>")
     
     
     Response.Write "<p>Song Name: " & rsSongInfo("Song_Name") & "<br/>"
     Response.Write "Artist: " &rsSongInfo("Artist") & "<br/>"
     Response.Write "Album: " & rsSongInfo("Album") & "<br/>"
     Response.Write "URL of Clip: " & rsSongInfo("Clip_URL") & "<br/>"
     Response.Write "URL of Full song: " & rsSongInfo("Full_URL") & "<br/>"
     Response.Write "Lyrics: " &rsSongInfo("Lyrics") & "</p>"


     Response.Write "<form method=""post"" action=""song_update.asp"">"
     Response.Write "<input type=""hidden"" name=""song_id"" value=" & rsSongInfo("Song_ID") & ">"
     Response.Write "<input type=""submit"" name=""submit"" value=""Update Song Information"">"
     Response.Write "</form>"

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


