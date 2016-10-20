Feature: first attempt

Scenario: CLP works for files with >5 lines
  Given a set of specific large files:
	 | fin 			| fout       | expected    |
	 | test1.txt    | test11.txt | test111.txt |
	 | test2.txt    | test22.txt | test222.txt |
 When we run our CLP2
 Then we will find fout matches expected

 Scenario: CLP works for files with 1-5 lines
  Given a set of specific small files:
	| fin 		   | fout       |
	| test3.txt    | test33.txt |
	| test4.txt    | test44.txt |
 When we run our CLP2
 Then we will find fin matches fout

 Scenario: CLP works for empty files
  Given a set of specific empty files:
	| fin 		   |
	| test5.txt    |
	| test6.txt	   |
 When we try to run our CLP2
 Then we will find CLP returns correct error