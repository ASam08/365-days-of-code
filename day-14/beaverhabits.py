import os
import dotenv
import requests

def get_habit():
    dotenv.load_dotenv()
    BEAVERHABITS_URL = os.getenv("BEAVERHABITS_URL")
    BEAVERHABITS_USERNAME = os.getenv("BEAVERHABITS_USERNAME")
    BEAVERHABITS_PASSWORD = os.getenv("BEAVERHABITS_PASSWORD")

    auth_token = get_auth(BEAVERHABITS_URL, BEAVERHABITS_USERNAME, BEAVERHABITS_PASSWORD)

    all_habits = get_habits(BEAVERHABITS_URL, auth_token)

    specific_habit = choose_habit(all_habits)
    
    print(f"Habit ID: {specific_habit['id']}")
    return specific_habit['id']

def complete_habit(habit_id,complete_date):
    dotenv.load_dotenv()
    BEAVERHABITS_URL = os.getenv("BEAVERHABITS_URL")
    BEAVERHABITS_USERNAME = os.getenv("BEAVERHABITS_USERNAME")
    BEAVERHABITS_PASSWORD = os.getenv("BEAVERHABITS_PASSWORD")

    auth_token = get_auth(BEAVERHABITS_URL, BEAVERHABITS_USERNAME, BEAVERHABITS_PASSWORD)

    update_habit(habit_id, auth_token, complete_date, BEAVERHABITS_URL)
    print("Habit marked as complete for today.")
    
def get_auth(BEAVERHABITS_URL, BEAVERHABITS_USERNAME, BEAVERHABITS_PASSWORD):
    headers = {'content-type': 'application/x-www-form-urlencoded', 'accept': 'application/json'}
    data={
        'grant_type': 'password',
        'username': BEAVERHABITS_USERNAME,
        'password': BEAVERHABITS_PASSWORD
    }
    url = f"{BEAVERHABITS_URL}/auth/login"
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    
    return response.json()['access_token']

def get_habits(BEAVERHABITS_URL, auth_token):
    headers = {'accept': 'application/json', 'Authorization': f'Bearer {auth_token}'}
    url = f"{BEAVERHABITS_URL}/api/v1/habits"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
   
def choose_habit(all_habits):
    print("Available habits:")
    for index, habit in enumerate(all_habits):
        print(f"{index + 1}. {habit['name']}")
    
    choice = int(input("Select a habit by number: ")) - 1
    selected_habit = all_habits[choice]
    print(f"You selected: {selected_habit['name']}")
    return selected_habit

def update_habit(habit_id, auth_token, complete_date, BEAVERHABITS_URL):
    headers = {'content-type': 'application/json', 'Authorization': f'Bearer {auth_token}'}
    url = f"{BEAVERHABITS_URL}/api/v1/habits/{habit_id}/completions"
    data = {'date_fmt': '%d-%m-%Y', 'done': True, 'date': complete_date.strftime('%d-%m-%Y')}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

