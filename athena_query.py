"""
Run with out passing aws credentials because it is already set in the
AWS CLI configuration in the system
"""

import boto3
import os

# take the cred from env
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# session
session = boto3.Session(
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    region_name='us-east-1'
)

client = session.client('athena')

# Example function to run an Athena query
def run_athena_query(query, database, output_location):
    try:
        response = client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': output_location}
        )
        return response
    except Exception as e:
        print(f"Error running Athena query: {e}")
        return None

# Example usage
query = """SELECT * FROM "default"."s3_salaries" LIMIT 10;"""  # Use triple quotes for multi-line strings
database = "s3_analyze_salaries_db"
output_location = "s3://athenajenkinstestbucket/"

response = run_athena_query(query, database, output_location)
if response:
    print("Query executed successfully. Query execution ID:", response['QueryExecutionId'])
else:
    print("Query execution failed.")