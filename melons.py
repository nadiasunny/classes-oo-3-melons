"""Classes for melon orders."""
class AbstractMelonOrder:
    """similarities between shipping"""
    #AbstractMelonOrder global variables
    tax = 0
    order_type = None

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        
    #get total
    #mark shipped
    
    def get_total(self):
        """Calculate price, including tax."""
        #if christmas melon it will cost more
        #else will be 5
        #could we maybe do species.christmas?
        if self.species == "christmas melon":
            base_price = (5 * 1.5)
        else:
            base_price = 5

        #if international order and has < 10 melons add $3
        if self.order_type == "international" and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price
            total += 3
        else:
            total = (1 + self.tax) * self.qty * base_price
        # total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """gov orders w no tax, and see if it passes inspection"""
    tax = 0
    order_type = "government"

    #when we call the function govmelon("type", 22, False)

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False 
        print(self.passed_inspection)

    #method to tak in boolean of passed inspection and update variable
    def mark_inspection(self, passed): #passed is the argument, we will input True or False based on the melon input
        self.passed_inspection = passed #passed is the boolean that WE will pass through True/False BOOLEAN
        print(self.passed_inspection)


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

        
    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False


    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    

    order_type = "international"
    tax = 0.17
        
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
        

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
