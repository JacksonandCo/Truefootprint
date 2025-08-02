# Truefootprint

This project aims to build a web application that estimates the **end‑to‑end carbon footprint** of a consumer product from production through transportation, usage and end‑of‑life disposal.  Many companies only provide high‑level carbon figures for consumers to understand the impact of their purchases.  **Truefootprint** models the journey of a product by combining user‑provided shipment details (distance, weight and transport mode) with published emission factors for manufacturing and disposal.

## Features

- **Interactive footprint calculator** – Users enter the product name, weight (short tons), distance travelled (miles), transport mode (truck, air, rail or ocean) and material (plastic, steel or cotton).
- **Transport emissions** – The application multiplies distance, weight and a transport‑mode‑specific emission factor.  Emission factors are taken from U.S. EPA data compiled by ClimeCo: truck 0.17 kg CO₂ per ton‑mile, air 0.698 kg CO₂ per ton‑mile, rail 0.021 kg CO₂ per ton‑mile and ocean 0.044 kg CO₂ per ton‑mile【449790012178953†L188-L197】.
- **Manufacturing emissions** – Average carbon intensities for common materials are used to estimate manufacturing footprint.  For example, conventional fossil polyethylene plastics emit **3.10 kg CO₂ per kg of plastic**【113838441178126†L78-L83】; typical steel production emits **1.85 kg CO₂ per kg of steel**【831224257615691†L39-L66】; cotton’s footprint varies widely, so we use the mid‑range (≈3.61 kg CO₂ per kg) based on lifecycle assessments【518315162093020†L96-L100】.
- **End‑of‑life emissions** – Disposal factors model the carbon emitted when the product is incinerated or landfilled.  For plastics, production plus incineration is roughly **6 kg CO₂ per kg of plastic** and manufacturing accounts for 3.1 kg CO₂; hence disposal contributes ≈2.9 kg CO₂ per kg【487754603814092†L45-L59】【487754603814092†L115-L117】.  Disposal emissions for steel and cotton are set to zero (data unavailable) but can be extended.
- **Transparent breakdown** – Results show transport, manufacturing, disposal and total emissions separately.

## Data

All emission factors are stored in CSV files within the `data/` folder:

- `emission_factors.csv` – Transport emission factors in kg CO₂ per ton‑mile for each mode.
- `manufacturing_factors.csv` – Emission factors in kg CO₂ per kg for materials (plastic, steel and cotton).
- `disposal_factors.csv` – End‑of‑life emission factors in kg CO₂ per kg (2.9 kg for plastics; 0 for steel and cotton).

You can update these datasets with additional modes or materials as new research becomes available.

## Running the application locally

1. **Clone or download** this repository.
2. Ensure you have Python 3.7+ installed.  Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Flask app:
   ```bash
   python app.py
   ```
   or use `new_app.py` if you prefer the version that loads the extended datasets.
4. Open a browser at `http://localhost:5000` and enter your product details.  The app will display transport, manufacturing and disposal emissions and the total footprint.

## Future work

- Integrate live tracking APIs to automatically infer distances from shipment tracking numbers.
- Expand the list of materials and include usage‑phase emissions for certain products (e.g., electronics energy consumption during use).
- Add a database to store user queries and compute aggregate emissions statistics.
- Consider deploying the app on a cloud platform (e.g., Heroku, Render) and securing API keys for geocoding and tracking services.

## License

This project is provided for educational purposes.  Please check local laws and licensing requirements before commercial use.
