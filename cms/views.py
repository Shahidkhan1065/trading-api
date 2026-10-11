from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models, serializers


def _sections_map(page: str):
    sections = models.PageSection.objects.filter(page=page, is_active=True)
    return {s.key: serializers.PageSectionSerializer(s).data for s in sections}


@api_view(['GET'])
def site_bootstrap(request):
    settings = models.SiteSettings.load()
    nav = models.NavLink.objects.filter(is_active=True)
    offices = models.Office.objects.filter(is_active=True)
    return Response({
        'settings': serializers.SiteSettingsSerializer(settings).data,
        'nav': {
            'header': serializers.NavLinkSerializer(
                nav.filter(location='header'), many=True
            ).data,
            'footer': serializers.NavLinkSerializer(
                nav.filter(location='footer'), many=True
            ).data,
        },
        'offices': serializers.OfficeSerializer(offices, many=True).data,
    })


@api_view(['GET'])
def home_content(request):
    return Response({
        'sections': _sections_map('home'),
        'stats': serializers.StatSerializer(
            models.Stat.objects.filter(page='home', is_active=True), many=True
        ).data,
        'divisions': serializers.HomeDivisionSerializer(
            models.HomeDivision.objects.filter(is_active=True), many=True
        ).data,
        'pillars': serializers.PillarSerializer(
            models.Pillar.objects.filter(is_active=True), many=True
        ).data,
        'partners': serializers.PartnerSerializer(
            models.Partner.objects.filter(is_active=True), many=True
        ).data,
        'testimonials': serializers.TestimonialSerializer(
            models.Testimonial.objects.filter(is_active=True), many=True
        ).data,
        'corridors': serializers.CorridorSerializer(
            models.Corridor.objects.filter(is_active=True), many=True
        ).data,
        'market_indices': serializers.MarketIndexSerializer(
            models.MarketIndex.objects.filter(is_active=True), many=True
        ).data,
        'vessel_streams': serializers.VesselStreamSerializer(
            models.VesselStream.objects.filter(is_active=True), many=True
        ).data,
        'rfq_benefits': serializers.RfqBenefitSerializer(
            models.RfqBenefit.objects.filter(is_active=True), many=True
        ).data,
        'settings': serializers.SiteSettingsSerializer(
            models.SiteSettings.load()
        ).data,
    })


@api_view(['GET'])
def about_content(request):
    return Response({
        'sections': _sections_map('about'),
        'stats': serializers.StatSerializer(
            models.Stat.objects.filter(page='about', is_active=True), many=True
        ).data,
        'offices': serializers.OfficeSerializer(
            models.Office.objects.filter(is_active=True, show_in_about=True),
            many=True,
        ).data,
    })


@api_view(['GET'])
def trading_content(request):
    return Response({
        'sections': _sections_map('trading'),
        'divisions': serializers.TradingDivisionSerializer(
            models.TradingDivision.objects.filter(is_active=True), many=True
        ).data,
        'incoterms': serializers.IncotermSerializer(
            models.Incoterm.objects.filter(is_active=True), many=True
        ).data,
    })


@api_view(['GET'])
def quality_content(request):
    return Response({
        'sections': _sections_map('quality'),
        'frameworks': serializers.QualityFrameworkSerializer(
            models.QualityFramework.objects.filter(is_active=True), many=True
        ).data,
    })


@api_view(['GET'])
def contact_content(request):
    return Response({
        'sections': _sections_map('contact'),
        'faqs': serializers.FAQSerializer(
            models.FAQ.objects.filter(is_active=True), many=True
        ).data,
        'settings': serializers.SiteSettingsSerializer(
            models.SiteSettings.load()
        ).data,
        'offices': serializers.OfficeSerializer(
            models.Office.objects.filter(is_active=True), many=True
        ).data,
    })


@api_view(['GET'])
def supply_chain_content(request):
    return Response({
        'sections': _sections_map('supply-chain'),
    })


@api_view(['POST'])
def submit_rfq(request):
    serializer = serializers.RFQSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        return Response(
            {
                'ok': True,
                'reference': obj.reference,
                'message': (
                    f'Quotation request submitted to Al Ealami Trading Desk. '
                    f'Reference #{obj.reference} generated.'
                ),
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_contact(request):
    serializer = serializers.ContactInquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'ok': True, 'message': 'Inquiry received. Our commercial desk will respond shortly.'},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def subscribe_newsletter(request):
    serializer = serializers.NewsletterSubscriberSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        models.NewsletterSubscriber.objects.update_or_create(
            email=email,
            defaults={'is_active': True},
        )
        return Response(
            {'ok': True, 'message': 'Subscribed to Al Ealami institutional commodity indices.'},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
