This folder contains some generic tests for the CLP.py. Implemented with python and behave. 

***********************************************************************************
***                              LIBRARY                                        ***
***********************************************************************************
- features: contains 4 feature files each with various 
scenarios groupped by validation type (filename, format, length, content)
- reports: output folder for saving test execution reports (if required)
- test data: folder with test data that should be used when running 
your tests. Groupped based on feature tested
- Test Scenarios.pdf: simple diagram that outlines all scenarios covered in tests


************************************************************************************
***                               USAGE                                          ***
************************************************************************************
#to run all feature tests
   behave 
#to run all positive feature tests
   behave --tags=positive 
#to run all positive feature tests
   behave --tags=negative
#to run feature tests and save output as 
   behave -v --junit


************************************************************************************
***                               PREREQUISITE                                   ***
************************************************************************************
#install behave
   pip install behave
##or other install options:
http://pythonhosted.org/behave/install.html
