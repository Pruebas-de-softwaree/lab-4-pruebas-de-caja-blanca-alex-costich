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
    print("\nActividad 2: Cobertura de Decisiones ---")

    # D1
    students_D1 = [{'name': 'Jorge', 'grades': None}]
    print("Caso D1:", process_grades(students_D1))

    # D2
    students_D2 = [{'name': 'Ana', 'grades': [80, 90, 85]}]
    print("Caso D2:", process_grades(students_D2))

    # D3
    students_D3 = [{'name': 'Luis', 'grades': [60, 55, 65]}]
    print("Caso D3:", process_grades(students_D3))

    # D4
    students_D4 = [{'name': 'Marta', 'grades': [40, 45, 50]}]
    print("Caso D4:", process_grades(students_D4))
