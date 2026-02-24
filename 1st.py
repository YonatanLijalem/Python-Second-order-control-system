import control
import matplotlib.pyplot as plt
import numpy as np

# Define "s"
s = control.TransferFunction.s

# Parameters
wn = 5.0  # Natural Frequency (Speed of vibration)

# We will test 3 different "Shock Absorbers" (Damping Ratios)
zeta_values = [0.2, 0.7, 2.0]
labels = ['Bouncy (0.2)', 'Perfect (0.7)', 'Stiff (2.0)']

plt.figure(figsize=(10, 6))

for i, zeta in enumerate(zeta_values):
    # The Formula for Second Order System
    # G(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)
    G = (wn**2) / (s**2 + 2*zeta*wn*s + wn**2)
    
    # Simulate Step Response
    t, y = control.step_response(G)
    
    # Plot
    plt.plot(t, y, linewidth=2, label=f'Zeta = {zeta} ({labels[i]})')

# Add a reference line at 1.0 (Target)
plt.axhline(1.0, color='black', linestyle='--', label='Target')

plt.title('Second Order Systems: The Effect of Damping (Zeta)')
plt.xlabel('Time (seconds)')
plt.ylabel('Position')
plt.legend()
plt.grid(True)
plt.show()