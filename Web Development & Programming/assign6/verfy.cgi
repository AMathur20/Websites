#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';


my $username = param('username');
my $pass = param('pass');
my $first_name = param('first_name');
my $last_name = param('last_name');
my $address = param('address');
my $city = param('city');
my $state = param('state');
my $zip = param('zip');
my $phone = param('phone');
my $cct = param('cct');
my $ccn = param('ccn');
my $cced = param('cced');

use Digest::MD5 qw(md5_hex);

#the md5 makes it so the password is not stored as clear text in the data file
$pass = md5_hex($pass);

my $output = "$username, $pass, $first_name, $last_name, $address, $city, $state, $zip, $phone, $cct, $ccn, $cced, ";

my $quant1 = param('quant1');
my $quant2 = param('quant2');
my $quant3 = param('quant3');
my $quant4 = param('quant4');
my $quant5 = param('quant5');
my $quant6 = param('quant6');

my $product1 = param('product1');
my $product2 = param('product2');
my $product3 = param('product3');
my $product4 = param('product4');
my $product5 = param('product5');
my $product6 = param('product6');

$output = $output . "$product1, $quant1, $product2, $quant2, $product3, $quant3, $product4, $quant4, $product5, $quant5, $product6, $quant6";





open (OUTFILE, ">>users.txt");


print OUTFILE "$output\n";
close (OUTFILE);



print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Thank you</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
</head>
<body>
<p>&nbsp;</p>
	<div id="container">
		<h1 class="center">
			Thank you
		</h1>
				<br />
		<form action="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/search.cgi" method="get"><p>
			<a href="http://i5.nyu.edu/~am1383/assign6/register.html">Register</a> | <a href="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/products.cgi">See all Products</a> | <a href="http://i5.nyu.edu/~am1383/assign6/view.html">See Last Order</a> | <a href="http://i5.nyu.edu/~am1383/assign6/order.html">Shopping Cart</a> | Search <input type="text" name="search"><input type="submit" value="Search">
		</p></form>

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
