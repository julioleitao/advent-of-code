def calculate_module_full(mass):
    return round((mass / 3), 0) - 2 

if __name__ == "__main__":
    assert calculate_module_full(12) == 2
    assert calculate_module_full(14) == 2
    assert calculate_module_full(1969) == 654
    assert calculate_module_full(100756) == 33583

    with open('./input.txt') as f:
        mass = map(int, f.readlines())

        fuels = map(calculate_module_full, mass)
        result = sum(fuels)
        assert result == 3266053
