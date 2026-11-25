import csv

data_rows = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, start=1):
            rows_attempted += 1

            # Hint 2: Separate guard for extra columns before try/except
            if None in row:
                skipped_rows.append(f"  Row {row_num}: extra column detected — skipped")
                continue

            try:
                name = row["name"]
                category = row["category"]
                raw_amount = row["amount"]

                # Guard against None (when a row is shorter than the header)
                if raw_amount is None:
                    raise ValueError("could not convert None to float")

                amount = float(raw_amount)

                # Also reject rows missing name or category values
                if not name or not name.strip() or not category or not category.strip():
                    raise ValueError("missing name or category")

                data_rows.append({
                    "name": name.strip(),
                    "category": category.strip(),
                    "amount": amount,
                })

            except ValueError:
                skipped_rows.append(
                    f"  Row {row_num}: ValueError — could not convert {raw_amount!r} to float"
                )
            except KeyError as e:
                skipped_rows.append(f"  Row {row_num}: KeyError — missing column {e}")

except FileNotFoundError:
    print('Error: "messy_data.csv" was not found. Please check the file path and try again.')
    raise SystemExit(1)

# Print the final summary report
print("=== CSV Report ===")
print(f"Rows attempted: {rows_attempted:>3}")
print(f"Rows parsed:    {len(data_rows):>3}")
print(f"Rows skipped:   {len(skipped_rows):>3}")

print("\nSkipped rows:")
for entry in skipped_rows:
    print(entry)

print("\nClean data:")
for item in data_rows:
    print(f"  {item['name']} | {item['category']} | ${item['amount']:.2f}")