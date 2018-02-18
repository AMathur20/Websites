#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';




my $file_name = param('file');



open (OUTFILE, $file_name);


#and print out the thank you page
print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>View Code</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
</head>
<body>
<p>&nbsp;</p>
	<div id="container">
		<h1 class="center">
			Code:
		</h1>
		<textarea cols="75" rows="20" >
		
HTML code

my @text = <OUTFILE>;
foreach (@text) {
	print "$_\n";
}

close (OUTFILE);

print <<"HTML code1";

		</textarea>
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


HTML code1
