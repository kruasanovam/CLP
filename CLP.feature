Feature: first attempt

Scenario: some scenario
  Given a set of specific files:
	 | fin 			| fout       |
	 | test1.txt    | test11.txt |
	 | test2.txt    | test22.txt |
 When we run our CLP2
 Then we will find fin matches fout

