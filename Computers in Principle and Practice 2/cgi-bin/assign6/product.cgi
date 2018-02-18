#!/usr/bin/perl
use strict;
#there are a bunch of changes to this page, outlined in more detail below

#we are serving html
print "Content-type: text/html\n\n";

#start printing out html code
print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Product Choice</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT

// Set up the expire date for cookies that will be set on this page
expiredate= new Date;
expiredate.setMonth(expiredate.getMonth() + 6);

// Set the default style to 1
var style_change = 1;
// set some more defaults
total_price=0;
var SG1_s1 = 0;
var SG1_s2 = 0;
var SG1_s3 = 0;
var SG1_s4 = 0;
var SG1_s5 = 0;
var SG1_s6 = 0;
var SG1_s7 = 0;
var SG1_s8 = 0;

//Test if a cookie exists, if it does, get the value of the  cookies using the getCookie function
//Even if one cookie exists for this domain, the if statement is true and will be evaluated. 
//  Need to take this into account later on, because if there is no value for the cookie, the
//  getCookie function returns a null value
if (document.cookie != "") {
//alert("Cookie exists");
   SG1_s1=getCookie("SG1_Season_1");
   SG1_s2=getCookie("SG1_Season_2");
   SG1_s3=getCookie("SG1_Season_3");
   SG1_s4=getCookie("SG1_Season_4");
   SG1_s5=getCookie("SG1_Season_5");
   SG1_s6=getCookie("SG1_Season_6");
   SG1_s7=getCookie("SG1_Season_7");
   SG1_s8=getCookie("SG1_Season_8");
   total_price=getCookie("Total_Order_Price");
   style_change=getCookie("Style_sheet");
} /* end if cookie */

// the following tests all of the cookie values we just got, if we have a null value, we set it to 0
if(SG1_s1==null){
SG1_s1=0;
}
if(SG1_s2==null){
SG1_s2=0;
}
if(SG1_s3==null){
SG1_s3=0;
}
if(SG1_s4==null){
SG1_s4=0;
}
if(SG1_s5==null){
SG1_s5=0;
}
if(SG1_s6==null){
SG1_s6=0;
}
if(SG1_s7==null){
SG1_s7=0;
}
if(SG1_s8==null){
SG1_s8=0;
}
//If we have a null value for the style sheet, set it to 1
if(style_change==null){
style_change=1;
}
// write out the link to correct style sheet
document.write("<link href='http://i5.nyu.edu/~am1383/assign6/style"+style_change+".css' rel='stylesheet' type='text/css'>");


function calculateTotalPrice() {
//this function figures out the total price of what we have ordered

// based on what we have ordered, calculate the cost for it
var SG1_s1_order_price = SG1_s1 * 25.99;
var SG1_s2_order_price = SG1_s2 * 25.99;
var SG1_s3_order_price = SG1_s3 * 29.99;
var SG1_s4_order_price = SG1_s4 * 29.99;
var SG1_s5_order_price = SG1_s5 * 39.99;
var SG1_s6_order_price = SG1_s6 * 39.99;
var SG1_s7_order_price = SG1_s7 * 49.99;
var SG1_s8_order_price = SG1_s8 * 49.99;
// set the total price to 0. I can set the total to 0 every time because we recalculate the total price
//   each time any value is changed
var total_price = 0;

// calculate the total price. I broke it up, just to make it easier to see for myself
total_price = SG1_s1_order_price+SG1_s2_order_price+SG1_s3_order_price;
total_price = total_price + SG1_s4_order_price+SG1_s5_order_price+SG1_s6_order_price;
total_price = total_price + SG1_s7_order_price+SG1_s8_order_price;
var total_order = "Total_Order_Price";

// set the cookie with the total price
setCookie(total_order, total_price);

// and update the form on the page
document.forms[0].tot_price.value=total_price;
}// end function calculateTotalPrice

function setCookie(name, value, expires, path, domain, secure) {
// this function set a cookie based on the info passed to it
  var curCookie = name + "=" + escape(value) + "; expires=" +expiredate.toGMTString() +
      ((path) ? "; path=" + path : "") +
      ((domain) ? "; domain=" + domain : "") +
      ((secure) ? "; secure" : "");
  document.cookie = curCookie;
} // end function

function getCookie(name) {
// this function gets the info stored in the cookie based on the name passed to it
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
<h1>Ankur's Store</h1>
<p align="center">Please enter the number of each DVD set you would like, then press &quot;Check Out&quot; on this page, or &quot;Confirm Order&quot; on the left</p>


<form name="myform" action="">
<!-- So with this part, I know it is not neat, but it gets the job done. 
I didn't want to have a whole lot of document.writes, so I enter javascript, and end it very often
-->

<table width="100%"  border="0" cellspacing="2" cellpadding="5">
  
HTML code


#Open and read the stock file to see what we have in stock
open (Stock, "<stock.txt");
my @CurrentStock = <Stock>;
close (Stock);

#declare vars
my $n=1;
my $price;

#start of the loop that will print out the product info
foreach (@CurrentStock) {

    #since each product has a different price, I created the price var to keep
    #track of it, the n var is a simple counter for the loop
    if($n==1) { $price = "25.99";}
    if($n==2) { $price = "25.99";}
    if($n==3) { $price = "29.99";}
    if($n==4) { $price = "29.99";}
    if($n==5) { $price = "39.99";}
    if($n==6) { $price = "39.99";}
    if($n==7) { $price = "49.99";}
    if($n==8) { $price = "49.99";}

    #start print the table row
    print"<tr>\n";
    if ($_ ==0) {
        #if there is nothing in stock, I print the info of the product, but I
	#don't let them order any of them, there is no text field to enter a number
	#and I have an out of stock image
        print "<td><p>Stargate SG-1 Season $n: \$$price</p>\n";
        print "<p>Quantity\n";
	print "</p></td>\n";
	print "<td width=\"150\"><img src=\"http://i5.nyu.edu/~am1383/assign6/images/out_of_stock.gif\" width=\"150\" height=\"170\" alt=\"Out of Stock\"></td>\n";
     } else {
	#but on the other hand, if the product is in stock, then I print out the
	#same thing that I had in assign 4, but using the N counter and Price
	#variables to supply the info that is changing as we go through the loop
        print "<td><p>Stargate SG-1 Season $n: \$$price</p>\n";
	print "<p>Quantity\n";
	print "<script language=\"JavaScript\" type=\"text/javascript\">\n";
	print "<!-- HIDE IT\n";
	print "var SG1_season$n =\"SG1_Season_$n\";\n";
	print "document.write(\"<input type='text' name='SG1_$n' size='5' onBlur='SG1_s$n=this.value; setCookie(SG1_season$n, SG1_s$n); calculateTotalPrice()' \"\);\n";
	print "if (SG1_s$n!=\"\") {\n";
	print "document.write(\" value='\"+SG1_s$n+\"'\");\n";
	print "}\n";
	print "else{\n";
	print "document.write(\" value='0'\");\n";
	print "}\n";
	print "document.write("> ");\n";
	print "// END HIDING -->\n";
	print "</script>\n";
	print "</p></td>\n";
	print "<td width=\"150\"><img src=\"http://i5.nyu.edu/~am1383/assign6/images/sg1_season$n.jpg\" width=\"150\" height=\"170\" alt=\"Season $n\"></td>\n";
     }
    #increment the counter
    $n++;
    #end the table row
    print"</tr>\n";

    #and loop back
    }



#and now print out the rest of the html code to finish the page
print "</table>\n";
print "<h2 align=\"center\">Total Price\n";
print "<script language=\"JavaScript\" type=\"text/javascript\">\n";
print "<!-- HIDE IT\n";

print "document.write(\"<input type='text' name='tot_price' size='5' value='\$\"+total_price+\"' >\");\n";
print "// END HIDING -->\n";
print "</script>\n";

print "</h2>\n";



print "</form>\n";
print "<!-- Button for the user to continue on to the next part\n";
print "-->\n";
print "<div id=\"center\">\n";
print "<input type=\"submit\" name=\"Submit\" value=\"Check Out\" onClick=\"document.location.href='confirm.cgi'\">\n";
print "</div>\n";

print "<p>&nbsp;</p>\n";

print "</div>\n";
print "</div>\n";
print "</body>\n";
print "</html>\n";

