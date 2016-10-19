from behave import *
import os
import filecmp


@given('a set of specific files')
def step_impl(context):
	data = []
	for row in context.table:
		fin=row['fin']
		out=row['fout']
		data.append(fout)


@when('we run our CLP2')
def step_impl(context):
	for row in context.table:
		context.fin=row['fin']
		context.fout=row['fout']
		os.system ("python CLP.py %s >%s"% (context.fin, context.fout))

@then('we will find fin matches fout')
def step_impl(context):
	assert (filecmp.cmp(context.fin, context.fout))
	