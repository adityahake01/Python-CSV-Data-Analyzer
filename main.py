
import csv


def calculate_revenue(quantity, price):
    return quantity * price


def analyze_sales(filename):
    print("Starting sales analysis...")

    total_revenue = 0
    total_quantity = 0
    product_count = 0
    invalid_rows = 0

    highest_revenue = 0
    highest_product = ""

    try:
        
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            expected_header = ["Product", "Quantity", "Price"]
            actual_header = next(reader, None)

            if actual_header != expected_header:
                print("Error: Invalid CSV header.")
                print("Expected:", expected_header)
                print("Found:", actual_header)
                return


            for row in reader:
                try:
                    product = row[0]
                    quantity = int(row[1])
                    price = int(row[2])

                    if not product.strip():
                        invalid_rows += 1
                        print("Skipping row: Empty product name.")
                        continue

                    if quantity < 0 or price < 0:
                        invalid_rows += 1
                        print("Skipping row: Negative values.")
                        continue

                except (ValueError, IndexError):
                    invalid_rows += 1
                    print("Skipping invalid row:", row)
                    continue

                revenue = calculate_revenue(quantity, price)

                total_revenue += revenue
                total_quantity += quantity
                product_count += 1

                if product_count == 1 or revenue > highest_revenue:
                    highest_revenue = revenue
                    highest_product = product

                print(product, "Revenue:", revenue)

    except FileNotFoundError:
        print("Error: File not found:", filename)
        return

    if product_count > 0:
        average_revenue = total_revenue / product_count
    else:
        average_revenue = 0

    
    print("\n" + "=" * 40)
    print("         SALES ANALYSIS REPORT")
    print("=" * 40)

    print(f"Total Revenue         : Rs. {total_revenue:,}")
    print(f"Total Quantity Sold   : {total_quantity}")
    print(f"Valid Product Records : {product_count}")
    print(f"Average Revenue       : Rs. {average_revenue:,.2f}")
    print(f"Top Revenue Product   : {highest_product}")
    print(f"Highest Revenue       : Rs. {highest_revenue:,}")
    print(f"Invalid Rows Skipped  : {invalid_rows}")

    print("=" * 40)



if __name__ == "__main__":
    analyze_sales("sales.csv")
