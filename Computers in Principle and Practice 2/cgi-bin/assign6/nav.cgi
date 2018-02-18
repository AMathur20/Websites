#!/usr/bin/perl
use strict;

#the only change to this file is the addition of a link to the inventory page

print "Content-type: text/html\n\n";

print <<"HTML code";

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Nav Menu</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT

// Set up the expire date for cookies that will be set on this page
expiredate= new Date;
expiredate.setMonth(expiredate.getMonth() + 6);

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


function changePage(new_pg) {
// this function changes the content frame based on what radio button you click
parent.Content.document.location.href= new_pg+".cgi";
} // end function

function setCookie(name, value, expires, path, domain, secure) {
// this function sets a cookie based on the information passed to it
  var curCookie = name + "=" + escape(value) + "; expires=" +expiredate.toGMTString() +
      ((path) ? "; path=" + path : "") +
      ((domain) ? "; domain=" + domain : "") +
      ((secure) ? "; secure" : "");
  document.cookie = curCookie;
} // end function

function changeStyle(new_Style) {
// this function changes the style sheet based on user prefreneces
Cookie_Name = "Style_sheet";
setCookie(Cookie_Name, new_Style); // first set a cookie so the other pages can change as well

// and then reload both frames
parent.Content.document.location.reload();
parent.Nav.document.location.reload();
} // end function

function clearOrder() {
// the function resets the order if the user clicks on that radio button.
// the order is reset by setting the cookie expire date to the past

// first reset the 8 products that we have. its easy for me because they are all seasons of the same show
for (i=1;i<9;i++) {
if (getCookie("SG1_Season_"+i)) {
    document.cookie = "SG1_Season_"+i+"=; expires=Thu, 01-Jan-70 00:00:01 GMT";
}
}
// and then reset the total price cookie as well
if (getCookie("Total_Order_Price")) {
    document.cookie = "Total_Order_Price=; expires=Thu, 01-Jan-70 00:00:01 GMT";
}
// and now send the user to the products page
parent.Content.document.location.href="product.cgi";
} // end function

function getCookie(name) {
// this fuctions reads the info stored in the cookies based on the info passed to it
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
<h1>Nav Menu</h1>
 <p>&nbsp;</p>
 
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT
// here we have the radio buttons for navigation

  document.write("<input type='radio' name='Nav' value='personal' onClick='main_pg=this.value; changePage(main_pg)'> Personal Info <br/>");
  document.write("<input type='radio' name='Nav' value='product' onClick='main_pg=this.value; changePage(main_pg)'> Product Choice <br/>");
  document.write("<input type='radio' name='Nav' value='confirm' onClick='main_pg=this.value; changePage(main_pg)'> Confirm <br/>");  
  document.write("<input type='radio' name='Nav' value='order' onClick='main_pg=this.value; changePage(main_pg)'> Order <br/>");
  document.write("<br/><br/><br/>");
  document.write("<input type='radio' name='Nav' value='order' onClick='clearOrder()'> Reset Order <br/>");
  document.write("<br/><br/><br/>");
  document.write("<br/><br/><br/>");
  document.write("<input type='radio' name='Nav' value='inventory' onClick='main_pg=this.value; changePage(main_pg)'>Manage Inventory <br/>");

// END HIDING -->
</script>
<br/><br/><br/><br/><br/><br/>
<script language="JavaScript" type="text/javascript">
<!-- HIDE IT
// and now the buttons to change the style sheet
  document.write("<input type='radio' name='Style' value='1' onClick='new_style=this.value; changeStyle(new_style)'> Style 1<br/>");
  document.write("<input type='radio' name='Style' value='2' onClick='new_style=this.value; changeStyle(new_style)'> Style 2 <br/>");
  document.write("<input type='radio' name='Style' value='3' onClick='new_style=this.value; changeStyle(new_style)'> Style 3 <br/>");  
// END HIDING -->
</script> 
</div></div>
</body>
</html>



HTML code

