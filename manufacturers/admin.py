from django.contrib import admin

from .models import (EstablishmentProfile, 
                     Association, 
                     Employees, 
                     RawMaterial, 
                     UtilityConsumption, 
                     UnOperatingCapacityReason, 
                     Production,
                     Sales,
                     SolidWasteData,
                     WasteWaterData,
                     WasteManagementCost,
                     EnvironmentConservationActivity,
                     TechnologiesUsed)

admin.site.register(EstablishmentProfile)
admin.site.register(Association)
admin.site.register(Employees)
admin.site.register(RawMaterial)
admin.site.register(UtilityConsumption)
admin.site.register(UnOperatingCapacityReason)
admin.site.register(Production)
admin.site.register(Sales)
admin.site.register(SolidWasteData)
admin.site.register(WasteWaterData)
admin.site.register(WasteManagementCost)
admin.site.register(EnvironmentConservationActivity)
admin.site.register(TechnologiesUsed)