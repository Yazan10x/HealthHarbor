import csv

from bson import ObjectId
from models.treatment import Treatment
from mongodb_api.health_harbor_db import HealthHarborDB

# Define the CSV file path
csv_file = 'mongodb_api/.db_migrations/treatments/treatments.csv'


def run() -> None:

    # Initialize an empty list to store the data
    data: list[dict] = []

    # Open the CSV file and read its contents
    with open(csv_file, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV
        for row in csv_reader:
            # Append the row as a dictionary to the data list
            data.append(row)

    treatments_coll = HealthHarborDB.treatments_coll

    # Print the data for verification
    for item in data:
        item.setdefault('_id', ObjectId())
        item = Treatment.from_json(item).to_json()
        print(item)
        treatments_coll.insert_one(item)


if __name__ == '__main__':
    if input("Are you sure {} (n/YeS): ") == "YeS":
        run()
        print("Completed")
    else:
        print("Terminated")
