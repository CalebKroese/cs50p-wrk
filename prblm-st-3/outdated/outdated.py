def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Numeric format (M/D/YYYY)
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break

            # Month D, YYYY
            elif "," in date:
                month_day, y = date.split(",")
                y = int(y.strip())
                month_str, d = month_day.strip().split(" ")
                d = int(d)
                if month_str in months and 1 <= d <= 31:
                    m = months.index(month_str) + 1
                    print(f"{y:04}-{m:02}-{d:02}")
                    break

        except (ValueError, IndexError):
            pass  


if __name__ == "__main__":
    main()