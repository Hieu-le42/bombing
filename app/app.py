from flask import Flask, render_template
import os

app = Flask(__name__,
            template_folder='templates',  # Flask looks for HTML files in 'templates'
            static_folder='data',         # Flask serves files from 'data' as static files
            static_url_path='/data')      # Access files in 'data' via /data/ URL prefix

# --- Flask Routes ---

@app.route("/")
def index():
    """
    Serves the main HTML page which contains the D3.js map visualization.
    The HTML will then request the GeoJSON and CSV files from the /data/ URL.
    """
    return render_template("index.html")

# --- Main execution ---
if __name__ == "__main__":
    # Optional: Basic check to confirm data files exist
    required_files = [
        'vietnam-provinces.geojson',
        'laos.geojson',
        'cambodia.geojson',
        'count.csv',           # Assuming this has overall counts for choropleth
        'operations_points.csv' # If you want to include points, ensure this file exists
    ]

    missing_files = []
    for f in required_files:
        if not os.path.exists(os.path.join(app.static_folder, f)):
            missing_files.append(f)

    if missing_files:
        print(f"WARNING: The following data files are missing from '{app.static_folder}':")
        for mf in missing_files:
            print(f"- {mf}")
        print("The map visualization might not load correctly without these files.")
        print("Please ensure your 'data' folder is set up as described in the project structure.")
    else:
        print(f"All required data files found in '{app.static_folder}'.")

    print("\nStarting Flask app...")
    print(f"Access your app at: http://127.00.1:5000/")
    app.run(debug=True) # Run with debug mode for development
