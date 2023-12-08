import numpy as np
import matplotlib.pyplot as plt


## INIT

mass = 0.05
angle = 45
force = 1000
F_x = np.cos(angle) * force
F_y = np.cos(angle) * force


g = -9.81
starting_height = 0.001
starting_speed_x = 0
starting_speed_y = 0

simulation_length = 5
simulation_step_size = 0.001

time_array = np.arange(0, simulation_length, simulation_step_size)
x_array = np.zeros(len(time_array))
y_array = np.zeros(len(time_array))
vx_array = np.zeros(len(time_array))
vy_array = np.zeros(len(time_array))
ax_array = np.zeros(len(time_array))
ay_array = np.zeros(len(time_array))

## SETUP STEP T=0
x_array[0] = 0
y_array[0] = starting_height
vx_array[0] = starting_speed_x
vy_array[0] = starting_speed_y
ax_array[0] = (F_x / mass) * simulation_step_size
ay_array[0] = (F_y / mass) * simulation_step_size

for idx in range(1, len(time_array)):
    # update location
    x_array[idx] = x_array[idx - 1] + vx_array[idx - 1] * simulation_step_size
    y_array[idx] = (
        y_array[idx - 1] + vy_array[idx - 1] * simulation_step_size
        if (y_array[idx - 1] + vy_array[idx - 1] * simulation_step_size) > 0
        else 0
    )

    # update speeds
    vx_array[idx] = (
        vx_array[idx - 1] + ax_array[idx - 1] * simulation_step_size
        if y_array[idx - 1] > 0
        else 0
    )
    vy_array[idx] = (
        vy_array[idx - 1] + ay_array[idx - 1] * simulation_step_size
        if y_array[idx - 1] > 0
        else 0
    )

    # update accelerations
    ax_array[idx] = 0
    ay_array[idx] = g if y_array[idx - 1] > 0 else 0

print(vy_array)
plt.plot(x_array, y_array)
plt.ylim(0, starting_height * 1.2)
plt.show()
