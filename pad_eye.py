
import streamlit as st
import math

shackle_data = {
    # G213 series (15 entries)
    "G213 - 1/2T":   {"SWL": 0.50,  "Jaw Width": 11.9,   "Pin Diameter": 7.9,   "Inside Length": 28.7},
    "G213 - 3/4T":   {"SWL": 0.75,  "Jaw Width": 13.5,   "Pin Diameter": 9.7,   "Inside Length": 31.0},
    "G213 - 1T":     {"SWL": 1,     "Jaw Width": 16.8,   "Pin Diameter": 11.2,  "Inside Length": 36.6},
    "G213 - 1-1/2T": {"SWL": 1.50,  "Jaw Width": 19.1,   "Pin Diameter": 12.7,  "Inside Length": 42.9},
    "G213 - 2T":     {"SWL": 2,     "Jaw Width": 20.6,   "Pin Diameter": 16,    "Inside Length": 47.8},
    "G213 - 3-1/4T": {"SWL": 3.25,  "Jaw Width": 26.9,   "Pin Diameter": 19.1,  "Inside Length": 60.5},
    "G213 - 4-3/4T": {"SWL": 4.75,  "Jaw Width": 31.8,   "Pin Diameter": 22.4,  "Inside Length": 71.5},
    "G213 - 6-1/2T": {"SWL": 6.50,  "Jaw Width": 36.6,   "Pin Diameter": 25.4,  "Inside Length": 84},
    "G213 - 8-1/2T": {"SWL": 8.50,  "Jaw Width": 42.9,   "Pin Diameter": 28.7,  "Inside Length": 95.5},
    "G213 - 9-1/2T": {"SWL": 9.50,  "Jaw Width": 46.0,   "Pin Diameter": 31.8,  "Inside Length": 108},
    "G213 - 12T":    {"SWL": 12,    "Jaw Width": 51.5,   "Pin Diameter": 35.1,  "Inside Length": 119},
    "G213 - 13-1/2T":{"SWL": 13.50, "Jaw Width": 57,     "Pin Diameter": 38.1,  "Inside Length": 133},
    "G213 - 17T":    {"SWL": 17,    "Jaw Width": 60.5,   "Pin Diameter": 41.4,  "Inside Length": 146},
    "G213 - 25T":    {"SWL": 25,    "Jaw Width": 73,     "Pin Diameter": 51,    "Inside Length": 178},
    "G213 - 35T":    {"SWL": 35,    "Jaw Width": 82.5,   "Pin Diameter": 57,    "Inside Length": 197},

    # G209 series (17 entries)
    "G209 - 1/3T":   {"SWL": 0.33,  "Jaw Width": 9.65,   "Pin Diameter": 6.35,  "Inside Length": 22.4},
    "G209 - 1/2T":   {"SWL": 0.50,  "Jaw Width": 11.9,   "Pin Diameter": 7.85,  "Inside Length": 28.7},
    "G209 - 3/4T":   {"SWL": 0.75,  "Jaw Width": 13.5,   "Pin Diameter": 9.65,  "Inside Length": 31},
    "G209 - 1T":     {"SWL": 1,     "Jaw Width": 16.8,   "Pin Diameter": 11.2,  "Inside Length": 36.6},
    "G209 - 1-1/2T": {"SWL": 1.50,  "Jaw Width": 19.1,   "Pin Diameter": 12.7,  "Inside Length": 42.9},
    "G209 - 2T":     {"SWL": 2,     "Jaw Width": 20.6,   "Pin Diameter": 16,    "Inside Length": 47.8},
    "G209 - 3-1/4T": {"SWL": 3.25,  "Jaw Width": 26.9,   "Pin Diameter": 19.1,  "Inside Length": 60.5},
    "G209 - 4-3/4T": {"SWL": 4.75,  "Jaw Width": 31.8,   "Pin Diameter": 22.4,  "Inside Length": 71.5},
    "G209 - 6-1/2T": {"SWL": 6.50,  "Jaw Width": 36.6,   "Pin Diameter": 25.4,  "Inside Length": 84},
    "G209 - 8-1/2T": {"SWL": 8.50,  "Jaw Width": 42.9,   "Pin Diameter": 28.7,  "Inside Length": 95.5},
    "G209 - 9-1/2T": {"SWL": 9.50,  "Jaw Width": 46.0,   "Pin Diameter": 31.8,  "Inside Length": 108},
    "G209 - 12T":    {"SWL": 12,    "Jaw Width": 51.5,   "Pin Diameter": 35.1,  "Inside Length": 119},
    "G209 - 13-1/2T":{"SWL": 13.50, "Jaw Width": 57,     "Pin Diameter": 38.1,  "Inside Length": 133},
    "G209 - 17T":    {"SWL": 17,    "Jaw Width": 60.5,   "Pin Diameter": 41.4,  "Inside Length": 146},
    "G209 - 25T":    {"SWL": 25,    "Jaw Width": 73,     "Pin Diameter": 51,    "Inside Length": 178},
    "G209 - 35T":    {"SWL": 35,    "Jaw Width": 82.5,   "Pin Diameter": 57,    "Inside Length": 197},
    "G209 - 55T":    {"SWL": 55,    "Jaw Width": 105,    "Pin Diameter": 70,    "Inside Length": 267},

    # G2130 series (20 entries)
    "G2130 - 1/3T":   {"SWL": 0.33,  "Jaw Width": 9.65,  "Pin Diameter": 6.35,  "Inside Length": 22.4},
    "G2130 - 1/2T":   {"SWL": 0.50,  "Jaw Width": 11.9,  "Pin Diameter": 7.85,  "Inside Length": 28.7},
    "G2130 - 3/4T":   {"SWL": 0.75,  "Jaw Width": 13.5,  "Pin Diameter": 9.65,  "Inside Length": 31},
    "G2130 - 1T":     {"SWL": 1,     "Jaw Width": 16.8,  "Pin Diameter": 11.2,  "Inside Length": 36.6},
    "G2130 - 1-1/2T": {"SWL": 1.50,  "Jaw Width": 19.1,  "Pin Diameter": 12.7,  "Inside Length": 42.9},
    "G2130 - 2T":     {"SWL": 2,     "Jaw Width": 20.6,  "Pin Diameter": 16,    "Inside Length": 47.8},
    "G2130 - 3-1/4T": {"SWL": 3.25,  "Jaw Width": 26.9,  "Pin Diameter": 19.1,  "Inside Length": 60.5},
    "G2130 - 4-3/4T": {"SWL": 4.75,  "Jaw Width": 31.8,  "Pin Diameter": 22.4,  "Inside Length": 71.5},
    "G2130 - 6-1/2T": {"SWL": 6.50,  "Jaw Width": 36.6,  "Pin Diameter": 25.4,  "Inside Length": 84},
    "G2130 - 8-1/2T": {"SWL": 8.50,  "Jaw Width": 42.9,  "Pin Diameter": 28.7,  "Inside Length": 95.5},
    "G2130 - 9-1/2T": {"SWL": 9.50,  "Jaw Width": 46,    "Pin Diameter": 31.8,  "Inside Length": 108},
    "G2130 - 12T":    {"SWL": 12,    "Jaw Width": 51.5,  "Pin Diameter": 35.1,  "Inside Length": 119},
    "G2130 - 13-1/2T":{"SWL": 13.50, "Jaw Width": 57,    "Pin Diameter": 38.1,  "Inside Length": 133},
    "G2130 - 17T":    {"SWL": 17,    "Jaw Width": 60.5,  "Pin Diameter": 41.4,  "Inside Length": 146},
    "G2130 - 25T":    {"SWL": 25,    "Jaw Width": 73,    "Pin Diameter": 51,    "Inside Length": 178},
    "G2130 - 35T":    {"SWL": 35,    "Jaw Width": 82.5,  "Pin Diameter": 57,    "Inside Length": 197},
    "G2130 - 55T":    {"SWL": 55,    "Jaw Width": 105,   "Pin Diameter": 70,    "Inside Length": 267},
    "G2130 - 85T":    {"SWL": 85,    "Jaw Width": 127,   "Pin Diameter": 82.5,  "Inside Length": 330},
    "G2130 - 120T":   {"SWL": 120,   "Jaw Width": 133,   "Pin Diameter": 95.5,  "Inside Length": 372},
    "G2130 - 150T":   {"SWL": 150,   "Jaw Width": 140,   "Pin Diameter": 108,   "Inside Length": 368},

    # G2140 series (21 entries)
    "G2140 - 2T":      {"SWL": 2,     "Jaw Width": 16.8,  "Pin Diameter": 11.2,  "Inside Length": 36.6},
    "G2140 - 2.67T":   {"SWL": 2.67,  "Jaw Width": 19.1,  "Pin Diameter": 12.7,  "Inside Length": 42.9},
    "G2140 - 3.33T":   {"SWL": 3.33,  "Jaw Width": 20.6,  "Pin Diameter": 16.3,  "Inside Length": 47.8},
    "G2140 - 5T":      {"SWL": 5,     "Jaw Width": 26.9,  "Pin Diameter": 19.6,  "Inside Length": 60.5},
    "G2140 - 7T":      {"SWL": 7,     "Jaw Width": 31.8,  "Pin Diameter": 22.6,  "Inside Length": 71.4},
    "G2140 - 9.5T":    {"SWL": 9.5,   "Jaw Width": 36.6,  "Pin Diameter": 25.9,  "Inside Length": 84.1},
    "G2140 - 12.5T":   {"SWL": 12.5,  "Jaw Width": 42.9,  "Pin Diameter": 29.2,  "Inside Length": 95.3},
    "G2140 - 15T":     {"SWL": 15,    "Jaw Width": 46,    "Pin Diameter": 31.8,  "Inside Length": 108},
    "G2140 - 18T":     {"SWL": 18,    "Jaw Width": 51.6,  "Pin Diameter": 35.6,  "Inside Length": 119.1},
    "G2140 - 21T":     {"SWL": 21,    "Jaw Width": 57.2,  "Pin Diameter": 38.9,  "Inside Length": 133.4},
    "G2140 - 30T":     {"SWL": 30,    "Jaw Width": 60.5,  "Pin Diameter": 41.4,  "Inside Length": 146},
    "G2140 - 40T":     {"SWL": 40,    "Jaw Width": 73.2,  "Pin Diameter": 50.8,  "Inside Length": 178},
    "G2140 - 55T":     {"SWL": 55,    "Jaw Width": 82.6,  "Pin Diameter": 57.2,  "Inside Length": 197},
    "G2140 - 85T":     {"SWL": 85,    "Jaw Width": 105,   "Pin Diameter": 69.9,  "Inside Length": 267},
    "G2140 - 120T":    {"SWL": 120,   "Jaw Width": 127,   "Pin Diameter": 82.6,  "Inside Length": 330},
    "G2140 - 150T":    {"SWL": 150,   "Jaw Width": 133,   "Pin Diameter": 95.3,  "Inside Length": 372},
    "G2140 - 175T":    {"SWL": 175,   "Jaw Width": 140,   "Pin Diameter": 108,   "Inside Length": 368},
    "G2140 - 200T":    {"SWL": 200,   "Jaw Width": 184,   "Pin Diameter": 121,   "Inside Length": 386},
    "G2140 - 250T":    {"SWL": 250,   "Jaw Width": 216,   "Pin Diameter": 127,   "Inside Length": 470},
    "G2140 - 300T":    {"SWL": 300,   "Jaw Width": 213,   "Pin Diameter": 152,   "Inside Length": 475},
    "G2140 - 400T":    {"SWL": 400,   "Jaw Width": 210,   "Pin Diameter": 178,   "Inside Length": 572}
}

st.title("Pad-Eye Design & Shackle Selection Tool")
st.markdown("Enter all design parameters:")

# ---------------------------------------------------------
# 1: Loading Inputs
# ---------------------------------------------------------
st.header("1: Loading Inputs")
Ps    = st.number_input("Static sling load (Ps) in kN:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
DAF   = st.number_input("Dynamic Amplification Factor,DAF (f):", value=0.0, min_value=0.0, step=0.1, format="%.2f")
theta = st.number_input("Loading angle with horizontal (θ) in degrees:", value=0.0, min_value=0.0, max_value=90.0, step=0.1, format="%.2f")
phi   = st.number_input("Sling's out-of-plane angle with pad-eye (φ) in degrees:", value=0.0, min_value=0.0, max_value=90.0, step=0.1, format="%.2f")
fop   = st.number_input("Additional out-of-plane load percentage (fop) in %:", value=0.0, min_value=0.0, step=0.1, format="%.2f")

# ---------------------------------------------------------
# 2: Shackle Details
# ---------------------------------------------------------
# Section 2: Shackle Details (Dropdown + Auto-Update)
st.header("2: Shackle Details")

# Dropdown to select a shackle type from our full dictionary.
selected_shackle = st.selectbox("Select a Shackle Type:", list(shackle_data.keys()))

# Conversion factor: 1 metric ton (MT) = 10 kN 
conversion_factor = 10

# Get SWL in MT from the dictionary and convert to kN.
Psh_mt = shackle_data[selected_shackle]["SWL"]
Psh = Psh_mt * conversion_factor

# Use the other parameters directly from the dictionary (they are in mm)
A_val = shackle_data[selected_shackle]["Jaw Width"]
B_val = shackle_data[selected_shackle]["Pin Diameter"]
C_val = shackle_data[selected_shackle]["Inside Length"]

# Display the auto-filled values
st.write(f"**SWL of Shackle:** {Psh:.2f} kN")
st.write(f"**Jaw Width (B):** {B_val:.2f} mm")
st.write(f"**Pin Diameter (A):** {A_val:.2f} mm")
st.write(f"**Inside Length (C):** {C_val:.2f} mm")

# ---------------------------------------------------------
# 3: Rope/Sling Details
# ---------------------------------------------------------
st.header("3: Rope/Sling Details")
fr  = st.number_input("FOS against MBL of rope (fr):", value=0.0, min_value=0.0, step=0.1, format="%.2f")
MBL = st.number_input("MBL of rope required (MBL) in kN:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
dr  = st.number_input("Rope Diameter selected (dr) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")

# ---------------------------------------------------------
# 4: Pad-Eye Dimensions and Shackle Compatibility
# ---------------------------------------------------------
st.header("4: Pad-Eye Dimensions and Shackle Compatibility")
fy   = st.number_input("Yield Strength of Pad-Eye Plate (fy) in MPa:", value=0.0, min_value=0.0, step=10.0, format="%.2f")
dh   = st.number_input("Diameter of Pad-Eye Hole (dh) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
R    = st.number_input("Radius of Main Plate (R) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
T    = st.number_input("Thickness of Main Plate (T) in mm:", value=00.0, min_value=0.0, step=0.1, format="%.2f")
r_val = st.number_input("Radius of Cheek Plate (r) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
t_val = st.number_input("Thickness of Cheek Plate (t) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
min_spread = st.number_input("Minimum Shackle Spread Percentage required (%):", value=0.0, min_value=0.0, step=0.1, format="%.2f")
twc  = st.number_input("Weld thickness between Cheek Plate and Pad-Eye Plate (twc) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")
l_val = st.number_input("Base Length of Pad-Eye (l) in mm:", value=00.0, min_value=0.0, step=0.1, format="%.2f")
e_val = st.number_input("Eccentricity of Pad-Eye Hole from Base (e) in mm:", value=0.0, min_value=0.0, step=0.1, format="%.2f")

# ---------------------------------------------------------
# Derived Geometry Calculations
# ---------------------------------------------------------
st.header("Derived Geometry Information")
min_inside_length_required = 1.5 * dr
actual_inside_length = C_val - (R - (dh / 2))
jaw_width_clearance = A_val - (T + 2*t_val)
actual_shackle_spread_pct = ((T + 2*t_val) / A_val) * 100 if A_val != 0 else 0

if st.button("Compute Derived Geometry & Design Checks"):
    st.subheader("Derived Geometry Calculations")
    st.write(f"Minimum Inside Length Clearance Required: {min_inside_length_required:.2f} mm")
    st.write(f"Actual Inside Length Clearance Provided: {actual_inside_length:.2f} mm")
    st.write(f"Pin Diameter Clearance Provided: {jaw_width_clearance:.2f} mm")
    st.write(f"Actual Shackle Spread Percentage: {actual_shackle_spread_pct:.2f} %")
    
    # ---------------------------------------------------------
    # Section 2: Design Calculations
    # ---------------------------------------------------------
    st.header("DESIGN CALCULATIONS")
    rad_theta = math.radians(theta)
    rad_phi = math.radians(phi)
    P = Ps * DAF
    Pv = P * math.sin(rad_theta)
    Ph = P * math.cos(rad_theta) * math.cos(rad_phi)
    Po = P * math.cos(rad_theta) * math.sin(rad_phi) + (fop / 100.0) * P

    st.subheader("Computed Design Loads")
    st.write(f"Design Dynamic Load (P): {P:.2f} kN")
    st.write(f"In-plane Vertical Force (Pv): {Pv:.2f} kN")
    st.write(f"In-plane Horizontal Force (Ph): {Ph:.2f} kN")
    st.write(f"Out-of-plane Force (Po): {Po:.2f} kN")
    max_force = max(abs(Pv), abs(Ph), abs(Po))
    st.write(f"Maximum Applied Force Component: {max_force:.2f} kN")
    
    # 2.1 Bearing Check
    Ab = B_val * (T + 2*t_val)  # in mm²
    fby = 0.9 * fy          # in MPa (N/mm²)
    Pb_kN = (Ab * fby) / 1000.0  # convert N to kN
    st.subheader("Bearing Check")
    st.write(f"Allowable Bearing Load (Pb): {Pb_kN:.2f} kN")
    if max_force <= Pb_kN:
        st.success("Bearing Check PASSED.")
    else:
        st.error("Bearing Check FAILED.")
    
    # 2.2 Pull-Out Shear Check
    Av = 2 * (((R - dh/2) * T) + (2 * (r_val - dh/2) * t_val))
    fv = 0.4 * fy
    pullout_load_kN = Av * fv / 1000.0
    st.subheader("Pull-Out Shear Check")
    st.write(f"Pull-Out Shear Area (Av): {Av:.2f} mm²")
    st.write(f"Allowable Pull-Out Load: {pullout_load_kN:.2f} kN")
    
    # 2.3 Tear Out Stress Check
    At = (2 * R - dh) * T + 2 * (2 * r_val - dh) * t_val
    ft = 0.45 * fy
    tear_load_kN = At * ft / 1000.0
    st.subheader("Tear Out Stress Check")
    st.write(f"Tear Out Resisting Area (At): {At:.2f} mm²")
    st.write(f"Allowable Tearing Load: {tear_load_kN:.2f} kN")
    
    # 2.4 Tensile Stress Check
    Ate = 2 * R * T
    fte = 0.6 * fy
    tensile_load_kN = Ate * fte / 1000.0
    st.subheader("Tensile Stress Check")
    st.write(f"Tensile Resisting Area (Ate): {Ate:.2f} mm²")
    st.write(f"Allowable Tensile Load: {tensile_load_kN:.2f} kN")
    
    # 2.6 Pad-Eye Base Check (Simplified Calculation)
    Aba = l_val * T  		      		# Axial area in mm²
    I_ip = (T * (l_val**3)) / 12.0    		# In-plane moment of inertia
    I_op = (l_val * (T**3)) / 12.0    		# Out-of-plane moment of inertia
    Zip = I_ip / (l_val/2.0) if l_val != 0 else float('inf')
    Zop = I_op / (T/2.0) if T != 0 else float('inf')
    
    fa = (Pv * 1000.0) / Aba
    fbip = (Ph * 1000.0 * e_val) / Zip if Zip != 0 else float('inf')
    fbop = (Po * 1000.0 * e_val) / Zop if Zop != 0 else float('inf')
    tau_ip = (Ph * 1000.0) / Aba
    tau_op = (Po * 1000.0) / Aba
    tau_combined = tau_ip + tau_op
    sigma_vm = math.sqrt(fa**2 + fbip**2 + fbop**2 + tau_combined**2)
    allowable_vm = 0.7 * fy
    st.subheader("Pad-Eye Base Check")
    st.write(f"Axial Area (Aba): {Aba:.2f} mm²")
    st.write(f"Von-Mises Stress: {sigma_vm:.2f} MPa")
    st.write(f"Allowable Von-Mises Stress: {allowable_vm:.2f} MPa")
    if sigma_vm <= allowable_vm:
        st.success("Pad-Eye Base Check PASSED.")
    else:
        st.error("Pad-Eye Base Check FAILED.")
    
    # 2.7 Weld Check Between Pad-Eye and Cheek Plate
    st.subheader("Weld Check")
    if (T + 2*t_val) != 0:
        Pc = P * (t_val / (T + 2*t_val))
    else:
        Pc = 0
    if r_val > 0 and twc > 0:
        Awc = 0.5 * (2 * math.pi * r_val) * (0.707 * twc)
        tau_wc = (Pc * 1000.0) / Awc
        allowable_weld = 0.3 * 70 * 6.895  # Approximately 144.8 MPa

        
        st.write(f"Weld Stress (τ_wc): {tau_wc:.2f} MPa")
        st.write(f"Allowable Weld Stress: {allowable_weld:.2f} MPa")
        if tau_wc <= allowable_weld:
            st.success("Weld Check PASSED.")
        else:
            st.error("Weld Check FAILED.")
    else:
        st.warning("Weld Check not applicable (ensure r and twc are > 0).")
    
    # ---------------------------------------------------------
    # Shackle Selection Recommendation
    # ---------------------------------------------------------
    st.header("Shackle Selection")
    if P <= Psh:
        st.success(f"Recommended Shackle: {selected_shackle} with SWL {Psh:.2f} kN is adequate for the design load ({P:.2f} kN).")
    else:
        st.error(f"Warning: {selected_shackle} with SWL {Psh:.2f} kN is NOT adequate (design load = {P:.2f} kN). Consider a higher-capacity shackle.")
