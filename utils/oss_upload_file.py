# import oss2
#
# ENV_ACCESS_KEYID = "LTAI4FoC6hbbmHx6Pjifr9tN"
# ENV_ACCESS_SECRET = "a2IEzTPbemslHR5yjwAs8NbFGvODOf"
# ENV_OSS_URL = 'http://oss-cn-hongkong.aliyuncs.com'
# ENV_BUCKET_NAME = 'global-swg'
#
#
# class UploadFile(object):
#
#     def __init__(self):
#         self.AccessKeyId = ENV_ACCESS_KEYID
#         self.AccessKeySecret = ENV_ACCESS_SECRET
#         self.OSS_url = ENV_OSS_URL
#         self.BucketName = ENV_BUCKET_NAME
#         auth = oss2.Auth(self.AccessKeyId, self.AccessKeySecret)
#         self.bucket = oss2.Bucket(auth, self.OSS_url, self.BucketName)
#
#     def upload_env(self):
#         self.bucket.put_object_from_file('parcel-test-env/dev.env', '../dev.env')
#         self.bucket.put_object_from_file('parcel-test-env/ap1-staging.env', '../ap1-staging.env')
#         # self.bucket.put_object_from_file('parcel-test-env/ap2-staging.env', '../ap2-staging.env')
#         # self.bucket.put_object_from_file('parcel-test-env/ap1-sandbox.env', '../ap1-sandbox.env')
#         # self.bucket.put_object_from_file('parcel-test-env/ap2-sandbox.env', '../ap2-sandbox.env')
#
#     def upload_report(self, filename):
#         path = "parcel-test-report/" + filename + ".html"
#         self.bucket.put_object_from_file(path, 'report.html')
#
#
# if __name__ == '__main__':
#     try:
#         upload = UploadFile()
#         upload.upload_env()
#         print("上传成功！")
#     except oss2.exceptions as _:
#         raise FileExistsError("上传失败")
