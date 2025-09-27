def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if grades == None:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        # counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    print("\n--- Actividad 3: Cobertura de Caminos ---")

    students_C1 = [{'name': 'Jorge', 'grades': None}]
    print("Camino 1:", process_grades(students_C1))

    students_C2 = [{'name': 'Ana', 'grades': [90, 95, 85]}]
    print("Camino 2:", process_grades(students_C2))

    students_C3 = [{'name': 'Luis', 'grades': [60, 55, 65]}]
    print("Camino 3:", process_grades(students_C3))

    students_C4 = [{'name': 'Marta', 'grades': [40, 30, 35]}]
    print("Camino 4:", process_grades(students_C4))