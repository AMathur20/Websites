<!-- This page creates a new .smil file on the server. This smil file contains the urls for the full length songs. -->
<!-- Once the file is created it is sent to the user, who opens it with Real Player, and the songs then stream via Real Player. -->

<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<%
user_id = Session("user")
'Response.Write (user_id)
'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User WHERE User_ID = " & user_id & " ; "

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon
user = rsUserInfo("User_Name")
'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

Const ForReading   = 1
Const ForWriting   = 2

u_file="F:\Spring2005\Ankur/lists/"&user&"_"&user_id&"_list.smil"   REM This is the full path the file

'set fsa = CreateObject("Scripting.FileSystemObject")
'fsa.DeleteFile(u_file, true)
   
   
   
set fs = CreateObject("Scripting.FileSystemObject")

'Response.write(u_file)
set file = fs.OpenTextFile(u_file, ForWriting, true, false)

REM All smil files need to start with this.
file.WriteLine("<smil>")
file.WriteLine("<body>")
file.WriteLine("<seq>")  REM This tells Real Player to play the files in sequential order




'Create an ADO connection object
Set adoCon = Server.CreateObject("ADODB.Connection")

'Set an active connection to the Connection object using DSN connection
adoCon.Open "DSN=Ankur"

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT Playlist.User_ID, Playlist.Song_ID, Songs.Full_Url FROM Songs INNER JOIN Playlist ON Songs.Song_ID = Playlist.Song_ID WHERE (((Playlist.User_ID)= " & user_id & " ));"
REM The SQL query is a bit complicated. I want to select the full url from the Songs table. But I only want the songs
REM    that the user has in their playlist. So, I need to join the two tables, so that I am only selecting full urls for
REM    those songs that the user has in their playlist.


'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF


     file.Writeline("<audio src=""" &  rsUserInfo("Full_Url") & """/>") REM Write the full url of the song into the smil file


     rsUserInfo.MoveNext

Loop


'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

REM This is the end of the smil file, again this information is needed to make it valid.
file.WriteLine("</seq>")
file.WriteLine("</body>")
file.WriteLine("</smil>")

file.Close REM Close the smil file on the server


Response.redirect("index.asp") REM Sends the user back to the index page.


 %>