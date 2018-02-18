<!-- This page has all the information about the song. -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->


<div id="user_info">
<%
user_id = Session("user")

intURL = CInt(Request.QueryString("song_id"))

'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM Songs WHERE Song_ID = " & intURL & " ; "

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Write the HTML to display the current record in the recordset
Response.Write ("<br>")

Response.Write "<p>Song Name: " & rsSongInfo("Song_Name") & "<br />"
Response.Write "Artist: " &rsSongInfo("Artist") & "<br />"
Response.Write "Album: " & rsSongInfo("Album") & "<br />"
Response.Write "<a href=""lyrics.asp?song_id=" & intURL &"""> Lyrics</a><br />"

clip_url = rsSongInfo("Clip_URL")


Response.Write "<a href="""&clip_url&""">Listen to clip</a>"
Response.Write "<br />"

Response.Write "<a href=""add_to_playlist.asp?song_id=" & intURL & "&user_id=" & user_id & """>Add to playlist</a>"

'Reset server objects
rsSongInfo.Close
Set rsSongInfo = Nothing
Set adoCon = Nothing


%>

</div>

<br />
<br />
<br />
<div id="content_text_of_page">

<%
Response.Write "<h3 align=""center"">Comments on this song:</h3>"

'Create an ADO connection object
Set adoCon = Server.CreateObject("ADODB.Connection")

'Set an active connection to the Connection object using DSN connection
adoCon.Open "DSN=Ankur"


'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT Comments.Comment, Comments.Song_ID, User.User_Name, User.User_ID FROM [User] INNER JOIN Comments ON User.User_ID = Comments.User_ID WHERE (((Comments.Song_ID)= " & intURL & " ));"

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset
     user = rsUserInfo("User_ID")
     Response.Write ("<br />")
     Response.Write " - <a href=""user_info.asp?user_id=" & user & """>"&rsUserInfo("User_Name")&"</a> - "
     Response.Write rsUserInfo("Comment")&"<br />"
     Response.Write "<br />"
     Response.Write "<br />"
     'Move to the next record in the recordset
     rsUserInfo.MoveNext

Loop
Response.Write "<br />"
Response.Write "<br />"

Response.Write "<a href=""comment.asp?song_id=" & intURL & """>Leave a comment</a>"



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
