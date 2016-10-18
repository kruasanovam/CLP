Feature: first attempt

  Scenario: Large File
     Given we have a big file
      when we run our CLP pr
      then print only last 5 lines