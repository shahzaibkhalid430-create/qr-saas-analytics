import streamlit as st
import pandas as pd
import qrcode
from PIL import Image
import io
import cv2
import numpy as np

# Page Configuration - Premium Enterprise Look
st.set_page_config(
    page_title="ScanPulse - Advanced QR & Barcode Micro-SaaS",
    page_icon="🔍",
    layout="wide"
)

# Custom Styling for a Corporate Digital Product
st.markdown("""
    <style>
    .main-title { font-size: 36px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .subtitle { font-size: 18px; color: #4B5563; margin-bottom: 25px; }
    .feature-header { font-size: 22px; font-weight: bold; color: #1E3A8A; margin-top: 15px; }
    .scanned-box { padding: 15px; background-color: #D1FAE5; border-left: 5px solid #10B981; border-radius: 4px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation Control
st.sidebar.markdown("<h2 style='color: #1E3A8A;'>🛡️ ScanPulse Tech</h2>", unsafe_allow_html=True)
st.sidebar.markdown("`v1.0.0 Enterprise Asset` 🚀")
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Select Platform Module:",
    ["📊 Analytics Dashboard", "📷 Live Web-Cam Scanner", "🖼️ Bulk Image Upload", "✨ Premium QR Generator"]
)

# Shared Mock Data State Initialization
if "scans_log" not in st.session_state:
    st.session_state.scans_log = [
        {"Timestamp": "2026-06-29 11:30", "Scan Source": "Mobile iOS", "Target URL/Data": "https://google.com", "Status": "✅ Safe"},
        {"Timestamp": "2026-06-29 11:15", "Scan Source": "Android App", "Target URL/Data": "https://stripe.com", "Status": "✅ Safe"},
        {"Timestamp": "2026-06-29 10:45", "Scan Source": "Bulk Image upload", "Target URL/Data": "Inventory_ID_9082", "Status": "📦 Logged"},
    ]

# ---------------- MODULE 1: ANALYTICS DASHBOARD ----------------
if menu == "📊 Analytics Dashboard":
    st.markdown('<div class="main-title">SaaS Analytics & Scanning Trends</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Monitor system-wide metric distribution and commercial client logs</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total System Scans", f"{len(st.session_state.scans_log) + 1245}", "+14% This Week")
    col2.metric("Unique Assets Tracked", "142", "All Verified Safe")
    col3.metric("Quishing/Fraud Alerts", "0", "Clean System Scan")
    col4.metric("Bulk CSV Exports", "32 Files", "Enterprise Tier")
    
    st.write("---")
    st.subheader("📈 Live Traffic Distribution Data")
    df = pd.DataFrame(st.session_state.scans_log)
    st.dataframe(df, use_container_width=True)

# ---------------- MODULE 2: LIVE WEB-CAM SCANNER ----------------
elif menu == "📷 Live Web-Cam Scanner":
    st.markdown('<div class="main-title">Enterprise Web-Cam Scanner</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Utilize the universal browser-client camera feed to decode QR codes dynamically</div>', unsafe_allow_html=True)
    
    img_file_buffer = st.camera_input("Scan a QR Code")
    if img_file_buffer is not None:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
        
        if data:
            st.markdown(f"""
            <div class="scanned-box">
                <h4 style="margin:0; color:#065F46;">🎯 Successfully Decoded Asset:</h4>
                <p style="margin:5px 0 0 0; font-size:18px; font-weight:bold; color:#047857;">{data}</p>
            </div>
            """, unsafe_allow_html=True)
            if data.startswith("http"):
                st.write(f"🔗 [Click here to open target URL]({data})")
        else:
            st.warning("⚠️ Image received but no QR pattern detected.")

# ---------------- MODULE 3: BULK IMAGE UPLOAD (FIXED ERROR) ----------------
elif menu == "🖼️ Bulk Image Upload":
    st.markdown('<div class="main-title">Static Batch Processing</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Upload pre-captured corporate assets to parse encoded details</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Choose a QR image file...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Load via PIL
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Asset Image', width=300)
        
        # Convert PIL Image safely to OpenCV Format (RGB to BGR NumPy Array)
        cv2_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Core Decoding Engine
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
        
        if data:
            st.markdown(f"""
            <div class="scanned-box">
                <h4 style="margin:0; color:#065F46;">🎯 Decoded QR Content:</h4>
                <p style="margin:5px 0 0 0; font-size:18px; font-weight:bold; color:#047857;">{data}</p>
            </div>
            """, unsafe_allow_html=True)
            if data.startswith("http"):
                st.markdown(f"🔗 **[Open Target Link]({data})**")
        else:
            st.warning("⚠️ Image loaded successfully, but OpenCV could not detect a valid QR code pattern. Please try a clearer high-contrast image.")

# ---------------- MODULE 4: PREMIUM QR GENERATOR ----------------
elif menu == "✨ Premium QR Generator":
    st.markdown('<div class="main-title">Custom Brand QR Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Create personalized, color-coded, high-resolution QR assets</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        qr_data = st.text_input("Enter Destination URL or Data:", "https://khetify.com")
        fill_color = st.color_picker("Choose QR Code Color (Foreground):", "#1E3A8A")
        back_color = st.color_picker("Choose Background Color:", "#FFFFFF")
        box_size = st.slider("QR Code Resolution (Box Size):", 5, 20, 10)
        
    with col2:
        st.markdown('<div class="feature-header">Live Preview</div>', unsafe_allow_html=True)
        if qr_data:
            qr = qrcode.QRCode(version=1, box_size=box_size, border=4)
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.image(byte_im, caption="Generated Enterprise Asset", width=250)
            st.download_button(
                label="📥 Download High-Res PNG",
                data=byte_im,
                file_name="scanpulse_qr.png",
                mime="image/png"
            )