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
    rho = 998.2  
    pressure_loss = -(friction_factor * pipe_length * rho * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

# Calculate the pressure loss from pipe fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2
    pressure_loss = -(0.04 * rho * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss

# Calculates the Reynolds number for the waterflow
def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2
    mu = 0.0010016 # Pascal seconds
    return (rho * hydraulic_diameter * fluid_velocity) / mu

# Calculate pressure loss from pipe diameter reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    rho = 998.2
    k = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -(k * rho * fluid_velocity**2) / 2000
    return pressure_loss

# Converts kPa to PSI
def kPa_to_psi(kPa):
    return kPa * 0.145038  # Conversion factor from kPa to psi




PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Convert kPa to psi
    pressure_psi = kPa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} psi")


if __name__ == "__main__":
    main()
