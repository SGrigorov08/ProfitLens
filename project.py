import math
import csv

from tabulate import tabulate


def revenue(price, units):
    if price > 0 and units >= 0:
        return price * units
    raise ValueError("Enter a valid price and sold units")


def total_cost(units, cpu, fixed):
    if units >= 0 and cpu >= 0 and fixed >= 0:
        return units * cpu + fixed
    raise ValueError("Enter a positive numbers")


def profit(price, units, cpu, fixed):
    return revenue(price, units) - total_cost(units, cpu, fixed)


def margin(price, units, cpu, fixed):
    if revenue(price, units) != 0:
        margin = profit(price, units, cpu, fixed) / revenue(price, units) * 100
        return f"{margin:.2f}%"
    return "N/A"


def break_even(price, cpu, fixed):
    if price > cpu and fixed != 0:
        break_even = fixed / (price - cpu)
        return math.ceil(break_even)
    elif price >= cpu and fixed == 0:
        return 0
    return "N/A"


def main():
    try:
        price = float(input("Price per unit: "))
        units = int(input("Sold units: "))
        cpu = float(input("Cost for unit: "))
        fixed = float(input("Fixed costs: "))
    except ValueError:
        print("Enter valid numbers")
        return
    try:
        rev = revenue(price, units)
        cost = total_cost(units, cpu, fixed)
        prof = profit(price, units, cpu, fixed)
        marg = margin(price, units, cpu, fixed)
        b_even = break_even(price, cpu, fixed)
    except ValueError:
        print("Enter positive numbers")
        return

    data = {
        "Revenue": f"{rev:.2f}$",
        "Total Cost": f"{cost:.2f}$",
        "Profit": f"{prof:.2f}$",
        "Margin": f"{marg}",
        "Break-even": f"{b_even}",
    }

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=":")
        writer.writerow(["Metric", "Value"])
        for key, value in data.items():
            writer.writerow([key, value])
        print(tabulate(data.items() , headers=["Metric", "Value"], tablefmt="grid"))


if __name__ == "__main__":
    main()
