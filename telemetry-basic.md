# F1 Telemetry Analysis in C

## 🎯 Objective
Analyze Formula 1 telemetry data using C to identify:
- Racing lines (straights vs curves)
- Braking points
- Acceleration zones
- Driver behavior patterns

## 🛠️ Technologies
- **Python**: Data extraction with FastF1
- **C**: Data processing and analysis
- **matplotlib**: Visualization

## 📊 Output Example
```
IN POSITION: 0.0234 VER IS IN A CURVE - SPEED: 187.34; THROTTLE: 45.23; BRAKE: 1
IN POSITION: 0.0456 VER ARE COMING OUT THE CURVE - SPEED: 201.12; THROTTLE: 78.45; BRAKE: 0
```

## 🧠 Algorithm Logic
1. **Curve Detection**: Brake active OR (Low throttle + Low speed)
2. **Corner Exit**: No brake + Increasing speed + Partial throttle
3. **Straight**: Full throttle + High speed


## Theorical Dictionare

### Speed

What it is: The car's speed in km/h (or m/s depending on the unit used).

Basic interpretation:

High speed = straightaway or smooth curve.

Low speed = braking or tight turns.

Peaks and dips help identify braking points, acceleration points, and even where the car encounters resistance (curves or lane changes).

### Throttle (Accelerator)

What it is: The position of the accelerator pedal as a percentage (0–100%).

Basic interpretation:

0% (or close to it): The driver is lifting their foot off the accelerator or braking.

100% (or close to it): The driver has their foot fully on the accelerator (usually on a straightaway or exiting a corner).

Intermediate fluctuations (e.g., 60–90%) indicate throttle modulation, very common in high-speed corners.

### Brake

What it is: The intensity of the brake, usually represented as 0 (no braking) to 1 (maximum braking).

Basic interpretation:

0% (or close to it): The rider is not applying the brake (on a straightaway or with their foot off the throttle).

100% (or close to it): The rider is applying the brake completely (braking point).

The interaction between brake and throttle reveals the riding style, such as trail braking (where the rider continues to apply the brake while starting to accelerate).

### G-forces

What it is: The G-forces experienced by the car in different directions:

Lateral G-force (cornering): How strong the curve is in terms of force on the car.

Longitudinal G-force (accelerating or braking): The acceleration or deceleration.

Basic interpretation:

High lateral G-force: High-speed cornering.

Negative G-force (braking): When the driver applies the brakes, especially at points of high deceleration.

High longitudinal G-force: Very aggressive acceleration (usually on straights or corner exits).

### RPM (Revolutions Per Minute)

What it is: The engine's rotation (usually in RPM).

Basic interpretation:

High RPM: The driver is applying high power to the engine (usually on straightaways or corner exits).

Low RPM: The driver may be decelerating or in a lower gear, which can also happen in corners.

### Distance and RelativeDistance

What it is:

Distance: The actual distance traveled in meters or kilometers.

RelativeDistance: The distance relative to the course, from 0 to 1, representing progress on the lap.

Basic interpretation:

Distance helps measure the length traveled on the track.

RelativeDistance is especially useful for comparing laps between drivers, regardless of time—since all cars are "at the same point" on the track.

### Temperature

What it is: The temperature of the tires, engine, or other components.

Basic interpretation:

High tire temperature: May indicate excessive wear or low pressure.

Low tire temperature: The rider may not be warming up the tires properly or may not be using the maximum potential for grip.

Engine or battery temperature: Can affect performance. An overheated engine can lose power, for example.

### Tire Data Telemetry

What it is: Tire pressure and wear.

Basic interpretation:

Uneven wear: May indicate that the driver is applying excessive force to one side of the track or that the pit stop strategy is not being efficient.

Low pressure: May indicate loss of grip and a greater propensity to skid.

