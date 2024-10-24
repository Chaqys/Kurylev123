import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Работа с numpy
# Создание одномерного массива
array = np.array([1, 2, 3, 4, 5])

# Вычисление среднего значения
mean_value = np.mean(array)

print("Исходный массив:", array)
print("Среднее значение:", mean_value)

# Визуализация массива
plt.figure(figsize=(10, 5))  # Размер графика
plt.plot(array, marker='o', label='Значения массива', color='blue')
plt.axhline(y=mean_value, color='r', linestyle='--', label='Среднее значение')
plt.title('График массива')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()

# 2. Работа с matplotlib
plt.show()

# 3. Работа с Pillow
# Открытие изображения
image = Image.open('example.jpg')

# Изменение размера изображения
resized_image = image.resize((200, 200))

# Сохранение измененного изображения
resized_image.save('resized_image.jpg')

# Показ оригинального и измененного изображений
image.show()
resized_image.show()