# PARSEC Query GUI

The application provides predefined queries and an interactive UI for accessing astrophysical data products in a structured way.

---

## Requirements

- Python stable versions so far: **3.11.3** and **3.14.3**
- pip package manager

All dependencies are listed in `requirements.txt`.

---

## Installation

### 1. Clone the repository
```bash
git clone [https://github.com/mavrommat/PARSEC_Query_GUI.git](https://github.com/mavrommat/PARSEC_Query_GUI.git)
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

### 4. Setup the Database (Required)

The application is connected to a database strictly for object resolving and coordinate searches. You must set this up before running the main application.

**Option A: Generate the mock database**
We provide a script that queries SIMBAD via TAP to generate a mock 10,000-row catalog.

1. Run the database script:
```bash
python mock_database.py

```


2. Move the newly generated `astro_10k.parquet` file into a `Database/` folder within your project directory, as the GUI expects this path.

**Option B: Use your own database**
If you want to use a custom database, ensure it is formatted identically (requiring columns like `id`, `ra`, `dec`, and `otype`). You will need to update the source code to point to your custom file.

1. Open `SearchAroundFanc.py`.
2. Locate the `pd.read_parquet(...)` call (around line 34).
3. Change the path string to match the location and name of your custom `.parquet` file.

---

## Run the application

```bash
python main.py

```

---

