from behave import *
import os
import subprocess


@when('we run our CLP an expect error returned')
def step_impl(context):
	for row in context.data:
		context.fin=context.data_folder+row['fin']
		context.error = subprocess.check_output("python CLP.py %s"%context.fin, shell=True)

@when ('we try to run our CLP with no filename argument specified')
def step_imp(context):
	context.error = subprocess.check_output("python CLP.py", shell=True)

@then('we will find CLP returns file is empty error')
def step_impl(context):
	for row in context.data:
		context.fin=context.data_folder+row['fin']
		assert (context.error=="File is empty")

@then('we will find CLP returns file is binary error')
def step_impl(context):
	for row in context.data:
		context.fin=context.data_folder+row['fin']
		assert (context.error=="Sorry, binary files are not supported")

@then('we will find CLP returns file not specified error')
def step_impl(context):
		assert (context.error=="No file specified")

@then('we will find CLP returns no such file error')
def step_impl(context):
	for row in context.data:
		context.fin=context.data_folder+row['fin']
		assert (context.error=="I/O error(2): No such file or directory")