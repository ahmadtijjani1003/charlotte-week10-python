# Charlotte Project — Week 10 / Class 1: NumPy Sensor Lab

## Project overview
This lab loads 12 synthetic sensor observations from three wells, inspects the numeric data, converts units, identifies readings above specified thresholds, and calculates summaries. The solution uses Python's `csv` module and NumPy; it does not use Pandas or hard-code calculated results.

## Files
- `numpy_sensor_lab_completed.py` — completed Parts A–D.
- `multiwell_sensor_readings.csv` — original, unmodified input data.
- `requirements.txt` — Python dependency.
- `.gitignore` — ignores the virtual environment and Python cache files.

## Environment setup
Run these commands from the project folder.

### Windows
```bash
py -m venv .venv
.venv\\Scripts\\activate
py -m pip install -r requirements.txt
py numpy_sensor_lab_completed.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python numpy_sensor_lab_completed.py
```

## Data channels and units
The numeric matrix columns are kept in this order:
1. `pressure_psi` — pressure in pounds per square inch (psi).
2. `temperature_f` — temperature in degrees Fahrenheit (°F).
3. `vibration_mm_s` — vibration in millimetres per second (mm/s).
4. `flow_bpd` — flow in barrels per day (bpd).

The identifiers `sample_id` and `well_id` are stored separately from the numeric matrix.

## Missing-value policy
An empty numeric CSV cell is converted to `np.nan`. Missing readings are not replaced with invented values. `np.nanmean` and `np.nanmax` are used for summaries so missing readings are ignored. Missing pressure values are excluded from the high-pressure count.

## Unit conversions
- Pressure: kPa = psi × 6.8947572932
- Temperature: °C = (°F − 32) × 5/9

The processed matrix contains `[pressure_kpa, temperature_c, vibration_mm_s, flow_bpd]`. The four channels are not combined into one overall average because they represent different measurements and units.

## Results from the supplied CSV
- Numeric matrix shape: `(12, 4)`; dimensions: `2`; data type: `float64`; elements: `48`.
- High-pressure readings above 3500 psi: **4** — sample IDs `S003`, `S009`, `S010`, `S011`.
- High-vibration readings above 6.0 mm/s: **4**.
- Missing pressure entries: **1**.
- Missing flow entries: **1**.
- Average pressure: **3363.64 psi**.
- Maximum pressure: **3900.00 psi**.
- Average flow: **442.73 bpd**.
- Average pressure by well:
  - WELL-11: **3400.00 psi**
  - WELL-12: **2950.00 psi**
  - WELL-13: **3637.50 psi**

## Concise interpretation
WELL-13 has the highest average pressure among the three wells at 3637.50 psi. Four observations exceed the 3500 psi pressure threshold, and four exceed the 6.0 mm/s vibration threshold. The CSV contains one missing pressure reading and one missing flow reading. The program preserves these missing values as `np.nan` and excludes them from the relevant summaries.

## GitHub submission
Commit the script, original CSV, README, `requirements.txt`, and `.gitignore`. Create a Pull Request from `feature/class-01-numpy` into your own `main` branch. Add your actual Pull Request URL to your submission; do not invent or use a placeholder URL.
