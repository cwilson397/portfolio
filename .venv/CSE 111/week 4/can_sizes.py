#########################################
# Monday January 27th
# Can Sizes(cylinder efficiency)
# Programmed by Colby Wilson
#########################################

# important the math libray
import math;

# calculating the volume
def compute_volume(radius, height):
    return math.pi * radius**2 * height

# calculating surface area
def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius+height)

# calculating the efficiency of the storage
def compute_storage_effic(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

# calculating the cost efficiency of the volume
def compute_cost_effic(volume, cost):
    return volume / cost

# main function
def main():
    # a list of can sizes with their attributes
    can_sizes = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42)
    ]

    best_storage_effic = (None, 0) # (name, efficiency)
    best_cost_effic = (None, 0) # (name, efficiency)

    print(f"{'Name':<12}{'Storage Efficiency':<20}{'Cost Efficiency':<20}")
    print("-" * 52)

    # loop to calculate for the entire aray
    for name, radius, height, cost, in can_sizes:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_effic(radius, height)
        cost_efficiency = compute_cost_effic(volume, cost)

        print(f"{name:<12}{storage_efficiency:<20.4f}{cost_efficiency:<20.4f}")

        if storage_efficiency > best_storage_effic[1]:
            best_storage_effic = (name, storage_efficiency)

        if cost_efficiency > best_cost_effic[1]:
            best_cost_effic = (name, cost_efficiency)

    print("\nBest Storage Efficiency: ", best_storage_effic[0])
    print("\nBest Cost Efficiency: ", best_cost_effic[0])


main()

