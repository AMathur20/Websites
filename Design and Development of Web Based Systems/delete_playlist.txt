<!-- This page will delete the everything in the Table Playlist that matches the user ID of the current user -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->
<%

user_id = Session("user")

strDelete="DELETE FROM Playlist WHERE User_ID="&user_id&""

'execute the delete
adoCon.Execute (strDelete)

REM Send the user back to the manage playlist page.
Response.Redirect "manage_playlist.asp"
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