# Test Cases – Cybersecurity Asset Inventory System

| # | Test Case | Steps | Expected Result | Status |
|---|-----------|-------|------------------|--------|
| 1 | Add a valid asset | Menu → 1 → fill all fields with valid values | Asset is added and saved to `data/assets.json`; confirmation message shown | Pass |
| 2 | Add asset with duplicate Asset ID | Menu → 1 → enter an ID that already exists | Program rejects the ID and re-prompts until a unique ID is given | Pass |
| 3 | Add asset with invalid Asset Type | Menu → 1 → type something not in the allowed list (e.g. "Laptop") | Program shows an error and re-prompts until a valid type is entered | Pass |
| 4 | Add asset with invalid Risk Level | Menu → 1 → type "Extreme" for Risk Level | Program rejects and re-prompts with the valid options | Pass |
| 5 | Add asset with invalid Security Status | Menu → 1 → type "Unknown" for Security Status | Program rejects and re-prompts with the valid options | Pass |
| 6 | Bulk add (sample input) | Menu → 2 → enter 3, then fill in A101/A102/A103 exactly as in the sample input | Output matches the "Expected Output" in the project spec when displayed | Pass |
| 7 | Search for an existing asset | Menu → 3 → enter "A102" | Full asset details for A102 are printed | Pass |
| 8 | Search for a non-existent asset | Menu → 3 → enter "A999" | "No asset found with ID 'A999'." message shown | Pass |
| 9 | Update an existing asset's fields | Menu → 4 → enter "A101" → change Risk Level to "High" | A101's Risk Level is updated to High and persisted | Pass |
| 10 | Update with blank input keeps old value | Menu → 4 → enter "A101" → leave Asset Name blank | Asset Name remains unchanged | Pass |
| 11 | Update a non-existent asset | Menu → 4 → enter "A999" | "No asset found with ID 'A999'." message shown | Pass |
| 12 | Delete an existing asset (confirmed) | Menu → 5 → enter "A103" → confirm with "y" | A103 is removed from inventory and file is updated | Pass |
| 13 | Delete an existing asset (cancelled) | Menu → 5 → enter "A103" → answer "n" | Deletion cancelled, asset remains in inventory | Pass |
| 14 | Delete a non-existent asset | Menu → 5 → enter "A999" | "No asset found with ID 'A999'." message shown | Pass |
| 15 | Display all assets | Menu → 6 | All assets printed with a summary footer: Total, Critical, High Risk, Medium Risk, Vulnerable counts | Pass |
| 16 | Display with empty inventory | Delete all assets, then Menu → 6 | "No assets to display." with Total Assets: 0 | Pass |
| 17 | Security summary breakdown | Menu → 7 | Counts by Risk Level, Security Status, and Asset Type are all correct | Pass |
| 18 | Data persistence across runs | Add an asset, exit program, relaunch it | Previously added asset is still present (loaded from `assets.json`) | Pass |
| 19 | Invalid menu choice | Main menu → enter "9" or "abc" | "Invalid choice. Please enter a number from 1 to 8." shown, menu re-displayed | Pass |
| 20 | Exit saves data | Add/update/delete an asset, then Menu → 8 | All changes are present in `data/assets.json` after exit | Pass |
