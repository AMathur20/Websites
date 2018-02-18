#!/usr/bin/perl
use strict;

#when the user submits changes to the inventory, I call the file update.cgi to
#handle the updating of the data file

#we are sending html
print "Content-type: text/html\n\n";

#This is the start of the html page
print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Store Home</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT

// Set the default style to 1
var style_change = 1;


//Test if a cookie exists, if it does, get the value of the  cookies using the getCookie function
//Even if one cookie exists for this domain, the if statement is true and will be evaluated.
//  Need to take this into account later on, because if there is no value for the cookie, the
//  getCookie function returns a null value
if (document.cookie != "") {

   style_change=getCookie("Style_sheet");

} /* end if cookie */
//If we have a null value for the style sheet, set it to 1
if(style_change==null){
style_change=1;
}

// write out the link to correct style sheet
document.write("<link href='http://i5.nyu.edu/~am1383/assign6/style"+style_change+".css' rel='stylesheet' type='text/css'>");


function getCookie(name) {
// this function reads the info saved in a cookie, based on the name passed to it
  var dc = document.cookie;
  var prefix = name + "=";
  var begin = dc.indexOf("; " + prefix);
  if (begin == -1) {
    begin = dc.indexOf(prefix);
    if (begin != 0) return null;
  } else
    begin += 2;
  var end = document.cookie.indexOf(";", begin);
  if (end == -1)
    end = dc.length;
  return unescape(dc.substring(begin + prefix.length, end));
} // end function


// END HIDING -->
</script>
</head>
<body>
<div id="content">
<div id="text">
<h1>Store Inventory</h1>
<br>
<form action="update.cgi" method="post">
<table width="100%"  border="1" cellspacing="0" cellpadding="0">
  <tr>
    <th scope="col">Product</th>
    <th scope="col">Quantity on Stock </th>
    <th scope="col">Qantity Sold</th>
  </tr>
  
  
HTML code



#This is were I write out the number on hand, and the number sold
# I decided to use two different data files to get this done, instead of one

#So, first I read the file that has the number of items sold in total
open (Sold, "<sold.txt");
my @NumSold = <Sold>;
close (Sold);

#Next, I read the file that has the number of items in stock
open (Stock, "<stock.txt");
my @CurrentStock = <Stock>;
close (Stock);

#set up two counter vars
my $n=1;
my $z=0;

#For each item, print out the that info into the table
foreach (@CurrentStock) {
    print"<tr>\n";
    print"<td>Stargate Season $n</td>\n";
    print "<td><input type=\"text\" name=\"sg$n\" size=\"5\" value=\"$_\"></td>";
    print "<td>$NumSold[$z]</td>";
    print"</tr>\n";
    $n++;
    $z++;
    }

#and then print out the rest of the html to finish the page.
print"</table>\n";
print"<input type=\"submit\" value=\"submit\">\n";
print"</form>\n";
print"<p>&nbsp;</p>\n";
print"<p>&nbsp;</p>\n";
print"</div>\n";
print"</div>\n";

print"</body>\n";
print"</html>\n";








