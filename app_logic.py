import os
import pandas as pd
from datetime import datetime

# Risk rules for each parameter
risk_rules = {
    'Cycle Time (s)': {'min': 30, 'max': 180, 'defect': 'Cycle Delay'},
    'Job Count': {'min': 0, 'max': 100, 'defect': 'Inconsistent Operation'},
    'Machine Utilization (%)': {'min': 40, 'max': 100, 'defect': 'Underutilization'},
    'Spindle Speed (RPM)': {'min': 1000, 'max': 6000, 'defect': 'Spindle Overload'},
    'Feed Rate (mm/min)': {'min': 200, 'max': 1500, 'defect': 'Feed Rate Error'},
    'Tool Wear (%)': {'min': 0, 'max': 60, 'defect': 'Tool Wear/Breakage'},
    'Vibration Level (mm/s)': {'min': 0, 'max': 12, 'defect': 'Excessive Vibration'},
    'Spindle Temperature (°C)': {'min': 20, 'max': 60, 'defect': 'Overheating'},
    'Power Consumption (kWh)': {'min': 50, 'max': 400, 'defect': 'Power Surge or Drop'},
}

# Main logic to evaluate input parameters
def evaluate_parameters(inputs):
    status = "✅ OK"
    machine_status = "🟢 Running"
    defects = []
    triggered = False
    confidence = 100
    detailed_results = []

    for param, value in inputs.items():
        rule = risk_rules.get(param)
        in_range = True
        defect = "None"
        if rule:
            if value < rule['min'] or value > rule['max']:
                in_range = False
                defect = rule['defect']
                status = "❌ NG"
                machine_status = "🔴 Breakdown"
                defects.append(defect)
                triggered = True
        detailed_results.append({
            'parameter': param,
            'value': value,
            'safe_range': f"{rule['min']} - {rule['max']}",
            'status': "❌ Out of Range" if not in_range else "✅ OK",
            'defect': defect if not in_range else "-"
        })

    if triggered:
        confidence = 100 - len(defects) * 10
        if confidence < 50:
            confidence = 50

    return {
        'Part Status': status,
        'Confidence': confidence,
        'Machine Status': machine_status,
        'Defect Types': defects if defects else ['None'],
        'Detailed Results': detailed_results
    }

# Function to save evaluations to logs
def save_to_log(inputs, result, mode="manual"):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, "evaluation_log.csv")

    data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Mode": mode,
        **inputs,
        "Part Status": result['Part Status'],
        "Machine Status": result['Machine Status'],
        "Confidence": result['Confidence'],
        "Defect Types": ", ".join(result['Defect Types'])
    }

    df = pd.DataFrame([data])
    if not os.path.exists(log_file):
        df.to_csv(log_file, index=False)
    else:
        df.to_csv(log_file, mode='a', index=False, header=False)