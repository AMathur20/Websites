<!-- This is just a test page for myself, nothing links to it, I wanted a way to list all the user in the database at once. -->

<!--#include file="incas/regheader.asp"-->


<!--#include file="incas/db_connect.asp"-->
<div id="user_info"></div>

<br />
<br />
<br />
<div id="content_text_of_page">
<%

'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT * FROM User;"

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the current record in the recordset
     Response.Write ("<br>")
     Response.Write (rsUserInfo("User_ID"))
     Response.Write ("<br>")
     Response.Write (rsUserInfo("User_name"))
     Response.Write ("<br>")
     Response.Write (rsUserInfo("Email_address"))
     Response.Write ("<br>")
     Response.Write (rsUserInfo("verify"))
     Response.Write ("<br>")
     'Move to the next record in the recordset
     rsUserInfo.MoveNext

Loop


'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
%>

</div>
<div id="menu">

</div>

<!--#include file="incas/footer.asp"-->

