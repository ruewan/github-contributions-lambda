import boto3
from github_contributions import get_contributions

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    resp = get_contributions(event['usernames'])
    s3.Object('prominent-edge-static', 'contributions.json').put(Body=resp,
                                                                 ContentType='application/json')
    return resp