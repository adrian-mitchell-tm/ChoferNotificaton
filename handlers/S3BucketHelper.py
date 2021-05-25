import boto3
import pandas as pd
from io import StringIO

class S3BucketHelper:

    def __init__(self):
        self.client = boto3.client('s3')
    
    
    def readCsvFile(self, bucket_name, filename):

        csv_obj = self.client.get_object(Bucket=bucket_name, Key=filename)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')

        df = pd.read_csv(StringIO(csv_string))

        return df
