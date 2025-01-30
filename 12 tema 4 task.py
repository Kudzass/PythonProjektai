def tikrinti_amziu(amzius):
    if amzius < 0:
        raise ValueError("Amžius negali būti neigiamas!")
    elif amzius >= 18:
        return "Vartotojas pilnametis."
    else:
        return "Vartotojas nepilnametis."

test_values = [-5, 15, 21]
test_results = {}

for value in test_values:
    try:
        test_results[value] = tikrinti_amziu(value)
    except ValueError as e:
        test_results[value] = str(e)

for key, result in test_results.items():
    print(f"Amžius: {key} → {result}")
