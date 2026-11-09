import os
import requests
from dotenv import load_dotenv #hides my key but also suggested so I can even
#run an API in VS Code

#Also hides my key!
load_dotenv()

# Code to retrieve the API
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

print("GREETINGS SPACE RANGER!, THE WEATHER ON MARS IS....WAIT...") #added cute dialog to the user getting space information lol
print()
cadet_name = input("WHATS YOUR NAME SPACE RANGER?: ")

#Function 1 
def fetch_mars_weather(api_key):
  # NASA InSight Mars Weather endpoint
  url = "https://api.nasa.gov/insight_weather/"
  params = {"api_key": api_key, "feedtype": "json", "ver": "1.0"}

  print()
  print()
  print(f"Now that we're formally introduced, {cadet_name}\n" "Head to the Ship and Analyze the Weather Reports Cadet")
  response = requests.get(url, params=params)

  #Booleans 
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Data not received. Status code: {response.status_code}")
    return None


if __name__ == "__main__":
  weather_data = fetch_mars_weather(NASA_API_KEY)

if weather_data:
  
  sol_keys = weather_data.get("sol_keys", [])
  
  print(f"\nHELLO {cadet_name}, IM TOKKI YOUR BUILT IN SHIP ASSISTANT\n")
  print("HERE ON YOUR COMMAND I WILL SHOW YOU THE REPORTS FOR MARS SOL\n")
  print("WHAT'S SOL? WELL SOLAR DAYS OF COURSE, EARTH DAY IS WORTH 24 HRS")
  print("HOWEVER, ON MARS A DAY IS 24 HRS 39 MINS & 35 SECS\n")
  
  
  user_reply = input(f"READY TO RECEIVE THE INFO CADET {cadet_name}? (Type Y or N): ").strip().upper()
  
  
  is_ready = (user_reply == "Y")
  
 
  if is_ready:
    print(f"\nAccessing weather for martian {len(sol_keys)} Sols...\n")
    
    # Loops th martiam day or sol
    for sol in sol_keys:
      print(f"--- Martian Sol (Day) {sol} ---")
      sol_data = weather_data.get(sol, {})

      # for data/metr
      avg_temp = sol_data.get("AT", {}).get("av", "N/A")
      avg_wind = sol_data.get("HWS", {}).get("av", "N/A")
      pressure = sol_data.get("PRE", {}).get("av", "N/A")

      print(f"  Average Temperature : {avg_temp} °C")
      print(f"  Average Wind Speed  : {avg_wind} m/s")
      print(f"  Atmospheric Pressure: {pressure} Pa\n")
      
  else:
    print(f"\nUnderstood, cadet {cadet_name}. Waiting until you want the reports.")

else:
  print("SORRY CADET, NO WEATHER REPORTS FOUND.")