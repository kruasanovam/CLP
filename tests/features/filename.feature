Feature: File Name Validation

Background: Test Data Folder Setup
  Given we prepare test data for file name checks

@positive
Scenario: CLP works for files with valid file names, even if it is: max/min long,contains allowed special chars, contains space
  Given a set of specific files is given:
| fin 																									| fout       | expected    	|
| thisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilenamethathas255charactersthisisalongfilena.txt  | longout.txt| longexp.txt   |
| has\ space\ in.txt 												| hasspaceout.txt 	| hasspaceexp.txt 	|
| 1 																| 1out.txt 			| 1exp.txt 			|
| spch~\`\!\@#\$%\^\&\*\(\)_+-\=\[\]\\\{\}\"\;\'\<\>\?\,.\:\".txt	| spchout.txt		| spchexp.txt		|
				
When we run our CLP										
Then we will find fout matches expected

@negative
Scenario: CLP does not work when file specified does not exist
 Given a set of specific files is given:
| fin 				|
| filenotpresent	|
| foldername		|
| 1exp.html			|
| 1exp				|

 When we run our CLP an expect error returned
 Then we will find CLP returns no such file error

@negative
 Scenario: CLP does not work when no filename specified
 When we try to run our CLP with no filename argument specified
 Then we will find CLP returns file not specified error