#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';

my $user_check = param('user_name');
my $pass_check = param('user_pass');

use Digest::MD5 qw(md5_hex);

#the md5 makes it so the password is not stored as clear text in the data file
$pass_check = md5_hex($pass_check);


open (DATA, "<users.txt");

my @data = <DATA>;

close (DATA);

my $counter = 0;

foreach (@data) {
	my @temp = split(/, /, @data[$counter]);
	if ($temp[0] eq $user_check) {
		
		if ($temp[1] eq $pass_check) {
			
		print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Last Order</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
</head>
<body>
<p>&nbsp;</p>
	<div id="container">
		<h1 class="center">
			Last Order
		</h1>
		<br />
		<form action="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/search.cgi" method="get"><p>
			<a href="http://i5.nyu.edu/~am1383/assign6/register.html">Register</a> | <a href="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/products.cgi">See all Products</a> | <a href="http://i5.nyu.edu/~am1383/assign6/view.html">See Last Order</a> | <a href="http://i5.nyu.edu/~am1383/assign6/order.html">Shopping Cart</a> | Search <input type="text" name="search"><input type="submit" value="Search">
		</p></form>
		
HTML code

print "<p>Welcome back, $temp[2]!</p>";		
print "<table width=\"100%\">\n";
print "<tr>\n";

my $count_product = 12;
my $count_quant = 13;

open(PRODUCTS, "<product.txt");
my @product_lines = <PRODUCTS>;
close (PRODUCTS);

my $product_db_counter = 0;

while ($count_product < 27) {
	
	if ($temp[$count_product] eq " ") {
		$count_product = $count_product +2;
		$count_quant = $count_quant +2;
	} else {
		while ($product_lines[$product_db_counter]) {
			my @temp = split(/:/, @product_lines[$product_db_counter]);
			if ($temp[0] =~ m/$temp[$count_product]/i) {
				print "<tr><td>$temp[0]</td>\n";
				print "<td>\$$temp[2]</td>\n";
				print "<td><img src=\"http://i5.nyu.edu/~am1383/assign6/$temp[1]\"  width=\"100\"  alt=\"$temp[0]\"></td>\n";
				print "</tr>\n";
			}
			$product_db_counter++;
		}
		$count_product = $count_product +2;
		$count_quant = $count_quant +2;
	}
}
print "</tr>\n";
print "</table>";


		
		
		print <<"HTML code1";
		
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


	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		} else {
			print"<meta HTTP-EQUIV=\"REFRESH\" CONTENT=\"0; URL=http://i5.nyu.edu/~am1383/assign6/view.html\">";
		}
	} else {
		print"<meta HTTP-EQUIV=\"REFRESH\" CONTENT=\"0; URL=http://i5.nyu.edu/~am1383/assign6/view.html\">";
		
	}
}

