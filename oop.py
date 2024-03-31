"""
circle class with and circumference calculation
"""
import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * (radius ** 2) for radius in self.radius_list]
        return areas

    def calculate_circumference(self):
        circumferences = [2 * math.pi * radius for radius in self.radius_list]
        return circumferences

if __name__ == "__main__":
    # List of radii
    radii = [10, 501, 22, 37, 100, 999, 87, 351]
    
    # Create an instance of Circle
    circle = Circle(radii)
    
    # Calculate areas and circumferences
    areas = circle.calculate_area()
    circumferences = circle.calculate_circumference()
    
    # Display results
    print("Areas:", areas)
    print("Circumferences:", circumferences)


"""
circle class with private pi variable
"""
# define a class named Circle
class Circle:
# class variable
    pi = 3.14
# constructor
    def __init__(self, radius):
        self.radius = radius
# instance method
    def area_of_circle(self):
        area = self.pi * self.radius * self.radius
        return area

 # instance method
    def perimeter_of_circle(self):
        perimeter = 2 * self.pi * self.radius
        return perimeter
   
    def display_pi(self):
        return self.pi
if __name__ == "__main__":    
    # object of the class Circle
    c = Circle(10)


    print("Area of Circle : ", c.area_of_circle())


    print("Perimeter of Circle : ", c.perimeter_of_circle())


    print("Value of pi : ", c.display_pi())


"""
circle class with class methods for area and perimeter calculation

"""
import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    @classmethod
    def calculate_area(cls, radius):
# Parameters, radius (float): The radius of the circle.
# Returns float: The area of the circle.
        return math.pi * (radius ** 2)

    @classmethod
    def calculate_perimeter(cls, radius):
     
        return 2 * math.pi * radius

if __name__ == "__main__":
    # List of radii
    radii = [10, 501, 22, 37, 100, 999, 87, 351]
    
    # Calculate areas and circumferences for each radius
    for radius in radii:
        area = Circle.calculate_area(radius)
        perimeter = Circle.calculate_perimeter(radius)
        print(f"For radius {radius}: Area = {area}, Perimeter = {perimeter}")

"""
TV class hierachy and features implementation
"""
class TV:
    def __init__(self, brand):
    
# Initialize TV object with default properties.
# You can set default values for price, inches, etc. here
        self.brand = brand
        self.channel = 1
        self.price = 0  
        self.inches = 0
        self.on_off = False
        self.volume = 50
 
# Increase the volume of the TV by 1, up to a maximum of 100.
    def increase_volume(self):
       
        
        if self.volume < 100:
            self.volume += 1

# decrease the volume of the tv by 1, down to a minimum of 0.
    def decrease_volume(self):
        

        if self.volume > 0:
            self.volume -= 1
# Set the channel of the TV to the specified channel, within the range of 1 to 50.
    def set_channel(self, channel):
        

    
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        
# Reset the TV to its default settings: channel 1 and volume 50.
        
        self.channel = 1
        self.volume = 50

    def status(self):
        
# Get the status of the TV including brand, channel, and volume.
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
    

"""
subclasses of tv: led tv and plasma with additional features
"""    
class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        
# Initialize LedTV object with additional properties.super().__init__(brand)
        
        super() . __init__ (brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight, display_details):
        
#  Initialize PlasmaTV object with additional properties.

        
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.display_details = display_details


# Example usage:

# Creating a LED TV instance
led_tv = LedTV("Sony", screen_thickness="Slim", energy_usage="Low", lifespan="Long", refresh_rate=120, viewing_angle="Wide", backlight="LED", display_details="4K resolution")

# Increasing volume
led_tv.increase_volume()
led_tv.increase_volume()

# Setting channel
led_tv.set_channel(10)

# Getting status
print(led_tv.status())  # Output: Sony at channel 10, volume 52

# Resetting TV
led_tv.reset()

# Getting status after reset
print(led_tv.status())  # Output: Sony at channel 1, volume 50
