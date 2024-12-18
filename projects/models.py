from django.db import models

# Modelo de Marcas
class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)      # Fecha de última actualización
    
    def __str__(self):
        return self.name

# Modelo de Modelos
class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.brand.name})"

# Modelo de Series
class Series(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="series")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="series_brand")  # Agregar referencia a Brand
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)    
        
    def __str__(self):
        return f"{self.name} ({self.model.name})"

# Modelo de Categorías
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name

# Modelo de Lotes (Inventory)

class Inventory(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="batches")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="batches_model")  # Relacionar con Model
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="batches_brand")  # Relacionar con Brand
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="batches_category")  # Relacionar con Category
    quantity = models.IntegerField()
    status_i = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Batch {self.batch_code} - {self.series.name}"
