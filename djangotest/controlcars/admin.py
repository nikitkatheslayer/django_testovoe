from django.contrib import admin
import controlcars.models as model

admin.site.register(model.color_car)
admin.site.register(model.brand_car)
admin.site.register(model.model_car)
admin.site.register(model.orders)