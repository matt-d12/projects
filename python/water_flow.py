"""
File Name: water_flow.py
Author: Matt D.
Course: CSE 111 | BYU-Idaho
Purpose: To test out multiple functions interracting with more complex formulas
"""
#Function to get water column height
def water_column_height(tower_height, tank_height):
    tower_h = tower_height
    tank_h = tank_height
    #WCH = Water Column Height
    wch = tower_h + (3 * tank_h / 4)
    return wch

#Function to get pressure based on water height
def pressure_gain_from_water_height(height):
    #wd = water density = 998.2 kg/m^3
    wd = 998.2
    #gravity = Earths gravity = 9.80665 m/second^2
    gravity = 9.80665
    #wh = water column height
    wh = height
    pressure_gain = (wd * gravity * wh) / 1000
    return pressure_gain

#Function to get pressure lost due to pipe dimensions
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    pd = pipe_diameter
    pl = pipe_length
    ff = friction_factor
    fl = fluid_velocity
    #wd = water density = 998.2 kg/m^3
    wd = 998.2
    lost_pressure = (-ff * pl * wd * (fl**2)) / (2000 * pd)
    return lost_pressure

#Function to get pressure lost due to pipe fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    p = 998.2   #Density of water
    v = fluid_velocity
    n = quantity_fittings
    lost_pressure_fittings = (-0.04 * p * (v**2) * n) / 2000
    return lost_pressure_fittings

#Function to get the reynolds number of a pipe with water flowing through it
def reynolds_number(hydraulic_diameter, fluid_velocity):
    p = 998.2   #Density of water
    d = hydraulic_diameter
    v = fluid_velocity
    u = 0.0010016   #Dynamic viscosity of water
    r_number = (p * d * v) / u
    return r_number

#Function to get pressure lost from large pipe to smaller pipe
def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    r = reynolds_number
    d = larger_diameter
    small_d = smaller_diameter
    k = (0.1 + 50 / r) * ((d / small_d) **4 - 1)
    p = 998.2   #Density of water
    v = fluid_velocity
    pressure = (-k * p * v**2) / 2000
    return pressure


#Copied section from assignment
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

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()