from behave import *
import filecmp

@then('we will find fout matches expected')
def step_impl(context):
	for row in context.data:
		context.fout=context.data_folder+row['fout']
		context.expected=context.data_folder+row['expected']
		result= (filecmp.cmp(context.fout, context.expected))
		if (result==False):
			print ('Assertion failed for '+context.fout+context.expected)
		assert result