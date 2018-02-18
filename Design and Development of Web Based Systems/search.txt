<!-- This page allows the user to search for songs in the database -->
<!-- This was perhaps the hardest page to get working for me, because of the SQL Queries. -->

<!-- There are four ways the user can search for a new song: One - Search by Artist name, -->
<!-- Two - Search by Album name, Three - Search by Tack name, and Four - See a listing -->
<!-- of all songs that begin with a specific letter. --


<!--#include file="incas/check.asp"-->  <!-- Checks a session cookie to see if the visitor is logged in, if not send to login.asp -->
<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->

<%
user_id = Session("user")


REM This part figures out what type of search the user wants to do. The form that
REM      the user fills out, asks the user to specify what they want to search by,
REM      using radio buttons, and passing a number, either 1, 2 or 3. The
REM 	 following If statements change the number back into text that can be
REM      used as a part of the SQL query later.
search_type_form = Request.Form("search_type")

if search_type_form = 1 then
   search_type_string = "Artist"
End if

if search_type_form = 2 then
   search_type_string = "Album"
End if

if search_type_form = 3 then
   search_type_string = "Song_Name"
End if

sr_string = Request.Form("sr_string") REM This is what the user typed into the field
%>
<div id="user_info">

<!-- Here is the actual form that user fills out. -->
<form method="post" action="search.asp">
<p>Search for: <input type="text" name="sr_string" /> <br />
in: </p>
<p>Artist:
    <input type="radio" name="search_type" value="1" />
    |
  Album:
    <input type="radio" name="search_type" value="2" />
    |
  Track:
    <input type="radio" name="search_type" value="3" />
    <br />
       <input type="submit" name="Submit" value="Submit" />
 </p>
</form>


</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<!-- The user can also see all the songs that begin with a specific character -->
<a href="search.asp?limtor=a">A</a>
<a href="search.asp?limtor=b">B</a>
<a href="search.asp?limtor=c">C</a>
<a href="search.asp?limtor=d">D</a>
<a href="search.asp?limtor=e">E</a>
<a href="search.asp?limtor=f">F</a>
<a href="search.asp?limtor=g">G</a>
<a href="search.asp?limtor=h">H</a>
<a href="search.asp?limtor=i">I</a>
<a href="search.asp?limtor=j">J</a>
<a href="search.asp?limtor=k">K</a>
<a href="search.asp?limtor=l">L</a>
<a href="search.asp?limtor=m">M</a>
<a href="search.asp?limtor=n">N</a>
<a href="search.asp?limtor=o">O</a>
<a href="search.asp?limtor=p">P</a>
<a href="search.asp?limtor=q">Q</a>
<a href="search.asp?limtor=r">R</a>
<a href="search.asp?limtor=s">S</a>
<a href="search.asp?limtor=t">T</a>
<a href="search.asp?limtor=u">U</a>
<a href="search.asp?limtor=v">V</a>
<a href="search.asp?limtor=w">W</a>
<a href="search.asp?limtor=x">X</a>
<a href="search.asp?limtor=y">Y</a>
<a href="search.asp?limtor=z">Z</a>
<br />

<br />
<br />

<%
REM If the user chooses the see all songs that start with a specific character,
REM    the variable "char_limitor" holds the character
char_limitor = Request.QueryString("limtor")

 
'Create an ADO recordset object
Set rsUserInfo = Server.CreateObject("ADODB.Recordset")

'Initialise the strSQL variable with an SQL statement to query the database


REM There are three possible SQL Statements that might be needed. First, the user
REM       could want to see all songs that start with a specific character, next
REM       the user could have entered a string to search for, and finally, this
REM       could be the first time the user comes to the search page, and I don't
REM       want to show any songs to the user. So, the following If Statements
REM       figure out which case is true at this point, and creates the correct
REM       SQL statement for that instance.


REM First, I look to see if there is a character limitor, if there is, then I
REM        create an SQL statement that searches for songs where the Song_Name
REM        field is like the character followed by anything else.

if NOT IsEmpty(char_limitor) then
	REM This SQL searches when the user clicks a letter
	strSQL = "SELECT * FROM Songs WHERE Song_Name LIKE '"& char_limitor & "%%'"
End if


REM The next If statement looks to see if the user entered anything into the field.
REM     If the user did, I create an SQL statement that searches for songs, where
REM     (depending on radio button the user selected) the Song_Name, the Artist,
REM     or Album field is like the search string. Anything can be before the
REM     search string, and anything can be after the search string. This allows
REM     the user to enter the middle of a song name, and still have the correct
REM     song show up in the results.
if NOT IsEmpty(search_type_string) then
	REM This SQL searches when the user has typed something in
	strSQL = "SELECT * FROM Songs WHERE "  & search_type_string & " LIKE  '%%"& sr_string & "%%'"
End if


REM Finally, if both the search type and character limitor are both blank, then
REM     this is the first time the user is looking at this page, and the SQL
REM     Query should not have any results.
if IsEmpty(search_type_string) then
   if IsEmpty(char_limitor) then
   REM This SQL is blank, to start the page off
   strSQL = "SELECT Song_ID FROM Songs WHERE Song_ID = 0; "
   End if
End if

'Open the recordset with the SQL query
rsUserInfo.Open strSQL, adoCon

'Loop through the recordset
Do While not rsUserInfo.EOF

     'Write the HTML to display the song information
     song_id = rsUserInfo("Song_ID")
     Response.Write "<br /> Song name: <a href=""song.asp?song_id=" & song_id & """> "
     Response.Write (rsUserInfo("Song_Name"))
     Response.Write ("</a><br>Artist: ")
     Response.Write (rsUserInfo("Artist"))
     Response.Write ("<br /> Album: ")
     Response.Write (rsUserInfo("Album"))
     Response.Write ("<br />")
     'Move to the next song
     rsUserInfo.MoveNext

Loop


'Reset server objects
rsUserInfo.Close
Set rsUserInfo = Nothing
Set adoCon = Nothing
%>

</div>
<div id="menu">
<a href="search.asp">Search for a new song</a><br />
<%

u_file="lists/"&user&"_"&user_id&"_list.smil"


set fso = createobject("scripting.filesystemobject")

' This will check to see if the parent directory has an index.asp page in its directory
' if so it will hyper-link it
if fso.FileExists (server.mappath(u_file)) then
Response.Write "<a href='"& u_file &"'>Listen to your playlist</a><br />"
Response.Write "<a href=""playlist_generator.asp"">Regenerate your playlist</a><br />"
else
Response.Write "<a href=""playlist_generator.asp"">Generate your playlist</a><br />"
end if
%>


<a href="manage_playlist.asp">Manage Playlist</a><br />
<a href="logout.asp">Logout</a>
</div>

<!--#include file="incas/footer.asp"-->
