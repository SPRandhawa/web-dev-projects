from django.db import models


# ✅ BRAND
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()

    def __str__(self):
        return self.name


# ✅ CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.URLField()

    def __str__(self):
        return self.name


# ✅ BANNER
class Banner(models.Model):
    BANNER_TYPES = (
        ('top_slider', 'Top Auto Slider'),
        ('big_banner', 'Big Banner'),
        ('carousel', 'Carousel Slider'),
    )

    title = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    banner_type = models.CharField(max_length=20, choices=BANNER_TYPES)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# ✅ LAPTOP
class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=200)
    price_min = models.IntegerField()
    price_max = models.IntegerField()

    rating = models.FloatField(default=4.0)
    image_url = models.URLField()

    amazon_url = models.URLField(blank=True, null=True)
    flipkart_url = models.URLField(blank=True, null=True)

    last_updated = models.DateTimeField(auto_now=True)

    is_featured = models.BooleanField(default=False)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ✅ REVIEW (IMPORTANT FOR YOUR FEATURE)
class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ✅ CONTACT MESSAGE
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    reply = models.TextField(blank=True)
    is_replied = models.BooleanField(default=False)  # 🔥 ADD THIS

    def __str__(self):
        return self.name
    
 # compare model
class Comparison(models.Model):
    raw_data = models.TextField(help_text="Paste full specs here")
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(null=True, blank=True)

    ram = models.CharField(max_length=50, blank=True)
    ssd = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=200, blank=True)
    display = models.CharField(max_length=100, blank=True)
    battery = models.CharField(max_length=100, blank=True)
    gpu = models.CharField(max_length=100, blank=True)

    portability = models.CharField(max_length=100, blank=True)
    ports = models.CharField(max_length=200, blank=True)
    connectivity = models.CharField(max_length=200, blank=True)

    category = models.CharField(max_length=100, blank=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Laptop"

    def save(self, *args, **kwargs):
        if self.raw_data:

            # 🔥 FIX: convert single-line paste into structured lines
            text = self.raw_data.replace("Brand:", "\nBrand:") \
                                .replace("Price:", "\nPrice:") \
                                .replace("Rating:", "\nRating:") \
                                .replace("Ram:", "\nRam:") \
                                .replace("RAM:", "\nRAM:") \
                                .replace("SSD:", "\nSSD:") \
                                .replace("Processor:", "\nProcessor:") \
                                .replace("Display:", "\nDisplay:") \
                                .replace("Battery:", "\nBattery:") \
                                .replace("Gpu:", "\nGpu:") \
                                .replace("GPU:", "\nGPU:") \
                                .replace("Portability:", "\nPortability:") \
                                .replace("Ports:", "\nPorts:") \
                                .replace("Connectivity:", "\nConnectivity:") \
                                .replace("Category:", "\nCategory:")

            lines = text.split("\n")

            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip().lower()
                    value = value.strip()
                   
                    
                    if key == "name":
                        self.name = value
                    elif key == "brand":
                        self.brand = value
                    elif key == "price":
                        self.price = value
                    elif key == "rating":
                        try:
                            self.rating = float(value.split()[0])
                        except:
                            pass
                    elif key == "ram":
                        self.ram = value
                    elif key == "ssd":
                        self.ssd = value
                    elif key == "processor":
                        self.processor = value
                    elif key == "display":
                        self.display = value
                    elif key == "battery":
                        self.battery = value
                    elif key == "gpu":
                        self.gpu = value
                    elif key == "portability":
                        self.portability = value
                    elif key == "ports":
                        self.ports = value
                    elif key == "connectivity":
                        self.connectivity = value
                    elif key == "category":
                        self.category = value

       
        super().save(*args, **kwargs)

# accessory model
class Accessory(models.Model):

    TYPE_CHOICES = [
        ('mouse', 'Mouse'),
        ('keyboard', 'Keyboard'),
        ('headphones', 'Headphones'),
        ('speaker', 'Speaker'),
        ('laptop_bag', 'Laptop Bag'),
        ('cooling_pad', 'Cooling Pad'),
        ('webcam', 'Webcam'),
        ('microphone', 'Microphone'),
        ('usb_hub', 'USB Hub'),
        ('adapter', 'Adapter'),
        ('charger', 'Charger'),
        ('stand', 'Stand'),
        ('dock', 'Docking Station'),
        ('power_bank', 'Power Bank'),
        ('external_hard_drive', 'External Hard Drive'),
        ('stylus_pen', 'Stylus Pen'),
        ('case', 'Case'),
        ('screen_protector', 'Screen Protector'),
        ('webcam_cover', 'Webcam Cover'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
    