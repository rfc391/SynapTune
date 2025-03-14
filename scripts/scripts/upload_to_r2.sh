
#!/bin/bash

# Input variables
BUCKET_NAME="immudb-storage"
FILE_PATH=$1
FILE_NAME=$(basename "$FILE_PATH")

# Upload file to R2
echo "Uploading $FILE_NAME to R2 bucket $BUCKET_NAME..."
# Actual command: wrangler r2 object put "$BUCKET_NAME/$FILE_NAME" --file "$FILE_PATH"

# Generate R2 URL
R2_URL="https://<account_id>.r2.cloudflarestorage.com/$BUCKET_NAME/$FILE_NAME"

# Store metadata in immudb
echo "Storing metadata in immudb..."
# Actual command: immuclient safeset "file:$FILE_NAME" "$R2_URL"

echo "File uploaded to R2 and metadata stored in immudb."
echo "R2 URL: $R2_URL"
