"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: 2A202600647
Name: Nguyen Van Chung

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = "raw_data.json"
OUTPUT_FILE = "processed_data.csv"


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.
    Returns:
        list: Danh sach cac records
    """
    print(f"Extracting data from {file_path}...")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"Extract complete. {len(data)} records extracted.")
        return data

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file.")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac validation:
       - Price phai > 0
       - Category khong duoc rong

    Returns:
        list: Danh sach cac records hop le
    """
    valid_records = []
    dropped_records = []

    for record in data:
        price = record.get("price", 0)
        category = record.get("category")

        # Check price
        if price <= 0:
            dropped_records.append({
                "id": record.get("id"),
                "reason": "Price <= 0"
            })
            continue

        # Check category
        if not category:
            dropped_records.append({
                "id": record.get("id"),
                "reason": "Missing Category"
            })
            continue

        valid_records.append(record)

    error_count = len(dropped_records)

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    print(f"Validation summary: {len(valid_records)} kept, {error_count} dropped.")

    if dropped_records:
        print(f"Errors found: {dropped_records}")

    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Yeu cau:
       - discounted_price = price * 0.9
       - category thanh Title Case
       - processed_at = timestamp hien tai

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    df = pd.DataFrame(data)

    if df.empty:
        print("Transform skipped. No valid records.")
        return df

    # Logic 1: Discount
    df["discounted_price"] = df["price"] * 0.9

    # Logic 2: Formatting
    df["category"] = df["category"].str.title()

    # Logic 3: Metadata / Observability
    df["processed_at"] = datetime.datetime.now().isoformat()

    print(f"Transform complete. {len(df)} records processed.")

    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
    print(f"Successfully loaded {len(df)} records to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")