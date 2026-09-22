# JSON Social Data Cleaner

A Python utility designed to load, display, and clean structured social network JSON data containing user profiles, friend connections, and liked pages.

## Features

- **Data Inspection:** Parses raw JSON datasets and formats user profiles and page details into clean console output.
- **Missing Name Removal:** Filters out user entries with empty or whitespace-only names.
- **Deduplication:**
  - Removes duplicate friend IDs within user profiles.
  - Resolves duplicate page entries by keeping the latest unique page record by ID.
- **Inactive User Filtering:** Strips out user profiles that have no friends and no liked pages.
- **Cleaned Export:** Writes processed, valid JSON data directly to an output file.

## Setup and Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Script

1. Clone this repository:
   ```bash
   git clone [https://github.com/anujkurmi22/json-social-data-cleaner.git](https://github.com/anujkurmi22/json-social-data-cleaner.git)
   cd json-social-data-cleaner
