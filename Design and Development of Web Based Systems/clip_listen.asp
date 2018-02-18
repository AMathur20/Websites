<!-- This file creates a temporary .ram file on the server. This file is then sent to the user so the song clip can be correctly streamed to the user. -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->
<%

song_id = CInt(Request.QueryString("song_id")) REM Get the Song ID from the URL

REM Create a file, this is just temporary for this clip, if is exists already, it will overwrite the file
u_file="F:\Spring2005\Ankur/lists/temp"&user_id&".ram"
set fs = CreateObject("Scripting.FileSystemObject")
set file = fs.CreateTextFile(u_file, true, false)

REM Connect to the Database
Set adoCon = Server.CreateObject("ADODB.Connection")
adoCon.Open "DSN=Ankur"
REM This will get the clip url from the database, where the song ID is equal to what the URL gave
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")
strSQL = "SELECT Songs.Song_ID, Songs.Clip_Url FROM Songs WHERE (((Songs.Song_ID)= " & song_id & " ));"
rsUserInfo.Open strSQL, adoCon
Do While not rsUserInfo.EOF
     REM Once I have the url, I write the URL into the file
     file.Writeline(rsUserInfo("Clip_Url") )

     rsUserInfo.MoveNext

Loop

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
REM And close the file
file.Close

REM Open the temp file, so it starts to play, and streams the clip into Real Player
Response.redirect("lists/temp"&user_id&".ram")

%>