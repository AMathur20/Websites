#!/usr/bin/perl

#The above line is required and should remain unchanged. It is a
#special command that tells the operating system the location of Perl.

######################### Section 1 ##############################
######### Read in the environment variable. This script is only
######### written to use the Get method.
##################################################################

#The following line reads in the QUERY_STRING environment variable

$query_string = $ENV{ 'QUERY_STRING' };

#The following is an example of a query string:
# >> fname=Mike&lname=Notch&address=1+Poppy+Place&submit=submit
# fname, lname, address and submit are the values assigned
# to the NAME attribute of the INPUT tag (see assign5.html).
# Mike, Notch, 1+Poppy+Place and submit are the values that the user
# entered into the web page. Note that the all spaces are substituted
# with + signs. For example, the user entered "1 Poppy Pl", then the
# string received by the cgi script is 1+Poppy+Pl

######################### Section 2 ##############################
######### Parse the input string (stored in the query_string
######### variable).
##################################################################

# Place the input string into an array.

@pairs=split(/&/,$query_string);

#"pairs" is the name of the array. The following values will be placed in
#the array:
# First element: fname=Mike
# Second element: lname=Notch
# Third element: address=1+Poppy+Place
# Forth element: sumbit=submit

#The foreach loop will take that array and make an associative array.
# The result will be the following:
# $FORM{"fname"} = Mike
# $FORM{"lname"} = Notch
# $FORM{"address"} = 1 Poppy Place
# $FORM{"submit"} = submit

foreach $pair (@pairs) {

#Splits the elements in the pair array.
#On the first iteration of the loop: $name="fname" and $value="Mike"
#On the second iteration of the array: $name="lname" and $value="Notch", etc

($name,$value)=split(/=/,$pair);

# Replace any + signs with a space. This is mainly for "1+Poppy+Place".

$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

# Stop people from using subshells to execute commands.
# This is a security measure that prevents the web user from
# executing operating system commands.

$value =~ s/~!/ ~!/g;


#This line actually creates the associative array. On the first
#iteration of the loop $FORM{"fname"} = "Mike". The other values
#will be added on subsequent iterations of the loop.

$FORM{$name} = $value;

}

######################### Section 3 ##############################
######### Print the output and save information to a
######### file.
##################################################################

#MODIFICATION 3
#The address information that the user has provided will be written
#to a file. Currently, I have used the name cpp_assignment.txt to be
#the name of this file. You need to use a different name for the file.
#Where you see cpp_assignment.txt, change it to a different name.
#Hint: You only need to modify two lines - where you see cpp_assignment.txt

#MODIFICATION 3 Note
#When you modify the "open" command (found below), make sure you
#keep the ">>". This is a special symbol that means you want to
#append to an exist file, not overwrite. So the new line
#would look like - open(OUTFILE,">>newfile.txt");

#Opens the output file for appending. The data that the user entered
#will be placed in this file.

open(OUTFILE,">>am1383_assignment_5.txt");

#The following command sets the permission for the datafile.

chmod(0644, "am1383_assignment_5.txt");


#The following lines print out the information placed in the
#associative array. The "\t" means that a tab should be placed after
#the value. Make a special note of the "\n" on the last line.
#This means end-of-line. Make sure you put it after the last
#print statement.

#MODIFICATION 4
#During MODIFICATION 2 you modified the NAME attribute of the INPUT tag. In my
#example, I used fname, lname etc. You must change the values below
#to reflect the changes you made. So, if your INPUT tag
#looks like <INPUT TYPE="text" NAME="klingon_fname">, then you
#need to rewrite one of the following lines to use the
#value "klingon_fname", etc.


print OUTFILE $FORM{FirstName} . "\t";
print OUTFILE $FORM{LastName} . "\t";
print OUTFILE $FORM{StAddress} . "\t";
print OUTFILE $FORM{City} . "\t";
print OUTFILE $FORM{State} . "\t";
print OUTFILE $FORM{Zip} . "\t";
print OUTFILE $FORM{EmailAddress} . "\n";

#This line closes the output file
close(OUTFILE);

######################### Section 4 ##############################
######### Print the output and save information to a
######### file.
##################################################################

#The first print line is necessary. It denotes that the output is html text.
#Without this line, the web browser would not realize that the statements
#should be interpreted as html.

print("Content-Type: text/html\n\n\n");

# MODIFICATION 5
#We need to customize the output given to the user. You will need to
#modify three lines that are provided below.
# 1) Rewrite the line that prints "Thank you ...". Change this line
# so that it uses one of names you used for your INPUT fields.
# 2) Rewrite the first line that has the HREF tag. The HREF tag should
# reference the output file that you used above, not cpp_assignment.txt.
# 3) Rewrite the next line that has the HREF tag. This line should provide a
# link to your assign5.html.
#
#Hint: Be very careful how you modify the print statements. Try to stick to my format.

# Print out the header info, this is to make the website look like all of my other pages

print("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"\n");
print("\"http://www.w3.org/TR/html4/loose.dtd\">\n");
print("<html>\n");
print("<head>\n");
print("<title>Assignment 5</title>\n");
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\">\n");
print("<link href=\"http://i5.nyu.edu/~am1383/style.css\" rel=\"stylesheet\" type=\"text/css\">\n");
print("</head>\n");
print("<body>\n");
print("<div id=\"content\">\n");
print("<div id=\"text\">\n");
print("<h1>Assignment 5</h1>\n");
print("<br>\n");


#This line prints out a thank you message. It uses the INPUT tag that
#was assigned fname for the NAME attribute. You must change fname into
#a NAME that you are using for your INPUT tags.

print("<h1>Thank You, " . $FORM{FirstName} . " " . $FORM{LastName} . "!</h1>\n");

#This line references the file where the CGI script writes the output.
#Make sure that cpp_assignment.txt is changed to the file name that
#you have decided to use. Also, make sure that mn208 is changed to your
#user id for i5.

print("<h3><a href=\"http://i5.nyu.edu/~am1383/cgi-bin/am1383_assignment_5.txt\">Look at the address book (you will need to reload!).</a></h3>\n");

print("<br><br>\n");

#This line should be a link back to your assign5.html, not mine. So
#change the user name.

print("<h3><a href=\"http://i5.nyu.edu/~am1383/assign5.html\">Go Back</a></h3>\n");

# And now print out the ending of the file, again this is to make it look like the rest of my site

print("<br>\n");
print("</div>\n");
print("</div>\n");
print("</body>\n");
print("</html>\n");


exit;

