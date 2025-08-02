from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load datasets
emissions_df = pd.read_csv('data/emission_factors.csv')
manufacturing_df = pd.read_csv('data/manufacturing_factors.csv')
disposal_df = pd.read_csv('data/disposal_factors.csv')

TON_TO_KG = 907.185  # conversion constant

def calculate_emissions(weight_ton, distance_miles, mode, material):
    """Calculate total emissions for a product shipment.

    Parameters:
        weight_ton (float): Weight of the product in short tons.
        distance_miles (float): Distance traveled in miles.
        mode (str): Transportation mode key (e.g., 'truck', 'air', 'rail', 'ocean').
        material (str): Material name for manufacturing/disposal factors.

    Returns:
        dict or None: Dictionary with transport, manufacturing, disposal, and total emissions in kg CO2e.
                      Returns None if the mode is not recognized.
    """
    # Transportation emissions
    row = emissions_df.loc[emissions_df['mode'] == mode]
    if row.empty:
        return None
    factor = row.iloc[0]['emission_kg_per_ton_mile']
    transport_kg = distance_miles * weight_ton * factor

    # Manufacturing emissions
    m_row = manufacturing_df.loc[manufacturing_df['material'] == material]
    m_factor = m_row.iloc[0]['emission_kg_per_kg'] if not m_row.empty else 0.0
    weight_kg = weight_ton * TON_TO_KG
    manufacturing_kg = weight_kg * m_factor

    # Disposal emissions
    d_row = disposal_df.loc[disposal_df['material'] == material]
    d_factor = d_row.iloc[0]['emission_kg_per_kg'] if not d_row.empty else 0.0
    disposal_kg = weight_kg * d_factor

    total = transport_kg + manufacturing_kg + disposal_kg
    return {
        'transport': transport_kg,
        'manufacturing': manufacturing_kg,
        'disposal': disposal_kg,
        'total': total
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        material = request.form.get('material')
        try:
            weight = float(request.form.get('weight'))
            distance = float(request.form.get('distance'))
            result = calculate_emissions(weight, distance, mode, material)
        except (TypeError, ValueError):
            result = None
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
