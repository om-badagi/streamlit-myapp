def calculate_positions(sensor_direction, reference_distance, current_reading, reference_values):
    # Direction multiplier
    direction_multiplier = 1 if sensor_direction == 'up' else -1

    # Delta between readings
    delta_t = current_reading - reference_distance

    # Current positions
    DL_t = reference_values['DL'] - (delta_t * direction_multiplier)
    DR_t = reference_values['DR'] - (delta_t * direction_multiplier)
    UL_t = reference_values['UL'] + (delta_t * direction_multiplier)
    UR_t = reference_values['UR'] + (delta_t * direction_multiplier)

    # Axial positions
    RAP = (DR_t - UR_t) / 2
    LAP = (DL_t - UL_t) / 2
    AP = (LAP + RAP) / 2

    return {
        'direction_multiplier': direction_multiplier,
        'delta_t': delta_t,
        'DL_t': DL_t,
        'DR_t': DR_t,
        'UL_t': UL_t,
        'UR_t': UR_t,
        'RAP': RAP,
        'LAP': LAP,
        'AP': AP
    }


if __name__ == "__main__":
    print("=== Axial Position Calculator ===")

    # User Inputs
    sensor_direction = input("Sensor Direction (up/down): ").strip().lower()
    reference_distance = float(input("Reference Distance (mm): "))
    current_reading = float(input("Current Laser Reading (mm): "))

    print("\nEnter Reference Values (mm):")
    UL = float(input("UL: "))
    UR = float(input("UR: "))
    DL = float(input("DL: "))
    DR = float(input("DR: "))

    reference_values = {
        'UL': UL,
        'UR': UR,
        'DL': DL,
        'DR': DR
    }

    # Calculation
    results = calculate_positions(sensor_direction, reference_distance, current_reading, reference_values)

    # Output
    print("\n=== Results ===")
    print(f"Delta_t: {results['delta_t']:.2f} mm")
    print(f"Direction Multiplier (DM): {results['direction_multiplier']}")
    print(f"UL_t: {results['UL_t']:.2f} mm")
    print(f"UR_t: {results['UR_t']:.2f} mm")
    print(f"DL_t: {results['DL_t']:.2f} mm")
    print(f"DR_t: {results['DR_t']:.2f} mm")
    print(f"Left Axial Position (LAP): {results['LAP']:.2f} mm")
    print(f"Right Axial Position (RAP): {results['RAP']:.2f} mm")
    print(f"Overall Axial Position (AP): {results['AP']:.2f} mm")
