"""
Defaults module for AWS cleanup
"""
AWS_REGION = 'us-east-2'
CLUSTER_PREFIXES_SPECIAL_RULES = {
    'jnk': 36, 'dnd': 'never', 'lr1': 24, 'lr2': 48, 'lr3': 72, 'lr4': 96,
    'lr5': 120
}
MINIMUM_CLUSTER_RUNNING_TIME = 10
AWS_CLOUDFORMATION_TAG = 'aws:cloudformation:stack-name'
CONFIRMATION_ANSWER = 'yes-i-am-sure-i-want-to-proceed'
