<!--#include file="../incas/db_connect.asp"-->
<!--#include file="../incas/MD5.asp"-->


password_work = Ankman
final_password = MD5(password_work)
user = Anks329
user_id = 1

check1 = "" & user & "" & password & time
check_MD5 = MD5(check1)
'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")


'Initialise the strSQL variable with an SQL statement to query the database
strSQL = "SELECT Verify, Check FROM User WHERE User_ID=" & user_id & " ; "

'Set the cursor type we are using so we can navigate through the recordset
rsUserInfo.CursorType = 2

'Set the lock type so that the record is locked by ADO when it is updated
rsUserInfo.LockType = 3

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Update the record in the recordset
rsUserInfo.Fields("Verify") = "False"
rsUserInfo.Fields("Check") = check_md5

'Write the updated recordset to the database
rsUserInfo.Update

'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing

