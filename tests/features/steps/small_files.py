from behave import *
import filecmp


@then('we will find fin matches fout')
def step_impl(context):
	for row in context.data:
		context.fin=context.data_folder+row['fin']
		context.fout=context.data_folder+row['fout']
		assert (filecmp.cmp(context.fin, context.fout))