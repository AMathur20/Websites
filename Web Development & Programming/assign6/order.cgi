#!/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';

my $never_quant = param('never');
my $goldfinger_quant = param('goldfinger');
my $goldeneye_quant = param('goldeneye');
my $twine_quant = param('twine');
my $drno_quant = param('drno');
my $anotherday_quant = param('anotherday');





open(PRODUCTS, "<product.txt");
my @product_lines = <PRODUCTS>;
close (PRODUCTS);


my @never_info = split(/:/, @product_lines[0]);
my @goldfinger_info = split(/:/, @product_lines[1]);
my @goldeneye_info = split(/:/, @product_lines[2]);
my @twine_info = split(/:/, @product_lines[3]);
my @drno_info = split(/:/, @product_lines[4]);
my @anotherday_info = split(/:/, @product_lines[5]);

my $never_total = $never_quant * @never_info[2];
my $goldfinger_total = $goldfinger_quant * @goldfinger_info[2];
my $goldeneye_total = $goldeneye_quant * @goldeneye_info[2];
my $twine_total = $twine_quant * @twine_info[2];
my $drno_total = $drno_quant * @drno_info[2];
my $anotherday_total = $anotherday_quant * @anotherday_info[2];

my $total_price = $never_total+$goldfinger_total+$goldeneye_total+$twine_total+$drno_total+$anotherday_total;



print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Thank you</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="http://i5.nyu.edu/~am1383/style.css" type="text/css" rel="Stylesheet" media="screen, projection">
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT

function verify() {

if (document.forms[1].username.value=="")
{
	return false;
}

if (document.forms[1].pass.value=="")
{
	return false;
}

if (document.forms[1].first_name.value=="")
{
	return false;
}

if (document.forms[1].last_name.value=="")
{
	return false;
}

if (document.forms[1].address.value=="")
{
	return false;
}

if (document.forms[1].city.value=="")
{
	return false;
}

if (document.forms[1].state.value=="")
{
	return false;
}

if (document.forms[1].zip.value=="")
{
	return false;
}

if (document.forms[1].phone.value=="")
{
	return false;
}

if (document.forms[1].ccn.value=="")
{
	return false;
}

if (document.forms[1].cced.value=="")
{
	return false;
}

if (document.forms[1].cct.value=="0")
{
	return false;
}



return true;
	
	
}


// END HIDING -->	
</script>


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
		<hr />
		<h3 class="center">You have ordered the following items:</h3>
		
		
		<br />
		<ol>

<form onSubmit="return verify(this)" action="verfy.cgi" method="post">
		
HTML code


		
if($never_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>Never Say Never Again - $never_quant ordered, total price of $never_total.</li>\n";	
	print "<input type=\"hidden\" name=\"quant1\" value=\"$never_quant\" /><input type=\"hidden\" name=\"product1\" value=\"never\" />";
}

if($goldfinger_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>Goldfinger - $goldfinger_quant ordered, total price of $goldfinger_total.</li>\n";		
	print "<input type=\"hidden\" name=\"quant2\" value=\"$goldfinger_quant\" /><input type=\"hidden\" name=\"product2\" value=\"goldfinger\" />";
}

if($goldeneye_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>Goldeneye - $goldeneye_quant ordered, total price of $goldeneye_total.</li>\n";
	print "<input type=\"hidden\" name=\"quant3\" value=\"$goldeneye_quant\" /><input type=\"hidden\" name=\"product3\" value=\"goldeneye\" />";
}

if($twine_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>The World is Not Enough - $twine_quant ordered, total price of $twine_total.</li>\n";		
	print "<input type=\"hidden\" name=\"quant4\" value=\"$twine_quant\" /><input type=\"hidden\" name=\"product4\" value=\"twine\" />";
}

if($drno_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>Dr. No - $drno_quant ordered, total price of $drno_total.</li>\n";
	print "<input type=\"hidden\" name=\"quant5\" value=\"$drno_quant\" /><input type=\"hidden\" name=\"product5\" value=\"drno\" />";
}

if($anotherday_quant==0) {
	print "&nbsp;\n";
}
else {
	print "<li>Die Another Day - $anotherday_quant ordered, total price of $anotherday_total.</li>\n";		
	print "<input type=\"hidden\" name=\"quant6\" value=\"$anotherday_quant\" /><input type=\"hidden\" name=\"product6\" value=\"anotherday\" />";
}

print "</ol>\n";
print "Total Cost: $total_price\n";
		
print <<"HTML code1";		


<br /><br /><br /><br />

<table width="300">
<tr>
	<td>Username:</td>
	<td><input type="text" name="username" /></td>
</tr>

<tr>
	<td>Password:</td>
	<td><input type="password" name="pass" /></td>
</tr>

<tr>
	<td>First Name:</td>
	<td><input type="text" name="first_name" /></td>
</tr>

<tr>
	<td>Last Name:</td>
	<td><input type="text" name="last_name" /></td>
</tr>	

<tr>
	<td>Street Address:</td>
	<td><input type="text" name="address" /></td>
</tr>

<tr>
	<td>City:</td>
	<td><input type="text" name="city" /></td>
</tr>

<tr>
	<td>State:</td>
	<td><input type="text" name="state" /></td>
</tr>

<tr>
	<td>Zip code:</td>
	<td><input type="text" name="zip" /></td>
</tr>

<tr>
	<td>Phone Number:</td>
	<td><input type="text" name="phone" /></td>
</tr>

<tr>
	<td>Credit Card Type:</td>
	<td>
		<select name="cct">
			<option value="0">&nbsp;</option>
    		<option value="1">Mastercard</option>
    		<option value="2">Visa</option>
    		<option value="3">American Express</option>
    	</select>
    </td>
</tr>

<tr>
	<td>Credit Card Number:</td>
	<td><input type="text" name="ccn" /></td>
</tr>

<tr>
	<td>Credit Card Expiration Date:</td>
	<td><input type="text" name="cced" /></td>
</tr>

<tr>
<td colspan="2"><input type="submit" value="Send" /></td>
</tr>

</table>
</form>
		
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
