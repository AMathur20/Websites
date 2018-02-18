<!-- This page deletes a single song from the Table Playlist where the User ID is of the current user -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->

<%
user_id = Session("user")


REM I did not use my database connector include file for this page because I
REM   was getting errors when I was using it. So, I just recreated it here. I
REM   am not sure what the problem was, so I just worked around it.

intURL = CInt(Request.QueryString("song_id")) REM Get the song ID from the URL

Dim adoCon           'Holds the Database Connection Object
Dim rsDeleteEntry   'Holds the recordset for the record to be deleted
Dim strSQL            'Holds the SQL query to query the database
Dim lngRecordNo     'Holds the record number to be deleted

REM Connect to the database and delete the record
Set adoCon = Server.CreateObject("ADODB.Connection")
adoCon.Open "DSN=Ankur"
lngRecordNo = intURL
Set rsDeleteEntry = Server.CreateObject("ADODB.Recordset")
strSQL = "SELECT * FROM Playlist WHERE Song_ID=" & lngRecordNo
rsDeleteEntry.LockType = 3
rsDeleteEntry.Open strSQL, adoCon
rsDeleteEntry.Delete

'Reset server objects
rsDeleteEntry.Close
Set rsDeleteEntry = Nothing
Set adoCon = Nothing
REM Sends the user back to the manage playlist page
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