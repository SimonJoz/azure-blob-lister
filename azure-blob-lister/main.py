from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient

BLOB_PREFIX = "prefix/"
SEARCH_TERMS = ["search1", "search2"]

CONTAINER_NAME = ""
STORAGE_ACCOUNT_NAME = ""
AZURE_ACCOUNT_URL = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

CREDENTIALS = ClientSecretCredential(
    tenant_id="",
    client_id="",
    client_secret="",
)

blob_service_client = BlobServiceClient(AZURE_ACCOUNT_URL, CREDENTIALS)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)
blob_list = container_client.list_blobs(name_starts_with=BLOB_PREFIX)

for blob in blob_list:
    if all(search_text in blob.name for search_text in SEARCH_TERMS):
        print(blob.name)
