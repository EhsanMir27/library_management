def calculate_gravitational_energy():
    mass=float(input(f'enter mass : '))
    height=float(input(f'enter height : '))
    gravitational_energy=mass*height*(9.8)
    print(f'{mass} * {height} *9.8 \n->')
    return gravitational_energy
print(f'{calculate_gravitational_energy():.2f}')