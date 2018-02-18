<!-- processes the song update information -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<!--#include file="../incas/db_connect.asp"--> <!-- contains the info to connect to the database -->

<%

'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")

song = Request.Form("song_ID")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM Songs WHERE Song_ID=" & song & " ; "

'Set the cursor type we are using so we can navigate through the recordset
rsSongInfo.CursorType = 2

'Set the lock type so that the record is locked by ADO when it is updated
rsSongInfo.LockType = 3

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Update the record in the recordset
rsSongInfo.Fields("Song_Name") = Request.Form("name")
rsSongInfo.Fields("Artist") = Request.Form("artist")
rsSongInfo.Fields("Album") = Request.Form("album")
rsSongInfo.Fields("Lyrics") = Request.Form("lyrics")
rsSongInfo.Fields("Clip_URL") = Request.Form("clip")
rsSongInfo.Fields("Full_URL") = Request.Form("full")



'Write the updated recordset to the database
rsSongInfo.Update

'Reset server objects
rsSongInfo.Close
Set rsSongInfo = Nothing
Set adoCon = Nothing

'Return to the update select page in case another record needs deleting
  Response.Redirect "all_songs.asp"
%>

 <!--#include file="../incas/footer.asp"-->
