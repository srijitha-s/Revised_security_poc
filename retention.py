#describing
#$(gcloud beta logging buckets describe _Default --location=global="value(details)")
#print(details)
#$(gcloud projects list --format="value(projectId)")

#set retention period
#gcloud beta logging buckets update _Default --location=global --retention-days=15

# Execute the gcloud command to get a list of projects
# and load data in JSON format for further processing

import subprocess
import json
import shlex

project_list_command = "gcloud beta logging buckets describe my-bucket789 --location=global --format=json"

#print(type(project_list_command))
project_output = subprocess.check_output(shlex.split(project_list_command))
#print(project_output)
#print(type(project_output))
project_output_json = json.loads(project_output)
#print(type(project_output_json))
print(project_output_json)
#print(project_output_json[u'retentionDays'])
if project_output_json[u'retentionDays']<=30:
    print(" Activity Log Retention is set as per log retention Policy")
else:
    print("Not as per policy")