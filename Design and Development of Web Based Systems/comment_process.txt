<!-- This file process the comments sent from comment.asp, and inserts it into the database -->
<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->
<%
REM The information is passed via Post, so I use Request.Form to get the information
Comment = Request.Form("Comment")

user_id = Request.Form("user_id")

song_id = Request.Form("song_id")

REM Connect to the database and add the comment
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")
strSQL = "SELECT Song_ID, User_ID, Comment FROM Comments;"
rsUserInfo.CursorType = 2
rsUserInfo.LockType = 3
rsUserInfo.Open strSQL, adoCon
rsUserInfo.AddNew
rsUserInfo.Fields("Comment") = Comment
rsUserInfo.Fields("User_ID") = user_id
rsUserInfo.Fields("Song_ID") = song_id
rsUserInfo.Update

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

REM Send the user back to the song information page
send_back = "song.asp?song_id="&song_id&""

Response.redirect (send_back)

%>


<div id="user_info">
<h2 align="center">Please Wait</h2>
</div>
<br />
<br />
<br />
<div id="content_text_of_page">
</div>
<div id="menu">
<a href="search.asp">Search for a new song</a><br />
<%

u_file="lists/"&user&"_"&user_id&"_list.smil" REM This is the actual playlist file, an example: Anks329_1_list.smil
set fso = createobject("scripting.filesystemobject")
REM This will check if the file exists or not. If it does it will print "Regenerate your playlist" otherwise, simply "Generate"
if fso.FileExists (server.mappath(u_file)) then
Response.Write "<a href='"& u_file &"'>Listen to your playlist</a><br />"
Response.Write "<a href=""playlist_generator.asp"">Regenerate your playlist</a><br />"
else
Response.Write "<a href=""playlist_generator.asp"">Generate your playlist</a><br />"
end if



<a href="manage_playlist.asp">Manage Playlist</a><br />
<a href="logout.asp">Logout</a>
</div>

<!--#include file="incas/footer.asp"-->