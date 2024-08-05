def compute_impedance(resistance, reactance):
    # Use complex() to calculate impedance in an electrical circuit
    return complex(resistance, reactance)

def main():
    resistance = 50  # ohms
    reactance = 30   # ohms
    impedance = compute_impedance(resistance, reactance)
    
    # Print impedance details
    print(f"Impedance: {impedance}")
    print(f"Real part: {impedance.real}")
    print(f"Imaginary part: {impedance.imag}")

if __name__ == "__main__":
    main()
