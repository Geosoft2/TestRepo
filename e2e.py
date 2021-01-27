import requests
import json
import time
import sys
#import testjob.json

res = requests.get("http://0.0.0.0:8080/api/v1/jobs")
#print(res)
#print(res.text)
   # requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob.json, headers={"Content-Type": "application/json"})
    
    
testjob = {
  "title": "Example Title",
  "description": "Example Description",
  "process": {
    "process_graph": {
      "loadcollection1": {
        "process_id": "load_collection",
        "arguments": {
          "timeframe" : ["01-12-1981 00:00:00","30-12-1981 00:00:00","%d-%m-%Y %H:%M:%S"],
          "DataType": "SST"
        }
        },
        "SST": {
        "process_id": "mean_sst",
        "arguments": {
          "data":{
              "from_node": "loadcollection1"
          },
          "timeframe":["1981-12-01","1981-12-17"],
          "bbox":[-999,-999,-999,-999]
          }
        },
        "save":{
            "process_id": "save_result",
            "arguments":{
                "SaveData":{
                    "from_node":"SST"
                },
                "Format": "netcdf"
            }
        }
      }
      }
    }   

# print(testjob)
print("\n JSON AN FRONTEND ÜBERGEBEN \n")
x = requests.post("http://0.0.0.0:8080/api/v1/jobs", json=testjob, headers={"Content-Type": "application/json"})
print(x)

#res_1 = requests.get("http://0.0.0.0:8080/api/v1/jobs")
#print(res_1.text)

print("\n ID DES JOBS ERFRAGEN \n")

j = requests.get("http://0.0.0.0:8080/api/v1/jobs")
rjson = j.json()
job_id = rjson['jobs'][-1]['id']
#print(rjson)
print(job_id)

print("\n DEN JOB AUSFÜHREN ÜBER EINE POST ANFRAGE AN DEN RESULTS ENDPOINT DES JOBS. \n")

requests.post("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" , json=None, headers={"Content-Type": "application/json"})

print("\n 5 MINUTEN WAREN BIS DER SERVER BEREIT IST \n")
time.sleep(300)

print("\n JSON, dass leer ist: \n")
print(requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json())

#counter = 0
'''
def callCheckData():
   checkData();

def checkData():
  global counter
  data = requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json()
  if (counter === 3):
      sys.exit('unable to download data within 15 Minutes')
  elif(data['level'] == 'error'):
      print ("Daten noch nicht geladen")
      counter += 1
      time.sleep(300)
      callCheckData()
  else: 
      print ("Datensatz geladen")
      print(requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results" ).json())
      #res = requests.get("http://localhost/api/v1/jobs/" + job_id + "/results" )
      #dl = res.json()["assets"]
      #print(dl)

print("\n WARTEN BIS DATENSATZ GELADEN IST: \n")
checkData()
   

#print(" \n GET Anfrage an Frontend /jobRunning Endpoint \n ")

#x2 = requests.get("http://0.0.0.0:8080/jobRunning/" + job_id)
#print(x2.text)

#print(" \n Post an Database /doJob Endpoint \n ")

#while True:
 # try:
  #  x3 = requests.post("http://0.0.0.0:8080/doJob/" + job_id)
   # print(x3.text)
 # except requests.exceptions.RequestException as e:
  #  pass
#print(" \n Warte bis Job Fertig ist.. \n")
#while True:
 
#   time.sleep(300) 
 #   try:
  #    requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results")
   #   break
  #  except Error:
   #     print ("not ready, trying again in one minute")
         
#res_2 = requests.get("http://0.0.0.0:8080/api/v1/jobs/" + job_id + "/results").json()
#d1 = res_2.json()
#print(d1)
#print(res_2)
'''
