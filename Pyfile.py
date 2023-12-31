# Define a base class for Flower
class Flower:
    def __init__(self, name, color, petal_count):
        self.name = name
        self.color = color
        self.petal_count = petal_count

    def display(self):
        return f"{self.color} {self.name} with {self.petal_count} petals"


# Define derived classes for specific flower types
class Rose(Flower):
    def __init__(self, color, petal_count, fragrance):
        super().__init__("Rose", color, petal_count)
        self.fragrance = fragrance

    def display(self):
        return f"{super().display()}, Fragrance: {self.fragrance}"


class Daisy(Flower):
    def __init__(self, color, petal_count, bloom_time):
        super().__init__("Daisy", color, petal_count)
        self.bloom_time = bloom_time

    def display(self):
        return f"{super().display()}, Bloom Time: {self.bloom_time}"


class Lily(Flower):
    def __init__(self, color, petal_count, pollination_type):
        super().__init__("Lily", color, petal_count)
        self.pollination_type = pollination_type

    def display(self):
        return f"{super().display()}, Pollination Type: {self.pollination_type}"


# Define a class for FlowerType
class FlowerType:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def display_flowers(self):
        return [flower.display() for flower in self.flowers]


# Create instances of FlowerType
rose_type = FlowerType(name="Rose", description="Symbol of love and romance")
daisy_type = FlowerType(name="Daisy", description="Symbol of innocence and purity")
lily_type = FlowerType(name="Lily", description="Symbol of rebirth and renewal")

# Create instances of specific flowers
red_rose = Rose(color="Red", petal_count=32, fragrance="Sweet")
white_rose = Rose(color="White", petal_count=24, fragrance="Subtle")
yellow_daisy = Daisy(color="Yellow", petal_count=16, bloom_time="Spring")
pink_lily = Lily(color="Pink", petal_count=18, pollination_type="Insects")

# Add flowers to FlowerType instances
rose_type.add_flower(red_rose)
rose_type.add_flower(white_rose)
daisy_type.add_flower(yellow_daisy)
lily_type.add_flower(pink_lily)

# Display information
print(f"{rose_type.name} flowers: {rose_type.display_flowers()}")
print(f"{daisy_type.name} flowers: {daisy_type.display_flowers()}")
print(f"{lily_type.name} flowers: {lily_type.display_flowers()}")
