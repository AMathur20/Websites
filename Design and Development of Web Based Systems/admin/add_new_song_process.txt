<!-- This page processes the new song information -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->


<!--#include file="../incas/db_connect.asp"-->
<%



clip_start = Request.Form("Clip")
full_start = Request.Form("full")

base = "rtsp://jupiter.stern.nyu.edu:554/Spring2005/Ankur/media/"
clip_url = base & "clips/"&clip_start
full_url = base & "full/" & full_start


'Create an ADO recordset object
Set rsSongInfo = Server.CreateObject("ADODB.Recordset")



'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM Songs; "

'Set the cursor type we are using so we can navigate through the recordset
rsSongInfo.CursorType = 2

'Set the lock type so that the record is locked by ADO when it is updated
rsSongInfo.LockType = 3

'Open the recordset with the SQL query
rsSongInfo.Open strSQL, adoCon

'Tell the recordset we are adding a new record to it
rsSongInfo.AddNew

'Update the record in the recordset
rsSongInfo.Fields("Song_Name") = Request.Form("name")
rsSongInfo.Fields("Artist") = Request.Form("artist")
rsSongInfo.Fields("Album") = Request.Form("album")
rsSongInfo.Fields("Lyrics") = Request.Form("lyrics")
rsSongInfo.Fields("Clip_URL") = clip_url
rsSongInfo.Fields("Full_URL") = full_url



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
