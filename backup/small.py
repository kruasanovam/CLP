from behave import *
import os
import filecmp

@given('we have a small file')
def step_impl(context):
	pass

@when('we run our CLP')
def step_impl(context):
	fname="test.txt"
	os.system("python CLP.py %s >output.txt"%fname)

@then('print the whole file')
def step_impl(context):
	assert (filecmp.cmp("test.txt", "output.txt"))
