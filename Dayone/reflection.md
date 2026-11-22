# Charlotte Project — Week 10 / Class 1
## Homework: NumPy in Drilling Analytics

### Part 1 — Short-answer understanding

**1. Python list multiplication vs NumPy numeric-array multiplication**

Multiplying a Python list by an integer repeats the list. For example, `[2, 4] * 2` produces `[2, 4, 2, 4]`. Multiplying a NumPy numeric array by 2 performs element-by-element arithmetic: `np.array([2, 4]) * 2` produces `array([4, 8])`. List multiplication repeats items, while NumPy array multiplication scales the numeric values.

**2. Shape, ndim and dtype**

- **shape** describes the size of an array along each dimension. A matrix with 12 observations and 4 sensor channels has shape `(12, 4)`.
- **ndim** is the number of dimensions. This sensor matrix has `ndim` equal to `2`.
- **dtype** is the data type stored in the array, such as `float64`.

`dtype` matters because sensor readings can contain decimals and missing values represented by `np.nan`. A floating-point dtype can store both decimal measurements and `NaN`, allowing calculations to work consistently.

**3. Meaning of `axis=0`**

For a sensor matrix where rows are observations and columns are channels, `axis=0` performs an operation down the rows, separately for each column. For example, `np.nanmean(matrix, axis=0)` calculates one mean for pressure, one for temperature, one for vibration and one for flow. It does not combine the different channels into one average.

**4. Why use `np.nanmean` instead of `np.mean`?**

`np.mean` normally returns `NaN` for a calculation if the values being averaged contain a `NaN`. `np.nanmean` ignores missing (`NaN`) entries and calculates the mean from available readings. This is useful when a blank sensor cell means that a measurement was not recorded. It allows valid readings to be summarized without treating a missing value as zero. Missing readings should still be counted and reported.

---

### Part 2 — Python extensions

Run `homework.py` from the `class_01_numpy` folder. It reads the original CSV from `class_01_numpy/data/multiwell_sensor_readings.csv` and calculates the results using NumPy.

**5. Readings where flow exceeds 400 bpd AND vibration exceeds 6.0 mm/s**

Matching sample IDs:
- `S003`
- `S009`
- `S010`

Both conditions must be true. A reading with missing flow does not pass the flow threshold.

**6. Pressure ranges by well**

| Well | Minimum pressure (psi) | Maximum pressure (psi) | Range (psi) |
|---|---:|---:|---:|
| WELL-11 | 3,200 | 3,650 | 450 |
| WELL-12 | 2,800 | 3,100 | 300 |
| WELL-13 | 3,400 | 3,900 | 500 |

Missing pressure is ignored. **Observation:** WELL-13 has the widest pressure range at 500 psi, while WELL-12 has the narrowest at 300 psi, so the observed pressure variability is greatest in WELL-13 and lowest in WELL-12.

**7. Standardized pressure ratios relative to 3500 psi**

The ratio is `pressure_ratio = pressure_psi / 3500`.

Array in original sample order, rounded to three decimal places:

```text
[0.914, 0.986, 1.043, 0.943, 0.800, 0.843,
   nan, 0.886, 1.057, 1.114, 1.014, 0.971]
```

Ratios above 1:

| Sample ID | Pressure ratio |
|---|---:|
| S003 | 1.043 |
| S009 | 1.057 |
| S010 | 1.114 |
| S011 | 1.014 |

The missing pressure for S007 remains `NaN`; it is not replaced with zero or another invented value.

---

### Part 3 — Engineering interpretation (120–180 words)

Reliable handling of missing sensor readings is important because a blank measurement does not mean that the sensor recorded zero. Replacing missing pressure, temperature, vibration or flow values with zero could create false averages, hide abnormal operating conditions or make a well appear safer or less productive than it is. Using `NaN` and functions such as `np.nanmean` allows valid readings to be analyzed while missing entries remain identifiable and can be reported for investigation. Engineering units are equally important because each channel measures a different physical quantity. Pressure in psi, temperature in °F, vibration in mm/s and flow in barrels per day must not be mixed in one unqualified calculation. Unit conversion and clear labels help analysts compare readings correctly and avoid threshold errors. These practices provide a dependable foundation for later data-quality pipelines, where invalid, missing or unusual measurements can be flagged consistently before operational decisions are made.

---

## Submission

Place `homework.py` and `reflection.md` inside `class_01_numpy/`. Keep the supplied CSV unchanged in `class_01_numpy/data/`. Add the two files to your existing feature branch, commit them, push the branch, and update your existing Pull Request.
