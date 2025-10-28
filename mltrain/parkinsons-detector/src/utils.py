def log_message(message):
    print(f"[LOG] {message}")

def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def save_results(results, output_file):
    import json
    with open(output_file, 'w') as file:
        json.dump(results, file)

def normalize_data(data):
    return (data - data.mean()) / data.std()

def handle_missing_values(data):
    return data.fillna(data.mean())