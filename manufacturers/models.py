from django.db import models

class Association(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class EstablishmentProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    physical_location = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    gps_coordinates = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    telephone = models.CharField(max_length=50)

    contact_name = models.CharField(max_length=100)
    contact_designation = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField()

    kesic_code = models.CharField(max_length=10)
    kesic_description = models.CharField(max_length=255)

    COMMERCIAL_SPACE_CHOICES = [
        ('solely_owned', 'Solely Owned'),
        ('jointly_owned', 'Jointly Owned'),
        ('rented', 'Rented'),
    ]
    commercial_space_status = models.CharField(max_length=20, choices=COMMERCIAL_SPACE_CHOICES)

    has_branches = models.BooleanField(default=False)
    number_of_branches = models.PositiveIntegerField(blank=True, null=True)

    is_member_of_association = models.BooleanField(default=False)
    associations = models.ManyToManyField(Association, blank=True)
    other_association_name = models.CharField(max_length=255, blank=True, null=True)

    year_started_operations = models.PositiveIntegerField()
    achievements = models.TextField(blank=True, null=True)

    government_ownership_pct = models.DecimalField(max_digits=5, decimal_places=2)
    kenyan_citizens_ownership_pct = models.DecimalField(max_digits=5, decimal_places=2)
    non_citizens_ownership_pct = models.DecimalField(max_digits=5, decimal_places=2)

    OWNERSHIP_TYPE_CHOICES = [
        ('sole_proprietorship', 'Sole Proprietorship'),
        ('partnership', 'Partnership'),
        ('private_ltd', 'Private Limited Company'),
        ('public_ltd', 'Public Limited Company'),
        ('joint_venture', 'Joint Venture'),
        ('cooperative', 'Cooperative'),
        ('parastatal', 'Parastatal/State Corporation'),
        ('county_gov', 'County Government'),
        ('national_gov', 'National Government'),
        ('other', 'Other'),
    ]
    ownership_type = models.CharField(max_length=30, choices=OWNERSHIP_TYPE_CHOICES)
    other_ownership_type = models.CharField(max_length=255, blank=True, null=True)

    has_agpo_certificate = models.BooleanField(default=False)
    AGPO_CATEGORIES = [
        ('women', 'Women Owned'),
        ('youth', 'Youth Owned'),
        ('pwds', 'PWDs Owned'),
    ]
    agpo_category = models.CharField(max_length=10, choices=AGPO_CATEGORIES, blank=True, null=True)

    enjoyed_tax_incentive = models.BooleanField(default=False)
    tax_incentive_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Employees(models.Model):
    CATEGORY_CHOICES = [
        ('youth', 'Youth (<35)'),
        ('adult', 'Adult (≥35)'),
        ('proprietors', 'Proprietors'),
    ]

    LEVEL_CHOICES = [
        ('executive', 'Managerial/Executive'),
        ('professional', 'Technical/Professional'),
        ('skilled', 'Skilled'),
        ('semi_skilled', 'Semi-skilled'),
        ('unskilled', 'Unskilled'),
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    year = models.PositiveIntegerField(default=2024)

    regular_males = models.PositiveIntegerField(blank=True)
    regular_females = models.PositiveIntegerField(blank=True)
    casual_males = models.PositiveIntegerField(blank=True)
    casual_females = models.PositiveIntegerField(blank=True)
    proprietor_males = models.PositiveIntegerField(blank=True)
    proprietor_females = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = "Employee Record"
        verbose_name_plural = "Employee Records"

    def __str__(self):
        return f"{self.get_level_display()} - {self.get_category_display()} ({self.establishment})"

    @property
    def total_males(self):
        return (
            self.regular_male +
            self.casual_male +
            self.proprietor_male
        )

    @property
    def total_females(self):
        return (
            self.regular_female +
            self.casual_female +
            self.proprietor_female
        )

    @property
    def total_employees(self):
        return self.total_males + self.total_females
    

class RawMaterial(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('ltr', 'Litres'),
        ('pcs', 'Pieces'),
        ('ton', 'Tons'),
        # Add more units as needed
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    hs_code = models.CharField(max_length=50, verbose_name="HS Code")
    quantity_local = models.DecimalField(max_digits=15, decimal_places=2)
    quantity_imported = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    year = models.PositiveIntegerField(default=2024)

    class Meta:
        verbose_name = "Raw Material"
        verbose_name_plural = "Raw Materials"

    def __str__(self):
        return f"{self.name} ({self.establishment})"

    @property
    def total_quantity(self):
        return self.quantity_local + self.quantity_imported
    

class UtilityConsumption(models.Model):
    SATISFACTION_CHOICES = [
        (1, 'Very Satisfied'),
        (2, 'Satisfied'),
        (3, 'Neutral'),
        (4, 'Dissatisfied'),
        (5, 'Very Dissatisfied'),
    ]

    UTILITY_CHOICES = [
        ('coal', 'Coal (Tonne)'),
        ('water', 'Water (Cubic meters)'),
        ('wood_fuel', 'Wood Fuel (Tonne)'),
        ('gas_lpg', 'Gas (LPG) (Cubic meters)'),
        ('electricity_solar', 'Electricity - Solar (KWh)'),
        ('electricity_wind', 'Electricity - Wind (KWh)'),
        ('electricity_kplc', 'Electricity - KPLC (KWh)'),
        ('petrol', 'Petrol (Litre)'),
        ('diesel', 'Diesel (Litre)'),
        ('kerosene', 'Kerosene (Litre)'),
        ('biogas', 'Bio-gas (Cubic meters)'),
        ('charcoal', 'Charcoal (Tonne)'),
        ('other', 'Other (Specify)'),
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE, related_name='utility_consumptions')
    utility_type = models.CharField(max_length=30, choices=UTILITY_CHOICES)
    other_utility_name = models.CharField(max_length=100, blank=True, null=True)  # Only if utility_type is 'other'

    quantity_used = models.DecimalField(max_digits=12, decimal_places=2)
    value_ksh = models.DecimalField(max_digits=12, decimal_places=2)
    max_capacity_required = models.DecimalField(max_digits=12, decimal_places=2)
    satisfaction_level = models.IntegerField(choices=SATISFACTION_CHOICES)

    def __str__(self):
        return f"{self.get_utility_type_display()} - {self.establishment.name}"


class UnOperatingCapacityReason(models.Model):
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

class Production(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('primary', 'Primary Product'),
        ('secondary', 'Secondary Product'),
    ]

    SATISFACTION_SCALE = [
        (1, 'Very Satisfied'),
        (2, 'Satisfied'),
        (3, 'Neutral'),
        (4, 'Dissatisfied'),
        (5, 'Very Dissatisfied'),
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE, related_name="productions")
    
    # Product Details
    product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    hs_code = models.CharField(max_length=20)
    quantity_produced = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=50)
    max_production_capacity = models.DecimalField(max_digits=12, decimal_places=2)

    # Operating capacity
    operated_at_optimal_capacity = models.BooleanField(null=True, blank=True)
    reasons_for_not_operating = models.ManyToManyField(UnOperatingCapacityReason, blank=True)

    def __str__(self):
        return f"{self.product_type.title()} - {self.name} ({self.establishment.name})"
    

class Sales(models.Model):
    SALE_TYPE_CHOICES = [
        ('local', 'Local'),
        ('export', 'Export'),
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE, related_name='sales')
    sale_type = models.CharField(max_length=10, choices=SALE_TYPE_CHOICES)
    
    product = models.ForeignKey(Production, on_delete=models.CASCADE, related_name='sales')
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=50)
    value_ksh = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.get_sale_type_display()} Sale - {self.product.name}"


class SolidWasteData(models.Model):

    SOLID_WASTE_TYPES = [
        ('solid', 'Solid Waste'),
        ('hazardous', 'Hazardous Waste'),
        ('e-waste', 'E-Waste'),
    ]

    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=20, choices=SOLID_WASTE_TYPES)
    generated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    treated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    recycled = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disposed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.establishment} - {self.get_waste_type_display()}"

class WasteWaterData(models.Model):
    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE)

    WATER_WASTE_TYPES = [
        ('hazardous', 'Hazardous Water'),
        ('liquid', 'Liquid Waste / Waste Water'),
    ]

    waste_type = models.CharField(max_length=20, choices=WATER_WASTE_TYPES)
    collected = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    treated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    recycled = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disposed = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.establishment} - {self.get_waste_type_display()}"
    
class WasteManagementCost(models.Model):
    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE)

    WASTE_COST_TYPES = [
        ('solid', 'Solid Waste'),
        ('hazardous', 'Hazardous Waste'),
        ('e-waste', 'E-Waste'),
        ('liquid', 'Liquid Waste / Waste Water'),
    ]

    waste_type = models.CharField(max_length=20, choices=WASTE_COST_TYPES)
    collected = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    treated = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    recycled = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    disposed = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.establishment} - {self.get_waste_type_display()} Cost"


class EnvironmentConservationActivity(models.Model):
    establishment = models.ForeignKey(EstablishmentProfile, on_delete=models.CASCADE, related_name='conservation_activities')
    activity_name = models.CharField(max_length=255)
    amount_spent = models.DecimalField(max_digits=12, decimal_places=2)  # in KSH million

    def __str__(self):
        return f"{self.activity_name} - KSH {self.amount_spent}M"



from django.db import models

class TechnologiesUsed(models.Model):
    establishment = models.OneToOneField(EstablishmentProfile, on_delete=models.CASCADE, related_name='technologies_used')

    # 12.1 - Modern Manufacturing (4IR Technologies)
    big_data = models.BooleanField(default=False)
    cloud_computing = models.BooleanField(default=False)
    artificial_intelligence = models.BooleanField(default=False)
    internet_of_things = models.BooleanField(default=False)
    advanced_robotics = models.BooleanField(default=False)
    additive_manufacturing = models.BooleanField(default=False)
    ar_vr = models.BooleanField(default=False)
    other_4ir_tech = models.CharField(max_length=255, blank=True, null=True)

    # 12.2 - Waste/Water Use Technologies
    waste_reduction_tech_in_use = models.BooleanField(default=False)

    # 13 - Green Technologies
    renewable_energy = models.BooleanField(default=False)
    waste_management = models.BooleanField(default=False)
    decarbonization = models.BooleanField(default=False)
    emission_control = models.BooleanField(default=False)
    sustainable_materials = models.BooleanField(default=False)
    energy_efficiency = models.BooleanField(default=False)
    electric_vehicles = models.BooleanField(default=False)
    green_cloud_tech = models.BooleanField(default=False)
    other_green_tech = models.CharField(max_length=255, blank=True, null=True)

    # 14a - Circular Economy Contribution
    contributes_to_circular_economy = models.BooleanField(default=False)

    # 14b - How they contribute to circular economy
    product_design = models.BooleanField(default=False)
    resource_recovery = models.BooleanField(default=False)
    business_model_innovation = models.BooleanField(default=False)
    use_recycled_inputs = models.BooleanField(default=False)
    waste_to_value = models.BooleanField(default=False)
    industrial_symbiosis = models.BooleanField(default=False)
    eco_design_packaging = models.BooleanField(default=False)
    consumer_awareness = models.BooleanField(default=False)
    other_circular = models.CharField(max_length=255, blank=True, null=True)

    # 14c - Which of the 4R’s are employed?
    reduce = models.BooleanField(default=False)
    reuse = models.BooleanField(default=False)
    recycle = models.BooleanField(default=False)
    recover = models.BooleanField(default=False)
    none_of_4rs = models.BooleanField(default=False)

    def __str__(self):
        return f"Technologies used by {self.company}"
