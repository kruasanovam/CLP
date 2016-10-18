from behave import *
import os
import filecmp
import logging
from collections import deque


@given('we have a big file')
def step_impl(context):
	pass

@when('we run our CLP pr')
def step_impl(context):
	fname="test.txt"
	os.system("python CLP.py %s >output.txt"%fname)

@then('print only last 5 lines')
def step_impl(context):
	with open('test.txt') as fin, open('outputfile', 'w') as fout:
		fout.writelines(deque(fin, 6))
	