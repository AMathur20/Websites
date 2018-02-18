<!-- logs the admin user out -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->

<div id="user_info">
<h1 align="center">Admin Panel - Logout</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<%
Session.Contents.RemoveAll()
Session.Abandon
Response.write "You have logged out!"
%>

</div>
<div id="menu">
</div>

<!--#include file="../incas/footer.asp"-->