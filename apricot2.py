def days_to_zero_cases(recovers, new_cases, active_cases):
    if recovers <= new_cases:
        return "заболевших должно быть меньше"

    daily_change = recovers - new_cases
    days_required = active_cases // daily_change

    return days_required



recovered = 233
new_cases = 50
active_cases = 300


print(days_to_zero_cases(recovered, new_cases, active_cases))
