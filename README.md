# Commercial-Grade Data Validation & Automated PDF Reporting Kit

This repository serves as the core engine for the production toolkit distributed via [Clearline Analytics](https://clearlineanalytics.gumroad.com/l/datastarterkit). It provides an automated data validation pipeline paired with a dynamic PDF reporting engine.

### 💼 Why Agencies Care:
* **The Cost of Bad Data:** Manual data cleaning eats up senior developer hours. This tool shifts QA from a half-day engineering bottleneck into a 10-second background step.
* **Client-Ready Deliverables:** Beyond validation, the engine auto-compiles code execution results into a clean, unbranded, or custom-branded PDF audit report to pass directly to stakeholders.

[**Open Preview in Streamlit**](https://data--validator.streamlit.app) &nbsp;&nbsp; | &nbsp;&nbsp; [**📥 Download Full Kit for $97 →**](https://clearlineanalytics.gumroad.com/l/datastarterkit)



## The Problem

Most data work doesn't fail at the analysis stage. It fails earlier, quietly, in the data itself. Missing values, type mismatches, out-of-range entries, duplicate records. The kind of thing that doesn't throw an error. It just throws off the conclusions.

By the time you notice, you've already built the dashboard, written the report, or made the recommendation on top of it.

Building a custom validation layer from scratch takes days of engineering time most small teams don't have. This compresses that into a single afternoon.



## Live Demo

[**Open Preview in Streamlit**](https://data--validator.streamlit.app)

Upload any CSV. Select an industry profile. See what the validation engine surfaces, scored from 0–100 with a letter grade and a downloadable PDF report.



## What's Included in the Full Kit

| # | Item | Description |
|---|------|-------------|
| 1 | **Full source code** | Fully commented Python, MIT-licensed for personal and commercial use |
| 2 | **`requirements.txt`** | Version-locked dependencies for zero deployment friction |
| 3 | **30-Minute Setup & Extension Guide (PDF)** | Run it locally, understand the architecture, add custom rules |
| 4 | **Example dataset** | The exact messy retail CSV used in production testing |



## Key Features

- **Five automated checks**: Null rates, duplicates, type mismatches, outliers, schema drift
- **Industry presets**: Retail, Healthcare, Finance with tuned thresholds out of the box
- **Health scorecard**: 0–100 score with letter grade, errors weighted heavier than warnings
- **One-click PDF export**: PDF report ready to send to a client
- **Fully configurable**: Swap thresholds, key columns, and outlier methods via YAML



## Who It's For

- **Solo analysts and consultants** who want a repeatable QA step without building one from scratch
- **Small agencies** who take on client data work and want to catch problems before the client does
- **Streamlit developers** who want a production-grade example to study and extend



## Why Buy Instead of Build

This isn't a course or a concept demo. It's the actual validation pattern built and proven in a high-stakes regulated environment where bad data has real consequences.

The core logic is derived from patterns deployed inside **Bank of America change-request pipelines** where automated QA validation saved ~20 hours per release cycle. You're not getting a toy. You're getting the thing that's already been stress-tested.



## Quickstart (Preview Version)

```bash
git clone https://github.com/jtambe007/streamlit-data-validation-starter-kit.git
cd streamlit-data-validation-starter-kit
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The preview version shows the full interface but does not include the validation engine. Upload example_data/sample_retail.csv to see the UI in action.



## License
MIT (personal and commercial agency use allowed)



## Get the Full Kit
[**📥 Download Full Kit for $97 →**](https://clearlineanalytics.gumroad.com/l/datastarterkit)

One-time purchase. Lifetime access. MIT licensed.
