import json
import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    newRun = glue.start_workflow_run(
        Name = 'glue_wf',
        # RunProperties = { 'key1': 'value1' }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }