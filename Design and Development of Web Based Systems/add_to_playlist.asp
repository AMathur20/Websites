<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->
<<%
user_id = CInt(Request.QueryString("user_id")) REM Get the user ID from the url
song_id = CInt(Request.QueryString("song_id")) REM Get the song ID from the url

REM Connect to the Database
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")
REM This will add a new record to the table Playlist that has the user ID, and the song ID.
strSQL = "SELECT * FROM Playlist;"
rsUserInfo.CursorType = 2
rsUserInfo.LockType = 3
rsUserInfo.Open strSQL, adoCon
rsUserInfo.AddNew
rsUserInfo.Fields("User_ID") = user_id
rsUserInfo.Fields("Song_ID") = song_id
rsUserInfo.Update
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
Response.Redirect ("index.asp") REM Send the user back to the index page
%>

<!--#include file="incas/footer.asp"--> REM The html footer, contains the copyright, and end tags such as </body></html>