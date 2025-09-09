import csv
import json

def calculate_bonus(department, experience, salary):
    if department == 'Finance' and experience > 5:
        return salary * 0.10
    return 0

def process_employee_data():
    employees = []

    # Read CSV file
    with open('employee_data.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            employee = {
                "id": int(row["id"]),
                "name": row["name"],
                "experience": int(row["experience"]),
                "salary": int(row["salary"]),
                "department": row["department"]
            }

            # Checking bonus
            employee["bonus"] = calculate_bonus(
                employee["department"],
                employee["experience"],
                employee["salary"]
            )

            employees.append(employee)

    # Write to JSON file
    with open('employee_data_with_bonus', mode='w') as jsonfile:
        json.dump(employees, jsonfile, indent=2)

    print("Employee data processed and bonuses calculated successfully.")

if __name__ == "__main__":
    process_employee_data()
