import json
import yaml
import subprocess

#refer //cloud.google.com/logging/docs/quickstart-sdk
#refer //cloud.google.com/logging/docs/audit
# bucket creation
cmd1= "gcloud logging buckets create my-bucket001 --location global --description 'My first bucket001'"
proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)

cmd= "gcloud logging read 'resource.type=global'  --project=hpc-lab-316407"
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

my_bytes_value = out

# Decode UTF-8 bytes to Unicode, and convert single quotes
# to double quotes to make it valid JSON
my_str = my_bytes_value.decode('utf-8')

if my_str is not None:
    print("audit profile capturing all activities")

print(my_str)

# converting yaml format string to dict
docs1 = yaml.load_all(my_str)
yaml.warnings({'YAMLLoadWarning': False})
for doc in docs1:
    #print(doc)
    if doc['resource']['type']=="global":
        print("Ensuring that log profile captures audit logs for all regions including global")
    #converting from dict to string
    s=json.dumps(doc, indent=4, sort_keys=True) 
    #print(type(s))
    print(s)