from behave import *
import os
import filecmp

@given('a set of specific small files')
def step_impl(context):
	context.data = context.table

@then('we will find fin matches fout')
def step_impl(context):
	for row in context.data:
		context.fin=row['fin']
		context.fout=row['fout']
		assert (filecmp.cmp(context.fin, context.fout))
