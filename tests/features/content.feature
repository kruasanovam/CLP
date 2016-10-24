Feature: File Content Type Validation

Background: Test Data Folder Setup
  Given we prepare test data for content checks

@positive
 Scenario: CLP works for files each wth content in different languages: eng, russian, chinese
  Given a set of specific files is given:
	| fin 			| fout       	| expected    	|
	| rusin.txt   	| rusout.txt	| rusexp.txt    |
	| engin.txt 	| engout.txt	| engexp.txt 	|
 	| chin.txt 		| chout.txt		| chexp.txt 	| 
 When we run our CLP
 Then we will find fout matches expected


 