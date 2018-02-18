#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';

use Digest::MD5 qw(md5_hex);


my $Store_Name = param('user_name');
my $Store_Passwd = param('user_pass');

#the md5 makes it so the password is not stored as clear text in the data file
$Store_Passwd = md5_hex($Store_Passwd);

# open data.txt to append to bottom
open (OUTFILE, ">>data.txt");

#add in the information
print OUTFILE $Store_Name . ", " . $Store_Passwd . "\n";

#close the file
close (OUTFILE);

#and print out the thank you page
print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Register Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
</head>
<body>
<p>&nbsp;</p>
	<div id="container">
		<h1 class="center">
			Thank you for registerring
		</h1>
		<br />
		<h3 class="center"><a href="http://i5.nyu.edu/~am1383/assign5/order.html">Continue Shopping</a></h3>
		
		
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<div id="footer">
			Copyright 2006, <a href="http://www.anksconsulting.com">Ankur Mathur</a><br />
			<a href="http://validator.w3.org/check?uri=referer">Vaild HTML 4.01 Transitional</a>
			and <a href="http://jigsaw.w3.org/css-validator/validator?uri=http://i5.nyu.edu/~am1383/">Valid CSS</a>
		</div>
	</div>
</body>
</html>


HTML code
