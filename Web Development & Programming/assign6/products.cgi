#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';

open(PRODUCTS, "<product.txt");
my @product_lines = <PRODUCTS>;
close (PRODUCTS);

my $counter = 0;






print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Products</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
</head>
<body>
<p>&nbsp;</p>
	<div id="container">
	<br />
	<h2 align="center">Products</h2>
	<br />
		<br />
		<form action="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/search.cgi" method="get"><p>
			<a href="http://i5.nyu.edu/~am1383/assign6/register.html">Register</a> | <a href="http://i5.nyu.edu/cgi-bin/cgiwrap/am1383/products.cgi">See all Products</a> | <a href="http://i5.nyu.edu/~am1383/assign6/view.html">See Last Order</a> | <a href="http://i5.nyu.edu/~am1383/assign6/order.html">Shopping Cart</a> | Search <input type="text" name="search"><input type="submit" value="Search">
		</p></form>
	<hr />
	<table width="100%" border="1">
	<tr>
	<th>Name</th>
	<th>Price</th>
	<th>&nbsp;</th>
	</tr>
	


HTML code

@product_lines = sort @product_lines;
	
while ($product_lines[$counter]) {
	my @temp = split(/:/, @product_lines[$counter]);
	print "<tr><td>$temp[0]</td>\n";
	print "<td>\$$temp[2]</td>\n";
	print "<td><img src=\"http://i5.nyu.edu/~am1383/assign6/$temp[1]\"  width=\"100\" alt=\"$temp[0]\"></td>\n";
	print "</tr>\n";
	$counter++;
}

print <<"HTML code1";
		
		</table>
		<br />

		
		
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
