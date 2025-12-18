# 🏎️ F1 Telemetry Analysis in C

![Formula 1](https://img.shields.io/badge/F1-Telemetry-red)
![Language](https://img.shields.io/badge/Language-C-blue)
![Python](https://img.shields.io/badge/Python-FastF1-green)

📋 Overview
Professional-grade F1 telemetry analysis tool that processes real race data to identify driver behavior patterns, compare performance between drivers, and detect racing states. Built with automotive software principles in mind.
This project demonstrates:

✅ Multi-driver telemetry comparison (VER vs HAM)
✅ Speed delta analysis with interpolation
✅ Real-time state detection algorithm
✅ CSV parsing and processing in C
✅ Data extraction from F1 API (FastF1)
✅ Professional visualization and reporting
✅ Automotive data analysis skills

## 🎯 Key Features
1. Driver Comparison System

Compare telemetry between any two F1 drivers
Speed, throttle, and brake analysis side-by-side
Automatic best lap detection
Visual overlap comparison

2. Delta Analysis

Speed delta calculation with scipy interpolation
Percentage breakdown: who was faster where
Sector-by-sector analysis (3 sectors)
Top 5 advantage points for each driver

3. State Detection Algorithm
Identifies racing contexts in real-time:

🏁 Straights: Full throttle sections (short/medium/long)
🔄 Corners: Braking zones and low-speed sections
🚀 Corner Exits: Acceleration zones with lookahead prediction

4. Professional Output

High-resolution plots (300 DPI)
CSV exports for further analysis
Console statistics and breakdown
Analysis reports with insights

## 🛠️ Technologies

- **C**: Core processing and analysis
- **Python**: Data extraction via FastF1 library
- **CSV**: Data interchange format

## 📊 How It Works
```
1. Python extracts telemetry from F1 API
2. Data saved as CSV (speed, throttle, brake, position)
3. C program:
   - Parses CSV
   - Analyzes each point
   - Detects racing state
   - Exports results
```

## 📊 System Architecture
```
┌─────────────────────────────────────────────────────────┐
│                  F1 TELEMETRY ANALYSIS                  │
└─────────────────────────────────────────────────────────┘

    [F1 API] ──→ [FastF1 Python] ──→ [CSV Files]
                                          │
                                          ↓
    [telemetry_VER_brazil_2024.csv] ←────┤
    [telemetry_HAM_brazil_2024.csv] ←────┘
                                          │
                                          ↓
    [C Analyzer] ──→ State Detection ──→ [analysis_output.csv]
                 │                    
                 └──→ Statistics ──→ [Console Output]
                                          │
                                          ↓
    [Python Viz] ──→ [telemetry_comparison.png]
                 └──→ [delta_speed.png]
```

## 📈 Algorithm Logic
```c
IF (brake == 1 OR (throttle < 20 AND speed < 250))
    → CURVE
ELSE IF (brake == 0 AND throttle <= 95 AND speed_increasing)
    → CURVE_EXIT
ELSE IF (throttle > 95 AND throttle <= 98)
    → STRAIGHT (SHORT)
ELSE
    → STRAIGHT (MEDIUM/LONG)
```

## 📷 Sample Output
```
IN POSITION: 0.0234 -> SPEED: 187.34; THROTTLE: 45.23; BRAKE: 1
IN POSITION: 0.0456 -> SPEED: 201.12; THROTTLE: 78.45; BRAKE: 0
```

## 🎓 Learning Goals

This project is part of my journey to work in **automotive embedded systems** and **motorsport technology**, combining:
- Low-level programming (C)
- Data analysis
- Understanding of vehicle dynamics
- Real-world F1 telemetry

## 👤 Author

**Pedro Henrique Bonifácio da Rosa**  
Computer Engineering Student @ Unisinos  
Focused on: Automotive Embedded Systems | Motorsport Technology | Telemetry Analysis

📧 [pedrorosa.rb@gmail.com]  
🔗 [LinkedIn](https://www.linkedin.com/in/pedro-bonif%C3%A1cio-9869a9263/)  

## 📄 License

MIT License - Feel free to use this for learning!

---

⭐ **If you found this helpful, consider giving it a star!**

---
