import matplotlib.pyplot as plt

# Variables to store the total power saved in the battery
total_power_saved_in_battery = 0

# Lists to store power generated for each generator
hydro_power_values = []
wind_power_values = []
solar_power_values = []

# Lists to store the total power generated for each generator over 3 days
total_hydro_power = []
total_wind_power = []
total_solar_power = []

# A loop to capture values input by the engineer over the past 3 days
for i in range(3):
    hydro_power = float(input(f"Enter hydro power {i + 1} (kW): "))
    wind_power = float(input(f"Enter wind power {i + 1} (kW): "))
    solar_power = float(input(f"Enter solar power {i + 1} (kW): "))

    # Append the entered values to the respective lists
    hydro_power_values.append(hydro_power)
    wind_power_values.append(wind_power)
    solar_power_values.append(solar_power)

    # Calculate the total power produced for each user input per day
    total_power_produced = hydro_power + wind_power + solar_power

    # Append the daily total power generated for each generator
    total_hydro_power.append(hydro_power)
    total_wind_power.append(wind_power)
    total_solar_power.append(solar_power)

    # Total expected power load for this iteration
    expected_load = 100  # in kilowatts

    # Power distribution scenarios for this iteration
    if total_power_produced == expected_load:
        print(f"Day {i + 1}: Power optimum")
    elif total_power_produced < expected_load:
        # Check if there is enough power in the battery to compensate
        if total_power_saved_in_battery >= (expected_load - total_power_produced):
            # Compensate the deficit with power from the battery
            deficit = expected_load - total_power_produced
            total_power_saved_in_battery -= deficit
            print(f"Day {i + 1}: Compensating with {deficit} kW from the battery")
        else:
            print(f"Day {i + 1}: Insufficient power, only critical services will receive power.")
    else:
        excess_power = total_power_produced - expected_load
        total_power_saved_in_battery += excess_power  # Store excess power in the battery
        print(f"Day {i + 1}: Excess power saved to batteries: {excess_power} kilowatts")

# Print the total power saved in the battery across all days
print(f"Total power saved in the battery over {i + 1} days: {total_power_saved_in_battery} kilowatts")

# Plot the graph for total power generated over the past three days for each generator
days = [1, 2, 3]
plt.plot(days, total_hydro_power, label='Hydro Power')
plt.plot(days, total_wind_power, label='Wind Power')
plt.plot(days, total_solar_power, label='Solar Power')
plt.xlabel('Day')
plt.ylabel('Total Power Generated (kW)')
plt.legend()
plt.title('Total Power Generated Over 3 Days for Each Generator')
plt.show()
