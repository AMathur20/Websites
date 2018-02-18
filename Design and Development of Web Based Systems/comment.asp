<!-- This page gives the user the ability to leave comments for the song -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp-->
<!--#include file="incas/regheader.asp"--> <!--The html header information, such as <html><head><title> -->
<%
user_id = Session("user") REM Get user ID from the Session Variable
intURL = CInt(Request.QueryString("song_id")) REM Get the Song ID from the URL


%>
<div id="user_info">
<h2 align="center">Leave a Comment</h2>
<br />



</div>
<br />
<br />
<br />
<div id="content_text_of_page">
<br />
<br />
 <!-- This is the form which accepts the comments. When the user hits submit, the page "comment_process.asp" is loaded -->
<form name="form" method="post" action="comment_process.asp">
<h3>Comment: </h3><textarea name="Comment"></textarea><br /><br />
<input type="hidden" value="<%=user_id%>" name="user_id">
<input type="hidden" value="<%=intURL%>" name="song_id">
<input type="submit" name="Submit" value="Submit">
</form>
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

%>


<a href="manage_playlist.asp">Manage Playlist</a><br />
<a href="logout.asp">Logout</a>
</div>
<!--#include file="incas/footer.asp"-->
 
