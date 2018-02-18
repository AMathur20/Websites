<!-- This page processes the registration information of the user. -->

<!--#include file="incas/MD5.asp"--> <~-- This file is needed to create MD5 checksums, which I use for more security -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<%
REM The information is sent via Post, so I use Request.Form to retrieve it.
email = Request.Form("email")
email1 = Request.Form("email1")
password = Request.Form("password")
password1 = Request.Form("password1")
namer = Request.Form("name")

check_email = "stern.nyu.edu" REM All email address must contain this string in them


REM This if statement check to make sure the email is a Stern email. It checks
REM      by using the function InStr. It's checking to see if the check_email
REM      string is in the email string. If it is not, then the user is sent back
REM      to the registration page with the correct error code.
if InStr (1,email,check_email,1)>0 then
   check = "True"
Else
	namer1 = Server.URLEncode(namer)
	Response.Redirect "register.asp?error_id=3&name=" & namer1 & ""
End if



REM This if statement check to make sure the two email entries are the same.
REM      If they are not, the user is sent back to the registration page with
REM      the correct error code.
if email = email1 then
   valid1 = "yes"
Else
	namer1 = Server.URLEncode(namer)
	Response.Redirect "register.asp?error_id=1&name=" & namer1 & ""
End if



REM This if statement check to make sure the two password entries are the same.
REM      If they are not, the user is sent back to the registration page with
REM      the correct error code.
if password = password1 then
   valid2 = "yes"
Else
	namer1 = Server.URLEncode(namer)
	Response.Redirect "register.asp?error_id=2&name=" & namer1 & ""
end if



REM This checks to see if the user want their email address shown to everyone.
REM      Based on their answer, the variable "Show_email_enter" is set to true or false/
show = Request.Form("Show_email")
if show ="1" then
   Show_email_enter = "True"
Else
    Show_email_enter = "False"
End if


REM This takes the password and creates an MD5 checksum of it. The actual password
REM      is not put into the database, rather I use the checksums. This adds a
REM      layer of protection, incase someone manages to get their hands on the
REM      database, they won't be able to get any passwords out of it.
password_work = password
final_password = MD5(password_work)
user = Request.Form("name")


REM The check1 variable combines the user name, the password, and the current time.
REM     Then a MD5 checksum of it is created. I use to make users verify their
REM     email address.
check1 = "" & user & "" & password & time
check_MD5 = MD5(check1)

REM Send the confirmation email. This email contains a link to the verify page.
REM      The link also contains the user name, and the check_MD5 variable. This
REM      process makes it very hard for someone to create an account with a fabricated
REM      email address. The main reason I did was for the challenge. On other sites
REM      I have seen this in action, and wanted to replicate it.
Set myMail=CreateObject("CDO.Message")
myMail.Subject="Email Verification"
myMail.From="Ankur.Mathur@stern.nyu.edu"
myMail.To=email1
myMail.HTMLBody = "Complete your registration process by clicking on the following link:<br /><a href=""http://jupiter.stern.nyu.edu/spring2005/ankur/verify.asp?user=" & user & "&check=" & check_MD5& """>Verify Email Address</a>"
myMail.Configuration.Fields.Item ("http://schemas.microsoft.com/cdo/configuration/sendusing")=2
'Name or IP of remote SMTP server
myMail.Configuration.Fields.Item ("http://schemas.microsoft.com/cdo/configuration/smtpserver")="smtp.stern.nyu.edu"
'Server port
myMail.Configuration.Fields.Item ("http://schemas.microsoft.com/cdo/configuration/smtpserverport") =25
myMail.Configuration.Fields.Update

myMail.Send

REM Now comes the real meat of the page, inserting all this data into the database.


'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")


'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT User_Name, Password, Email_address, Show_email, Verify, Check FROM User;"

'Set the cursor type we are using so we can navigate through the recordset
rsUserInfo.CursorType = 2

'Set the lock type so that the record is locked by ADO when it is updated
rsUserInfo.LockType = 3

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Tell the recordset we are adding a new record to it
rsUserInfo.AddNew

'Add a new record to the recordset
rsUserInfo.Fields("User_Name") = user
rsUserInfo.Fields("Password") = final_password
rsUserInfo.Fields("Email_address") = email
rsUserInfo.Fields("Show_email") = Show_email_enter
rsUserInfo.Fields("Verify") = "False"
REM This field starts off as False, and the user can not log in, until it is true.
REM 	It becomes true when the user follows the link in their email
rsUserInfo.Fields("Check") = check_md5

'Write the updated recordset to the database
rsUserInfo.Update

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

%>

<div id="user_info">
<h2 align="center">Thank you for registering, please check your email and then log in</h2>

</div>

<br />
<br />
<br />
<div id="content_text_of_page">
</div>
<div id="menu">
</div>

<!--#include file="incas/footer.asp"-->