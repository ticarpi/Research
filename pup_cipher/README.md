Decrypt/Encrypt data with the 0A1Q1H1L1Gzu cipher
========================

## Installation:

Installation is simple: if you have Python 2.7\+ installed this will run.

The only imports are for argparse and urllib - both part of Python 2.7.


If you get any dependency errors then install the missing one via pip:

	pip install argparse
	pip install urllib


## Usage

This tool will decrypt valid strings using the cipher as seen in a bunch of different malware/PUP trojans.  
e.g. https://totalhash.cymru.com/analysis/?fc4e853ae04910ace6eb63e9451003e2eb95d8ca:
```0U0I0DzutDtDtD0A0C0DtBtD0EyCtD0CzytDtD0AtN0U0I0DtBzu0CtDyDzyzytDtD0AtGyByBzzyBzztA0E0FtN0A1E1E0N1T1H1Pzu0D1L1N1L2Z1T1ItT0S1L2Z1P1BtN0S2Z1T2Z1Pzu0I1G1B2Z1T1I1ItN0I0D0TzutN0I0R0V0E0RzutBtFtBtAtN0I0E0V1P1CzuyCtFtDtFtBzytDtDtFyDyDtCtBtN0O0SzuyDtFtCtN0S0VzutAtN1I1E2Z1EzutDtN1S2Z1C2UzutDtN0V0M0CzutN0R0E0GzutN0S1C1RzutN0L1T1G1NzutCtDtAtAtN0L1T1G1NzutCtDtAtAtN0A0D0V0FzuzztDtDtDtNtN0U1V0T0MzutDtCtAzytN0U1V0D0TzutBtDtCyEtDzytByEtN0U1V0S0D0TzutN1W2Y1O1Gzr1O1Q1FtG1WtAzutN0P1T1C1T1H0A0L0LzutOtB0F0R1P1E1F1C2Z0ItOtBtDtOtB0F0CtOtA0DtByDzytN0F1I1T1N1BzutByDzytN0A1Q1H1L1GzutCtN0I1Q1I1PzutBtCtN0T0D0YzuzytDtByEtN0L0T0D0YzutN0T0D0Y0CzutN0L0S0V0R0D0Tzu```

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
