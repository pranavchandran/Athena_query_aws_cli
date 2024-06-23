"""
Run with out passing aws credentials because it is already set in the
AWS CLI configuration in the system
"""

import boto3

# Boto3 will automatically use AWS credentials stored in your environment

# Create an Athena client
client = boto3.client('athena', region_name='us-east-1')

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