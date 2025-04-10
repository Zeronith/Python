# Өлзийтөгс эгч
import math
import random

def get_random_position_range(x_range, y_range):
    x = random.uniform(x_range[0], x_range[1])
    y = random.uniform(y_range[0], y_range[1])
    return (x, y)

def simulate_hunt(initial_positions, speeds, max_time, delta_t=0.01):
    x_m, y_m = initial_positions['mouse']
    x_s, y_s = initial_positions['cat']
    v_m, v_c = speeds['mouse'], speeds['cat']
    
    time = 0
    while time <= max_time:
        # 1. Хулгана могойноос эсрэг зүгт хөдөлнө
        dx_m = x_m - x_s
        dy_m = y_m - y_s
        distance_m = math.hypot(dx_m, dy_m)
        x_m += v_m * delta_t * (dx_m / distance_m)
        y_m += v_m * delta_t * (dy_m / distance_m)
        # 2. Могой хулгана руу хөдөлнө
        dx_s = x_m - x_s
        dy_s = y_m - y_s
        distance_s = math.hypot(dx_s, dy_s)
        if distance_s <= 1:
            return f"Могой хулганыг {time:.2f} цагийн дотор барилаа."
        if distance_s > 0:
            x_s += v_c * delta_t * (dx_s / distance_s)
            y_s += v_c * delta_t * (dy_s / distance_s)
        
        time += delta_t
    
    return "Хулгана үүрэндээ орлоо."

position_m = get_random_position_range((0, 500), (0, 300))
position_c = get_random_position_range((0, 500), (0, 300))

# Анхны өгөгдөл
initial_positions = {
    'mouse': position_m,
    'cat': position_c,
}

speeds = {
    'mouse': 8,
    'cat': 12,
}

maxtime = 100

# Симуляци хийх
result = simulate_hunt(initial_positions, speeds, maxtime)
print(result)