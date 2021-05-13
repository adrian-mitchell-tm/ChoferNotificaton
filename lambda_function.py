import json

# Email templates
from templates.finops.Chargeback import Chargeback
from templates.finops.Optimization import Optimization
from templates.security.PolicyViolation import PolicyViolation
from templates.security.AwsWildcard import AwsWildcard
from templates.security.AzureWildcard import AzureWildcard
from templates.security.Nuke import Nuke


def lambda_handler(event, context):
    
    # Init notifications with owner based consolidation
    spvn = PolicyViolation()
    snn = Nuke()
    forn = Optimization()

    # Sort and send notifications without consolidation
    for record in event['Records']:
        
        json_payload = json.loads(record["body"])
        message = json.loads(json_payload["Message"])

        if message["type"] == "FCBN":
            fcbn = Chargeback(message["month"], message["cloud"])
            fcbn.send()
        elif message["type"] == "FORN":
            forn.add(message)
        elif message["type"] == "SPVN":
            spvn.add(message)
        elif message["type"] == "SNN":
            snn.add(message)
        elif message["type"] == "SAWSW":
            sawsw = AwsWildcard(message["message"])
            sawsw.send()
        elif message["type"] == "SAZW":
            sazw = AzureWildcard(message["message"])
            sazw.send()
        else:
            print("invalid notification type")
    
    # Consolidate and send notifications
    spvn.consolidation()
    snn.consolidation()
    forn.consolidation()
