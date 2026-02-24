# 🛡️ CyberSurfaceMapper

CyberSurfaceMapper is a security reconnaissance tool developed in Python to evaluate the public-facing attack surface of web domains. The application combines passive header auditing and active port probing to provide a structured security posture assessment through an interactive dashboard.

---

## 🚀 Key Features

### 🔍 Passive Reconnaissance
- Audits HTTP security headers (HSTS, X-Frame-Options, Content-Security-Policy, etc.)
- Detects vulnerabilities such as protocol downgrade risks and clickjacking exposure
- Evaluates HTTPS enforcement and encryption posture

### 🌐 Active Port Probing
- Performs TCP discovery using Python’s `socket` library
- Scans common service ports:
  - SSH (22)
  - FTP (21)
  - MySQL (3306)
  - RDP (3389)
- Identifies potentially exposed network services

### 📊 Risk Assessment Engine
- Aggregates findings into a real-time security rating:
  - ✅ Secure
  - ⚠️ Moderate Risk
  - ❌ High Risk
- Uses custom scoring logic based on exposed services and missing security headers

### 🖥️ Interactive Dashboard
- Built with Streamlit for real-time visualization
- Displays server fingerprints, header analysis, and port audit data
- Dynamic metrics and structured tables for readability

---

## 🛠️ Technical Stack

- **Language:** Python  
- **Framework:** Streamlit  
- **Data Handling:** Pandas  
- **Network Interaction:** Socket, Requests  

---

## 📦 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saumitg26/CyberSurfaceMapper.git
cd CyberSurfaceMapper
```

### 2️⃣ Install Dependencies

Make sure Python 3.9+ is installed, then run:

```bash
pip install streamlit requests pandas
```

### 3️⃣ Launch the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 🧠 Project Significance

CyberSurfaceMapper demonstrates practical understanding of:

- The OSI model and network layers  
- TCP-based service discovery  
- HTTP security headers and encryption standards  
- Attack surface mapping and reconnaissance workflows  
- Bridging CLI-based scanning with visual reporting  

This project reflects applied cybersecurity engineering principles in a user-friendly interface.

---

## 👤 Author

**Saumit Guduguntla**  
Computer Science Student  
George Mason University
