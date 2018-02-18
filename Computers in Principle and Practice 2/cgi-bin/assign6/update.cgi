#!/usr/bin/perl
use strict;

print "Content-type: text/html\n\n";

use CGI ':standard';

my $sg1;
my $sg2;
my $sg3;
my $sg4;
my $sg5;
my $sg6;
my $sg7;
my $sg8;

$sg1 = param('sg1');
$sg2 = param('sg2');
$sg3 = param('sg3');
$sg4 = param('sg4');
$sg5 = param('sg5');
$sg6 = param('sg6');
$sg7 = param('sg7');
$sg8 = param('sg8');


open (OUTFILE, ">stock.txt");



print OUTFILE $sg1 . "\n";
print OUTFILE $sg2 . "\n";
print OUTFILE $sg3 . "\n";
print OUTFILE $sg4 . "\n";
print OUTFILE $sg5 . "\n";
print OUTFILE $sg6 . "\n";
print OUTFILE $sg7 . "\n";
print OUTFILE $sg8 . "\n";

close (OUTFILE);



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
<p>Inventory Updated</p>

</div>
</div>
</body>
</html>

HTML code
