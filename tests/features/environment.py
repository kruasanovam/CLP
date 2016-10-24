from behave import *

CLP_PATH=('../CLP\ Tool/CLP.py')

# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)
BEHAVE_DEBUG_ON_ERROR = False

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_all(context):
    setup_debug_on_error(context.config.userdata)

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)

#DATA PREPARATION STEPS
@given('we prepare test data for length checks')
def step_impl(context):
	context.data_folder="test_data/length/"

@given('we prepare test data for content checks')
def step_impl(context):
	context.data_folder="test_data/content/"

@given('we prepare test data for format checks')
def step_impl(context):
	context.data_folder="test_data/format/"

@given('we prepare test data for file name checks')
def step_impl(context):
	context.data_folder="test_data/filename/"