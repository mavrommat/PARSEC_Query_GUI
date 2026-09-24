# PARSEC Query GUI

The application provides predefined queries and an interactive UI for accessing astrophysical data products in a structured way.

---

## Requirements

* Python stable versions so far: **3.11.3** and **3.14.3**
* pip package manager

All dependencies are listed in `requirements.txt`.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mavrommat/PARSEC_Query_GUI.git
cd PARSEC_Query_GUI

```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv gui_env
source gui_env/bin/activate

```

**Windows**

```bash
python -m venv gui_env
gui_env\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Database Configuration

The application requires a database strictly for object resolving and coordinate searches.

**Default Mock Database:**
The repository **already contains a mock database** (`astro_10k.parquet` located in the `Database/` folder). You do not need to run any scripts to generate it—the application is ready to use it out of the box.

**Using a Custom Database:**
You can replace the mock database with your own custom database. However, please note the current limitations:

* **No API Access (Not Implemented):** There is currently no API access implemented to dynamically query or fetch the database. While future versions will automatically download Object IDs and coordinates from the PARSEC database to run local coordinate searches, you must currently provide a local file.
* **Format Requirements:** Your custom database must be a `.parquet` file formatted identically to the mock database. It requires the following columns: `id`, `ra`, `dec`, and `otype`.

**To implement a custom database:**

1. Open `SearchAroundFanc.py`.
2. Locate the `pd.read_parquet(...)` call (around line 34).
3. Change the path string to match the location and name of your custom `.parquet` file.

---

## How to Run the Application

Once the virtual environment is activated and dependencies are installed, you can start the GUI by running:

```bash
python main.py

```