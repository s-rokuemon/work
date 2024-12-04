import aws_cdk as core
import os
from dataclasses import dataclass


class ComputeStack(core.Stack): 
    def __init__(
        self, 
        scope: core.App, 
        name: str, 
        storage_stack_output,
        **kwargs
    ) -> None:
        super().__init__(scope, name, **kwargs)
        
        # storage info
        in_bucket = storage_stack_output["s3_in_bucket"]
        
        
        # Lambda
        lambda_handler = core.aws_lambda.Function(
            self, 'LambdaHandler',
            runtime=core.aws_lambda.Runtime.PYTHON_3_9,
            code=core.aws_lambda.Code.from_asset('lambda_src'), #関数が存在するディレクトリ指定を指定する
            handler="from_lambda_to_gluewf.lambda_handler", #
            memory_size=128, #必要に応じて見直す
            timeout=core.Duration.seconds(100),#必要に応じて見直す
            dead_letter_queue_enabled=False, #必要に応じて見直す
        )

        # lambdaにtriggerを付与
        lambda_handler.add_event_source(
            core.aws_lambda_event_sources.S3EventSource(
                in_bucket,
                events=[core.aws_s3.EventType.OBJECT_CREATED_PUT],
            )
        )
