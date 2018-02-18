<!-- This page let the admin add song information into the database. -->

<!--#include file="../incas/admin_check.asp"--> <!-- Makes sure that the admin is logged in -->
<!--#include file="../incas/header.asp"--> <!-- contains the header information -->
<div id="user_info">
<h1 align="center">Admin Panel - Add new Song</h1>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">
<form method="post" action="add_new_song_process.asp">
<p>Song Name: <input type="text" name="name" /><br />
Artist: <input type="text" name="artist"   /><br />
Album: <input type="text" name="album"  /><br />
URL of Clip: <input type="text" name="clip"  /><br />
URL of Full song: <input type="text" name="full"  /><br />
Lyrics: <textarea name="lyrics" rows="10" cols="35"></textarea></p>

<form method="post" action="song_update.asp">

<input type="submit" name="submit" value="Add Song Information">
</form>
</div>
<div id="menu">
<a href="add_new_song.asp">Add a new song</a><br />
<a href="all_songs.asp">List all songs</a><br />
<a href="all_users.asp">List all users<a><br />
<a href="logout.asp">Logout</a><br />

</div>

<!--#include file="../incas/footer.asp"-->
