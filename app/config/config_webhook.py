import os

from dotenv import load_dotenv
from nylas import Client
from nylas.models.webhooks import CreateWebhookRequest, WebhookTriggers

load_dotenv()

api_key = os.environ.get("NYLAS_API_KEY")
api_uri = os.environ.get("NYLAS_API_URI")
server_url = os.environ.get("SERVER_URL")
email = os.environ.get("EMAIL")

# validate environment
if api_key is None or api_uri is None or server_url is None or email is None:
    print("api key or uri is not avaiable")
    exit()

nylas = Client(
    api_key=api_key,
    api_uri=api_uri,
)

# Define the webhook properties
request_body = CreateWebhookRequest(
    trigger_types=[WebhookTriggers.MESSAGE_CREATED],
    # In the format https://YOURSERVER.COM/webhook
    webhook_url=server_url + "/events",
    description="Message Created Webhook",
    notification_email_addresses=[email],
)

# Create the webhook
webhook, _, _ = nylas.webhooks.create(request_body=request_body)
webhook_secret = webhook.webhook_secret

# Print the newly created webhook
print(webhook)
print(webhook_secret)
