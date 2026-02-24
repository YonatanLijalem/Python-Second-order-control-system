import control
import matplotlib.pyplot as plt
import numpy as np

# Define "s" for transfer functions
s = control.TransferFunction.s

# --- 1. THE PLANT (The System we want to control) ---
# Imagine a drone or a robot arm that is very "wobbly"
# s^2 + 0.1s + 1 -> Very low friction (0.1), so it bounces a lot.
Plant = 1 / (s**2 + 0.1*s + 1)

# --- 2. THE PID TUNING (Change these numbers!) ---
Kp = 10.0   # Proportional: "Go Fast!"
Ki = 2.0    # Integral:     "Fix the Error!"
Kd = 5.0    # Derivative:   "Apply Brakes!"

print(f"Simulating PID with: Kp={Kp}, Ki={Ki}, Kd={Kd}")

# --- 3. BUILD THE CONTROLLER ---
# PID Formula: Kp + Ki/s + Kd*s
Controller = Kp + (Ki / s) + (Kd * s)

# --- 4. CREATE THE FEEDBACK LOOP ---
# feedback(System, Sensor) -> We assume sensor is perfect (1)
ClosedLoop = control.feedback(Controller * Plant, 1)

# --- 5. SIMULATE ---
# We simulate for 15 seconds to see the settling
time_points = np.linspace(0, 15, 1000)
t, y = control.step_response(ClosedLoop, T=time_points)

# --- 6. PLOT ---
plt.figure(figsize=(10, 6))

# Plot the Output
plt.plot(t, y, 'b-', linewidth=3, label='System Output')

# Plot the Target Line (1.0)
plt.axhline(1.0, color='r', linestyle='--', label='Target')

plt.title(f'PID Control Simulation\nKp={Kp}, Ki={Ki}, Kd={Kd}')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()