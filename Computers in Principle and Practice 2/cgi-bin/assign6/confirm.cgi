#!/usr/bin/perl
use strict;

use CGI ':standard';

print "Content-type: text/html\n\n";


#Open and read the stock file to see what we have in stock
open (Stock, "<stock.txt");
my @CurrentStock = <Stock>;
close (Stock);

#get info from the cookies!
my $sg1 = cookie('SG1_Season_1');
my $sg2 = cookie('SG1_Season_2');
my $sg3 = cookie('SG1_Season_3');
my $sg4 = cookie('SG1_Season_4');
my $sg5 = cookie('SG1_Season_5');
my $sg6 = cookie('SG1_Season_6');
my $sg7 = cookie('SG1_Season_7');
my $sg8 = cookie('SG1_Season_8');

#test to see if the amt ordered was greater than the number in stock
#if it was throw an error and kick the user back the product choice page
#this is going to use java script, so first start up some of the html code
#so the javascript can be correctly placed in it



print <<"HTML code";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Confirmation Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT


HTML code

#the following are the if statements and the javascript error message
if ($sg1 > $CurrentStock[0]) {
print "alert(\"You have ordered too many copies of Season 1\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg2 > $CurrentStock[1]) {
print "alert(\"You have ordered too many copies of Season 2\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg3 > $CurrentStock[2]) {
print "alert(\"You have ordered too many copies of Season 3\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg4 > $CurrentStock[3]) {
print "alert(\"You have ordered too many copies of Season 4\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg5 > $CurrentStock[4]) {
print "alert(\"You have ordered too many copies of Season 5\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg6 > $CurrentStock[5]) {
print "alert(\"You have ordered too many copies of Season 6\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg7 > $CurrentStock[6]) {
print "alert(\"You have ordered too many copies of Season 7\");";
print "document.location.href=\"product.cgi\";";
}
if ($sg8 > $CurrentStock[7]) {
print "alert(\"You have ordered too many copies of Season 8\");";
print "document.location.href=\"product.cgi\";";
}




#the rest of is the same as assign 4, no further changes
print <<"more HTML code";

// Set up the expire date for cookies that will be set on this page
expiredate= new Date;
expiredate.setMonth(expiredate.getMonth() + 6);

// Set the default style to 1
var style_change = 1;
// set some more defaults, used later on to test to see if the user has filled out previous information
var fname = 0;
var total_price =0;


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
   fname=getCookie("FirstName");
} /* end if cookie */
//If we have a null value for the style sheet, set it to 1
if(style_change==null){
style_change=1;
}
// write out the link to correct style sheet
document.write("<link href='http://i5.nyu.edu/~am1383/assign6/style"+style_change+".css' rel='stylesheet' type='text/css'>");

//If there is no order information, show an alert box, and send the user back to products page
if (total_price==null || total_price==0){
alert("Please place an order first");
document.location.href="product.cgi";
}

// If there is no first name saved, show an alert field and send the user back to the personal info page
if (fname==null || fname==0){
alert("Please fill out your personal information");
document.location.href="personal.cgi";
}

//If nothing of that product has been order set it equal to 0
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


//create two arrarys, one with quantity, one that keeps track of the associated pics pointers
picID = new Array("1","2","3","4","5","6","7","8")
quant = new Array(SG1_s1,SG1_s2,SG1_s3,SG1_s4,SG1_s5,SG1_s6,SG1_s7,SG1_s8)


//sort in decending order, keeping the second arrary linked to the first one
for(var l =0;l<8;l++)
	{
	for(var r=l+1;r<8;r++)
	{
		if(quant[l]<quant[r])
		{
			var temp = quant[r];
			quant[r]=quant[l];
			quant[l]=temp;
			temp1=picID[l];
			picID[l]=picID[r];
			picID[r]=temp1;
		}
	}
}
	

function pageTo(nextP) {
//This function takes you to the next page depeding on which button you click on

if (nextP=="Adjust Order")
	parent.Content.location='product.cgi'
	
if (nextP=="Confirm Order")
	parent.Content.location='order.cgi'

} // End function


function setCookie(name, value, expires, path, domain, secure) {
// This function sets a cookie based on the info passed to it
  var curCookie = name + "=" + escape(value) + "; expires=" +expiredate.toGMTString() +
      ((path) ? "; path=" + path : "") +
      ((domain) ? "; domain=" + domain : "") +
      ((secure) ? "; secure" : "");
  document.cookie = curCookie;
} // End function

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
} // End function




// END HIDING -->	
</script>
</head>

<body>
<div id="content">
<div id="text">
<h1>Confirm Order</h1>
<p>&nbsp;</p>

<script language="JavaScript" type="text/javascript">
<!-- HIDE IT
// using document.write set up the table that will display your order
document.write("<table width='100%'  border='0' cellspacing='4' cellpadding='4'>");
document.write("  <tr>");
document.write("    <th scope='col'>Product</th>");
document.write("    <th scope='col'>Description</th>");
document.write("    <th scope='col'>Quantity Ordered</th>");
document.write("  </tr>");

// start a loop that will go through the arrary we sorted earlier and print out the assoicated info
for(var i=0;i<8;i++)
{
	temp=picID[i]; // this has the pointer to the correct images, basically in my set up it is also the season number
	if(quant[i] !=0){
	// if the quantity is not zero we will see how much we ordered of it
	document.write("<tr>");
	document.write("<td width='150'>");
	document.write("<img src='images/sg1_season"+temp+".jpg' alt=' "+temp+"'>"); // show the images of the product
	document.write("</td>");
	document.write("<td>");
	document.write("<p>Stargate Season " + temp +"</p>"); // print the description of the season
	document.write("</td>");
	document.write("<td align='center'>");
	document.write("<input type='text' name='SG1_'"+temp+"' size='5' value='"+quant[i]+"'>")
	// and print out the quantity ordered
	document.write("</td>");
	document.write("</tr>");
	}// end of if statement
}// end of the for loop, we have now gone through all 8 products we sell
// so we can print out the total for the order
document.write("<tr>");
document.write("<td colspan='2'>Total:</td>");
document.write("<td align='center'>");
document.write("<input type='text' name='total' size='5' value='"+total_price+"'>");
document.write("</td>");
document.write("</tr>");
// and close the table as well
document.write("</table>");
// END HIDING -->	
</script>

<br>
<br>

<!-- 
Two buttons that allow the user to adjust their order, or confirm it
-->
  <input type="submit" name="adjust" value="Adjust Order" onClick="nextP=this.value; pageTo(nextP)">
  <input type="submit" name="confirm" value="Confirm Order" onClick="nextP=this.value; pageTo(nextP)">

<p>&nbsp;</p>
</div>
</div>
</body>
</html>


more HTML code
