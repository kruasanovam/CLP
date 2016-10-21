from behave import *

@given('we prepare test data for length checks')
def step_impl(context):
	context.data_folder="test_data/length/"

@given('we prepare test data for content checks')
def step_impl(context):
	context.data_folder="test_data/content/"

