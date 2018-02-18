/*	Ankur Mathur
	Assignment 1
	Letter Counter
	Web Development & Programming
	Professor Sana' Odeh
	September 27, 2006
	
	
	Language: JavaScript
	Platform Used: PC, Windows XP Pro */


function count_letters() {
	// all of the commented alerts are there for testing
	
	//grab the text, and convert to uppercase, we don't care what case the characters are in, and uppercase is easier to deal with.
	input = document.forms[0].textbx.value; 
	var input = input.toUpperCase();
	
	//Declare two arrary that will use to count the occurances
	//use a for loop to set the entire array equal to 0, otherwise we get error when we try to add 1 to nothing
	var counter_letters = new Array();
	var counter_other = new Array();
	for (i=0,n=25;i<n;i++) {
    	counter_letters[i]=0;
    }
    for (i=0,n=32;i<n;i++) {
	    counter_other[i]=0;
    }
    
    //start going through text entered
    for (j=0,n=input.length;j<n;j++) {
	    
	    //determine the character code of the character we are looking at
	    temp = input.charCodeAt(j); 
	    //alert(temp);
	    
	    //if the character code of text entered is between 65 and 90, it is a normal character
	    //and we will add one to that counter
	    if(temp > 64 && temp < 91) {
		    temp = temp - 65;
		    counter_letters[temp]++;
		    //alert(counter_letters[temp]);
    	}
    	
    	//on the other hand, if the character code is between 32 and 64, it is a "special" character
    	//and we will add one to that counter
    	if (temp > 31 && temp < 65) {
	    	temp = temp - 32;
	    	counter_other[temp]++;
	    	//alert(counter_other[temp]);
    	}
	}

	
	//start creating the output
	output = "Ankur Mathur\n";
	output = output + "Web Development & Programming\n";
	output = output + "Assignment 1\n\n\n";
	output = output + "Count of Normal Characters:\n";
	
	//go through the normal character counter and add the result to the output
	for (i=0,n=25;i<n;i++) {
		let = i + 65; //we need to add 65 to i so that we get the correct letter output from the the fromCharCode function
    	letter = String.fromCharCode(let);
    	count = counter_letters[i];
    	
    	//we only want to see the count if it was counted
    	if (count > 0) {
	    	output = output + letter + " = " + count + "\n";
    	}
    }
	
    output = output + "\nCount of Special Characters:\n";
    
    //go through the special character counter and add the result to the output
	for (i=0,n=32;i<n;i++) {
		spec = i + 32; //we need to add 65 to i so that we get the correct output from the the fromCharCode function
    	special = String.fromCharCode(spec);
    	count = counter_other[i];
    	
    	//we only want to see the count if it was counted
    	if (count > 0) {
	    	output = output + special + " = " + count + "\n";
    	}
    }
    
    vowel_count = 0;
    consonant_count = 0;

    
	//go through the normal character array and figure out number of vowels, and the number of consonants.
	for (i=0,n=25;i<n;i++) {
		
		//use a switch and case statement to add to either the vowel or consonant counter for the character we are looking at
		switch (i) {
			case 0: vowel_count = vowel_count + counter_letters[i]; break;
			case 4: vowel_count = vowel_count + counter_letters[i]; break;
			case 8: vowel_count = vowel_count + counter_letters[i]; break;
			case 14: vowel_count = vowel_count + counter_letters[i]; break;
			case 20: vowel_count = vowel_count + counter_letters[i]; break;
			default: consonant_count = consonant_count + counter_letters[i]; break;
		}
		//alert(vowel_count);
    }    
	
    
    output = output + "\nVowel count is: " + vowel_count + "\n";
    output = output + "Consonant count is: " + consonant_count + "\n\n";
	
    
    
    var counter_letter_holder = new Array();
    for (i=0,n=25;i<n;i++) {
	    counter_letter_holder[i]=i;
    }
    
    //sort in decending order, keeping the second arrary linked to the first one
	for(var l=0;l<25;l++)
		{
			for(var r=l+1;r<25;r++)
			{
				if(counter_letters[l]<counter_letters[r])
				{
					var temp = counter_letters[r];
					counter_letters[r]=counter_letters[l];
					counter_letters[l]=temp;
					temp1=counter_letter_holder[l];
					counter_letter_holder[l]=counter_letter_holder[r];
					counter_letter_holder[r]=temp1;
				}
			}
		}
    //alert(counter_letter_holder[0]);
    
    output = output + "Most common letter(s):\n";
    output = output + String.fromCharCode(counter_letter_holder[0]+65) + "\n";
    
    
    //the following will check the array to see if there are any other characters that showed up just as often
    temp_count = 0;
   	while (counter_letters[temp_count]==counter_letters[temp_count+1])
    {
	    output = output + String.fromCharCode(counter_letter_holder[temp_count+1]+65) + "\n";
	    temp_count++;
    }
    
   
    
    
    //sort in accending order, keeping the second arrary linked to the first one
	for(var l=0;l<25;l++)
		{
			for(var r=l+1;r<25;r++)
			{
				if(counter_letters[l]>counter_letters[r])
				{
					var temp = counter_letters[r];
					counter_letters[r]=counter_letters[l];
					counter_letters[l]=temp;
					temp1=counter_letter_holder[l];
					counter_letter_holder[l]=counter_letter_holder[r];
					counter_letter_holder[r]=temp1;
				}
			}
		}
    output = output + "\nLeast common letter(s):\n";
    
    //alert(counter_letters[0]);
    
    //figure out which letters showed up the least in the input, and then output that character correctly
    
    for (i=0,n=25;i<n;i++) {
	    if (counter_letters[i]>0) {
		    
		    output = output + String.fromCharCode(counter_letter_holder[i]+65) + "\n";
		    
		    while (counter_letters[i]==counter_letters[i+1]) {
			    output = output + String.fromCharCode(counter_letter_holder[i+1]+65) + "\n";
			    i++;
		    }
		    
		    break;
		}
	}
 	
	//write the output into the text box
	document.forms[0].textbx.value=output;


}
