def get_minimum_runtime(batteryCapacity, initialBattery, tasks, chargeRate):
    total_runtime = 0.0
    current_battery = float(initialBattery)

    for duration_i, drainRate_i in tasks:
        # Calculate energy cost 
        energy_needed = duration_i * drainRate_i
        
        # Check task
        if energy_needed > batteryCapacity:
            return -1.0
  
        # Idle/Charging Logic
        if current_battery < energy_needed:
            energy_gap = energy_needed - current_battery
            # Time spent idle = energy missing / charge rate
            idle_duration = energy_gap / chargeRate
            
            total_runtime += idle_duration
            current_battery = energy_needed 
        
        # STask Execution
        total_runtime += duration_i
        current_battery -= energy_needed
    return round(total_runtime, 1)

if __name__ == "__main__":
    try:
        cap = float(input("Enter batteryCapacity (mAh): "))
        init = float(input("Enter initialBattery (mAh): "))
        rate = float(input("Enter chargeRate (mAh/sec): "))
        
        # Format: 10,3; 10,5
        raw_tasks = input("Enter tasks (duration,drainRate; ...): ")
        task_list = [[float(x) for x in t.split(',')] for t in raw_tasks.split(';')]

        result = get_minimum_runtime(cap, init, task_list, rate)
        print(f"\n>>> Minimum Total Runtime: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")