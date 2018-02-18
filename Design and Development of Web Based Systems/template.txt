<!-- This is my template file. -->


<!--#include file="incas/regheader.asp"--> <!--  The html header information, such as <html><head><title>-->
<!--#include file="incas/db_connect.asp"--> <!-- contains the basic DNS information to connect to the database-->


<div id="user_info">


<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur dapibus nulla ac leo. Aliquam ac pede vel diam gravida adipiscing. Nulla nibh. Sed vitae quam in libero tincidunt tempor. Quisque ultrices massa vel purus. In hac habitasse platea dictumst. Fusce pellentesque vehicula libero. In sagittis wisi at lorem aliquet dignissim. Donec aliquam elit a turpis. Mauris aliquam vestibulum urna.</p>


</div>

<br />
<br />
<br />
<div id="content_text_of_page">



<p>Quisque ornare nunc vel mi. Integer sit amet wisi. Donec ultrices. Etiam suscipit pharetra sapien. Morbi cursus vestibulum augue. Vestibulum accumsan dignissim neque. Phasellus et purus sit amet nisl porttitor semper. Donec turpis ligula, cursus quis, iaculis ac, pretium eu, justo. Donec at lorem vitae ipsum aliquam gravida. Phasellus sed elit nec diam fermentum viverra. Praesent facilisis. Curabitur eleifend. Suspendisse potenti. Nulla et quam sed eros scelerisque congue. Pellentesque hendrerit laoreet purus. Integer non risus ut augue dignissim cursus. Nulla dolor. Suspendisse sodales. Cras leo nunc, consequat a, rutrum sit amet, adipiscing ut, magna. Sed sit amet enim.</p>
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
