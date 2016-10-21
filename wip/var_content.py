from behave import *
import os
import filecmp

data_folder = "test_data/content/"

@given('a set of specific files with various content')
def step_impl(context):
	context.data = context.table

 