from storages.backends.s3boto3 import S3Boto3Storage, SpooledTemporaryFile


class CustomS3Boto3Storage(S3Boto3Storage):
    def _save(self, name, content):
        content.seek(0)
        with SpooledTemporaryFile() as tmp:
            tmp.write(content.read())
            return super()._save(name, tmp)
