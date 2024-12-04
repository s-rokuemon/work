import aws_cdk as core
import os
from dataclasses import dataclass

class GlueStack(core.Stack): 
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
        out_bucket = storage_stack_output["s3_out_bucket"]


        # setting
        crawler_role_name = 'glue_role_access_s3'
        crawler_name = 'crawler_test'
        etl_job_name = 'glue_etl_job'
        athena_db_name = 'database_for_athena'
        workflow_name = 'glue_wf'
        glue_crawler_trigger_name = 'trigger_crawler_data'
        glue_job_trigger_name = 'trigger_etl_job'
        


        # s3 assets
        # Archived and uploaded to Amazon S3 as a .zip file
        dirname = os.path.dirname(__file__)
        etl_job_file_asset = core.aws_s3_assets.Asset(self, "glue-etl-job-assets",
            path=os.path.join(dirname, "glue_job_src/glue_etl_job.py")
        )

        # glue crawler role
        crawler_role = core.aws_iam.Role(
            self, crawler_role_name,
            assumed_by=core.aws_iam.ServicePrincipal("glue.amazonaws.com"),
        )
        crawler_role.add_managed_policy(
            core.aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')
        )

        glue_crawler_allow_resource_path = f"{in_bucket.bucket_arn}/*"
        glue_etl_allow_resource_path = f"{out_bucket.bucket_arn}/*"
        crawler_role.add_to_policy(
            core.aws_iam.PolicyStatement(
                effect=core.aws_iam.Effect.ALLOW,
                resources=[glue_crawler_allow_resource_path],
                actions=["s3:GetObject"]
            ),
        )
        crawler_role.add_to_policy(
            core.aws_iam.PolicyStatement(
                effect=core.aws_iam.Effect.ALLOW,
                resources=[glue_etl_allow_resource_path],
                actions=["s3:PutObject"]
            )
        )
        # crawler
        cfn_crawler = core.aws_glue.CfnCrawler(
            self, crawler_name,
            role=crawler_role.role_arn,
            name=crawler_name,
            database_name=athena_db_name,
            targets={
                "s3Targets":[{"path":f"s3://{in_bucket.bucket_name}/"}]
            }
        )

        # ETL
        glue_etl = core.aws_glue.CfnJob(
            self, etl_job_name
            , role=crawler_role.role_arn
            , command=core.aws_glue.CfnJob.JobCommandProperty(
                name="pythonshell",
                python_version="3",
                script_location=f"{etl_job_file_asset.s3_object_url}"
            )
            , glue_version="1.0"
            , name=etl_job_name
            # , worker_type="G.1X"
        )

        # workflow
        cfn_workflow = core.aws_glue.CfnWorkflow(
            self, workflow_name,
            name=workflow_name,
        )
        
        # step1: Trriger-crawler
        cfn_trigger_crawler = core.aws_glue.CfnTrigger(
            self, glue_crawler_trigger_name,
            actions=[core.aws_glue.CfnTrigger.ActionProperty(
                crawler_name=cfn_crawler.name,
            )],
            type="ON_DEMAND",
            name=glue_crawler_trigger_name,
            # schedule="cron(*/5 * * * *)",
            start_on_creation=False,
            workflow_name=cfn_workflow.name
        )
        
        
        # step2: Trriger-etl_job
        cfn_trigger_etl_job = core.aws_glue.CfnTrigger(
            self, glue_job_trigger_name
            , actions=[core.aws_glue.CfnTrigger.ActionProperty(
                job_name=glue_etl.name,
            )]
            , predicate=core.aws_glue.CfnTrigger.PredicateProperty(
                conditions=[core.aws_glue.CfnTrigger.ConditionProperty(
                    crawler_name=cfn_crawler.name,
                    crawl_state="SUCCEEDED",
                    logical_operator="EQUALS",
                )],
                logical="ANY"
            )
            , name=glue_job_trigger_name
            , type="CONDITIONAL"
            , start_on_creation=True
            , workflow_name=cfn_workflow.name
        )
        
