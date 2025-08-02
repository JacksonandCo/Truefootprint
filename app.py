from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load emission factors
df = pd.read_csv('data/emission_factors.csv')

def calculate_emissions(weight_ton, distance_miles, mode):
    row = df.loc[df['mode'] == mode]
    if row.empty:
        return None
    factor = row.iloc[0]['emission_kg_per_ton_mile']
    # result in kg CO2e
    return distance_miles * weight_ton * factor

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        try:
            weight = float(request.form.get('weight'))
            distance = float(request.form.get('distance'))
            result = calculate_emissions(weight, distance, mode)
        except (TypeError, ValueError):
            result = None
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
