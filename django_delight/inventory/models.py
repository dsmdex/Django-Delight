from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """
    Represents an Ingredient contained within the restaurant inventory.

    Attributes:
        ingredient_name; represents the name of the ingredient, char type
        inventory_of_ingredient; represents the amount available for use, int type
        ingredient_price; represents the price for the ingredient, decimal type
    """
    # corresponding fields related to the model
    # chat: ingredient_name should be unique=True to avoid duplicate names.
    # chat: inventory_of_ingredient should consider non-int values, say sugar for example, you would weigh it, set a min-value too
    ingredient_name = models.CharField(max_length=50, unique=True)
    inventory_of_ingredient = models.DecimalField(max_digits=7,decimal_places=2, default=0)
    ingredient_price = models.DecimalField(max_digits=5,decimal_places=2, default=0)

    def __str__(self):
        """Returns a string representation of the Ingredient object"""
        return f"Ingredient: {self.ingredient_name}"
    

class MenuItem(models.Model):
    """
    Represents a Menu Item available for a restaurant. 
    
    Attributes:
        menu_item_name; represents the name for a item shown on a menu, char type
        menu_item_price; represents the price that is associated with a menu item, decimal type
    """
    # corresponding fields related to the model
    # chat: menu_item_name should be unique=True to avoid duplicate menu names.
    # chat: Default quantity=0 ensures new ingredients don’t start with NULL.
    menu_item_name = models.CharField(max_length=80, unique=True)
    menu_item_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        """Returns string representation of a menu item and the price for that item."""
        return f"Menu item: {self.menu_item_name} - ${self.menu_item_price}"
    

class RecipeRequirements(models.Model):
    """
    Represents an ingredient that is required to be used as part of recipe for a menu item.

    Consists of fields that will link Ingredient and MenuItems to establish a relationship.

    Attributes:
        ingredient; a foreign key to Ingredient that establishes a link with a menu item, Ingredient type
        menu_item; a foreign key to MenuItems that establishes a link with an Ingredient, MenuItem type
        quantity; represents the amount of an ingredient that is required to be included for a menu item, decimal type
    """
    # corresponding fields related to the model
    # on_delete keyword argument to ensure deletion of either object of either model will remove relation to this model
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # chat: quantity > 0 should be enforced at the form level.
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        # Need a unique constraint on (ingredient, menu_item) to prevent duplicates entries.
        unique_together = ('ingredient', 'menu_item')

    def __str__(self):
        """Returns a string representation of a Recipe requirement needed for a specific Menu item, 
        and the quantity needed for that item"""
        return f"The menu item: {self.menu_item}, requires {self.ingredient}, with a quantity of {self.quantity}."

class Purchases(models.Model):
    """
    Represents a way of taking account of tracking menu items that have been bought, on what day, and logging total price

    Attributes:
        menu_item; Foreign key that establishes a link to the MenuItem model to properly refenece in logging 
        date (datetime): Timestamp of the purchase.
        quantity (int): Number of times the item was bought.

    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # when purchase is made, get the current date and time it was placed
    date = models.DateTimeField(auto_now_add=True)
    # chat: Tracks how many items were bought.
    quantity  = models.PositiveIntegerField(default=1)
    def __str__(self):
        """Returns a string representation of the Purchase made for a menu item, the cost, and the date placed."""
        return f"{self.quantity} x {self.menu_item.name} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"