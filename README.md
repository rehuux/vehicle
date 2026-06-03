# Vehicle Registration Details API (VAHAN)

**Developer:** Syed Rehan

---

## 📌 Overview

This API provides a clean interface to fetch **vehicle registration details** from the Indian Government's **VAHAN API** (Ministry of Road Transport & Highways). Simply provide an RC (Registration Certificate) number, and get complete vehicle information.

> 🇮🇳 **Legal & Public API** — Uses official Government of India API (apisetu.gov.in)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🚗 **RC Lookup** | Fetch vehicle details by registration number |
| 📋 **Complete Data** | Owner info, vehicle specs, insurance, PUC, tax status |
| 🔓 **No Authentication** | Fully public API — no API key required |
| ⚡ **Fast Response** | Direct government data source |
| 📊 **Clean Output** | Formatted JSON response |
| 🛡️ **Error Handling** | Proper HTTP status codes |

---

## 🔍 How It Works

```

1. User sends RC number to /lookup endpoint
   ↓
2. API validates the registration number
   ↓
3. Calls official VAHAHAN Public API
   ↓
4. Government server returns vehicle data
   ↓
5. API formats and returns clean JSON response

```

---

## 📥 API Endpoint

### Lookup Vehicle Details

```http
GET /lookup?rc=MH01AB1234
```

Query Parameters:

Parameter Type Required Description
rc string ✅ Yes Vehicle registration number (RC)

---

📤 Response Examples

✅ Success (Vehicle Found)

```json
{
  "Registration Number": "MH01AB1234",
  "Registration Date": "15-01-2020",
  "Registration State": "MH",
  "RTO Office": "MH01",
  "Vehicle Class": "MOTOR CAR",
  "Maker": "MARUTI SUZUKI INDIA LTD",
  "Model": "SWIFT",
  "Fuel Type": "PETROL",
  "Fuel Norms": "BS6",
  "Vehicle Category": "LMV",
  "Chassis Number (masked)": "MA3XXXXXX123456",
  "Engine Number (masked)": "K12XXXXX7890",
  "Insurance Valid Upto": "14-01-2025",
  "PUC Valid Upto": "30-12-2024",
  "Fitness Upto": "14-01-2027",
  "Tax Upto": "31-03-2025",
  "Loan / Hypothecation": "HDFC BANK",
  "RC Status": "APPROVED",
  "RC Validity": "14-01-2035",
  "developer": "@istgrehu"
}
```

❌ Missing Parameter

```json
{
  "error": "Missing parameter: rc",
  "developer": "@istgrehu"
}
```

❌ Invalid RC Number

```json
{
  "error": "API error: 404",
  "developer": "@istgrehu"
}
```

---

📊 Available Data Fields

Field Description
Registration Number Vehicle registration number
Registration Date Date of registration
Registration State State code (MH, DL, KA, etc.)
RTO Office Regional Transport Office code
Vehicle Class Type of vehicle (CAR, BIKE, TRUCK, etc.)
Maker Manufacturer name
Model Vehicle model
Fuel Type PETROL / DIESEL / CNG / ELECTRIC
Fuel Norms BS4, BS6, etc.
Vehicle Category LMV, HMV, etc.
Chassis Number (masked) Partially hidden chassis number
Engine Number (masked) Partially hidden engine number
Insurance Valid Upto Insurance expiry date
PUC Valid Upto Pollution certificate expiry date
Fitness Upto Fitness certificate validity
Tax Upto Road tax paid until
Loan / Hypothecation Bank / financier name (if any)
RC Status APPROVED, SUSPENDED, etc.
RC Validity Registration certificate valid until

---

🛠️ Technical Stack

Component Technology
Framework Flask (Python)
HTTP Client Requests
API Source apisetu.gov.in (Government of India)
Port 5000 (default)

---

📥 Installation

Prerequisites

· Python 3.7+
· pip

Setup Steps

```bash
# 1. Clone or create project
mkdir vahan-vehicle-api
cd vahan-vehicle-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install flask requests

# 4. Save the script as app.py

# 5. Run the server
python app.py
```

---

🎮 Usage Examples

Using cURL

```bash
curl "http://localhost:5000/lookup?rc=MH01AB1234"
```

Using Python (Requests)

```python
import requests

response = requests.get(
    'http://localhost:5000/lookup',
    params={'rc': 'MH01AB1234'}
)

data = response.json()
print(data)
```

Using JavaScript (Fetch)

```javascript
fetch('http://localhost:5000/lookup?rc=MH01AB1234')
  .then(res => res.json())
  .then(data => console.log(data));
```

Using Postman

```
Method: GET
URL: http://localhost:5000/lookup?rc=MH01AB1234
```

---

🚀 Deployment

Deploy on Render

```bash
# Create render.yaml
services:
  - type: web
    name: vahan-api
    runtime: python
    buildCommand: pip install flask requests
    startCommand: gunicorn app:app
```

Deploy on Railway

```bash
# Add to railway.toml
[build]
  command = "pip install flask requests gunicorn"

[deploy]
  startCommand = "gunicorn app:app"
```

Deploy on Vercel (with Vercel Flask)

```bash
npm install -g vercel
vercel deploy
```

---

⚠️ Important Notes

Note Explanation
Legal & Public Uses official Government of India open API
No Authentication No API key required
Rate Limits Government API may have limits (check apisetu.gov.in)
Data Accuracy Data comes directly from government RTO records
Masked Numbers Chassis & Engine numbers are partially hidden (privacy)

---

🔒 Privacy & Legal

✅ This API is FULLY LEGAL

· Uses official Government of India public API
· Same data available on Parivahan Sewa website
· No unauthorized data scraping
· For legitimate vehicle verification only

---

🚫 Do Not Use For

Misuse Why
Stalking vehicle owners Privacy violation
Fraudulent activities Criminal offense
Mass data collection May violate rate limits
Selling vehicle data Illegal commercial use

---

📋 Valid RC Number Formats

Format Example
State + RTO + Number MH01AB1234
State + RTO + Letters + Numbers DL1SAA1234
State + RTO + 4-digit KA03N1234

⚠️ Format varies by state. Ensure correct format for your state.

---

🐛 Error Handling

Error Cause Solution
400: Missing parameter No RC provided Add ?rc=NUMBER to URL
404: API error Invalid RC number Check registration number format
500: Request timeout API down or slow Try again later
Connection error No internet Check network connection

---

🔧 Customization Options

Modification How To
Change port app.run(port=8080)
Add logging Add logging module
Cache results Add Redis/memcache
Add rate limiting Use Flask-Limiter
Add frontend UI Create HTML template

---

👨‍💻 Developer

Syed Rehan

---

📄 License

MIT License - Free for legitimate use.

---

📞 Source

Government API: apisetu.gov.in/vahanapi

---

🙏 Credits

· Ministry of Road Transport & Highways (MoRTH)
· National Informatics Centre (NIC)
· Government of India

---

🔄 Future Improvements

· Add caching for frequent lookups
· Support for bulk RC lookup
· Add response pagination
· Optional WhatsApp/Telegram bot integration
· PDF report generation
· Owner name masking for privacy

---


🇮🇳 Built on Indian Government Open Data APIs
