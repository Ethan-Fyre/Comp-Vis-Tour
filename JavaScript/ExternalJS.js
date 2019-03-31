
//Global Variables:
var goodCount=0;
var badCount=0;

function testForNum(strInput) 
{
	if(isPosInt(strInput) == true)
	{
		goodCount++;
		outcome.innerHTML="Good";
	} // end if
	else
	{
		badCount++;
		outcome.innerHTML="Bad";
	} // end else

	alert("Good Inputs = "+goodCount+"   "+"Bad Inputs = "+badCount);
} // end function


// Function to convert base 10 to base 2.
function b10ToBase2(intDividend)
{
	alert("Converting "+intDividend+" to binary");
	var fltQuotient=1.0;
	var intQuotient=1;
	var intRem=0;
	var fltDiff=0.0;
	var strB2=" ";



	if(isPosInt(intDividend) == true)
	{
		while (intDividend != 0)
		{
			fltQuotient=intDividend/2;
			intQuotient=parseInt(fltQuotient);
			fltDiff=fltQuotient-intQuotient;
			if (fltDiff == 0)
			{
				intRem = 0;
			} // end if
			else
			{
				intRem = 1;
			} // end else
			strB2 = intRem + strB2;
			intDividend=intQuotient;
		} // end while

		alert ("B2 value = " + strB2);
	} // end if
	else
	{
		alert ("Error, invalid value \""+intDividend+"\" entered, please enter a positive integer");
	} // end else
} // end function


// Function to determine if input is a positive integer
function isPosInt(isint)
{
	for (var i = 0; i<= isint.length; i++) 
	{
		if (isNaN(isint.charAt(i))) 
		{
		return false;
		} // end if
	} // end for
	return true;
} // end function

// Function to convert base 2 to base 10.
function b2ToBase10(binary)
{
	alert("Converting "+binary+" to base 10");
	var total=0;
	
	if(isPosInt(binary) == true)
	{
		for (var i = 0; i < binary.length; i++)
		{
			total+= binary[binary.length-i-1] * (Math.pow(2,i));
		} // end for		

		alert ("B10 value = " + total);
	} // end if
	else
	{
		alert ("Error, invalid value \""+binary+"\" entered, please enter a positive integer");
	} // end else
} // end function

// Function to determine if input is a positive integer
function isPosInt(isint)
{
	for (var i = 0; i<= isint.length; i++) 
	{
		if (isNaN(isint.charAt(i))) 
		{
		return false;
		} // end if
	} // end for
	return true;
} // end function

// Function to convert base 2 to base 10.
function Exp(base, power)
{
	alert("Computing "+base+"^"+power);
	var result=0;
	
	if((isPosInt(base) == true) && (isPosInt(power) == true))
	{
		result = Math.pow(base,power);	

		alert (base+"^"+power+" = " + result);
	} // end if
	else
	{
		alert ("Error, invalid value(s) \""+base+"\" and \""+power+"\" entered, please enter positive integers");
	} // end else
} // end function

// Function to convert base 2 to base 10.
function testPrime(prime)
{
	alert("Testing "+prime+" for primality");
	var result = true
	if (isPosInt(prime) == true)
	{
		for (var i = 2; i < prime; i++)
		{
			if (prime % i == 0)
			{
				result = false
			}
		} // end for		

		alert ("Result of primality test for "+prime+": " + result);
	} // end if
	else
	{
		alert ("Error, invalid value \""+prime+" entered, please enter positive integers");
	} // end else
} // end function


