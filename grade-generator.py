import csv

def validate_grade(grade_input):
    """Check if the grade is a number between 0 and 100."""
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return True, grade
        else:
            print("Error: Grade must be between 0 and 100.")
            return False, None
    except ValueError:
        print("Error: Grade must be a valid number.")
    return False, None

######################################
def validate_category(category_input):
    """Check if the category is FA or SA (should be case-insensitive) """
    category = category_input.strip().upper()
    if category in ["FA", "SA"]:
        return True, category
    else:
        print("Error: Category must be 'FA' (Formative) or 'SA' (Summative).")
        return False, None

#####################################
def validate_weight(weight_input):
    """Check if the weight is a positive number."""
    try:
        weight = float(weight_input)
        if weight > 0:
            return True, weight
        else:
            print("Error: Weight must be a positive number.")
            return False, None
    except ValueError:
            print("Error: Weight must be a valid number.")
            return False, None

#####################################
def collect_assignment_data():
    """Collecta all the assignment data from the user."""
    assignment = []

    print("=" * 60)
    print("Grade Generator")
    print("Intoduction to python programming and databases")
    print("=" * 60)
    print()

    while True:
        print("\n--- Enter assignment details ---")

        #Get assignment name
        name = input("Assignment name: ").strip()
        if not name:
            print("Error: Assignment name cannot be empty.")
            continue

        #Get and validate category
        while True:
            category_input = input("Category (FA for Formative, SA for Summative): ")
            valid, category = validate_category(category_input)
            if valid:
               break

        #Get and validate grade
        while True:
            grade_input = input("Grade obtained (0-100): ")
            valid, grade = validate_grade(grade_input)
            if valid:
                break

        while True:
           weight_input = input("Weight: ")
           valid, weight = validate_weight(weight_input)
           if valid:
             break


        #Store the assignment
        assignment.append({
            'name': name,
            'category': category,
            'grade': grade,
            'weight': weight,
        })

        print(f"\n Assignment '{name}' added successfully.")

        #Prompt user if they would like to add another assignment
        while True:
            continue_input = input("\nAdd another assignment? (y/n): " ).strip().lower()
            if continue_input in ['y', 'n']:
                break
            print("Please enter 'y' for yes or 'n' for no.")

        if continue_input == 'n':
            break

    return assignment

################################
def calculate_grades(assignment):
    """Calculate weigted grades, totals, GPA, and pass/fail status."""   
    total_fa = 0
    total_sa = 0
    total_fa_weight = 0
    total_sa_weight = 0

    #Calculate weighted grades and totals
    for assignment in assignment:
        weighted_grade = (assignment['grade'] / 100) * assignment['weight']
        assignment['weighted_grade'] = weighted_grade

        if assignment['category'] == 'FA':
            total_fa += weighted_grade
            total_fa_weight += assignment['weight']

    #Calculate final grade and GPA
        total_grade = total_fa + total_sa
    gpa = (total_grade / 100) * 5.0

    # Determine pass/fail
    fa_threshold = total_fa_weight * 0.5
    sa_threshold = total_sa_weight * 0.5

    passes_fa = total_fa >= fa_threshold if total_fa_weight > 0 else True
    passes_sa = total_sa >= sa_threshold if total_sa_weight > 0 else True
    passes_overall = passes_fa and passes_sa

    return {
        'total_fa': total_fa,
        'total_sa': total_sa,
        'total_fa_weight': total_fa_weight,
        'total_sa_weight': total_sa_weight,
        'total_grade': total_grade,
        'gpa': gpa,
        'passes_fa': passes_fa,
        'passes_sa': passes_sa,
        'passes_overall': passes_overall,
        'fa_threshold': fa_threshold,
        'sa_threshold': sa_threshold
    }

#######################################
def print_summary(assignments, results):
    """Print a detailed summary of all assignments and final results."""
    print("\n" + "=" * 60)
    print("GRADE SUMMARY")
    print("=" * 60)

    # Print individual assignments
    print("\nAssignments:")
    print("-" * 60)
    for i, assignment in enumerate(assignments, 1):
        print(f"{i}. {assignment['name']}")
        print(f"   Category: {assignment['category']}")
        print(f"   Grade: {assignment['grade']:.2f}/100")
        print(f"   Weight: {assignment['weight']}")
        print(f"   Weighted Grade: {assignment['weighted_grade']:.2f}")
        print()

    # Print category totals
    print("-" * 60)
    print("CATEGORY TOTALS:")
    print(f"Total Formative (FA): {results['total_fa']:.2f} / {results['total_fa_weight']:.2f}")
    print(f"  Required to pass: {results['fa_threshold']:.2f}")
    print(f"  Status: {'PASS ' if results['passes_fa'] else 'FAIL '}")
    print()
    print(f"Total Summative (SA): {results['total_sa']:.2f} / {results['total_sa_weight']:.2f}")
    print(f"  Required to pass: {results['sa_threshold']:.2f}")
    print(f"  Status: {'PASS ' if results['passes_sa'] else 'FAIL '}")

    # Print final results
    print("-" * 60)
    print("FINAL RESULTS:")
    print(f"Total Grade: {results['total_grade']:.2f}/100")
    print(f"GPA: {results['gpa']:.2f}/5.0")
    print(f"\nOverall Status: {'PASS ✓' if results['passes_overall'] else 'FAIL '}")

    if not results['passes_overall']:
        print("\nNote: You must score at least 50% in BOTH categories to pass.")

    print("=" * 60)

######################################################
def export_to_csv(assignments, filename='grades.csv'):
    """Export all assignment data to a CSV file."""
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write header
            writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])

            # Write assignment data
            for assignment in assignments:
                writer.writerow([
                    assignment['name'],
                    assignment['category'],
                    assignment['grade'],
                    assignment['weight']
                ])

        print(f"\n Data successfully exported to '{filename}'")
    except Exception as e:
        print(f"\n Error exporting to CSV: {e}")

#########################################
def main():
    """Main function to run the grade generator."""
    # Collect assignment data
    assignments = collect_assignment_data()

    if not assignments:
        print("\nNo assignments entered. Exiting.")
        return

    # Calculate grades
    results = calculate_grades(assignments)

    # Print summary
    print_summary(assignments, results)

    # Export to CSV
    export_to_csv(assignments)

if __name__ == "__main__":
    main()