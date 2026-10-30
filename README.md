<h1 align="center">Deep Punj</h1>
<p align="center">
  <b>Optical engineer and data scientist · PhD in nano-optics</b><br>
  I turn measurements and records into tested, explainable models: from photonic devices to patient data.
</p>
<p align="center">
  <a href="https://punjdeep.com/">punjdeep.com</a> ·
  <a href="https://www.linkedin.com/in/deeppunj/">LinkedIn</a> ·
  <a href="mailto:deep.punj@outlook.com">deep.punj@outlook.com</a> ·
  Ghent, Belgium
</p>

---

Ten years of optics research at Institut Fresnel, KAUST, UC Irvine, IIT Madras and Leiden University, and now
at Ghent University's Faculty of Pharmaceutical Sciences, where I build optical set-ups and the Python behind them:
instrument control, image analysis and quality checks of laser systems. First-author paper in *Nature Nanotechnology*;
h-index 13.

On GitHub I build complete projects in two areas: **data science** on healthcare, industrial and energy data,
and **photonics** design and packaging.

**Open to** data science and ML roles (healthcare, pharma, industry, energy) and optical / photonics engineering roles.

---

## Featured projects

### Data science

**[Patient finding: undiagnosed kidney disease](https://github.com/deeppunj/patient-finding-synthea)** · healthcare<br>
Which adults will be diagnosed with chronic kidney disease in the next 12 months?
- Yearly patient snapshots built with SQL in PostgreSQL from 10,000 synthetic health records; features only from the 2 years before each snapshot, checked by leakage tests
- Rare target (0.5% positive): models compared on PR-AUC, trained on 2019-2023 and tested on 2024-2025, runs tracked in MLflow
- **Result:** reviewing the top 10% of patients finds 49% of next year's cases; 42% of new patients had an abnormal kidney test a median of 55 months before diagnosis

`Python` `PostgreSQL` `scikit-learn` `MLflow` `Streamlit` `pytest`

**[Laser weld defect inspection](https://github.com/deeppunj/laser-defect-inspection-ml)** · industrial ML, thermal imaging<br>
Can a thermal camera tell when a laser weld turns defective?
- 16,362 labelled infrared frames from 97 real welds; 7 physics-based features computed without labels or future frames
- Random Forest with nested cross-validation split by weld, checked against a leakage baseline; SHAP explanations
- **Result:** ROC AUC 0.974; 91% of defective frames detected at 5.6% false alarms

`Python` `scikit-learn` `SHAP` `Streamlit` `pytest` `GitHub Actions`

**[Battery dispatch on Belgian electricity prices](https://github.com/deeppunj/battery-dispatch-be)** · energy, forecasting + optimisation<br>
How much can a battery earn when it is scheduled from price forecasts instead of known prices?
- Day-ahead price forecast (gradient boosting) on 10 years of hourly prices, chronological train / validation / test split
- Daily battery schedule as a linear program (CVXPY), made from forecasts only and settled at real 2024 prices
- **Result:** forecast error 17.2 vs 23.2 EUR/MWh for the same-hour-yesterday baseline; 73.5% of the perfect-foresight profit, only about 1 point above the baseline

`Python` `pandas` `scikit-learn` `CVXPY`

### Photonics

**[SiN edge-coupler study](https://github.com/deeppunj/sipho-coupler-study)** · silicon photonics, packaging<br>
From waveguide mode design to assembly yield for fibre-to-chip and chip-to-chip coupling at 1550 nm.
- Finite-difference mode solver checked against the exact slab solution; misalignment, gap loss and Monte Carlo assembly yield
- Gaussian-process surrogate for the process window; expanded-beam micro-optic relay ray-traced in Optiland; test-chip DOE layout in GDS
- **Result:** 0.43 dB coupling to UHNA7 fibre; at a 1 dB spec, 96% assembly yield at 0.25 µm placement accuracy vs 19% at 1 µm

`Python` `NumPy/SciPy` `Optiland` `gdstk` `pytest` `GitHub Actions`

<!-- RECENT:START -->
## More projects

Last update: [light-and-data](https://github.com/deeppunj/light-and-data), 2026-10-30

**[US drug shortages dashboard](https://github.com/deeppunj/powerbi_fda_drug_shortages)**<br>
Power BI dashboard analyzing 1,141 active shortage listings (69 drugs) by category, manufacturer and duration

`data-analysis` `data-visualization` `powerbi`

**[Earlier data projects](https://github.com/deeppunj/portfolio-projects_old)**<br>
Earlier projects: Goodreads Streamlit app, Tableau dashboards, breast-cancer and banknote classifiers

`portfolio-project` `scikit-learn` `streamlit` `tableau`

**[Fab reporting ba](https://github.com/deeppunj/fab-reporting-ba)**<br>
Business analysis case for a semiconductor pilot line: requirements, KPI dictionary, Kimball star schema, data-quality checks, SQL analysis, Streamlit dashboard and Power BI model. Finds the litho bottleneck and an etch-tool yield excursion. Simulated data.

`business-analysis` `business-intelligence` `data-analytics` `data-modeling` `dax` `kimball` `kpi-dashboard` `manufacturing-analytics` `pandas` `portfolio-project` `postgresql` `power-bi` `python` `semiconductor` `sql` `star-schema` `streamlit` `yield-analysis`

<!-- RECENT:END -->

---

## Skills

| | |
|---|---|
| **Data science** | Python (pandas, NumPy, SciPy, scikit-learn), SQL (PostgreSQL), feature engineering, leakage-safe validation, imbalanced classification, time-series forecasting, linear optimisation, SHAP |
| **Engineering** | MLflow, pytest, GitHub Actions, Git, Streamlit, Power BI, Tableau |
| **Photonics and optics** | Waveguide mode solving, FDTD (Lumerical), COMSOL, Optiland, GDS layout, lasers, OCT, microscopy, nanofabrication (FIB, SEM) |

## How I work
- **Evaluation that can't cheat:** data split by time (patients, prices) or by group (welds), and always compared with a simple baseline or an exact result
- **Reproducible:** one environment file per project, fixed seeds, data downloaded or generated by script
- **Tested:** pytest checks for leakage and physics, run on GitHub Actions where the project allows it
- **Written up honestly:** every README states the result, how it was measured and its limitations
