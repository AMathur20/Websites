<!-- This page logs the user out of the system. -->

<!--#include file="incas/regheader.asp"-->
<div id="user_info">

<%
REM This deleted the Session variables and abandons the session, effectively logging them out of the system.
Session.Contents.RemoveAll()
Session.Abandon
Response.write "<h2>You have logged out!</h2>"

%>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
</div>
<div id="menu">
</div>

<!--#include file="incas/footer.asp"-->