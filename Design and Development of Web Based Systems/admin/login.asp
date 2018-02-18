<!--#include file="../incas/header.asp"--> <!-- contains the header information -->

<h1 align="center">Admin Panel - Login</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<!-- Begin form code -->
 <form name="form" method="post" action="login_process.asp">
     User Name: <input type="text" name="name" maxlength="20">
     <br>
     Password: <input type="password" name="password" maxlength="10">
     <input type="submit" name="Submit" value="Submit">
 </form>
<!-- End form code -->
</div>
<div id="menu">
<a href="add_new_song.asp">Add a new song</a><br />
<a href="all_songs.asp">List all songs</a><br />
<a href="all_users.asp">List all users<a><br />
<a href="logout.asp">Logout</a><br />

</div>

<!--#include file="../incas/footer.asp"-->

