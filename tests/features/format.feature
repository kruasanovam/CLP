Feature: File Format Validation (binary and non-binary)

Background: Test Data Folder Setup
  Given we prepare test data for format checks

@positive
 Scenario: CLP works for files reagrdless of format as long as non-binary, e.g.: json, html, xml, crash, log
  Given a set of specific files is given:
	| fin 			| fout       	| expected    		|
	| jsonin	  	| jsonout.txt	| jsonexp.txt		|
	| htmlin		| htmlout.txt	| htmlexp.txt		|
	| xmlin			| xmlout.txt	| xmlexp.txt		|
	| crashin		| crashout.txt	| crashexp.txt		|
	| login 		| logout.txt	| logexp.txt   		|
 When we run our CLP
 Then we will find fout matches expected

@negative
 Scenario: CLP should not work with binary files, e.g.: .png, .jpg, .mp3
  Given a set of specific files is given:
	| fin 			|
	| jpgin.jpg		|
	| pngin.png     |
	| mp3in         |

 When we run our CLP an expect error returned
 Then we will find CLP returns file is binary error