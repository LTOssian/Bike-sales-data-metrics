# import subprocess
# import time


# def wait_for_postgres(host, max_retries=5, delay_seconds=5):
#     retries = 0

#     while retries < max_retries:
#         try:
#             result = subprocess.run(
#                 ["pg_isready", "-h", host], check=True, capture_output=True, text=True
#             )
#             if "accepting connections" in result.stdout:
#                 print("Successfully connected to Postgres")
#                 return True
#         except subprocess.CalledProcessError as e:
#             print(f"Error connecting to Postgres: {e}")
#             retries += 1
#             print(f"Retrying in {delay_seconds} secondes. Attempt: {retries}/{max_retries}")
#             time.sleep(delay_seconds)
#         print("Max retries reached. Exiting")
#         return False


# if not wait_for_postgres(host="bike_postgres"):
#     exit(1)

# print("Starting Bike sales batch processing...")

# bike_db_config = {
#     "dbname": "bike_db",
#     "user": "postgres",
#     "password": "secret",
#     "host": "bike_postgres"
# }

# bike_destination_config = {
#     "dbname": "bike_db",
#     "user": "postgres",
#     "password": "secret",
#     "host": "bike_destination"
# }

# dump_command = [
#     "pg_dump",
#     "-h", bike_db_config["host"],
#     "-U", bike_db_config["user"],
#     "-d", bike_db_config["dbname"],
#     "-f", "data_dump.sql",
#     "-w"
# ]

# subprocess_env = dict(PGPASSWORD=bike_db_config["password"])

# subprocess.run(dump_command, env=subprocess_env, check=True)

# load_command = [
#     "psql",
#     "-h", bike_destination_config["host"],
#     "-U", bike_destination_config["user"],
#     "-d", bike_destination_config["dbname"],
#     "-a", "-f", "data_dump.sql"
# ]

# subprocess_env = dict(PGPASSWORD=bike_destination_config["password"])

# subprocess.run(load_command, env=subprocess_env, check=True)

# print("Ending bike sales batch processing...")
