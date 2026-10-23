### Hi Visitor 👀 <img src="https://raw.githubusercontent.com/iampavangandhi/iampavangandhi/master/gifs/Hi.gif" width="30px">

<h1 align="center">Hi 👋, I'm Deep Punj</h1>
<h3 align="center">git commit -m "Optical engineer and physicist 🔬 building tested scientific Python"</h3>

Optical engineer (PhD, nano-optics) with ten years of modelling, nanofabrication and optical
measurement. I build end-to-end, tested Python projects in **photonics and optical design** and in
**data science**, on real industrial and scientific data. I use physics to design meaningful features and models, and I check results honestly.

**Contact:** [LinkedIn](https://www.linkedin.com/in/deeppunj/) | deep.punj@outlook.com | [Bio link](https://punjdeep.bio.link/)

---

## ⭐ Featured projects

### [SiN edge-coupler study](https://github.com/deeppunj/sipho-coupler-study): photonics
From waveguide mode design to packaging yield for fibre-to-chip and chip-to-chip coupling.

- **Model:** finite-difference mode solver, checked against the exact slab solution (Δn_eff 2×10⁻⁵)
- **Packaging:** chip-to-chip misalignment and gap tolerance; Monte Carlo assembly yield vs bonder accuracy
- **Process window:** Gaussian-process surrogate over tip width and SiN thickness
- **Micro-optics:** expanded-beam relay ray-traced in Optiland; test-chip DOE layout in GDS
- **Result:** 0.43 dB to UHNA7 fibre; at a 1 dB spec, 96 % yield at σ = 0.25 µm vs 19 % at σ = 1 µm

`Python` `NumPy/SciPy` `Optiland` `scikit-learn` `gdstk` `pytest` `GitHub Actions`

### [Laser weld defect inspection](https://github.com/deeppunj/laser-defect-inspection-ml): data science
Detecting laser-weld defects from thermal camera frames.

- **Data:** 16,362 labelled infrared frames from 97 real laser beam welds (public dataset, CC BY 4.0)
- **Approach:** 7 physics-based thermal features, computed without labels or future frames
- **Evaluation:** nested cross-validation split by weld, compared with a leakage baseline
- **Result:** ROC AUC 0.974; 91% of defective frames detected at 5.6% false alarms
- **Also:** SHAP explanation, Streamlit dashboard, 31 pytest tests with GitHub Actions

`Python` `pandas` `scikit-learn` `SHAP` `Streamlit` `pytest` `GitHub Actions`

---

## 🕒 Recently updated
*Updated automatically every day.*

<!-- RECENT:START -->
Latest activity: [patient-finding-synthea](https://github.com/deeppunj/patient-finding-synthea), 2026-10-23

| Project | What it is | Updated |
|---|---|---|
| [powerbi_fda_drug_shortages](https://github.com/deeppunj/powerbi_fda_drug_shortages) | Power BI dashboard analyzing 1,141 active US FDA drug shortages by category, manufacturer and duration | 2026-10-11 |
| [optical-design-lab](https://github.com/deeppunj/optical-design-lab) |  | 2026-10-08 |
| [punjdeep-website](https://github.com/deeppunj/punjdeep-website) |  | 2026-10-03 |
| [Case_Studies_GoogleDataAnalyticsCourse](https://github.com/deeppunj/Case_Studies_GoogleDataAnalyticsCourse) | Case studies for the Google data analytics course on Coursera | 2023-01-22 |
<!-- RECENT:END -->

---

## Skills

- **Optics and photonics:** waveguide mode solving, FDTD (Lumerical), COMSOL, optical design (Optiland, Zemax basics), lasers, OCT, microscopy, nanofabrication (FIB, SEM, AFM)
- **Programming:** Python (NumPy, SciPy, pandas, scikit-learn, matplotlib), SQL, MATLAB
- **Machine learning:** feature engineering, cross-validation, leakage control, Gaussian-process, model explanation (SHAP)
- **Engineering practice:** packaging (pyproject.toml), pytest, Git, GitHub Actions, Streamlit
- **Visualisation:** Power BI, Tableau, matplotlib

## How I build projects
1. **Reproducible:** one environment, pinned requirements, data downloaded by script
2. **Honest evaluation:** checked against analytic results or simple baselines, no data leakage
3. **Tested:** pytest tests that run automatically on GitHub
4. **Explained:** README with results, figures and limitations

### What can we chat about :question:
<code>git commit -m "Photonics, optics, data science, machine learning and other nerd stuff!"</code> :grin:
