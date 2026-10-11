from rest_framework import serializers
from . import models


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteSettings
        fields = [
            'company_name', 'tagline', 'logo_url', 'phone_primary',
            'phone_secondary', 'email_trading', 'email_general',
            'footer_blurb', 'accreditation_badges',
        ]


class NavLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NavLink
        fields = ['path', 'label', 'location']


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Office
        fields = ['name', 'address', 'phone', 'show_in_about', 'show_in_footer']


class PageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PageSection
        fields = [
            'key', 'eyebrow', 'title', 'subtitle', 'body',
            'image_url', 'cta_label', 'cta_href', 'extra',
        ]


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stat
        fields = ['value', 'label', 'sublabel', 'color_class']


class HomeDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HomeDivision
        fields = [
            'division_id', 'tag', 'title', 'description',
            'image_url', 'rows', 'cta_label',
        ]


class PillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pillar
        fields = ['icon', 'title', 'description', 'badge']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['name', 'role']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Testimonial
        fields = ['quote', 'name', 'role']


class CorridorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Corridor
        fields = [
            'key', 'label', 'badge', 'title', 'description',
            'ports', 'transit', 'volume', 'goods',
        ]


class MarketIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarketIndex
        fields = ['label', 'value', 'trend']


class VesselStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VesselStream
        fields = ['name', 'route', 'status', 'status_style']


class RfqBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RfqBenefit
        fields = ['icon', 'title', 'description']


class TradingDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TradingDivision
        fields = [
            'category', 'badge', 'code', 'title', 'description',
            'image_url', 'image_alt', 'corridor', 'stock', 'image_left',
            'specs', 'chips', 'cta_label', 'division_name',
        ]


class IncotermSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incoterm
        fields = ['code', 'title', 'description', 'badge']


class QualityFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QualityFramework
        fields = ['icon', 'title', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ['question', 'answer']


class RFQSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RFQSubmission
        fields = [
            'organization', 'officer_name', 'email', 'phone',
            'division', 'incoterm', 'quantity', 'pol', 'pod',
            'specifications', 'require_nda', 'source_page',
        ]

    def create(self, validated_data):
        from django.utils import timezone
        ts = timezone.now().strftime('%Y%m%d%H%M%S')
        validated_data['reference'] = f'AE-{ts}-RFQ'
        return super().create(validated_data)


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactInquiry
        fields = [
            'procurement_type', 'full_name', 'company', 'email',
            'phone', 'country', 'commodity', 'quantity', 'message', 'payload',
        ]


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsletterSubscriber
        fields = ['email']
