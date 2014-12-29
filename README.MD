# PyRow - CSV to formatted text!

#### PyRow is a CSV to plain text exportation tool that reformats/exports rows into a list of formatted strings.

#### Why I made this:

I originally wrote this script to format output from a search engine keyword tool that displayed the estimated CPC based on search volume. I was doing it by hand through Google Docs before, but it was time consuming. As a programmer I thought why not make a script to do it for me!

Hopefully someone else will find this useful as well. :)

#### How to use it:
**HOW TO IMPORT**

Importing it works like any other library.

`from PyRow import PyRow`

with that, you instatiate the class as normal

`pyrow = PyRow()`

then you can call it with it's run function to output to the file you've specified in your new script

`pyrow.run()`

**CLI FLAGS - For stand-alone use**

"-o" or "--original-file" is the CSV file you want to use.
"-d" or "--destination-file" is the txt file you would like to output to.

if you would like to change the columns and output you have to edit the script manually!

**WARNINGS**

If you do decide to edit the column names it takes as arguments, be sure to leave a space in front of the column name if there is one in the CSV file! This is an issue I'm aware of and working on.

####TO-DO:
* **Make it more user friendly**:
	* Fix the way choosing columns work
    * Allowing user to specify which columns they want to take.
	* Allowing user to choose what they want to add to the output strings.
	* Build GUI to make it more friendly.

* **Can't forget reusability**:
	* Refactor code to make it easily importable into other projects.

------

Feel free to fork it or clone it to make it better! Pull requests also very welcomed.

\- Alex "Wigglyjoe" Caza
