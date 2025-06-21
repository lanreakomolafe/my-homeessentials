class Category(models.Model):
    name = models.CharField(max_length=64)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name      = models.CharField(max_length=120)
    price     = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    in_stock  = models.BooleanField(default=True)git remote add origin https://github.com/lanreakomolafe/my-homeessentials.git
git branch -M main
git push -u origin main