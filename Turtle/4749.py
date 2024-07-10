# Python code example to generate unique geometric patterns

import numpy as np
import matplotlib.pyplot as plt

def generate_pattern():
    size = (1000, 1000)
    img = np.zeros(size)

    # Generate complex geometric shapes
    for i in range(1, 10):
        theta = np.linspace(0, 2*np.pi, 1000)
        r = np.random.randint(100, 300)
        x = r * np.cos(theta * i) + size[0] // 2
        y = r * np.sin(theta * i) + size[1] // 2
        img[x.astype(int), y.astype(int)] = i

    # Add color and visual effects
    plt.figure(figsize=(10, 5))
    plt.imshow(img, cmap='viridis')
    plt.axis('off')
    plt.title('Generated Geometric Pattern')
    plt.show()

generate_pattern()
