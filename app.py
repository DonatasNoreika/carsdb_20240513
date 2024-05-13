import sqlite3

conn = sqlite3.connect("cars.db")
c = conn.cursor()


while True:
    choice = int(input("1 - search cars\n2 - insert car\n3 - exit\n"))
    match choice:
        case 1:
            make = input("Make: ")
            model = input("Model: ")
            color = input("Color: ")
            year_from = int(input("Year from: "))
            year_to = int(input("Year to: "))
            price_from = float(input("Price from: "))
            price_to = float(input("Price to: "))
            query = """SELECT * FROM car
                    WHERE make LIKE ?
                    AND model LIKE ?
                    AND color LIKE ?
                    AND year BETWEEN ? AND ?
                    AND price BETWEEN ? AND ?
            """
            with conn:
                c.execute(query, [make, model, color, year_from, year_to, price_from, price_to])
                for car in c.fetchall():
                    print(car)
        case 2:
            print("Enter a car:")
            make = input("Make: ")
            model = input("Model: ")
            color = input("Color: ")
            year = int(input("Year: "))
            price = float(input("Price: "))
            with conn:
                c.execute("INSERT INTO car VALUES (?, ?, ?, ?, ?)", [make, model, color, year, price])
            print("Your car inserted to database!")
        case 3:
            print("Bye")
            break


