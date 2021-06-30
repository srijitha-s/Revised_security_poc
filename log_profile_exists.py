import google.cloud.logging
#preq create a service account and assign it to an envinornment variable -//cloud.google.com/logging/docs/reference/libraries#client-libraries-install-python

import logging

client = google.cloud.logging.Client()

#client.setup_logging()
#text = 'Hello, world!'
#logging.warning(text)
#print("Logged: {}".format(text))

filter_str ="resource.labels.type:gcs_bucket"
count=0
#x = client.list_entries(filter_=filter_str)
#print(x)

for entry in client.list_entries():
    print(entry)
    print("****************")
    count=count+1
   
print(count)
if count>=1:
    print("logging profile is sucessfully verified")
