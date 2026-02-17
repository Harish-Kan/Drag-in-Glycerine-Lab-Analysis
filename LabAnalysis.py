# ------------------------------------------------------------
# Labtorials 7 & 8: Drag in Glycerine
# ------------------------------------------------------------

import qexpy as q
import math
import matplotlib.pyplot as plt
import numpy as np

# Distance between the two lines on the cylinder (in meters)
d = 0.16   # 16 cm

# -----------------------------
# Experimental Data
# -----------------------------
trial        = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diameter_cm  = [1.588, 1.588, 2.381, 2.381, 3.175, 3.175, 3.969, 3.969, 4.762, 4.762]
t_initial    = [11.54, 23.87, 6.42, 5.30, 5.90, 44.40, 3.77, 13.13, 5.96, 14.06]
t_final      = [23.24, 37.17, 12.04, 10.83, 9.48, 47.59, 5.88, 15.30, 7.45, 15.54]

# -----------------------------
# Calculations
# -----------------------------
# Convert to numpy arrays for better handling
diameter_cm = np.array(diameter_cm)
t_initial = np.array(t_initial)
t_final = np.array(t_final)

# Compute quantities
radius_m = (diameter_cm / 2) * 0.01                   # cm → m
t_fall = t_final - t_initial                           # time (s)
v_t = d / t_fall                                       # terminal velocity (m/s)
r_squared = radius_m ** 2                              # r² for linear model
r_sqrt = np.sqrt(radius_m)                             # √r for quadratic model

# -----------------------------
# Display Table (clean spacing)
# -----------------------------
print(f"{'Trial':<6}{'Diameter [cm]':<16}{'Initial [s]':<14}{'Final [s]':<10}"
      f"{'Time [s]':<12}{'Velocity [m/s]':<16}{'r² [m²]':<12}{'√r [m^0.5]':<12}")
print("-" * 90)

for i in range(len(trial)):
    print(f"{trial[i]:<6}{diameter_cm[i]:<16.3f}{t_initial[i]:<14.2f}{t_final[i]:<10.2f}"
          f"{t_fall[i]:<12.3f}{v_t[i]:<16.5f}{r_squared[i]:<12.6f}{r_sqrt[i]:<12.6f}")

# -----------------------------
# Graph 1: v_t vs r²  → Linear model (Stokes’ law)
# -----------------------------
fit1 = np.polyfit(r_squared, v_t, 1)
slope1, intercept1 = fit1
y_pred1 = np.polyval(fit1, r_squared)
r_squared_val1 = np.corrcoef(r_squared, v_t)[0, 1] ** 2

plt.figure(figsize=(6,4))
plt.scatter(r_squared, v_t, color='blue', label='Data')
plt.plot(r_squared, y_pred1, color='black', linestyle='--', label='Best Fit')
plt.title("Terminal Velocity vs r² (Linear Model: Stokes’ Regime)")
plt.xlabel("r² (m²)")
plt.ylabel("v_t (m/s)")
plt.text(min(r_squared)*1.05, max(v_t)*0.8,
         f"y = {slope1:.4f}x + {intercept1:.4f}\nR² = {r_squared_val1:.4f}",
         fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 2: v_t vs √r  → Quadratic model (High Reynolds number)
# -----------------------------
fit2 = np.polyfit(r_sqrt, v_t, 1)
slope2, intercept2 = fit2
y_pred2 = np.polyval(fit2, r_sqrt)
r_squared_val2 = np.corrcoef(r_sqrt, v_t)[0, 1] ** 2

plt.figure(figsize=(6,4))
plt.scatter(r_sqrt, v_t, color='red', label='Data')
plt.plot(r_sqrt, y_pred2, color='black', linestyle='--', label='Best Fit')
plt.title("Terminal Velocity vs √r (Quadratic Model)")
plt.xlabel("√r (m^0.5)")
plt.ylabel("v_t (m/s)")
plt.text(min(r_sqrt)*1.05, max(v_t)*0.8,
         f"y = {slope2:.4f}x + {intercept2:.4f}\nR² = {r_squared_val2:.4f}",
         fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
