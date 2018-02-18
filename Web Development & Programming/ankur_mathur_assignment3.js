/*	Ankur Mathur
	Assignment 3
	Web Development & Programming
	Professor Sana' Odeh
		
	Language: JavaScript
	Platform Used: PC, Windows XP Pro */

//Create the table
document.write("<table border='1' align='center' cellpadding='15'>\n");
	
//The first row should span all the columns under it, and will be a header row that has the name of the Month, and the year
// 	for the current calendar
document.write("<tr ><th colspan='7' ><h3>Calendar for " + monName[useMonth] + ", " + m.getFullYear() + "</h3></th></tr>\n");
document.write("<tr>\n");

// Used a loop to write the next row, which is the days of the week.
for(i=0;i<7;i++) {
	document.write("<td width='100' align='center'>" + dayName[i] + "</td>\n");
}
document.write("</tr>\n<tr>");	


//The heart and guts of the calander writer. I used a for loop to create 6 rows (just in case the calendar needed it). Then I 
//	go through and print out the type of table data needed and calendar is built.

for(j=0;j<42;j++){
	var displayNum = (j-firstDay+1); 
		// displayNum is the number that will be shown in the calendar
		// j minus the firstDay is used to figure out how many blank spaces we need before the first of the month
		// we add 1 to it because the getDay() function starts at 0 and not 1
	
	if(j<firstDay){  // This is the case when the first of the month is not on Sunday
		//write the leading empty cells
		document.write("<td height='75' align='right' valign='top' class='num'>&nbsp;</td>\n");
	}else if(displayNum==now.getDate()&&now.getMonth()==m.getMonth()&&now.getFullYear()==m.getFullYear()){ // Is it today?
		//write out the today cell, different formating than the rest
		document.write("<td height='75' align='right' valign='top' class='today'><b>" + displayNum + "</b></td>\n");
	}else if(displayNum > monleng){ // at the end of the month we have nothing, just blank space. 
		//Empty cells at bottom of calendar
		document.write("");
	}else{ //otherwise it is just another day of the month
		//the rest of the numbered cells
		document.write("<td height='75' align='right' valign='top' class='dates'>" + displayNum + "</td>\n");
	}
	if(j%7==6){ //make the table only have 7 columns
		document.write("</tr>\n<tr>\n");
	}
}

document.write("</tr></table>\n"); // YAY! all done with the calendar!








// Now we get to write out the holidays for the slected month

//This switch section figures out what month we have, and creates a variable with a list of the holidays for that month
switch(m.getMonth()){
	case 0:
		holidays = "<li>January 1st - New Year's Day </li>\n";
		holidays += "<li>January 7th - Christmas (Orthodox)</li>\n";
		holidays += "<li>January 16th - Religious Freedom Day</li>\n";
		break;
	case 1:
		holidays = "<li>February 2nd - Groundhog Day</li>\n";
		holidays += "<li>February 14th - Valentine's Day</li>\n";
		break;
case 2:
		holidays = "<li>March 17th - St. Patrick's Day</li>\n";
		holidays += "<li>March 22nd - World Water Day</li>\n";
		holidays += "<li>March 25th - Greek Independence Day</li>\n";
		break;
case 3:
		holidays = "<li>April 1st - April Fool's Day</li>\n";
		holidays += "<li>April 22nd - Earth Day</li>\n";
		holidays += "<li>April 24th - Armenian Remembrance Day</li>\n";
		break;
case 4:
		holidays = "<li>May 1st - Loyalty Day</li>\n";
		holidays += "<li>May 1st - Law Day, USA</li>\n";
		holidays += "<li>May 5th - Cinco de Mayo</li>\n";
		holidays += "<li>May 22nd - National Maritime Day</li>\n";
		break;
case 5:
		holidays = "<li>June 8th - World Ocean Day</li>\n";
		holidays += "<li>June 14th - Flag Day</li>\n";
		holidays += "<li>June 19th - Juneteenth</li>\n";
		break;
case 6:
		holidays = "<li>July 4th - Independence Day</li>\n";
		break;
case 7:
		holidays = "<li>August 16th - National Airborne Day</li>\n";
		holidays += "<li>August 26th - Women's Equality Day</li>\n";
		break;
case 8:
		holidays = "";
		break;
case 9:
		holidays = "<li>October 6th - German-American Day</li>\n";
		holidays += "<li>October 9th - Leif Erikson Day</li>\n";
		holidays += "<li>October 11th - General Pulaski Memorial Day</li>\n";
		holidays += "<li>October 15th - White Cane Saftey Day</li>\n";
		holidays += "<li>October 24th - United Nations Day</li>\n";
		holidays += "<li>October 31st - Halloween</li>\n";
		break;
case 10:
		holidays = "<li>November 9th - World Freedom Day</li>\n";
		holidays += "<li>November 11th - Veterans Day</li>\n";
		holidays += "<li>November 15th - American Recycles Day</li>\n";
		break;
case 11:
		holidays = "<li>December 1st - World AIDS Day</li>\n";
		holidays += "<li>December 7th - National Pearl Harbor Remembrance Day</li>\n";
		holidays += "<li>December 10th - Human Rights Day</li>\n";
		holidays += "<li>December 15th - Bill of Rights Day</li>\n";
		holidays += "<li>December 17th - Wright Brothers Day</li>\n";
		holidays += "<li>December 25th - Christmas</li>\n";
		break;
default:
	break;
}

document.write("<div class='holiday'><br>");
document.write("<blockquote><ol>\n" + holidays + "</ol>\n\n");
document.write("<p>All Holiday dates are from the Wikipedia, <a href='http://en.wikipedia.org/wiki/Holidays_of_the_United_States'>Holidays of the United States</a> and <a href='http://en.wikipedia.org/wiki/List_of_observances_in_the_United_States_by_presidential_proclamation'>List of observances in the United States by Presidential Proclamation</a>.</p></blockquote>\n<br><br>");
document.write("</div>");






	