Feature: File Length Validations

Background: Test Data Folder Setup
  Given we prepare test data for length checks

 Scenario: CLP works for empty files
  Given a set of specific files is given:
	| fin 		   |
	| empty.txt    |
 When we run our CLP an expect error returned
 Then we will find CLP returns file is empty error

Scenario: CLP works for files with 1-5 lines
  Given a set of specific files is given:
	| fin 		   | fout       	|
	| small1in.txt | small1out.txt 	|
	| small2in.txt | small2out.txt 	|
	| small2in.txt | small3out.txt 	|
 When we run our CLP
 Then we will find fin matches fout

Scenario: CLP works for files with >5 lines
  Given a set of specific files is given:
	 | fin 			| fout       	| expected    	|
	 | large1in.txt | large1out.txt | large1exp.txt |
 When we run our CLP
 Then we will find fout matches expected

 

