from behave import *
import os
import subprocess
import filecmp
from environment import CLP_PATH


@given('a set of specific files is given')
def step_impl(context):
	context.data = context.table


@when('we run our CLP')
def step_impl(context):
 	for row in context.data:
		context.fin=row['fin']
		context.fout=row['fout']
		os.system ("python %s %s%s >%s%s"% (CLP_PATH, context.data_folder, context.fin, context.data_folder, context.fout))
