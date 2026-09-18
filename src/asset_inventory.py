"""
Cybersecurity Asset Inventory System
Weekly Mini Project - 01

A menu-driven CLI tool that lets a security administrator add, search,
update, delete and display an organization's IT assets, and view a
security summary of the current inventory.
"""

import json
import os

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def load_assets():
    """Load the asset list from the JSON data file. Returns [] if missing."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read existing data file. Starting fresh.")
        return []


def save_assets(assets):
    """Persist the current asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input helpers / validation
# ---------------------------------------------------------------------------

def prompt_choice(label, options):
    """Prompt until the user enters a value from `options` (case-insensitive)."""
    options_display = "/".join(options)
    while True:
        value = input(f"{label} ({options_display}): ").strip()
        for opt in options:
            if value.lower() == opt.lower():
                return opt
        print(f"Invalid value. Please choose one of: {options_display}")


def prompt_nonempty(label):
    """Prompt until the user enters a non-empty string."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"{label} cannot be empty.")


def prompt_unique_asset_id(assets, label="Asset ID"):
    """Prompt for an Asset ID that does not already exist in the inventory."""
    while True:
        asset_id = prompt_nonempty(label)
        if find_asset(assets, asset_id) is not None:
            print(f"Asset ID '{asset_id}' already exists. Please enter a different ID.")
            continue
        return asset_id


def find_asset(assets, asset_id):
    """Return the asset dict matching asset_id (case-insensitive), or None."""
    for asset in assets:
        if asset["Asset ID"].lower() == asset_id.lower():
            return asset
    return None


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = prompt_unique_asset_id(assets)
    asset = {
        "Asset ID": asset_id,
        "Asset Name": prompt_nonempty("Asset Name"),
        "Asset Type": prompt_choice("Asset Type", ASSET_TYPES),
        "IP Address": prompt_nonempty("IP Address"),
        "Operating System": prompt_nonempty("Operating System"),
        "Department": prompt_nonempty("Owner/Department"),
        "Risk Level": prompt_choice("Risk Level", RISK_LEVELS),
        "Security Status": prompt_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"Asset '{asset_id}' added successfully.\n")


def add_multiple_assets(assets):
    """Bulk-entry mode matching the project's sample input flow."""
    while True:
        try:
            count = int(input("Enter number of assets: ").strip())
            if count > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        asset_id = prompt_unique_asset_id(assets)
        asset = {
            "Asset ID": asset_id,
            "Asset Name": prompt_nonempty("Asset Name"),
            "Asset Type": prompt_choice("Asset Type", ASSET_TYPES),
            "IP Address": prompt_nonempty("IP Address"),
            "Operating System": prompt_nonempty("Operating System"),
            "Department": prompt_nonempty("Department"),
            "Risk Level": prompt_choice("Risk Level", RISK_LEVELS),
            "Security Status": prompt_choice("Security Status", SECURITY_STATUSES),
        }
        assets.append(asset)

    save_assets(assets)
    print(f"\n{count} asset(s) added successfully.\n")


def search_asset(assets):
    print("\n--- Search Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to search")
    asset = find_asset(assets, asset_id)
    if asset:
        print("\nAsset found:")
        print_asset(asset)
    else:
        print(f"No asset found with ID '{asset_id}'.\n")


def update_asset(assets):
    print("\n--- Update Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to update")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"No asset found with ID '{asset_id}'.\n")
        return

    print("Leave a field blank to keep its current value.")
    print(f"Current Asset Name: {asset['Asset Name']}")
    new_name = input("New Asset Name: ").strip()
    if new_name:
        asset["Asset Name"] = new_name

    print(f"Current Asset Type: {asset['Asset Type']}")
    if input("Change Asset Type? (y/n): ").strip().lower() == "y":
        asset["Asset Type"] = prompt_choice("Asset Type", ASSET_TYPES)

    print(f"Current IP Address: {asset['IP Address']}")
    new_ip = input("New IP Address: ").strip()
    if new_ip:
        asset["IP Address"] = new_ip

    print(f"Current Operating System: {asset['Operating System']}")
    new_os = input("New Operating System: ").strip()
    if new_os:
        asset["Operating System"] = new_os

    print(f"Current Department: {asset['Department']}")
    new_dept = input("New Owner/Department: ").strip()
    if new_dept:
        asset["Department"] = new_dept

    print(f"Current Risk Level: {asset['Risk Level']}")
    if input("Change Risk Level? (y/n): ").strip().lower() == "y":
        asset["Risk Level"] = prompt_choice("Risk Level", RISK_LEVELS)

    print(f"Current Security Status: {asset['Security Status']}")
    if input("Change Security Status? (y/n): ").strip().lower() == "y":
        asset["Security Status"] = prompt_choice("Security Status", SECURITY_STATUSES)

    save_assets(assets)
    print(f"Asset '{asset_id}' updated successfully.\n")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    asset_id = prompt_nonempty("Enter Asset ID to delete")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"No asset found with ID '{asset_id}'.\n")
        return
    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"Asset '{asset_id}' deleted successfully.\n")
    else:
        print("Deletion cancelled.\n")


def print_asset(asset):
    print(f"Asset ID       : {asset['Asset ID']}")
    print(f"Asset Name     : {asset['Asset Name']}")
    print(f"Asset Type     : {asset['Asset Type']}")
    print(f"IP Address     : {asset['IP Address']}")
    print(f"OS             : {asset['Operating System']}")
    print(f"Department     : {asset['Department']}")
    print(f"Risk Level     : {asset['Risk Level']}")
    print(f"Status         : {asset['Security Status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets to display.")
    else:
        for i, asset in enumerate(assets):
            print_asset(asset)
            if i < len(assets) - 1:
                print("-----------------------------------------")
    print("=========================================")
    print(f"Total Assets      : {len(assets)}")
    print(f"Critical Assets   : {count_by(assets, 'Risk Level', 'Critical')}")
    print(f"High Risk Assets  : {count_by(assets, 'Risk Level', 'High')}")
    print(f"Medium Risk Assets: {count_by(assets, 'Risk Level', 'Medium')}")
    print(f"Vulnerable Assets : {count_by(assets, 'Security Status', 'Vulnerable')}")
    print("=========================================\n")


def count_by(assets, field, value):
    return sum(1 for a in assets if a[field] == value)


def security_summary(assets):
    print("\n--- Security Summary ---")
    if not assets:
        print("No assets in inventory.\n")
        return
    print(f"Total Assets      : {len(assets)}")
    print("\nBy Risk Level:")
    for level in RISK_LEVELS:
        print(f"  {level:<9}: {count_by(assets, 'Risk Level', level)}")
    print("\nBy Security Status:")
    for status in SECURITY_STATUSES:
        print(f"  {status:<10}: {count_by(assets, 'Security Status', status)}")
    print("\nBy Asset Type:")
    for atype in ASSET_TYPES:
        print(f"  {atype:<12}: {count_by(assets, 'Asset Type', atype)}")
    print()


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

MENU = """
=========================================
 CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Add Multiple Assets (bulk entry)
3. Search Asset
4. Update Asset
5. Delete Asset
6. Display All Assets
7. Security Summary
8. Exit
=========================================
"""


def main():
    assets = load_assets()
    print("Cybersecurity Asset Inventory System")
    print(f"Loaded {len(assets)} existing asset(s) from data file.")

    while True:
        print(MENU)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            display_assets(assets)
        elif choice == "7":
            security_summary(assets)
        elif choice == "8":
            print("Exiting. All changes have been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
