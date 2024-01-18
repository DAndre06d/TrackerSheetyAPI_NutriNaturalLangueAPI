import requests
import os
from datetime import datetime

NUTRi_BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_HEADERS = {
    "x-app-id": os.environ.get("NUTRI_APP_ID"),
    "x-app-key": os.environ.get("NUTRI_API_KEY")
}
NUTRI_PARAMS = {
    "query": input("What exercise did you do? ")
}
SHEETY_URL = "https://api.sheety.co/5141383324b25af850fa0e3b5c652dcd/workoutTracker/workouts"
SHEETY_HEADERS = {
    "Authorization": f"Bearer {os.environ.get("BEARER_TOKEN")}"
}

response = requests.post(url=NUTRi_BASE_URL, json=NUTRI_PARAMS,headers=NUTRI_HEADERS)
data = response.json()
today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
hour = datetime.now().strftime("%H:%M:%S")
for exercise in data["exercises"]:
    sheety_params = {
        "workout": {
            "date": formatted_date,
            "time": hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response_sheety = requests.post(url=SHEETY_URL, json=sheety_params, headers=SHEETY_HEADERS)
    print(response_sheety)
