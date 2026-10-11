from django.contrib import admin
from . import models


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email_trading', 'phone_primary', 'updated_at')

    def has_add_permission(self, request):
        return not models.SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'path', 'location', 'order', 'is_active')
    list_filter = ('location', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'order', 'show_in_about', 'show_in_footer', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('page', 'key', 'title', 'order', 'is_active')
    list_filter = ('page', 'is_active')
    search_fields = ('key', 'title', 'eyebrow')
    list_editable = ('order', 'is_active')


@admin.register(models.Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'page', 'order', 'is_active')
    list_filter = ('page',)
    list_editable = ('order', 'is_active')


@admin.register(models.HomeDivision)
class HomeDivisionAdmin(admin.ModelAdmin):
    list_display = ('division_id', 'title', 'tag', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Pillar)
class PillarAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Corridor)
class CorridorAdmin(admin.ModelAdmin):
    list_display = ('key', 'label', 'badge', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'key': ('label',)}


@admin.register(models.MarketIndex)
class MarketIndexAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'trend', 'order', 'is_active')
    list_editable = ('value', 'order', 'is_active')


@admin.register(models.VesselStream)
class VesselStreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'route', 'status', 'order', 'is_active')
    list_editable = ('status', 'order', 'is_active')


@admin.register(models.RfqBenefit)
class RfqBenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.TradingDivision)
class TradingDivisionAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.Incoterm)
class IncotermAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'badge', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.QualityFramework)
class QualityFrameworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(models.RFQSubmission)
class RFQSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'reference', 'organization', 'officer_name', 'email',
        'division', 'created_at', 'is_reviewed',
    )
    list_filter = ('is_reviewed', 'division', 'source_page')
    search_fields = ('reference', 'organization', 'email', 'officer_name')
    readonly_fields = ('reference', 'created_at')
    list_editable = ('is_reviewed',)


@admin.register(models.ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company', 'procurement_type', 'created_at', 'is_reviewed')
    list_filter = ('is_reviewed', 'procurement_type')
    search_fields = ('full_name', 'email', 'company')
    list_editable = ('is_reviewed',)


@admin.register(models.NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)
