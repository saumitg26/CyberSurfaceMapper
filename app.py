import streamlit as st
import socket
import requests
from datetime import datetime
import pandas as pd

# --- UI Header & Branding ---
st.set_page_config(page_title="Cyber Surface Mapper", page_icon="🛡️", layout="wide")

st.title("🛡️ Cyber Surface Mapper")
st.caption("Developed by Saumit Guduguntla | GMU Cybersecurity Project")

# --- Sidebar Controls ---
with st.sidebar:
    st.header("Scan Settings")
    target = st.text_input("Target Domain", placeholder="scanme.nmap.org")
    scan_btn = st.button("🚀 Launch Recon", use_container_width=True)
    st.divider()
    st.markdown("""
    ### About
    This tool performs **Passive Reconnaissance** (Header Audit) and **Active Probing** (Port Scanning) to identify potential attack surfaces.
    """)

# --- Port Scanning Logic ---
def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

# --- Main Dashboard Logic ---
if scan_btn and target:
    # Clean the target URL logic
    clean_host = target.replace("https://", "").replace("http://", "").split('/')[0]
    
    with st.status("🔍 Initializing Reconnaissance...", expanded=True) as status:
        st.write(f"Testing connectivity to {clean_host}...")
        
        # 1. Header Analysis
        header_data = {}
        try:
            res = requests.get(f"http://{clean_host}", timeout=3)
            header_data['Server'] = res.headers.get('Server', 'Hidden')
            header_data['HSTS'] = "✅ Present" if 'Strict-Transport-Security' in res.headers else "❌ Missing"
            header_data['X-Frame-Options'] = res.headers.get('X-Frame-Options', '❌ Missing')
        except:
            header_data['Error'] = "Failed to reach server."

        # 2. Port Scanning
        ports_to_check = {
            21: "FTP", 22: "SSH", 23: "Telnet", 
            80: "HTTP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"
        }
        port_results = []
        for port, name in ports_to_check.items():
            is_open = scan_port(clean_host, port)
            port_results.append({"Port": port, "Service": name, "Status": "OPEN" if is_open else "CLOSED"})

        status.update(label="Reconnaissance Complete!", state="complete", expanded=False)

    # --- Risk Calculation Logic ---
    risk_points = 0
    if header_data.get('HSTS') == "❌ Missing": risk_points += 1
    if header_data.get('X-Frame-Options') == "❌ Missing": risk_points += 1
    
    open_ports = [p['Port'] for p in port_results if p['Status'] == 'OPEN']
    # High-risk ports if exposed to public web
    dangerous_ports = [21, 23, 3306, 3389]
    for p in open_ports:
        if p in dangerous_ports: risk_points += 2

    # Determine Grade
    if risk_points == 0:
        grade, color = "SECURE", "green"
    elif risk_points <= 2:
        grade, color = "MODERATE RISK", "orange"
    else:
        grade, color = "HIGH RISK", "red"

    # --- Display Results ---
    st.divider()
    st.subheader(f"Security Rating: :{color}[{grade}]")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌐 Server Fingerprint")
        for key, value in header_data.items():
            st.metric(label=key, value=value)

    with col2:
        st.subheader("🚪 Port Audit")
        df = pd.DataFrame(port_results)
        
        def color_status(val):
            color = '#2ecc71' if val == 'OPEN' else '#95a5a6'
            return f'color: {color}; font-weight: bold'
        
        st.table(df.style.applymap(color_status, subset=['Status']))

    st.success(f"Report generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

elif scan_btn and not target:
    st.warning("Please enter a target domain first!")
