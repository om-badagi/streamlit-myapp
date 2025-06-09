import streamlit as st

st.set_page_config(page_title="Axial Position Calculator", layout="wide")

st.title("🔧 Axial Position Calculator")

# Two columns for inputs
col1, col2 = st.columns(2)

with col1:
    sensorDirection = st.selectbox("Sensor Direction", ["up", "down"])
    directionMultiplier = 1 if sensorDirection == "up" else -1

    referenceDistance = st.number_input("Reference Distance (mm)", value=900)
    currentReading = st.number_input("Current Laser Reading (mm)", value=727)

with col2:
    st.subheader("Reference Values (mm)")
    UL = st.number_input("UL", value=1.6, step=0.1)
    UR = st.number_input("UR", value=3.4, step=0.1)
    DL = st.number_input("DL", value=2.0, step=0.1)
    DR = st.number_input("DR", value=3.0, step=0.1)

# --- Calculations ---
delta_t = currentReading - referenceDistance

DL_t = DL - (delta_t * directionMultiplier)
DR_t = DR - (delta_t * directionMultiplier)
UL_t = UL + (delta_t * directionMultiplier)
UR_t = UR + (delta_t * directionMultiplier)

RAP = (DR_t - UR_t) / 2
LAP = (DL_t - UL_t) / 2
AP = (LAP + RAP) / 2

# Two columns for results
res1, res2 = st.columns(2)

with res1:
    st.header("📊 Results")
    st.markdown(f"**Direction Multiplier (DM)**: `{directionMultiplier}`")
    st.markdown(f"**Delta_t** = `{currentReading} - {referenceDistance} = {delta_t:.1f} mm`")

    st.subheader("Current Positions:")
    st.markdown(f"- UL_t = {UL_t:.2f} mm")
    st.markdown(f"- UR_t = {UR_t:.2f} mm")
    st.markdown(f"- DL_t = {DL_t:.2f} mm")
    st.markdown(f"- DR_t = {DR_t:.2f} mm")

with res2:
    st.subheader("Axial Positions:")
    st.success(f"Right Axial Position (RAP): {RAP:.2f} mm")
    st.success(f"Left Axial Position (LAP): {LAP:.2f} mm")
    st.info(f"Overall Axial Position (AP): {AP:.2f} mm")

    st.subheader("📘 Formula Summary")
    st.code(f"""
DL_t = DL_ref - (delta_t × DM) = {DL} - ({delta_t:.1f} × {directionMultiplier})
DR_t = DR_ref - (delta_t × DM) = {DR} - ({delta_t:.1f} × {directionMultiplier})
UL_t = UL_ref + (delta_t × DM) = {UL} + ({delta_t:.1f} × {directionMultiplier})
UR_t = UR_ref + (delta_t × DM) = {UR} + ({delta_t:.1f} × {directionMultiplier})
""")
