from behave import *
import os
import subprocess

@given('a set of specific empty files')
def step_impl(context):
	context.data = context.table

@when('we try to run our CLP2')
def step_impl(context):
 	for row in context.data:
		context.fin='test_data/'+row['fin']
		context.error = subprocess.check_output("python CLP.py %s"%context.fin, shell=True)


@then('we will find CLP returns correct error')
def step_impl(context):
	for row in context.data:
		context.fin='test_data/'+row['fin']
		assert (context.error=="File is empty")


