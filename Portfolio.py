print("Hello, World!")
if __name__ == "__main__":
    print("hello, Herbert")
if __name__ == "__main__":
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (9 / 5) * celsius + 32
        return fahrenheit
    temperature_celsius = 38.4
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print("Temperature in Celsius:", temperature_celsius, "C")
print("Equivalent Temperature in Fahrenheit:", temperature_fahrenheit, "F")
if __name__ == "__main__":
    matches_played = 609
    times_batted = 1014
    times_not_out = 162
    runs_scored = 48426
    innings_completed = times_batted - times_not_out
    batting_average = runs_scored / innings_completed
    print("Matches Played:", matches_played)
    print("Innings Completed:", innings_completed)
    print("Runs Scored:", runs_scored)
    print("Batting Average:", batting_average)
if __name__ == "__main__":
    students = [113, 175, 12]
    students_per_group = 24
    for num_students in students:
        full_groups = num_students // students_per_group
        remaining_students = num_students % students_per_group
        print(f"For {num_students} students:")
        print("Full groups:", full_groups)
        print("Remaining students in smaller group:", remaining_students)
        print()