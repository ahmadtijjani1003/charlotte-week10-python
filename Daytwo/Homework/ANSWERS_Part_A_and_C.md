# Week 10 Class 2 Homework — Written Answers

## Part A — Conceptual questions (20 marks)

### 1. How does a Series differ from a DataFrame? Give an operational example of each.
A **Series** is a one-dimensional labelled array: it contains one column of values with an index. For example, the `oil_bpd` column for a set of well readings is a Series. A **DataFrame** is a two-dimensional table with labelled rows and columns. For example, a daily production table containing `well_id`, `status`, `oil_bpd` and `water_bpd` is a DataFrame. A DataFrame can contain several Series, one for each column.

### 2. Why does CSV data need dtype checks after import?
CSV files store plain text and do not reliably preserve the intended data types. During import, a numeric column can be read as text if it contains unexpected characters, and dates may be read as strings. Checking `df.dtypes` helps confirm that production volumes are numeric, dates are datetime values and identifiers/status fields have suitable types. This prevents calculation, filtering and sorting errors.

### 3. Compare `.loc` and `.iloc` with one short example each.
`.loc` selects rows or columns by their labels. Example: `df.loc[df["status"] == "PRODUCING", ["well_id", "oil_bpd"]]` selects producing wells and the named columns. `.iloc` selects by integer position. Example: `df.iloc[0:3, 0:2]` selects the first three rows and first two columns. The key difference is label-based selection (`.loc`) versus position-based selection (`.iloc`).

### 4. Why do missing oil volume and a true production value of zero have different meanings?
A missing oil volume means no valid measurement was recorded or supplied. A true zero means a measurement or confirmed operating condition indicates that no oil was produced for that reading. They are not interchangeable: missing data is unknown, while zero is a known numerical value. Treating missing values as zero can make a well appear to have stopped producing when its measurement was simply unavailable.

### 5. What does `.copy()` help protect when enriching a table?
`.copy()` creates an independent DataFrame for the new work. Adding or changing derived columns on that copy does not unintentionally alter the original input table. This protects the raw measurements, supports reproducibility and makes it easier to compare original data with enriched data.

## Part C — Interpretation (20 marks)

Missing measurements can make management reports incomplete and can distort comparisons between wells, fields and reporting periods. A blank oil-volume reading means that the measurement is unavailable; it does not prove that the well produced zero barrels. If a report replaces that missing value with zero, managers may conclude that the well stopped producing or that field output fell on that day. For example, if a producing well has no recorded oil reading because its meter data was not received, converting the blank to zero would reduce the reported production total and could create a false production-loss alert. It may also affect averages, performance rankings, forecasts and decisions about maintenance or staff deployment. Missing pressure readings create a similar risk because an unknown pressure could be mistaken for a real zero-pressure condition. Reports should therefore show missing counts, preserve missing values as `NaN`, and clearly distinguish unavailable readings from genuine zero measurements. The data team should investigate missing records and document any later corrections so that management decisions are based on traceable evidence rather than assumptions.
