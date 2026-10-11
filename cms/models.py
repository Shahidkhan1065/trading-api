from django.db import models


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200, default='Al Ealami Trading')
    tagline = models.CharField(max_length=200, default='Global Enterprise Network')
    logo_url = models.URLField(blank=True)
    phone_primary = models.CharField(max_length=80, blank=True)
    phone_secondary = models.CharField(max_length=80, blank=True)
    email_trading = models.EmailField(blank=True)
    email_general = models.EmailField(blank=True)
    footer_blurb = models.TextField(blank=True)
    accreditation_badges = models.JSONField(default=list, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site settings'
        verbose_name_plural = 'Site settings'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class NavLink(models.Model):
    LOCATION_CHOICES = [
        ('header', 'Header'),
        ('footer', 'Footer'),
    ]
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='header')
    path = models.CharField(max_length=120)
    label = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['location', 'order']

    def __str__(self):
        return f'{self.location}: {self.label}'


class Office(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField()
    phone = models.CharField(max_length=80, blank=True)
    order = models.PositiveIntegerField(default=0)
    show_in_about = models.BooleanField(default=True)
    show_in_footer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class PageSection(models.Model):
    """Flexible key/value content blocks for each page."""
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('trading', 'Trading Divisions'),
        ('supply-chain', 'Supply Chain'),
        ('quality', 'Quality'),
        ('contact', 'Contact'),
    ]
    page = models.CharField(max_length=40, choices=PAGE_CHOICES, db_index=True)
    key = models.CharField(max_length=80)
    eyebrow = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=400, blank=True)
    subtitle = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    cta_label = models.CharField(max_length=120, blank=True)
    cta_href = models.CharField(max_length=200, blank=True)
    extra = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['page', 'order', 'key']
        unique_together = [('page', 'key')]

    def __str__(self):
        return f'{self.page}.{self.key}'


class Stat(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
    ]
    page = models.CharField(max_length=40, choices=PAGE_CHOICES, default='home')
    value = models.CharField(max_length=40)
    label = models.CharField(max_length=120)
    sublabel = models.CharField(max_length=200, blank=True)
    color_class = models.CharField(max_length=80, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['page', 'order']

    def __str__(self):
        return f'{self.value} {self.label}'


class HomeDivision(models.Model):
    division_id = models.CharField(max_length=10)
    tag = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    rows = models.JSONField(default=list)  # [["label", "value"], ...]
    cta_label = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Home division card'

    def __str__(self):
        return self.title


class Pillar(models.Model):
    icon = models.CharField(max_length=80)
    title = models.CharField(max_length=200)
    description = models.TextField()
    badge = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Corridor(models.Model):
    key = models.SlugField(unique=True)
    label = models.CharField(max_length=120)
    badge = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ports = models.CharField(max_length=200)
    transit = models.CharField(max_length=120)
    volume = models.CharField(max_length=120)
    goods = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label


class MarketIndex(models.Model):
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=80)
    trend = models.CharField(max_length=40, blank=True)  # up / flat / down
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Market indices'

    def __str__(self):
        return self.label


class VesselStream(models.Model):
    name = models.CharField(max_length=120)
    route = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    status_style = models.CharField(max_length=40, default='secondary')  # secondary | tertiary
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class RfqBenefit(models.Model):
    icon = models.CharField(max_length=80)
    title = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class TradingDivision(models.Model):
    CATEGORY_CHOICES = [
        ('metals', 'Industrial & Metals'),
        ('electrical', 'Electrical & Construction'),
        ('agri', 'Agri-Commodities & Food'),
        ('chemicals', 'Energy & Chemicals'),
    ]
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    badge = models.CharField(max_length=120)
    code = models.CharField(max_length=40)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    image_alt = models.CharField(max_length=200, blank=True)
    corridor = models.CharField(max_length=200)
    stock = models.CharField(max_length=120)
    image_left = models.BooleanField(default=True)
    specs = models.JSONField(default=list)  # [[label, value, note], ...]
    chips = models.JSONField(default=list)
    cta_label = models.CharField(max_length=120)
    division_name = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Incoterm(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    badge = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.code


class QualityFramework(models.Model):
    icon = models.CharField(max_length=80)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question[:80]


class RFQSubmission(models.Model):
    organization = models.CharField(max_length=255)
    officer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=80)
    division = models.CharField(max_length=200, blank=True)
    incoterm = models.CharField(max_length=120, blank=True)
    quantity = models.CharField(max_length=120, blank=True)
    pol = models.CharField(max_length=200, blank=True)
    pod = models.CharField(max_length=200, blank=True)
    specifications = models.TextField()
    require_nda = models.BooleanField(default=True)
    source_page = models.CharField(max_length=80, default='home')
    reference = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'RFQ submission'

    def __str__(self):
        return f'{self.reference or self.pk} — {self.organization}'


class ContactInquiry(models.Model):
    procurement_type = models.CharField(max_length=120, blank=True)
    full_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=120, blank=True)
    commodity = models.CharField(max_length=255, blank=True)
    quantity = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)
    payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contact inquiries'

    def __str__(self):
        return f'{self.full_name} — {self.email}'


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email
