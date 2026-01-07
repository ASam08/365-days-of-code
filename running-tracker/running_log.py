import sqlite3
from datetime import datetime
import logging

def main():
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='running_log.log',
                        filemode='a') 
    global logger
    logger = logging.getLogger(__name__)
    
    logging.debug('Logging is set up.')

    # Welcome message
    print(f"Welcome to your running log for 2026!\n")

    # Connect to the SQLite database
    with sqlite3.connect('running_log.db') as conn:
        cursor = conn.cursor()

        first_time_setup(conn, cursor)

        get_stats(conn, cursor)

        main_app_loop(conn, cursor)

def first_time_setup(conn, cursor):
    version = float("0.1")
    try:
        get_version(cursor,version)
    except sqlite3.OperationalError:
        cursor.execute('CREATE TABLE version (version REAL NOT NULL)')
        cursor.execute('INSERT INTO version (version) VALUES (?)', (version,))
        conn.commit()
        logging.info("Created version table.")

    try:
        get_totals(cursor)
    except sqlite3.OperationalError:
        create_log_table(cursor)

def main_app_loop(conn, cursor):
    while True:
        print("What would you like to do?\n")
        print("1. View total distance run this year")
        print("2. Add a new run")
        print("3. Set a new running goal")
        print("4. Quit\n")
        choice = input("Enter the number of your choice: ")
        print("\n")

        if choice == '1':
            get_stats(conn, cursor)
            input("Press Enter to continue...")
        elif choice == '2':
            add_run(conn, cursor)
        elif choice == '3':
            set_goal_per_day(conn, cursor)
            input("Press Enter to continue...")
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.\n")

def add_run(conn, cursor):
    date_str = input("\nEnter the date of the run (YYYY-MM-DD) or leave blank for today: ")
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    distance_km: float = float(input("Enter the distance run in km's: "))

    cursor.execute("INSERT INTO running_log (date, distance_km) VALUES (?, ?)", (date_str, distance_km))
    conn.commit()

    print(f'\nAdded run on {date_str} of {distance_km} km\'s to the database.\n')

def get_version(cursor, version):
    cursor.execute('SELECT version FROM version')
    result = cursor.fetchone()
    if result:
        db_version = result[0]
        if db_version != version:
            print(f"Current version {db_version} does not match expected version {version}. Consider updating.\n")
            logger.warning(f"Version mismatch: {db_version} != {version}")
        else:
            logger.debug(f"Current version {db_version} is up to date.\n")
    else:
        cursor.execute('INSERT INTO version (version) VALUES (?)', (version,))
        logger.info("Set database version.\n")

def get_stats(conn, cursor):
    total_distance = get_totals(cursor)
    print(f"Total distance run this year: {total_distance:.2f} km's")

    days_gone = get_days_this_year()
    print(f"Days gone this year: {days_gone}")
    average_distance = total_distance / days_gone if days_gone > 0 else 0
    print(f"Average distance per day: {average_distance:.2f} km's\n")
    goal_distance = get_goal_distance(conn, cursor, days_gone)
    print(f"Your goal distance so far this year is: {goal_distance:.2f} km's")

    if total_distance >= goal_distance:
        print("Congratulations! You are on track with your running goal!\n")
    else:
        print(f"Keep going! You need to run {goal_distance - total_distance:.2f} today to get back on track\n")

def create_log_table(cursor):
    cursor.execute('''
        CREATE TABLE running_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            distance_km REAL NOT NULL
        )
    ''')
    logger.info("Created running_log table.")

def get_totals(cursor):
    cursor.execute('SELECT SUM(distance_km) FROM running_log')
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

def get_days_this_year():
    today = datetime.now()
    start_of_year = datetime(today.year, 1, 1)
    delta = today - start_of_year
    return delta.days + 1  # Including today

def get_goal_distance(conn, cursor, days_gone):
    try:
        cursor.execute('SELECT goal_per_day FROM running_goals WHERE current is TRUE')
        result = cursor.fetchone()
        if result:
            goal_per_day = result[0]
        else:
            print("No current goal found, set a new goal.")
            set_goal_per_day(conn,cursor)
            cursor.execute('SELECT goal_per_day FROM running_goals WHERE current is TRUE') 
            goal_per_day = cursor.fetchone()[0]
    except sqlite3.OperationalError:
        cursor.execute('''
            CREATE TABLE running_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal_per_day REAL NOT NULL,
                current BOOLEAN NOT NULL
            )
        ''')
        logger.info("Created running_goals table.")
        print("No current goal found, set a new goal.")
        set_goal_per_day(conn,cursor)
        cursor.execute('SELECT goal_per_day FROM running_goals WHERE current is TRUE') 
        goal_per_day = cursor.fetchone()[0]
    
    return goal_per_day * days_gone

def set_goal_per_day(conn,cursor):
    now = datetime.now()
    today = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year, 12, 31)
    total_days_this_year = end_of_year - today
    total_days_this_year = total_days_this_year.days + 1  # Including today

    print("Set your running goal per:\n1. Day\n2. Week\n3. Month\n4. Year")
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        goal_per_day = float(input("Enter your running goal per day in km's: "))
    elif choice == '2':
        weekly_goal = float(input("Enter your running goal per week in km's: "))
        goal_per_day = weekly_goal / 7
    elif choice == '3':
        monthly_goal = float(input("Enter your running goal per month in km's: "))
        goal_per_day = monthly_goal * 12
        goal_per_day /= total_days_this_year
    elif choice == '4':
        yearly_goal = float(input("Enter your running goal per year in km's: "))
        goal_per_day = yearly_goal / total_days_this_year
    else:
        print("Invalid choice. Please select 1, 2 or 3.")
    
    cursor.execute('UPDATE running_goals SET current = FALSE')
    cursor.execute('INSERT INTO running_goals (goal_per_day, current) VALUES (?, TRUE)', (goal_per_day,))
    conn.commit()
    unit = 'km' if goal_per_day == 1 else "km's"
    print(f"Set new daily goal of {goal_per_day:.2f} {unit}.")

    
if __name__ == "__main__":
    main()
