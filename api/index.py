from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ------------------------------
#  BASIC CONFIG
# ------------------------------
VAHAN_PUBLIC_API = "https://apisetu.gov.in/vahanapi/rc-details"
API_KEY = "PUBLIC"   # This API is fully legal & public

@app.route("/lookup", methods=["GET"])
def lookup_vehicle():
    rc = request.args.get("rc")

    if not rc:
        return jsonify({
            "error": "Missing parameter: rc",
            "developer": "@istgrehu"
        }), 400

    # ----- CALL GOV PUBLIC API -----
    try:
        url = f"{VAHAN_PUBLIC_API}?reg_no={rc}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return jsonify({
                "error": f"API error: {res.status_code}",
                "developer": "@istgrehu"
            }), res.status_code

        data = res.json()

    except Exception as e:
        return jsonify({
            "error": str(e),
            "developer": "@istgrehu"
        }), 500

    # ------------------------------
    #  FORMAT OUTPUT CLEANLY
    # ------------------------------
    response = {
        "Registration Number": data.get("regn_no"),
        "Registration Date": data.get("regn_dt"),
        "Registration State": data.get("state_cd"),
        "RTO Office": data.get("rto_cd"),
        
        "Vehicle Class": data.get("vh_class_desc"),
        "Maker": data.get("maker_desc"),
        "Model": data.get("model_desc"),
        "Fuel Type": data.get("fuel_desc"),
        "Fuel Norms": data.get("norms_desc"),
        "Vehicle Category": data.get("vehicle_catg"),
        
        "Chassis Number (masked)": data.get("chasi_no"),
        "Engine Number (masked)": data.get("eng_no"),

        "Insurance Valid Upto": data.get("insurance_upto"),
        "PUC Valid Upto": data.get("puc_upto"),
        "Fitness Upto": data.get("fit_upto"),
        "Tax Upto": data.get("tax_upto"),

        "Loan / Hypothecation": data.get("financer"),
        "RC Status": data.get("rc_status"),
        "RC Validity": data.get("rc_valid_upto"),

        "developer": "@istgrehu"
    }

    return jsonify(response), 200


# Local run support
if __name__ == "__main__":
    app.run(debug=True)
