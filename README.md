## Azure Blob Lister

---

List and filter blobs in Azure Storage by prefix and keywords.


### Configuration

---

Update the following values in the script:

| Variable               | Description                                                                         |
|------------------------|-------------------------------------------------------------------------------------|
| `BLOB_PREFIX`          | Blob folder path to search under (e.g., `"2025/"`)                                  |
| `SEARCH_TERMS`         | List of keywords that must be in blob names                                         |
| `CONTAINER_NAME`       | Azure Blob Storage container name                                                   |
| `STORAGE_ACCOUNT_NAME` | Azure Storage account name                                                          |
| `CREDENTIALS`          | Azure AD credentials for authentication (`tenant_id`, `client_id`, `client_secret`) |

### Usage
 
---

```bash
poetry install
poetry run python azure_blob_lister.py
```
