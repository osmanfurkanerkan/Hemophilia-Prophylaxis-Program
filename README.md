# Hemophilia Prophylaxis & Clinical Decision Support Tool

A Python-based clinical calculation engine designed to automate factor dosage estimation, standard vial optimization, and cost analysis for hemophilia patients eligible for prophylaxis treatment.

## 📋 Overview

In hemophilia management, calculating the exact Factor VIII / Factor IX vial combination is critical to prevent both clinical under-dosing and high-cost medication waste. This tool processes patient biomarkers to establish treatment eligibility, classify disease severity, and generate an optimized 4-week treatment protocol.

## 🚀 Key Features

- **Biomarker Evaluation:** Evaluates Factor VIII/IX protein deficiency levels and the presence of neutralizing antibodies (inhibitors).
- **Rule-Based Severity Stratification:** Classifies the clinical manifestation into **Severe** (`<1%`), **Moderate** (`1-5%`), or **Mild** (`>5%`) automatically.
- **Vial Optimization Engine:** Calculates the exact combination of standard pharmaceutical vials needed to reach the target UI (International Units) with near-zero financial waste.
- **Protocol Cost Modeling:** Computes personalized 4-week prophylaxis treatment expenses in USD.
- **Cohort Analytics:** Aggregates multi-patient batch inputs to output clinic-level statistical summaries (patient distribution, severity ratios, and peak dosage demands).

## 💻 Tech Stack & Execution

Built with **Pure Python (3.x)** with zero external dependencies, emphasizing algorithmic accuracy and raw computational logic.

```bash
# Clone the repository
git clone [https://github.com/osmanfurkanerkan/Hemophilia-Prophylaxis-Program.git](https://github.com/osmanfurkanerkan/Hemophilia-Prophylaxis-Program.git)

# Navigate to directory
cd Hemophilia-Prophylaxis-Program

# Execute the decision engine
python main.py
