from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.site_bootstrap, name='site-bootstrap'),
    path('home/', views.home_content, name='home-content'),
    path('about/', views.about_content, name='about-content'),
    path('trading/', views.trading_content, name='trading-content'),
    path('quality/', views.quality_content, name='quality-content'),
    path('contact/', views.contact_content, name='contact-content'),
    path('supply-chain/', views.supply_chain_content, name='supply-chain-content'),
    path('rfq/', views.submit_rfq, name='submit-rfq'),
    path('inquiries/', views.submit_contact, name='submit-contact'),
    path('newsletter/', views.subscribe_newsletter, name='subscribe-newsletter'),
]
