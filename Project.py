"""
Project: Personal Finance & Investment Tracker
Course: COP 1500
Group Members: Cesar Maddalon & Javier Rosario
Date: 07 April 2026
Description: A multi-functional tool for basic arithmetic and investment tracking.
"""

import os
import sys


# =============================================================================
# CLASS DEFINITIONS (Object-Oriented Programming)
# =============================================================================

class Asset:

    def __init__(self, name, asset_type, purchase_price, quantity):
        self.name = name
        self.asset_type = asset_type  # e.g., 'Stock', 'Crypto', 'Gold'
        self.purchase_price = float(purchase_price)
        self.quantity = float(quantity)

    def calculate_value(self):
        return self.purchase_price * self.quantity

    def __str__(self):
        return f"{self.name} ({self.asset_type}) | Qty: {self.quantity} | Price: ${self.purchase_price:,.2f}"


class Portfolio:

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.assets = []  # List data structure to store Asset objects
        self.file_path = "portfolio_data.txt"

    def add_asset(self, asset):
        self.assets.append(asset)
        print(f"\n[SUCCESS] {asset.name} has been added to your portfolio.")

    def get_total_portfolio_value(self):
        total = 0
        for asset in self.assets:
            total += asset.calculate_value()
        return total

    def save_to_disk(self):
        try:
            with open(self.file_path, "w") as f:
                for a in self.assets:
                    f.write(f"{a.name}|{a.asset_type}|{a.purchase_price}|{a.quantity}\n")
            print(f"\n[INFO] Portfolio saved to {self.file_path}")
        except IOError as e:
            print(f"\n[ERROR] Could not save file: {e}")

    def load_from_disk(self):
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        name, a_type, price, qty = parts
                        self.assets.append(Asset(name, a_type, price, qty))
            print(f"\n[INFO] Loaded {len(self.assets)} assets from storage.")
        except (ValueError, IOError) as e:
            print(f"\n[ERROR] Failed to load portfolio: {e}")