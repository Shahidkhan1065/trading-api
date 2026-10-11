from django.core.management.base import BaseCommand
from cms import models

LOGO = '/logo.svg'

IMAGES = {
    'heroPort': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAYE3YYT1NGoI3DmxV_U7oRwu_QTGmESFOE2CtVTEEF-xDPaLQsT_ApLOQJJVSz-AEtmtUjMfqcleREpuC-3FFhylo7-WlZKK1IfhtInUjESwqFnDJ2tDL5lgM5BqDxbZzw2Y067ui_Gl_bQa-7aVCw4LKlvkwNSW7zRdQUl4dPDa1ZPmn5p0kiBT5x7QRyasT2oL7IBiAo91VI2dQxSOd2bPhWLOrTiIzrPWdTxeHJoIEkwp4-fl6jkg',
    'metals': 'https://lh3.googleusercontent.com/aida-public/AB6AXuARkEiT7RwZIhSQuq3IOUodBnpUQknsDBbElnYIvuefb7Ppt_ZdUYtshn7QnySi9nsZqYf9dsQs0JJB3tMDBrWV2zfrNMaky4Vx-G3uM_yUp-na8QZ7iKBkfm85EMDm6lcLv4-rOq_9lcZ1Fun53Uw9e2UuliOp4CxNgBew5AHY7X4InLDrT16N4vYF8v7hYimOeDa2C8KouVShcKOb4gQ6mH_UM5Hzob77mzieJXycnKXs3YBGhSSEOA',
    'airCargo': 'https://lh3.googleusercontent.com/aida-public/AB6AXuB6UzheDWLm91rIQJSe-yJiPq2S23gDXhRGn2e_tvLipikx91QgDLrYNJHQq4tWPxDKPgmuev_6-KIFkMxO2RXI54xMgrf3teMh5BAYSE2K43v5Ac8KTRfjNPQkEOi7BqkGVtTBAVWt1JglhZX8TAlvntca2lq24cyJ6faFLj4Ue8A9MgMlIYU05WwkiCtCz7CDelan6LaCM9xaG0E_dEOvkcLivg1mY7xUKvMKmpVDSrqg4t-2BIBtlg',
    'warehouse': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDdkgWmiMYkX_9nOLBR4kEe5dHyFKrFgbdaJ5PY9aikopdqTRejP8M3WxTjDl7x6NPoyHzO6AYSvG09LzLBW_Xff82ZzGAAPjV091V3ezLMJi2Oc7xA81sU62xAkil-Xi-aA-z1v4Zp9CARtx5oiM_TSI1DhJoZIOcXYHmuQqN8RWKcxNmDQJlMHSqjF1e_j1dATS4_w6UY56tn3ZR2fl50kcKT0n3WixByIP2wkvh7zpALDRxCyJ5pFg',
    'electrical': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDAJ00Hede1LsoTk9EgXiYQAXQNfY1oZ0T-PFJqZ6ex9JwJe6E-U4hrZ7kovAVl2SD3F4T9XGQl4fHX8d41wCepvxpXcXtjPovffHNkvKcgHLO06ukPxLcTaFrmIgbagQdR55M7dEMiWASvi9zZVlw5wKCfpprPzTm03PrDh0C7GJSupwkzEhno18q2TmFcoUhHFVmJ_h6Xkd5rGqNhbXsn3kFyo06ii9zqrWVX56DjOpU_NiTgvf_6zA',
    'agri': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCFPJImucQZ44CqNOwHTg6VBvuhW8aeHRcfS9sCrKZM0aU4lLaBMoONHrMw6y2jNg5J2eWgF778WqMWoyV3iCsepkvKjrRGdPI6MCx50KWGLngCYvs0O0K-TU8sANwDhvliEkSBu04lpOX6-4BFS4ErOocK7WxwAjHD631lNVoqQWRabiCGOhVw9ab-syi-fOkAvYe6tdlctQcMeF6ek9iiNlp4O-AWnZeetN8FMIWzzWBeisraaNHH7A',
    'chemicals': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDfYvKI_ZAnRBYFfpfaLxKTZRcnyYPxYQIk3dcbVEeTSyzu_Vimfx0RSAFNszLgLt08a0RXkaGIwn6dhRDz2ilNQ4aUgjnJReo8GZLziaEWhE9cVAjl3FG896QBqdbf4foW5N_6ZmRyMc2PgCt2c6Y0z9uHHeoRWIIhTnzkOUiNHc46bQ73O9HZm8FxEsjTAiRzxs5s-XTJVu6MLVDsOJsmnGncSa8s5FTzhFU8VYxVRymTL8m63CykGA',
}


class Command(BaseCommand):
    help = 'Seed Al Ealami Trading CMS with default site content'

    def handle(self, *args, **options):
        self.stdout.write('Seeding content...')
        self._site()
        self._nav()
        self._offices()
        self._sections()
        self._stats()
        self._home_divisions()
        self._pillars()
        self._partners()
        self._testimonials()
        self._corridors()
        self._market()
        self._vessels()
        self._rfq_benefits()
        self._trading_divisions()
        self._incoterms()
        self._quality()
        self._faqs()
        self.stdout.write(self.style.SUCCESS('Content seeded successfully.'))

    def _site(self):
        models.SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                'company_name': 'Al Ealami Trading',
                'tagline': 'Global Enterprise Network',
                'logo_url': LOGO,
                'phone_primary': '+971 4 800 EALAMI',
                'phone_secondary': '+971 (0)2 449 8800',
                'email_trading': 'trading-desk@alealamitrading.com',
                'email_general': 'info@alealamitrading.com',
                'footer_blurb': (
                    'Institutional multi-commodity trading, cold-chain transport corridors, '
                    'and sovereign procurement networks across GCC, Africa, and East Asia.'
                ),
                'accreditation_badges': ['ISO 9001:2015', 'GDP PHARMA', 'HACCP CERTIFIED'],
            },
        )

    def _nav(self):
        models.NavLink.objects.all().delete()
        header = [
            ('/', 'Home'),
            ('/about', 'About Us'),
            ('/trading-divisions', 'Trading Divisions'),
            ('/supply-chain', 'Supply Chain & Logistics'),
            ('/quality', 'Quality & Compliance'),
            ('/contact', 'Contact Us / RFQ'),
        ]
        footer = [
            ('/about', 'Institutional Profile'),
            ('/trading-divisions', 'Commercial Divisions'),
            ('/supply-chain', 'Freight Forwarding & Ports'),
            ('/quality', 'Compliance & Trade Regulations'),
            ('/contact', 'Submit Procurement Tender (RFQ)'),
        ]
        for i, (path, label) in enumerate(header):
            models.NavLink.objects.create(location='header', path=path, label=label, order=i)
        for i, (path, label) in enumerate(footer):
            models.NavLink.objects.create(location='footer', path=path, label=label, order=i)

    def _offices(self):
        models.Office.objects.all().delete()
        data = [
            ('Group Office', 'FF 472–473, Pushkar Industrial Estate, Shop No. 153, 96/1, Phase-1, Vatva, Ahmedabad, Gujarat 382445, India', '+91 81286 10269', True, True),
            ('Trade Corridor', 'Ahmedabad · Surat — Ports: Mundra · Hazira · Kandla', '', True, True),
            ('Jyotiling Industry', 'Thermal equipment & industrial projects — 200+ projects across 21 countries', '', True, False),
            ('Jyotiling Logistics', 'West-coast India container and bulk programmes', '', True, False),
            ('Global Corridors', 'India origin · World supply · Mill & plant delivery', '', False, True),
        ]
        for i, (name, address, phone, about, footer) in enumerate(data):
            models.Office.objects.create(
                name=name, address=address, phone=phone,
                show_in_about=about, show_in_footer=footer, order=i,
            )

    def _sections(self):
        models.PageSection.objects.all().delete()
        sections = [
            ('home', 'hero', 'Global Trade Network • Live Telemetry Active',
             'Connecting Global Markets Through Precision Trading & Logistics',
             'Al Ealami Trading is an international multi-commodity trading house and end-to-end logistics partner bridging manufacturers, industrial buyers, and global trade corridors.',
             '', IMAGES['heroPort'], 'Explore Trading Divisions', '#divisions',
             {'secondary_cta': 'Request Formal RFQ', 'secondary_href': '#rfq-desk',
              'bunker_index': 'Bunker Index: $592.40/MT', 'lc_status': 'LC Facility Active',
              'hub_badge': 'JAFZA • ADGM'}),
            ('home', 'divisions_header', 'Institutional Trading Capabilities',
             'Enterprise Commercial Divisions',
             'Integrated commodity arbitrage, chartering, multimodal routing, and bonded warehousing engineered for global scale.',
             '', '', '', '', {}),
            ('home', 'pillars_header', 'Strategic Edge',
             'Institutional Architecture & Governance',
             'Built on fiscal strength, certified provenance, and sovereign-grade compliance mechanisms.',
             '', '', '', '', {}),
            ('home', 'corridors_header', 'Geopolitical Reach',
             'Active Trans-Continental Trade Corridors', '', '', '', '', '', {}),
            ('home', 'partners_header', 'Accredited Sovereign & Maritime Alliances',
             '', 'Verified Under International Chamber of Commerce (ICC) Regulations', '', '', '', '', {}),
            ('home', 'testimonials_header', 'Institutional Validation',
             'Executive Stakeholder Testimonials', '', '', '', '', '', {}),
            ('home', 'rfq_header', 'Tender & Procurement Portal',
             'Request a Formal Institutional Quotation',
             'Connect directly with our commercial desk for multi-ton commodity orders, vessel slots, or time-sensitive multimodal supply chain contracts.',
             '', '', '', '', {}),
            ('about', 'hero', 'About Us',
             'Jyotiling Impex',
             'Lighting the path of global commodity trade',
             '', IMAGES['heroPort'], '', '',
             {'pills': 'AGRO · EDIBLE OILS · PETROLEUM CRUDE · UREA · AMMONIA · TEXTILE CHEMICALS',
              'group_line': 'A Jyotiling Group Company'}),
            ('about', 'story', '',
             'A trading house built on industrial trust.',
             'Jyotiling Impex Pvt. Ltd. is the dedicated global trading arm of the Jyotiling Group — a Gujarat industrial house trusted across thermal equipment, logistics and international projects.',
             'We bring that same discipline into agri-commodities, edible oils, petroleum crude, fertilizers and textile-process chemicals. Every parcel is a promise of specification, timing and honour — not an anonymous lot.\n\nFrom Ahmedabad and Surat, and through the deep-sea ports of Mundra, Hazira and Kandla, we connect Indian origin with global demand, and world supply with Indian mills, refiners and plants.',
             '', '', '',
             {
                 'name_title': 'The Name',
                 'name_body': 'Jyoti — the sacred flame. A promise of clarity, continuity and light in every contract we honour.',
                 'group_title': 'The Group',
                 'group_body': 'Born from a house that has delivered 200+ industrial projects across 21 countries. Jyotiling Impex trades with the same seriousness the Group engineers with.',
                 'cards': [
                     {'title': '01 · Origin & integrity',
                      'desc': 'Verified mills, crushers, refineries and chemical manufacturers. COA, specs and traceable lots as standard.'},
                     {'title': '02 · Port-led Gujarat',
                      'desc': 'Ahmedabad, Surat and the west-coast ports — Mundra, Hazira and Kandla — for container and bulk programmes.'},
                     {'title': '03 · Three desks, one standard',
                      'desc': 'Agro & oils, energy & fertilizers, and textile chemicals — each with a named counterpart and clean documentation.'},
                 ],
             }),
            ('about', 'desks', '',
             'What we trade',
             'Three desks. One paperwork standard. Flexible lots — from a trial container to a vessel nomination.',
             '', '', '', '',
             {
                 'desks': [
                     {
                         'title': 'Agro & Oils',
                         'items': [
                             'Sugar — refined, plantation white and raw, ICUMSA as specified',
                             'Rice — basmati and non-basmati, including 1121, IR64, Sona Masuri',
                             'Wheat — milling and feed grades',
                             'Pulses — toor, moong, urad, chana, masoor',
                             'Sunflower oil, palm oil (CPO, RBD olein & stearin), crude vegetable oils',
                             'Animal tallow — technical and feed grades',
                         ],
                     },
                     {
                         'title': 'Energy & Fertilizers',
                         'items': [
                             'Petroleum crude oil — grade, API and sulphur as nominated',
                             'Tanker, parcel and bonded programmes via west-coast India',
                             'Urea — prilled and granular, agri and industrial',
                             'Ammonia — anhydrous, for fertilizer and industrial circuits',
                             'ISO tank, bagged, bulk and terminal lots',
                         ],
                     },
                     {
                         'title': 'Textile Chemicals',
                         'items': [
                             'H-Acid — dye intermediate for azo and reactive dyes',
                             'Vinyl sulfone (VS) — reactive dye intermediates',
                             'LABSA — detergent active for cakes and powders',
                             'Sulphur — industrial grade',
                             'Allied process chemicals on indent, with COA and SDS',
                         ],
                     },
                 ],
             }),
            ('about', 'process', '',
             'How a desk works',
             'From enquiry to discharge, buyers and sellers always know where the parcel stands.',
             '', '', '', '',
             {
                 'steps': [
                     {'num': '01', 'title': 'Enquire', 'desc': 'Grade, quantity, packing, destination and window.'},
                     {'num': '02', 'title': 'Offer', 'desc': 'Firm or subject offer, FOB / CIF / CFR / ex-works.'},
                     {'num': '03', 'title': 'Contract', 'desc': 'PI with Incoterms, inspection and payment instrument.'},
                     {'num': '04', 'title': 'Quality', 'desc': 'Allocation, survey if nominated, COA and loading photos.'},
                     {'num': '05', 'title': 'Ship', 'desc': 'Booking, documents, insurance as agreed, tracked to arrival.'},
                     {'num': '06', 'title': 'Settle', 'desc': 'Documents against LC or agreed terms. Repeat programme.'},
                 ],
             }),
            ('about', 'cta', 'Let us open a desk for you',
             'Talk to Jyotiling Impex',
             '“Obsessed with quality — growth and profit follow.”',
             'The Jyotiling Group Philosophy',
             '', 'Contact Commercial Desk', '/contact',
             {
                 'phone': '+91 81286 10269',
                 'phone_href': 'tel:+918128610269',
                 'email': 'jyotilingindustry@gmail.com',
                 'email_href': 'mailto:jyotilingindustry@gmail.com',
                 'corridor': 'Ahmedabad · Surat\nPorts: Mundra · Hazira · Kandla',
                 'office': 'FF 472–473, Pushkar Industrial Estate,\nShop No. 153, 96/1, Phase-1, Vatva,\nAhmedabad, Gujarat 382445, India',
             }),
            ('quality', 'hero', 'Compliance & Trade Regulations',
             'Quality Assurance & Institutional Compliance Framework',
             'Every Al Ealami shipment is bound to internationally enforceable inspection protocols, clean title transfers, and sovereign-grade regulatory compliance.',
             '', '', '', '', {}),
            ('quality', 'cta', '', 'Need a Compliance Briefing?',
             'Our legal and compliance desk can provide sanctions screening protocols, inspection agency appointments, and Incoterm risk allocation memos.',
             '', '', 'Contact Compliance Desk', '/contact', {}),
            ('contact', 'hero', 'Global Commercial Gateway // RFQ Console 4.2',
             'Partner With Al Ealami Trading',
             'Submit your commercial trading specifications, bulk commodity requirements, or institutional logistics partnership proposals. Handled directly by registered trade directors across ADGM and JAFZA trade desks.',
             '', '', '', '',
             {'response_time': '3 hrs 42 mins', 'sla': '< 24h Commercial Term Sheet'}),
            ('trading', 'hero', 'Commercial Portfolio',
             'Trading Divisions',
             'Institutional commodity desks spanning metals, electrical infrastructure, agri-bulk, and petrochemical polymers.',
             '', '', '', '', {}),
            ('supply-chain', 'hero', 'Freight & Multimodal',
             'Supply Chain & Logistics',
             'Ocean, air, and land corridors with live port telemetry and bonded freezone distribution.',
             '', '', '', '', {}),
        ]
        for i, (page, key, eyebrow, title, subtitle, body, image, cta, href, extra) in enumerate(sections):
            models.PageSection.objects.create(
                page=page, key=key, eyebrow=eyebrow, title=title,
                subtitle=subtitle, body=body, image_url=image,
                cta_label=cta, cta_href=href, extra=extra, order=i,
            )

    def _stats(self):
        models.Stat.objects.all().delete()
        home = [
            ('38+', 'Countries Served', 'Integrated trade gateways', 'text-secondary-fixed'),
            ('1.8M', 'Metric Tons Traded', 'Annual cross-border throughput', 'text-surface-container-lowest'),
            ('99.4%', 'On-Time Dispatch', 'Ocean & multimodal freight SLA', 'text-secondary-container'),
            ('ISO', '9001:2015 • GDP', 'Global compliance certified', 'text-surface-container-lowest'),
        ]
        about = [
            ('38+', 'Countries Served', '', ''),
            ('1.8M', 'MT Annual Throughput', '', ''),
            ('450k+', 'SQM Bonded Storage', '', ''),
            ('99.4%', 'On-Time Dispatch', '', ''),
        ]
        for i, (v, l, s, c) in enumerate(home):
            models.Stat.objects.create(page='home', value=v, label=l, sublabel=s, color_class=c, order=i)
        for i, (v, l, s, c) in enumerate(about):
            models.Stat.objects.create(page='about', value=v, label=l, sublabel=s, color_class=c, order=i)

    def _home_divisions(self):
        models.HomeDivision.objects.all().delete()
        data = [
            ('01', 'Bulk & Structural', 'Industrial Commodities & Metals',
             'Primary and secondary raw materials, rebar, structural steel, aluminum billets, petrochemical polymers, and heavy manufacturing inputs.',
             IMAGES['metals'], [['Incoterms', 'CIF, FOB, CFR, DDP'], ['Min Order Quantity', '500 MT Standard']],
             'Procure Commodity →'),
            ('02', 'FCL / LCL / Breakbulk', 'Global Ocean & Multimodal Freight',
             'Full-vessel chartering, dry-bulk liners, deep-water port operations, ISO containerized shipments, and trans-Eurasian rail connections.',
             IMAGES['heroPort'], [["Container Types", "20' / 40' / OT / Reefer"], ['Port Terminals', '120+ Direct Gateways']],
             'Book Vessel Slot →'),
            ('03', 'Time-Definite Express', 'Air Cargo & Express Logistics',
             'Dedicated heavy air freighters, temperature-controlled pharmaceutical corridors, priority aerospace AOG dispatches, and emergency cargo.',
             IMAGES['airCargo'], [['Dispatch Window', '< 12-24 Hours Turnaround'], ['Specialized Handling', 'Pharma GDP, Dangerous Goods']],
             'Charter Aircraft →'),
            ('04', 'Bonded & Freezone', 'Warehousing & 3PL Distribution',
             'Freezone bonded hubs in Jebel Ali, ADGM and Rotterdam with automated racking, inventory cross-docking, and end-mile distribution.',
             IMAGES['warehouse'], [['Storage Area', '450,000+ SQM Combined'], ['Integration', 'WMS / SAP / Oracle Live EDI']],
             'Reserve Facility →'),
        ]
        for i, row in enumerate(data):
            models.HomeDivision.objects.create(
                division_id=row[0], tag=row[1], title=row[2], description=row[3],
                image_url=row[4], rows=row[5], cta_label=row[6], order=i,
            )

    def _pillars(self):
        models.Pillar.objects.all().delete()
        data = [
            ('account_balance', 'Trade Finance & LC Structuring',
             'Documentary letters of credit (DLC, SBLC), deferred payment options, and sovereign trade financing structured through top-tier global institutions.',
             '• UCP 600 Governed'),
            ('verified', 'Assurance & Origin Testing',
             'Independent SGS, Bureau Veritas, and Cotecna pre-shipment inspections ensuring material purity, mechanical grade, and accurate weight documentation.',
             '• SGS Verified Portals'),
            ('hub', 'Direct Tier-1 Producers',
             'Vetted partnerships directly with smelters, refineries, and industrial manufacturers eliminating intermediary inflation and speculative price gouging.',
             '• 400+ Qualified Mills'),
            ('shield_with_heart', 'Direct Customs Clearance',
             'Licensed in-house customs brokers managing Harmonized Tariff Schedules, bilateral free trade protocols, and accelerated bonded transit lanes.',
             '• Fast-Track Green Channel'),
        ]
        for i, (icon, title, desc, badge) in enumerate(data):
            models.Pillar.objects.create(icon=icon, title=title, description=desc, badge=badge, order=i)

    def _partners(self):
        models.Partner.objects.all().delete()
        for i, (name, role) in enumerate([
            ('DP WORLD', 'Licensed Operator'),
            ('MAERSK', 'Direct Carrier Allocation'),
            ('SGS GLOBAL', 'Certified Inspection'),
            ('BUREAU VERITAS', 'Quality Verification'),
            ('EMIRATES SKY', 'Airfreight Allotment'),
            ('ADGM REGISTERED', 'Financial Free Zone'),
        ]):
            models.Partner.objects.create(name=name, role=role, order=i)

    def _testimonials(self):
        models.Testimonial.objects.all().delete()
        data = [
            (
                '“Al Ealami Trading restructured our bulk hot-rolled coils delivery into King Abdulaziz Port with absolute punctuality. Their documentary LC execution eliminated foreign exchange risk completely.”',
                'Tariq Al-Mansoor',
                'VP Procurement • Gulf Infrastructure Conglomerate',
            ),
            (
                '“Chartering 3 dedicated 777 air freighters for pharmaceutical cool-chain transfers between Dubai and West Africa was managed impeccably. Real-time temperature logging was compliant with international GDP standards.”',
                'Dr. Helene Van Dijk',
                'Global Logistics Director • Euro-Med LifeSciences',
            ),
            (
                '“Having an integrated partner handling both bonded freezone storage at JAFZA and multimodal ocean logistics provided our supply chain with an unmatched operational moat.”',
                'Chen Wei Lin',
                'Managing Director • Asia-Pacific Raw Materials Ltd',
            ),
        ]
        for i, (quote, name, role) in enumerate(data):
            models.Testimonial.objects.create(quote=quote, name=name, role=role, order=i)

    def _corridors(self):
        models.Corridor.objects.all().delete()
        data = [
            ('middle-east', 'Middle East & GCC', 'GCC Sovereign Hub',
             'Arabian Gulf • Red Sea Strategic Corridor',
             'Primary operational hub headquartered in Abu Dhabi with direct berthing rights across Jebel Ali (Dubai), Khalifa Port, Dammam, and King Abdullah Port. Connecting regional downstream energy with import heavy machinery.',
             'Jebel Ali • Khalifa • Dammam', '2 - 4 Days Intra-GCC', '240,000 MT / Month', 'Steel, Polymers, Pipes, Petrochem'),
            ('asia-pacific', 'Asia-Pacific', 'Far East Gateway',
             'Singapore Straits • East Asia Industrial Belt',
             'Direct container lanes and breakbulk transport linking Shanghai, Ningbo, Busan, and Singapore to GCC energy and African raw materials corridors with expedited customs transit.',
             'Singapore • Shanghai • Busan', '12 - 16 Days Sea Freight', '410,000 MT / Month', 'Electronics, Heavy Equipment, Metals'),
            ('europe', 'Europe / North Sea', 'North Atlantic Terminal',
             'Rotterdam • Antwerp • Mediterranean Axis',
             'Deepwater container conduits and multimodal rail links across Northern Europe and the Mediterranean, interfacing specialized metallurgical products and high-grade industrial valves.',
             'Rotterdam • Antwerp • Genoa', '14 - 18 Days Maritime Line', '185,000 MT / Month', 'Specialty Alloys, Pharma, Machinery'),
            ('africa', 'Africa East/West', 'Sub-Saharan Corridor',
             'Mombasa • Durban • Djibouti Maritime Arc',
             'Strategic mineral ore extraction export corridors and agricultural commodities delivery routes servicing East and West African sovereign distribution authorities.',
             'Mombasa • Dar es Salaam • Durban', '7 - 10 Days Direct Corridor', '130,000 MT / Month', 'Agricultural Bulk, Copper, Cement'),
        ]
        for i, row in enumerate(data):
            models.Corridor.objects.create(
                key=row[0], label=row[1], badge=row[2], title=row[3],
                description=row[4], ports=row[5], transit=row[6],
                volume=row[7], goods=row[8], order=i,
            )

    def _market(self):
        models.MarketIndex.objects.all().delete()
        for i, (label, value, trend) in enumerate([
            ('Hot-Rolled Coil (FOB AG)', '$615/MT (+1.4%)', 'up'),
            ('Billet Steel (CFR GCC)', '$520/MT', 'flat'),
            ('Ocean Freight SCFI', '2,145 pts', 'up'),
            ('Industrial Copper Gr-A', '$9,310/MT', 'flat'),
            ('Jet Fuel FOB ME', '$94.80/bbl', 'up'),
        ]):
            models.MarketIndex.objects.create(label=label, value=value, trend=trend, order=i)

    def _vessels(self):
        models.VesselStream.objects.all().delete()
        models.VesselStream.objects.create(
            name='MV AL-EALAMI VOYAGE 409', route='Rotterdam → Jebel Ali (CIF)',
            status='Berthing', status_style='secondary', order=0,
        )
        models.VesselStream.objects.create(
            name='AIR CHARTER AE-772', route='DXB Hub → Singapore Changi',
            status='En Route', status_style='tertiary', order=1,
        )

    def _rfq_benefits(self):
        models.RfqBenefit.objects.all().delete()
        data = [
            ('speed', '4-Hour Commercial SLA',
             'Initial feasibility assessment and indicative freight index provided within 240 minutes.'),
            ('lock', 'Mutual NDA Governed',
             'Strict institutional confidentiality on pricing, shipping manifests, and banking coordinates.'),
            ('support_agent', 'Direct Broker Dispatch',
             'Desk assigned trade representative stationed in Abu Dhabi or Singapore.'),
        ]
        for i, (icon, title, desc) in enumerate(data):
            models.RfqBenefit.objects.create(icon=icon, title=title, description=desc, order=i)

    def _trading_divisions(self):
        models.TradingDivision.objects.all().delete()
        data = [
            dict(
                category='metals', badge='Division 01 // Heavy Metallurgy', code='MET-IND-880',
                title='Industrial Raw Materials & Structural Steel',
                description='Consolidated procurement and direct mill allocation for structural steel shapes, seamless carbon line pipe, reinforcing bar, and non-ferrous ingots serving EPC contractors, offshore yards, and mega-infrastructure developments across GCC and East Africa.',
                image_url=IMAGES['metals'],
                image_alt='Al Ealami Industrial Steel and Heavy Raw Materials Logistics Warehouse',
                corridor='Corridor: Jebel Ali • Dammam', stock='Ready Stock 140K MT', image_left=True,
                specs=[
                    ['Specification Standards', 'ASTM A36, A572, A106, DIN 17100, JIS G3101', 'EN 10025 S355JR Available'],
                    ['Minimum Order Quantity (MOQ)', '500 Metric Tons (Breakbulk)', 'FCL Containerized: 100 MT'],
                    ['Primary Origin Points', 'Japan, South Korea, Turkey, UAE', 'Mill Test Certificates 3.1 & 3.2'],
                ],
                chips=['Seamless C-Steel', 'H-Beams & UB', 'Deformed Rebar Gr 60', 'Hot Rolled Coils (HRC)'],
                cta_label='Inquire Metallurgy',
                division_name='Industrial Raw Materials & Steel',
            ),
            dict(
                category='electrical', badge='Division 02 // Power & Civil Works', code='ELEC-INFRA-410',
                title='Construction & Heavy Electrical Supplies',
                description='Engineered electrical balance of plant (eBoP), high and extra-high voltage transmission cabling, substation switchgear modules, ductile iron pressure piping, and heavy earthwork hardware engineered for power generation, municipal utilities, and renewable solar arrays.',
                image_url=IMAGES['electrical'],
                image_alt='Power distribution and cable infrastructure warehouse',
                corridor='Tested: KEMA & ASTA Certified', stock='Immediate Dispatch', image_left=False,
                specs=[
                    ['Specification Standards', 'IEC 60502, IEC 60840, IEEE C37, BS 5467', 'ISO 2531 Ductile Water Piping'],
                    ['Minimum Order Quantity (MOQ)', '3,000 Meters (HV / MV Cable)', 'Full Substation Bay Assembly Sets'],
                    ['Primary Origin Points', 'Germany, France, Saudi Arabia, Oman', 'Pre-commissioning factory witness'],
                ],
                chips=['XLPE Armoured 33kV', 'GIS Substation Skids', 'DI Piping Class K9', 'Copper Busbars (99.99%)'],
                cta_label='Inquire Electrical',
                division_name='Construction & Heavy Electrical Supplies',
            ),
            dict(
                category='agri', badge='Division 03 // Essential Food Security', code='AGRI-GRAIN-109',
                title='Agricultural Commodities & Bulk Foodstuff',
                description='National strategic reserve trading and commercial supply of milling wheat, animal feed barley, non-GMO yellow corn, refined ICUMSA 45 white cane sugar, and bulk crude sunflower/palm oils. Backed by dedicated charter tonnage and port transshipment elevators.',
                image_url=IMAGES['agri'],
                image_alt='Agricultural grain shipping and harbor discharge terminal',
                corridor='Corridors: Black Sea • Santos • Salalah', stock='GAFTA • FOSFA Compliant', image_left=True,
                specs=[
                    ['Specification Standards', 'GAFTA 119/120, FOSFA 53, ISO 22000, HACCP', 'Phytosanitary & Radiation Clean'],
                    ['Minimum Order Quantity (MOQ)', '12,500 MT (Handymax Lot)', 'Sugar: 2,500 MT Containerized'],
                    ['Primary Origin Points', 'Brazil, Australia, Romania, India, Ukraine', 'Independent SGS Loading Inspection'],
                ],
                chips=['Milling Wheat 12.5%', 'ICUMSA 45 Sugar', 'Crude Degummed Soy', 'Feed Barley Grade 2'],
                cta_label='Inquire Agri-Bulk',
                division_name='Agricultural Commodities & Foodstuff',
            ),
            dict(
                category='chemicals', badge='Division 04 // Polymers & Specialized Liquids', code='POLY-CHEM-602',
                title='Petrochemicals & Industrial Polymers',
                description='High-throughput commercial allocation of virgin polymer resins (HDPE, LDPE, PP, PVC), industrial chemical solvents, glycols, and synthetic lubricants. Engineered for blow molding, automotive extrusion, flexible film packaging, and industrial chemical processing plants.',
                image_url=IMAGES['chemicals'],
                image_alt='Petrochemical and polymer processing logistics facility',
                corridor='EU REACH & GHS Certified', stock='ISO Tank / Bulk Bag', image_left=False,
                specs=[
                    ['Specification Standards', 'ASTM D1238 (MFI), ISO 1133, REACH (EC) 1907/2006', 'Full SDS & Certificate of Analysis'],
                    ['Minimum Order Quantity (MOQ)', '100 Metric Tons (Resins)', 'Liquid Bulk: 4 x 24,000L ISO Tanks'],
                    ['Primary Origin Points', 'Saudi Arabia, UAE, South Korea, Singapore', 'Dedicated bonded chemical storage'],
                ],
                chips=['HDPE Film Grade', 'PP Homo/Copolymer', 'Monoethylene Glycol (MEG)', 'PVC Suspension K-67'],
                cta_label='Inquire Petrochemicals',
                division_name='Petrochemicals & Industrial Polymers',
            ),
        ]
        for i, row in enumerate(data):
            models.TradingDivision.objects.create(order=i, **row)

    def _incoterms(self):
        models.Incoterm.objects.all().delete()
        data = [
            ('CIF', 'CIF — Cost, Insurance and Freight',
             'Al Ealami covers maritime transport costs and procures comprehensive cargo insurance (Institute Cargo Clauses A) up to the nominated port of destination. Risk transfers once goods are loaded on board at the origin terminal.',
             'Primary Sovereign Mode'),
            ('FOB', 'FOB — Free On Board',
             "Al Ealami clears goods for export and delivers them on board the buyer's nominated vessel at the designated origin port. The buyer assumes all costs, ocean freight, and insurance risk from that moment onward.",
             'Standard Breakbulk & Steel'),
            ('CFR', 'CFR — Cost and Freight',
             'Al Ealami pays ocean freight carriage to the named discharge port. The buyer arranges marine cargo insurance and assumes transit loss risk upon loading onto the ocean carrier.',
             'Bulk Agri / Grain Traders'),
            ('DDP', 'DDP — Delivered Duty Paid',
             'Al Ealami assumes maximum institutional obligation: handling ocean freight, port handling, customs clearance, import tariffs, and inland transport directly to buyer regional staging silos or warehouses.',
             'Turnkey Contractor Tier'),
            ('EXW', 'EXW — Ex Works',
             'Commodities are prepared and verified at Al Ealami regional bonded warehouse or partner production mill. The buyer assumes total logistics responsibility and freight arrangement from warehouse gates.',
             'Local Spot Pickups'),
        ]
        for i, (code, title, desc, badge) in enumerate(data):
            models.Incoterm.objects.create(code=code, title=title, description=desc, badge=badge, order=i)

    def _quality(self):
        models.QualityFramework.objects.all().delete()
        data = [
            ('verified_user', 'Third-Party Inspection',
             'SGS, Bureau Veritas, Intertek, and Saybolt pre-shipment and disport surveys with clean CCQ documentation for LC presentation.'),
            ('gavel', 'Sanctions & AML',
             'Tier-1 screening against OFAC, EU, and UN regimes. Level-3 KYC/AML on all counterparties before draft allocation.'),
            ('policy', 'Incoterms 2020',
             'CIF, FOB, CFR, DDP, and EXW protocols with transparent risk transfer and Institute Cargo Clauses A insurance where applicable.'),
            ('account_balance', 'Trade Finance',
             'Confirmed irrevocable LCs, DLCs, and SBLCs via Tier-1 banks under UCP 600. ADGM/DIFC escrow for sovereign contracts.'),
            ('local_shipping', 'GDP & HACCP',
             'Pharmaceutical GDP cold-chain corridors and HACCP-certified food-grade bonded vaults across JAFZA and regional hubs.'),
            ('workspace_premium', 'ISO Certifications',
             'ISO 9001:2015 quality management with continuous audit cycles across commercial and logistics operations.'),
        ]
        for i, (icon, title, desc) in enumerate(data):
            models.QualityFramework.objects.create(icon=icon, title=title, description=desc, order=i)

    def _faqs(self):
        models.FAQ.objects.all().delete()
        data = [
            (
                'What standard payment and banking instruments are accepted for bulk transactions?',
                'We work exclusively through Tier-1 and Top-50 global banks via Confirmed, Irrevocable Letters of Credit (LC), Documentary Letters of Credit (DLC payable 100% at sight at port of discharge after SGS inspection), and Standby Letters of Credit (SBLC). For select long-term revolving government contracts, sovereign guarantee frameworks and structured escrow via ADGM or DIFC courts are utilized.',
            ),
            (
                'What documentation is mandatory for initial ICPO/LOI processing?',
                "Every commercial inquiry must include an Irrevocable Corporate Purchase Order (ICPO) or formal Letter of Intent (LOI) on corporate letterhead, signed by an authorized signatory. It must state complete commodity grade specifications, target metric tonnage, acceptable delivery schedule, nominated discharge port, and the Buyer's designated banking institution with full contact details.",
            ),
            (
                'Which third-party inspection agencies are deployed for quality certification?',
                'All physical commodity parcels are independently tested, inspected, and certified at both the loading port and port of discharge by internationally accredited inspection entities, predominantly SGS, Bureau Veritas, Intertek, or Saybolt. Official certificates of quantity and quality (Q&Q) form an integral requirement of our bill of lading documentation packets.',
            ),
            (
                'How does Al Ealami Trading manage maritime demurrage and laytime risk?',
                'Demurrage agreements follow strict BIMCO charterparty standards (such as NOR, GENCON, or ASBATANKVOY). Laytime allowances and demurrage rates per day (or pro rata) are established transparently inside the Commercial Contract based on current market fixtures in Singapore, London, and the Gulf.',
            ),
        ]
        for i, (q, a) in enumerate(data):
            models.FAQ.objects.create(question=q, answer=a, order=i)
