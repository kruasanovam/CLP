from behave import *
import os
import subprocess
import filecmp


@given('a set of specific files is given')
def step_impl(context):
	context.data = context.table


@when('we run our CLP')
def step_impl(context):
 	for row in context.data:
		context.fin=row['fin']
		context.fout=row['fout']
		os.system ("python CLP.py %s%s >%s%s"% (context.data_folder, context.fin, context.data_folder, context.fout))
