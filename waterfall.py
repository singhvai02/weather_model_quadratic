"""
WATERFALL WEATHER MODEL

This script simulates a basic weather prediction using a quadratic model
under the traditional Waterfall development methodology.

Model: T(t) = a*t^2 + b*t + c
Where:
    T = Predicted Temperature (°C)
    t = Time (hour of the day)
    a, b, c = Coefficients based on assumptions or historical data

Development Mode: Waterfall
- Plan -> Develop -> Test -> Deliver (executed in a single cycle)
"""

# === Coefficients for quadratic model ===
a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    """Predict temperature using a quadratic equation."""
    return a * (time ** 2) + b * time + c

# === WATERFALL MODE EXECUTION ===
print("=== WATERFALL MODE ===")
print("Plan -> Develop -> Test -> Deliver (Single Cycle)\n")

# Simulate predictions every 6 hours across a 24-hour period
for hour in range(0, 25, 6):
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")
