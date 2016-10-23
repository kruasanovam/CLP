Feature: File Name Validation

Background: Test Data Folder Setup
  Given we prepare test data for file name checks

Scenario: CLP works for files with valid file names, even if it is: long, contains allowed special chars, contains space
  Given a set of specific files is given:
| fin 																									| fout       | expected    	|
| thisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilena.txt  | longout.txt| longexp.txt   |
				
When we run our CLP										
Then we will find fout matches expected


Scenario: CLP does not work when no filename specified
 When we try to run our CLP with no filename argument specified
 Then we will find CLP returns file not specified error