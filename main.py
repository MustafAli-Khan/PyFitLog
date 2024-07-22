from datetime import datetime
import requests
import os

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
app_id = os.environ['APP_ID']
api_key =os.environ['API_KEY']

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 176.784
AGE = 22

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ['SHEET_ENDPOINT']

exercise_text = input("Tell me which exercises you did: ")




headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}



response = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }


sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      username,
      password,
  )
)
print(sheet_response.text)























