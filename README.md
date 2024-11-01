# search_for_cc
SWC - 12/14/2022


This script takes a text file and searches for payment card PAN number line by line. It then outputs any matches to the console.

Instructions:

1. Data that you would like to scan should be in the ".txt" file type. This can be done by either saving the data in that format, or copying it over to a ".txt" file.
	
2. Remove all test files from the "/results" folder and put your data that you would like to scan in the "/results" folder. This can be as many individual ".txt" files as you would like.

2. Run the "search_CC.py" file.
	* This may have to be done by right clicking the "search_CC.py" and selecting "open with" then "chose another app" then selecting the python application (Typically "C:\Program Files\Python*\python.exe").
	* Alternatively you may need to get IT to install Python for you.

3. The scan will run, then automatically save any results to the "/output" folder as "RESULTS_" + the original file name.


Note:

1. The "test_numbers.txt" file is there to give easy access to approved test payment card PANs to verify the scripts accuracy. It would be smart to simply scan this file or scatter these numbers throughout your data to ensure the script is functioning as intended.
