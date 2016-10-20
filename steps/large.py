from behave import *
import os
import filecmp


@given('a set of specific large files')
def step_impl(context):
	context.data = context.table

@when('we run our CLP2')
def step_impl(context):
 	for row in context.data:
		context.fin=row['fin']
		context.fout=row['fout']
		os.system ("python CLP.py %s >%s"% (context.fin, context.fout))

@then('we will find fout matches expected')
def step_impl(context):
	for row in context.data:
		context.fout=row['fout']
		context.expected=row['expected']
		assert (filecmp.cmp(context.fout, context.expected))

	
	