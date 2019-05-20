import boto3
import os
        
def lamda_sendMessage(event, context):
	send_to = os.environ.get('SEND_TO')
    toEmail = send_to
    fromEmail = send_to
    replyTo = fromEmail
    name = "Send-email"
    subject = "Test-Email"
    message = "My content"

    client = boto3.client('ses')
    response = client.send_email(
		Source=fromEmail,
		Destination={
			'ToAddresses': [
				toEmail,
			],
		},
		Message={
			'Subject': {
				'Data': subject,
				'Charset': 'utf8'
			},
			'Body': {
				'Text': {
					'Data': message,
					'Charset': 'utf8'
				}
			}
		},
		ReplyToAddresses=[
			replyTo
		]
	)
			
    print(response['MessageId'])
    return {'code': 0, 'message': 'success'}