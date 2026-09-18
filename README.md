# Week 01 – Cybersecurity Asset Inventory System

A menu-driven Python CLI application that lets a security administrator
**add, search, update, delete, and display** an organization's IT assets,
classify them by type and risk level, and generate a security summary.

## Problem Statement

Organizations manage many IT assets (computers, servers, routers, switches,
applications). Tracking them manually makes it hard to identify assets,
monitor their security status, and know which ones need urgent attention.
This tool centralizes that information in a simple inventory system.

## Features

- **Add Asset** – add a single asset with full validation
- **Add Multiple Assets** – bulk entry mode (matches the sample input flow)
- **Search Asset** – look up an asset by Asset ID
- **Update Asset** – edit any field of an existing asset
- **Delete Asset** – remove an asset (with confirmation)
- **Display All Assets** – view the full inventory with a summary footer
- **Security Summary** – breakdown by Risk Level, Security Status, and Asset Type
- **Persistent storage** – all data is saved to `data/assets.json` between runs
- **Input validation** – Asset Type, Risk Level, and Security Status are
  restricted to the allowed values; duplicate Asset IDs are rejected

## Data Fields

| Field | Description |
|-------|-------------|
| Asset ID | Unique identifier for the asset |
| Asset Name | Friendly name of the asset |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Network address of the asset |
| Operating System | OS running on the asset |
| Owner/Department | Department responsible for the asset |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## How to Run

Requires Python 3.7+ (no external libraries needed).

```bash
cd Week-01-Cybersecurity-Asset-Inventory/src
python3 asset_inventory.py
```

You'll see a menu:

```
1. Add Asset
2. Add Multiple Assets (bulk entry)
3. Search Asset
4. Update Asset
5. Delete Asset
6. Display All Assets
7. Security Summary
8. Exit
```

Pick option `2` and enter `3` to reproduce the sample walkthrough from the
project spec (assets A101, A102, A103), or use option `6` any time to see
the current inventory formatted exactly like the "Expected Output" in the
assignment.

## Sample Output

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID       : A101
Asset Name     : HR-PC-01
Asset Type     : Workstation
IP Address     : 192.168.1.10
OS             : Windows 11
Department     : HR
Risk Level     : Medium
Status         : Secure
-----------------------------------------
Asset ID       : A102
Asset Name     : Web-Server
Asset Type     : Server
IP Address     : 192.168.1.20
OS             : Ubuntu
Department     : IT
Risk Level     : Critical
Status         : Vulnerable
-----------------------------------------
Asset ID       : A103
Asset Name     : Core-Router
Asset Type     : Router
IP Address     : 192.168.1.1
OS             : Cisco IOS
Department     : Network
Risk Level     : High
Status         : Warning
=========================================
Total Assets      : 3
Critical Assets   : 1
High Risk Assets  : 1
Medium Risk Assets: 1
Vulnerable Assets : 1
=========================================
```

## Testing

See [`tests/test_cases.md`](tests/test_cases.md) for the full manual test
matrix (adding, searching, updating, deleting, validation, persistence, and
edge cases).

## Screenshots

The `screenshots/` folder should contain captures of each core operation
running in your terminal:

1. `01-add-asset.png` – adding a new asset
2. `02-display-assets.png` – full inventory display with summary
3. `03-search-asset.png` – searching by Asset ID
4. `04-update-asset.png` – updating an asset's fields
5. `05-delete-asset.png` – deleting an asset with confirmation
6. `06-security-summary.png` – the security summary breakdown
7. `07-input-validation.png` – an invalid entry being rejected (e.g. bad
   Asset Type or Risk Level) and the program re-prompting
