# 🏎️ F1 Telemetry Analysis in C

![Formula 1](https://img.shields.io/badge/F1-Telemetry-red)
![Language](https://img.shields.io/badge/Language-C-blue)
![Python](https://img.shields.io/badge/Python-FastF1-green)

## 📋 Overview

Analysis of Formula 1 telemetry data using **C programming**, focused on identifying driver behavior patterns through speed, throttle, and brake data.

This project demonstrates:
- Data extraction from F1 using Python (FastF1)
- CSV parsing and processing in C
- Real-time state detection algorithm
- Automotive data analysis skills

## 🎯 Features

- **State Detection Algorithm** that identifies:
  - 🏁 Straights (full throttle)
  - 🔄 Corners (braking/low speed)
  - 🚀 Corner exits (accelerating)
  
- **Lookahead Analysis**: Predicts acceleration by comparing speed N positions ahead

- **CSV Export**: Generates analysis output for further visualization

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

## 🚀 Usage

```bash
gcc -o analyzer telemetry_analyzer.c -lm
./analyzer
```

### Step 3: View Results
- Console: Real-time analysis output
- `analysis_output.csv`: Full data for visualization

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
