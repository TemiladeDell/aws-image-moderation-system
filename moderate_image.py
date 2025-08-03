import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    rekognition = boto3.client('rekognition')

    # Get image details from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Call Rekognition to detect moderation labels
    response = rekognition.detect_moderation_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MinConfidence=50
    )
    print(f"Full Rekognition response for {key}:")
    print(response)

    print(f"Moderation labels for {key}:")
    for label in response['ModerationLabels']:
        print(f"{label['Name']} - {label['Confidence']:.2f}%")

    return {
        'statusCode': 200,
        'body': json.dumps('Image moderation check complete.')
    }
