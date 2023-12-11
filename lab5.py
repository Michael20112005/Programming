"""
Wardrobe Management System

This script defines classes for clothing and wardrobe and demonstrates their usage.
"""

from enum import Enum


class ClothingType(Enum):
    """
    Enum representing different types of clothing.

    Enum Values:
        SHIRT (int): Clothing type for shirts.
        JEANS (int): Clothing type for jeans.
        JACKET (int): Clothing type for jackets.
        SHOES (int): Clothing type for shoes.
        SOCKS (int): Clothing type for socks.
    """
    SHIRT = 1
    JEANS = 2
    JACKET = 3
    SHOES = 4
    SOCKS = 5


class Clothing:
    """
    Represents an item of clothing.

    Attributes:
        name (str): The name of the clothing.
        description (str): Description of the clothing.
        size (str): Size of the clothing.
        clothing_type (ClothingType): Type of clothing.
    """

    def __init__(self, name, description, size="", clothing_type=None):
        """
        Initialize a Clothing object.

        Args:
            name (str): The name of the clothing.
            description (str): Description of the clothing.
            size (str, optional): Size of the clothing. Defaults to an empty string.
            clothing_type (ClothingType, optional): Type of clothing. Defaults to None.
        """
        self.name = name
        self.description = description
        self.size = size
        self.clothing_type = clothing_type

    def display_info(self):
        """Display information about the clothing."""
        print(f"{self.name} ({self.size}) - {self.description}")

    def is_formal(self):
        """
        Check if the clothing is formal.

        Returns:
            bool: True if the clothing is formal, False otherwise.
        """
        return self.clothing_type in {ClothingType.SHIRT, ClothingType.JACKET}


class Wardrobe:
    """
    Represents a wardrobe containing a collection of clothing.

    Attributes:
        clothes (list): List of Clothing objects in the wardrobe.
    """

    def __init__(self):
        self.clothes = []

    def add_clothing(self, *clothes):
        """Add clothing to the wardrobe."""
        self.clothes.extend(clothes)

    def are_going_out(self):
        """Check if ready to go out based on the types of clothing in the wardrobe."""
        clothing_types = {item.clothing_type for item in self.clothes}

        print(f"Number of clothing types: {len(clothing_types)}")
        print("Ready to go out: Yes" if len(clothing_types) > 3 else "Ready to go out: No")

    def sort_clothes_by_size(self):
        """Sort clothes in the wardrobe by size."""
        self.clothes.sort(key=lambda x: x.size)

    def display_wardrobe(self):
        """Display information about the clothing in the wardrobe."""
        for item in self.clothes:
            item.display_info()


def main():
    """Main function to demonstrate the usage of the Wardrobe class."""
    wardrobe = Wardrobe()

    t_shirt = Clothing("T-Shirt", "Casual wear", "M", ClothingType.SHIRT)
    jeans = Clothing("Jeans", "Slim fit", "32", ClothingType.JEANS)
    jacket = Clothing("Jacket", "Winter coat", "L", ClothingType.JACKET)
    r_shoes = Clothing("Running Shoes", "Sportswear", "9", ClothingType.SHOES)
    a_socks = Clothing("Ankle Socks", "Comfortable", "1 Size", ClothingType.SOCKS)

    wardrobe.add_clothing(t_shirt, jeans, jacket, r_shoes, a_socks)

    print("Wardrobe contents:")
    wardrobe.display_wardrobe()

    print("\nCheck if ready to go out:")
    wardrobe.are_going_out()

    print("\nSorted wardrobe by size:")
    wardrobe.sort_clothes_by_size()
    wardrobe.display_wardrobe()


if __name__ == "__main__":
    main()
