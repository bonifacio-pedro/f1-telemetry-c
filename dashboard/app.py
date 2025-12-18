import streamlit as st
import fastf1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# =============================
# CONFIG
# =============================
st.set_page_config(
    page_title="F1 Telemetry Dashboard",
    layout="wide"
)

fastf1.Cache.enable_cache('cache')

# =============================
# SIDEBAR
# =============================
st.sidebar.title("🏎️ F1 Telemetry")

year = st.sidebar.selectbox("Season", [2024])
race = st.sidebar.selectbox("Race", ["Brazil"])
session_type = st.sidebar.selectbox("Session", ["R", "Q"])

driver_a = st.sidebar.selectbox("Driver A", ["HAM", "VER"], index=0)
driver_b = st.sidebar.selectbox("Driver B", ["VER", "HAM"], index=1)

smooth = st.sidebar.checkbox("Smooth ΔSpeed", value=False)

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data(year, race, session_type, d1, d2):
    session = fastf1.get_session(year, race, session_type)
    session.load()

    laps_a = session.laps.pick_drivers(d1).pick_fastest()
    laps_b = session.laps.pick_drivers(d2).pick_fastest()

    tel_a = laps_a.get_telemetry()
    tel_b = laps_b.get_telemetry()

    return tel_a, tel_b

tel_a, tel_b = load_data(year, race, session_type, driver_a, driver_b)

# =============================
# ALIGN TELEMETRY
# =============================
df = pd.DataFrame()
df["RelDist"] = tel_a.RelativeDistance
df["Speed_A"] = tel_a.Speed

interp_b = interp1d(
    tel_b.RelativeDistance,
    tel_b.Speed,
    bounds_error=False,
    fill_value="extrapolate"
)

df["Speed_B"] = interp_b(df["RelDist"])
df["DeltaSpeed"] = df["Speed_A"] - df["Speed_B"]

if smooth:
    df["DeltaSpeed"] = df["DeltaSpeed"].rolling(15, center=True).mean()

# =============================
# METRICS
# =============================
a_pct = (df.DeltaSpeed >= 0).mean() * 100
b_pct = (df.DeltaSpeed < 0).mean() * 100

# =============================
# HEADER
# =============================
st.title("📊 F1 Telemetry Comparison")
st.subheader(f"{driver_a} vs {driver_b} — {race} {year}")

col1, col2 = st.columns(2)
col1.metric(driver_a, f"{a_pct:.2f}%".replace(".", ","))
col2.metric(driver_b, f"{b_pct:.2f}%".replace(".", ","))

# =============================
# SPEED COMPARISON
# =============================
st.markdown("### 🚀 Speed Comparison")

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(df.RelDist, df.Speed_A, label=driver_a)
ax.plot(df.RelDist, df.Speed_B, label=driver_b)
ax.set_ylabel("Speed (km/h)")
ax.set_xlabel("Relative Distance")
ax.legend()
st.pyplot(fig)

# =============================
# DELTA SPEED
# =============================
st.markdown("### 📉 ΔSpeed (A − B)")

fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(df.RelDist, df.DeltaSpeed)
ax.axhline(0, linestyle="--")
ax.set_ylabel("ΔSpeed (km/h)")
ax.set_xlabel("Relative Distance")
st.pyplot(fig)

# =============================
# SECTOR ANALYSIS
# =============================
st.markdown("### 🧩 Sector Analysis")

s1 = df[df.RelDist < 0.33]
s2 = df[(df.RelDist >= 0.33) & (df.RelDist < 0.67)]
s3 = df[df.RelDist >= 0.67]

sector_data = pd.DataFrame({
    "Sector": ["S1", "S2", "S3"],
    driver_a: [
        (s1.DeltaSpeed >= 0).mean() * 100,
        (s2.DeltaSpeed >= 0).mean() * 100,
        (s3.DeltaSpeed >= 0).mean() * 100,
    ],
    driver_b: [
        (s1.DeltaSpeed < 0).mean() * 100,
        (s2.DeltaSpeed < 0).mean() * 100,
        (s3.DeltaSpeed < 0).mean() * 100,
    ],
})

st.dataframe(
    sector_data.style.format(
        {
            driver_a: "{:.1f}%",
            driver_b: "{:.1f}%"
        }
    )
)


# =============================
# BRAKE & THROTTLE
# =============================
st.markdown("### 🛑 Brake & Throttle")

fig, axs = plt.subplots(2, 1, figsize=(14, 6), sharex=True)

axs[0].plot(tel_a.RelativeDistance, tel_a.Brake, label=driver_a)
axs[0].plot(tel_b.RelativeDistance, tel_b.Brake, label=driver_b)
axs[0].set_ylabel("Brake")
axs[0].legend()

axs[1].plot(tel_a.RelativeDistance, tel_a.Throttle, label=driver_a)
axs[1].plot(tel_b.RelativeDistance, tel_b.Throttle, label=driver_b)
axs[1].set_ylabel("Throttle")
axs[1].set_xlabel("Relative Distance")

st.pyplot(fig)

# =============================
# TRACK MAP DATA
# =============================
track_df = pd.DataFrame()
track_df["X"] = tel_a.X
track_df["Y"] = tel_a.Y
track_df["RelDist"] = tel_a.RelativeDistance

interp_b_speed = interp1d(
    tel_b.RelativeDistance,
    tel_b.Speed,
    bounds_error=False,
    fill_value="extrapolate"
)

track_df["Speed_A"] = tel_a.Speed
track_df["Speed_B"] = interp_b_speed(track_df["RelDist"])
track_df["DeltaSpeed"] = track_df["Speed_A"] - track_df["Speed_B"]

st.markdown("### 🗺️ Track Map — Who Is Faster")

fig, ax = plt.subplots(figsize=(3, 3), dpi=150)

a_faster = track_df[track_df.DeltaSpeed >= 0]
b_faster = track_df[track_df.DeltaSpeed < 0]

ax.scatter(
    a_faster.X,
    a_faster.Y,
    s=2,
    alpha=0.8,
    label=f"{driver_a}",
)

ax.scatter(
    b_faster.X,
    b_faster.Y,
    s=2,
    alpha=0.8,
    label=f"{driver_b}",
)

ax.set_aspect("equal", adjustable="box")
ax.axis("off")
ax.legend(
    loc="upper right",
    fontsize=6,
    frameon=False,
    markerscale=2
)

plt.tight_layout(pad=0.2)
st.pyplot(fig, use_container_width=False)
