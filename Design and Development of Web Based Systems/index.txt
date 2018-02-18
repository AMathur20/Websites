<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<%
user_id = Session("user") REM this gets the User ID of the person logged in. It is stored in Session Variables

REM connect to the Database and find out the User name, that goes with the user ID
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")
strSQL = "SELECT User_Name FROM User WHERE User_ID = " & user_id & " ; "
rsUserInfo.Open strSQL, adoCon
user = rsUserInfo("User_Name")
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
%>
<div id="user_info">

<h2>Welcome <%=user%></h2>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<h2>Menu is down there</h2>
<img src="incas/down_arrow.gif" alt="Down Arrow" width="187" height="196" />
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

<!--#include file="incas/footer.asp"--> REM This the ending html stuff
