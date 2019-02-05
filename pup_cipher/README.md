Decrypt/Encrypt data with the 0A1Q1H1L1Gzu cipher
========================

## Installation:

Installation is simple: if you have Python 2.7\+ installed this will run.

The only imports are for argparse and urllib - both part of Python 2.7.


If you get any dependency errors then install the missing one via pip:

	pip install argparse
	pip install urllib


## Usage

To decrypt a string just pass it as an argument:

	$ python pup_cipher.py 2X1T1CtCzu0H1P1I1I1FtN2X1T1CtBzu0W1F1C1I1Q
	> var1=Hello
	> var2=World

To decrypt without the 'pretty print' options use the \-n flag:

	$ python pup_cipher.py 2X1T1CtCzu0H1P1I1I1FtN2X1T1CtBzu0W1F1C1I1Q -n
	> var1=Hello&var2=World

To encrypt a string use the \-e flag:

	$ python pup_cipher.py "Hello World" -e 
	> 0H1P1I1I1FtT0W1F1C1I1Q
