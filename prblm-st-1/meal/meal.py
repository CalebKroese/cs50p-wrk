def main():
    time = input("What time is it? ").strip()
    hours = convert(time)

    if 7 <= hours <= 8:
        print("Breakfast Time")
    elif 12 <= hours <= 13:
        print("Lunch Time")
    elif 18 <= hours <= 19:
        print("Dinner Time")
    else:
        print("Eat a snack I guess.")

def convert(time):
    # Split into hours and minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Convert to float (e.g., 7:30 -> 7.5)
    return hours + minutes / 60


if __name__ == "__main__":
    main()