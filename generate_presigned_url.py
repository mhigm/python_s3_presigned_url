
def s3_generate_presigned_url(key, content_type, client_method='put_object', expired=7200, http_method='PUT'):
	s3 = boto3.client('s3')
	signed_url = s3.generate_presigned_url(ClientMethod=client_method,
	                                       Params={'Bucket': settings.AWS_BUCKET_NAME,
	                                               'Key': key,
	                                               'ContentType': content_type},
	                                       ExpiresIn=expired,
	                                       HttpMethod=http_method)
