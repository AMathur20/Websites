<!--This page has the lyrics for the song requested -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<div id="user_info">
<h2 align="center">Lyrics</h2>

</div>

<br />
<br />
<br />
<div id="content_text_of_page">

<%


user_id = Session("user")

intURL = CInt(Request.QueryString("song_id"))

'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT Lyrics FROM Songs WHERE Song_ID = " & intURL & " ; "

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Write the HTML to display the current record in the recordset
Response.Write ("<br>")

Response.Write "<h3>Lryrics:</h3> <p>" & rsSongInfo("Lyrics") & "</p>"


'Reset server objects
rsSongInfo.Close
Set rsSongInfo = Nothing
Set adoCon = Nothing

%>

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
