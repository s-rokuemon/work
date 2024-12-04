import aws_cdk as core
from glue_stack import GlueStack
from compute_stack import ComputeStack
from storage_stack import StorageStack
import os



app = core.App()
env = {
    "region": os.environ["CDK_DEFAULT_REGION"],
    "account": os.environ["CDK_DEFAULT_ACCOUNT"],
}

storage_stack = StorageStack(
    app,"StorageStack",
    env=env
)

compute_stack = ComputeStack(
    app,"ComputeStack",
    storage_stack_output=storage_stack.outputs,
    env=env
)

# Glue-stack
glue_stack = GlueStack(
    app,"GlueStack",
    storage_stack_output=storage_stack.outputs,
    env=env
)

app.synth()