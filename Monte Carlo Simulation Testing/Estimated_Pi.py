import random

def estimate_pi(num_samples):
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.random()  # Random x coordinate between 0 and 1
        y = random.random()  # Random y coordinate between 0 and 1
        
        # Check if the point (x, y) is inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # The ratio of points inside the circle to total points gives an estimate of π/4
    return 4 * inside_circle / num_samples

# Estimate π using 1,000,000 samples
estimated_pi = estimate_pi(1000000)
print(estimated_pi)  # Should be close to 3.14159
# I was wondering how they are calculating PI by 4*inside_circle/num_sample .
# But i understood it .
# Since we are finding PI and if we do little bit calculation our circle area is equal to PI 
# So we are finding estimated PI by finding area of circle that has S=PI 