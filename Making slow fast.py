import control
import matplotlib.pyplot as plt

# Define "s"
s = control.TransferFunction.s

# --- 1. The "Plant" (The Physical System) ---
# Imagine a heavy, slow flywheel
# Time Constant = 10 seconds (Very Slow!)
Plant = 1 / (10 * s + 1)

# --- 2. The "Controller" (Proportional Gain) ---
# Kp is how hard we push based on the error
# Try changing this from 1 to 5 to 10
Kp = 5.0 

# --- 3. The Open Loop (No Feedback) ---
# This is just the plant behaving naturally
OpenLoop = Plant

# --- 4. The Closed Loop (With Feedback) ---
# Formula: T = (Kp * Plant) / (1 + Kp * Plant)
# The control library does the math for us:
# feedback(System, Sensor) -> We assume Sensor = 1 (Unity Feedback)
ClosedLoop = control.feedback(Kp * Plant, 1)

# --- 5. Simulation ---
t1, y1 = control.step_response(OpenLoop)
t2, y2 = control.step_response(ClosedLoop)

# --- 6. Plotting ---
plt.figure(figsize=(10, 6))

# Plot the lazy Open Loop system
plt.plot(t1, y1, 'b--', label='Open Loop (Natural Behavior)')

# Plot the aggressive Closed Loop system
plt.plot(t2, y2, 'r-', linewidth=3, label=f'Closed Loop (Kp={Kp})')

# Target Line
plt.axhline(1.0, color='k', linestyle=':', label='Target')

plt.title('The Magic of Feedback: Making a Slow System Fast')
plt.xlabel('Time (seconds)')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.show()