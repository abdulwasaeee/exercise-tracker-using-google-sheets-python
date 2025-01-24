import datetime
import os
APIKEY="-----"
APIID="-----"

head={
    "x-app-id":os.environ['APIID'],
    "x-app-key":APIKEY,
    "x-remote-user-id":"0",
    "Authorization":"-----"
}

import requests
p={
    "query":input("what did you do?")
}
response=requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",headers=head,json=p)
data=response.json()['exercises']

exercise=data[0]["user_input"]
duration=data[0]["duration_min"]
calories=data[0]["nf_calories"]

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%I:%M:%S %p")

p2={
    "workout":{"date":date,
"time":time,
"exercise":exercise,
"duration":duration,
"calories":calories
             }

}
response2=requests.post(url="https://api.sheety.co/fffaae6390b12edf7c86a266b19f7f2a/myWorkoutVer2/workouts",json=p2,auth=(
      "wasae",
      "abdulwasaeee",
  ))
print(response2.text)
