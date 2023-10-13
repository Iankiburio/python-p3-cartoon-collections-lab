def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")
pass

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]
pass

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)
pass

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for string in strings:
        if string in cheeses:
            return string
    return None
pass
