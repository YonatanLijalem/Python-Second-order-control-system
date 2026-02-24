import control
import matplotlib.pyplot as plt

# Define "s"
s = control.TransferFunction.s

# --- 1. The Plant (The Physical System) ---
# A slow First Order System (e.g., a heavy motor)
Plant = 1 / (5 * s + 1)

# --- 2. The P-Controller (Proportional Only) ---
Kp = 2.0
Controller_P = Kp

# --- 3. The PI-Controller (Proportional + Integral) ---
# Ki is the "Integral Gain" (How fast it fixes the error)
Ki = 1.0
# Formula: Kp + (Ki / s)
Controller_PI = Kp + (Ki / s)

# --- 4. Create the Loops ---
# System 1: Just P
Sys_P = control.feedback(Controller_P * Plant, 1)

# System 2: P + I
Sys_PI = control.feedback(Controller_PI * Plant, 1)

# --- 5. Simulate ---
t, y_p = control.step_response(Sys_P)
t, y_pi = control.step_response(Sys_PI)

# --- 6. Plot ---
plt.figure(figsize=(10, 6))

# Plot P-Control
plt.plot(t, y_p, 'r--', linewidth=2, label='P-Control Only')

# Plot PI-Control
plt.plot(t, y_pi, 'g-', linewidth=3, label='PI-Control (With Integral)')

# Target Line
plt.axhline(1.0, color='black', linestyle=':', label='Target (1.0)')

plt.title('P vs. PI Control: Eliminating the Error')
plt.xlabel('Time (seconds)')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.show()