<!-- This is the login page for the user. gives the user a simple form to fill in. -->
<!--#include file="incas/regheader.asp"-->


<div id="user_info">
<h2 class="center">Log In</h2>
</div>

<br />
<br />
<br />
<div id="content_text_of_page">


<!-- Begin form code -->
 <form method="post" action="login_process.asp">
     <p>User Name: <input type="text" name="name" maxlength="20" />
     <br />
     Password: <input type="password" name="password" maxlength="10" />
     <br /><input type="submit" name="Submit" value="Submit" /></p>
 </form>
<!-- End form code -->
</div>
<div id="menu">
<a href="register.asp">Register</a>
</div>

<!--#include file="incas/footer.asp"-->