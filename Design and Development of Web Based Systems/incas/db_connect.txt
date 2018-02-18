<%
REM This has the basic information to connect to the database, which is common
REM     to all the pages. It made it easier for me when I transfered from my local
REM     computer to Jupiter.
'Dimension variables
Dim adoCon         'Holds the Database Connection Object
Dim rsGuestbook   'Holds the recordset for the records in the database
Dim strSQL          'Holds the SQL query to query the database
'Create an ADO connection object
Set adoCon = Server.CreateObject("ADODB.Connection")

'Set an active connection to the Connection object using DSN connection
adoCon.Open "DSN=Ankur"

%>