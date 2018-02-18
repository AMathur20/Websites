#!/usr/bin/perl
use strict;

use CGI ':standard';

#we are sending html
print "Content-type: text/html\n\n";

#declare a bunch of variables here
my ($sg1, $sg2, $sg3, $sg4, $sg5, $sg6, $sg7, $sg8);
my ($fname, $lname, $email, $total_price, $address1);
my ($city, $state1, $zipCode, $phone);


#get info from the cookies!
$sg1 = cookie('SG1_Season_1');
$sg2 = cookie('SG1_Season_2');
$sg3 = cookie('SG1_Season_3');
$sg4 = cookie('SG1_Season_4');
$sg5 = cookie('SG1_Season_5');
$sg6 = cookie('SG1_Season_6');
$sg7 = cookie('SG1_Season_7');
$sg8 = cookie('SG1_Season_8');
$email = cookie('email');
$total_price = cookie('Total_Order_Price');
$fname = cookie('FirstName');
$lname = cookie('lname');
$address1 = cookie('address1');
$city = cookie('city');
$state1 = cookie('state1');
$zipCode = cookie('zipCode');
$phone = cookie('phone');


#read the file that has the number of items sold in total
open (Sold, "<sold.txt");
my @NumSold = <Sold>;
close (Sold);


#read the file that has the number of items in stock
open (Stock, "<stock.txt");
my @CurrentStock = <Stock>;
close (Stock);




#the following if...then statements test to see if something was ordered.
#if it was, that CurrentStock variable gets decreased by 1, and the number
#sold is incremented by 1
if ($sg1 != 0) { $CurrentStock[0]=$CurrentStock[0]-$sg1; $NumSold[0]=$NumSold[0]+$sg1; }
if ($sg2 != 0) { $CurrentStock[1]=$CurrentStock[1]-$sg2; $NumSold[1]=$NumSold[1]+$sg2; }
if ($sg3 != 0) { $CurrentStock[2]=$CurrentStock[2]-$sg3; $NumSold[2]=$NumSold[2]+$sg3; }
if ($sg4 != 0) { $CurrentStock[3]=$CurrentStock[3]-$sg4; $NumSold[3]=$NumSold[3]+$sg4; }
if ($sg5 != 0) { $CurrentStock[4]=$CurrentStock[4]-$sg5; $NumSold[4]=$NumSold[4]+$sg5; }
if ($sg6 != 0) { $CurrentStock[5]=$CurrentStock[5]-$sg6; $NumSold[5]=$NumSold[5]+$sg6; }
if ($sg7 != 0) { $CurrentStock[6]=$CurrentStock[6]-$sg7; $NumSold[6]=$NumSold[6]+$sg7; }
if ($sg8 != 0) { $CurrentStock[7]=$CurrentStock[7]-$sg8; $NumSold[7]=$NumSold[7]+$sg8; }

my $count=0;

foreach (@CurrentStock) {
$CurrentStock[$count] =~ s/\D//gi;
#print $CurrentStock[$count];
$count++;
}

my $count2=0;
foreach (@NumSold) {
$NumSold[$count2] =~ s/\D//gi;
#print $CurrentStock[$count];
$count2++;
}




# write stock file with the new numbers
open (Stock1, ">stock.txt");
print Stock1 $CurrentStock[0] . "\n";
print Stock1 $CurrentStock[1] . "\n";
print Stock1 $CurrentStock[2] . "\n";
print Stock1 $CurrentStock[3] . "\n";
print Stock1 $CurrentStock[4] . "\n";
print Stock1 $CurrentStock[5] . "\n";
print Stock1 $CurrentStock[6] . "\n";
print Stock1 $CurrentStock[7] . "\n";
close (Stock1);

# write number sold file with the new numbers
open (Sold1, ">sold.txt");
print Sold1 $NumSold[0] . "\n";
print Sold1 $NumSold[1] . "\n";
print Sold1 $NumSold[2] . "\n";
print Sold1 $NumSold[3] . "\n";
print Sold1 $NumSold[4] . "\n";
print Sold1 $NumSold[5] . "\n";
print Sold1 $NumSold[6] . "\n";
print Sold1 $NumSold[7] . "\n";
close (Sold1);



#write out the email file, using html in it to format it and make it look pretty
open (OUTFILE, ">email.txt");
print OUTFILE "Content-type: text/html\n\n";
print OUTFILE "Thank you for placing your order. This email serves to confirm your order for the following items: \n";
print OUTFILE "<ul>\n";
print OUTFILE "<li>" . $sg1 . " Copies of Stargate SG-1 Season 1 </li>\n";
print OUTFILE "<li>" . $sg2 . " Copies of Stargate SG-1 Season 2 </li>\n";
print OUTFILE "<li>" . $sg3 . " Copies of Stargate SG-1 Season 3 </li>\n";
print OUTFILE "<li>" . $sg4 . " Copies of Stargate SG-1 Season 4 </li>\n";
print OUTFILE "<li>" . $sg5 . " Copies of Stargate SG-1 Season 5 </li>\n";
print OUTFILE "<li>" . $sg6 . " Copies of Stargate SG-1 Season 6 </li>\n";
print OUTFILE "<li>" . $sg7 . " Copies of Stargate SG-1 Season 7 </li>\n";
print OUTFILE "<li>" . $sg8 . " Copies of Stargate SG-1 Season 8 </li>\n";
print OUTFILE "</ul>";
print OUTFILE "<br>";
print OUTFILE "<p>The total for your order is: \$" . $total_price . "</p>\n";
print OUTFILE "<br>";
print OUTFILE "<p>The order will be shipped to the following address:<br>";
print OUTFILE $fname . " " . $lname . "<br>\n";
print OUTFILE $address1 . "<br>\n";
print OUTFILE $city . " , " . $state1 . " " . $zipCode . "\n";
print OUTFILE "</p>";
print OUTFILE "<h2>Thank you have a great day!</h2>";
print OUTFILE "";
close (OUTFILE);



#generate and send the email to the user's nyu account
my $the_command = "mail " . $email . "\@nyu.edu < email.txt";

system($the_command);





# print out the html code saying that your order was placed, and that you should check your email
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
<h1>Order Placed</h1>
<br>
<p>Your order has been successfully place, and you have recieved a confirmation email with all the details.</p>

</div>
</div>
</body>
</html>

HTML code
