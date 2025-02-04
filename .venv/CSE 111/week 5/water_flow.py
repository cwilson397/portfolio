############################################
# Febuary 3rd, 2025
# Colby Wilson
# A program designed to help calculate waterflow
# CSE 111
#############################################

# Calculate the height of a column of water from the tower height and tank wall height. 
def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

# Calculate the pressure caused by Earth's gravity on water stored in an elevated tank.
def pressure_gain_from_water_height(height):
    rho = 998.2  # kg/m^3
    g = 9.80665  # m/s^2
    pressure = (rho * g * height) / 1000
    return pressure

#  Calculate the pressure loss due to friction in a pipe.
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2  # kg/m^3
    pressure_loss = -(friction_factor * pipe_length * rho * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
