import json
import time
import requests


def get_analyzed_documents(payload, context):
    time.sleep(300)

    mutation = '''
        mutation ($documents: [String!]) {
            parseDocuments (documents: $documents) {
                success
            }
        }
    '''

    res = requests.post(
        payload["graphql_endpoint"],
        json={
            'query': mutation,
            'variables': payload
        },
        verify=False
    )
