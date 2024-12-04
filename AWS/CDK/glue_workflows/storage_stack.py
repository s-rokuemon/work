import aws_cdk as core
import os
# from aws_cdk.core import Stack,CfnOutput
from dataclasses import dataclass
# from aws_cdk.aws_lambda_event_sources import S3EventSource


class StorageStack(core.Stack): 
    def __init__(
        self, 
        scope: core.App, 
        name: str, 
        **kwargs
    ) -> None:
        super().__init__(scope, name, **kwargs)

        in_bucket_name = 'in-bucket-glue-etl'
        out_bucket_name = 'out-bucket-glue-etl'
        
        # s3 bucket In
        in_bucket = core.aws_s3.Bucket(
            self, in_bucket_name,
            bucket_name=in_bucket_name,
            removal_policy=core.RemovalPolicy.DESTROY,# cdk destroyした際にバケットも含めて削除
            auto_delete_objects=True,# cdk destroyした際にオブジェクトも含めて削除
        )

        # s3 bucket Out
        out_bucket = core.aws_s3.Bucket(
            self, out_bucket_name,
            bucket_name=out_bucket_name,
            removal_policy=core.RemovalPolicy.DESTROY,# cdk destroyした際にバケットも含めて削除
            auto_delete_objects=True,# cdk destroyした際にオブジェクトも含めて削除
        )

        self.output_props = {}
        self.output_props['s3_in_bucket'] = in_bucket
        self.output_props['s3_out_bucket'] = out_bucket
        

    @property
    def outputs(self):
        return self.output_props
        
        
