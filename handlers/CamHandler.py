import boto3
from boto3.dynamodb.conditions import Key

class CamHandler:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.dynamo_table = self.dynamodb.Table('ace-prod-cam-data')


    def get_contacts_by_account_name(self, account_name):
        contacts = []
        done = False
        response=self.dynamo_table.query(
            KeyConditionExpression=Key('Name').eq(account_name)
        )
        if response:
            for item in response.get('Items', []):
                contacts.append(item["Owner"])

        return contacts

    def get_contacts_by_accountid(self, account_id):

        scan_kwargs = {
            'FilterExpression': Key('Account_ID').eq(account_id)
        }
        
        contacts = []
        done = False
        start_key = None
        while not done:
            if start_key:
                scan_kwargs['ExclusiveStartKey'] = start_key
            response = self.dynamo_table.scan(**scan_kwargs)
            for item in response.get('Items', []):
                contacts.append(item["Owner"])
            start_key = response.get('LastEvaluatedKey', None)
            done = start_key is None
        
        # print(contacts)
        
        return contacts
        
        
    def get_all_aws_contacts(self):

        scan_kwargs = {
            'FilterExpression': Key('Cloud_Service_Provider').eq('AWS')
        }
        
        contacts = []
        done = False
        start_key = None
        while not done:
            if start_key:
                scan_kwargs['ExclusiveStartKey'] = start_key
            response = self.dynamo_table.scan(**scan_kwargs)
            for item in response.get('Items', []):
                contacts.append(item["Owner"])
            start_key = response.get('LastEvaluatedKey', None)
            done = start_key is None
        
        # remove duplicates
        contacts = list(dict.fromkeys(contacts))
        
        return contacts
    
    def get_all_azure_contacts(self):

        scan_kwargs = {
            'FilterExpression': Key('Cloud_Service_Provider').eq("Azure")
        }
        
        contacts = []
        done = False
        start_key = None
        while not done:
            if start_key:
                scan_kwargs['ExclusiveStartKey'] = start_key
            response = self.dynamo_table.scan(**scan_kwargs)
            for item in response.get('Items', []):
                contacts.append(item["Owner"])
            start_key = response.get('LastEvaluatedKey', None)
            done = start_key is None
        
        # remove duplicates
        contacts = list(dict.fromkeys(contacts))
        
        return contacts
