from google.cloud import storage
import os

class GoogleBucket:

    def __init__(self,credentials,bucket_name):
        self.bucket_name = bucket_name
        self.credentials = credentials
        self.storage_client = storage.Client.from_service_account_json(
        credentials)

    def upload_file(self,source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The path to your file to upload
        # source_file_name = "local/path/to/file"
        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"
      
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )

#
#def download_file(file_name, bucket):
#    """
#    Function to download a given file from an S3 bucket
#    """
#    s3 = boto3.resource('s3')
#    output = os.path.join("c:\\Users\\pmrodriguezc\\Downloads\\",file_name)
#    s3.Bucket(bucket).download_file(file_name, output)
#
#    return output
#
#
#def list_files(bucket):
#    """
#    Function to list files in a given S3 bucket
#    """
#    s3 = boto3.client('s3')
#    r = s3.list_objects(Bucket=bucket)
#    if 'Contents' in r:
#        contents = [f for f in r['Contents']]
#        return contents
#    else:
#        None