
Action: file_editor create /app/website/_generate.py --file-text "#!/usr/bin/env python3
\"\"\"Generate index.html for Taau Daaru Baaz Beer Shop website.
Produces a single, large, fully-static HTML file with 50+ products,
many sections, FAQs, gallery, reviews, etc.
\"\"\"
import os, textwrap

OUT = os.path.join(os.path.dirname(__file__), 'index.html')

# ----------------------- DATA ------------------------
BRANDS = [
    (\"Heineken\", \"Netherlands\", \"H\"),
    (\"Corona Extra\", \"Mexico\", \"C\"),
    (\"Budweiser\", \"USA\", \"B\"),
    (\"Carlsberg\", \"Denmark\", \"K\"),
    (\"Stella Artois\", \"Belgium\", \"S\"),
    (\"Guinness\", \"Ireland\", \"G\"),
    (\"Asahi\", \"Japan\", \"A\"),
    (\"Kingfisher\", \"India\", \"K\"),
    (\"Tuborg\", \"Denmark\", \"T\"),
    (\"Hoegaarden\", \"Belgium\", \"H\"),
    (\"Bira 91\", \"India\", \"B\"),
    (\"Peroni\", \"Italy\", \"P\"),
    (\"Erdinger\", \"Germany\", \"E\"),
    (\"Sapporo\", \"Japan\", \"S\"),
]

CATEGORIES = [
    (\"Lager\", \"fa-mug-saucer\", \"126\"),
    (\"Wheat Beer\", \"fa-wheat-awn\", \"84\"),
    (\"IPA\", \"fa-bottle-droplet\", \"72\"),
    (\"Stout\", \"fa-glass-water\", \"48\"),
    (\"Pilsner\", \"fa-beer-mug-empty\", \"60\"),
    (\"Craft\", \"fa-mountain\", \"92\"),
    (\"Imported\", \"fa-globe\", \"150\"),
    (\"Strong\", \"fa-fire-flame-curved\", \"55\"),
]

# 60 products
PRODUCT_NAMES = [
    (\"Heineken Original\",   \"lager\",    \"Netherlands\",  \"https://images.unsplash.com/photo-1618183479302-1e0aa382c36b?w=600&q=80\"),
    (\"Corona Extra Lime\",   \"lager\",    \"Mexico\",       \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80\"),
    (\"Budweiser King\",      \"lager\",    \"USA\",          \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=600&q=80\"),
    (\"Carlsberg Smooth\",    \"lager\",    \"Denmark\",      \"https://images.unsplash.com/photo-1608270586620-248524c67de9?w=600&q=80\"),
    (\"Stella Artois Gold\",  \"lager\",    \"Belgium\",      \"https://images.unsplash.com/photo-1566633806327-68e152aaf26d?w=600&q=80\"),
    (\"Guinness Draught\",    \"stout\",    \"Ireland\",      \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"Asahi Super Dry\",     \"lager\",    \"Japan\",        \"https://images.unsplash.com/photo-1613766689591-5eea6bd28a04?w=600&q=80\"),
    (\"Kingfisher Premium\",  \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600&q=80\"),
    (\"Tuborg Classic\",      \"lager\",    \"Denmark\",      \"https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=600&q=80\"),
    (\"Hoegaarden White\",    \"wheat\",    \"Belgium\",      \"https://images.unsplash.com/photo-1577897267749-50b5d5a3f8a3?w=600&q=80\"),
    (\"Bira 91 White\",       \"wheat\",    \"India\",        \"https://images.unsplash.com/photo-1546158243-2d3f86317c80?w=600&q=80\"),
    (\"Bira 91 Blonde\",      \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1626078297693-c47b67f7b95e?w=600&q=80\"),
    (\"Bira 91 Boom\",        \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80\"),
    (\"Peroni Nastro Azzurro\",\"pilsner\", \"Italy\",        \"https://images.unsplash.com/photo-1600788907416-456578634209?w=600&q=80\"),
    (\"Erdinger Weissbier\",  \"wheat\",    \"Germany\",      \"https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=600&q=80\"),
    (\"Sapporo Premium\",     \"lager\",    \"Japan\",        \"https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=600&q=80\"),
    (\"Foster's Strong\",     \"strong\",   \"Australia\",    \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=600&q=80\"),
    (\"Tiger Crystal\",       \"lager\",    \"Singapore\",    \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80\"),
    (\"Modelo Especial\",     \"lager\",    \"Mexico\",       \"https://images.unsplash.com/photo-1608270586620-248524c67de9?w=600&q=80\"),
    (\"Becks Pilsner\",       \"pilsner\",  \"Germany\",      \"https://images.unsplash.com/photo-1566633806327-68e152aaf26d?w=600&q=80\"),
    (\"Paulaner Hefeweizen\", \"wheat\",    \"Germany\",      \"https://images.unsplash.com/photo-1577897267749-50b5d5a3f8a3?w=600&q=80\"),
    (\"Pilsner Urquell\",     \"pilsner\",  \"Czech\",        \"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600&q=80\"),
    (\"Leffe Blonde\",        \"craft\",    \"Belgium\",      \"https://images.unsplash.com/photo-1546158243-2d3f86317c80?w=600&q=80\"),
    (\"Estrella Damm\",       \"lager\",    \"Spain\",        \"https://images.unsplash.com/photo-1626078297693-c47b67f7b95e?w=600&q=80\"),
    (\"Brewdog Punk IPA\",    \"ipa\",      \"Scotland\",     \"https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80\"),
    (\"Goose Island IPA\",    \"ipa\",      \"USA\",          \"https://images.unsplash.com/photo-1600788907416-456578634209?w=600&q=80\"),
    (\"Lagunitas IPA\",       \"ipa\",      \"USA\",          \"https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=600&q=80\"),
    (\"Sierra Nevada Pale\",  \"craft\",    \"USA\",          \"https://images.unsplash.com/photo-1618183479302-1e0aa382c36b?w=600&q=80\"),
    (\"Simba Stout\",         \"stout\",    \"India\",        \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"White Owl Spark\",     \"wheat\",    \"India\",        \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80\"),
    (\"Simba Wit\",           \"wheat\",    \"India\",        \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=600&q=80\"),
    (\"Kati Patang Lager\",   \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1608270586620-248524c67de9?w=600&q=80\"),
    (\"Royal Challenge\",     \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1566633806327-68e152aaf26d?w=600&q=80\"),
    (\"Haywards 5000\",       \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"Knock Out Strong\",    \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1613766689591-5eea6bd28a04?w=600&q=80\"),
    (\"Bro Code Lager\",      \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600&q=80\"),
    (\"Geist Kamerunder\",    \"stout\",    \"India\",        \"https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=600&q=80\"),
    (\"Geist Witty Wit\",     \"wheat\",    \"India\",        \"https://images.unsplash.com/photo-1577897267749-50b5d5a3f8a3?w=600&q=80\"),
    (\"Bira 91 IPA\",         \"ipa\",      \"India\",        \"https://images.unsplash.com/photo-1546158243-2d3f86317c80?w=600&q=80\"),
    (\"Kingfisher Ultra\",    \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1626078297693-c47b67f7b95e?w=600&q=80\"),
    (\"Kingfisher Storm\",    \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80\"),
    (\"Bira 91 Light\",       \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1600788907416-456578634209?w=600&q=80\"),
    (\"Hoegaarden Rosée\",    \"wheat\",    \"Belgium\",      \"https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=600&q=80\"),
    (\"Erdinger Dunkel\",     \"wheat\",    \"Germany\",      \"https://images.unsplash.com/photo-1618183479302-1e0aa382c36b?w=600&q=80\"),
    (\"Krombacher Pilsner\",  \"pilsner\",  \"Germany\",      \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"Singha Premium\",      \"lager\",    \"Thailand\",     \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80\"),
    (\"Chang Classic\",       \"lager\",    \"Thailand\",     \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=600&q=80\"),
    (\"San Miguel Light\",    \"lager\",    \"Philippines\",  \"https://images.unsplash.com/photo-1608270586620-248524c67de9?w=600&q=80\"),
    (\"Tsingtao Original\",   \"lager\",    \"China\",        \"https://images.unsplash.com/photo-1566633806327-68e152aaf26d?w=600&q=80\"),
    (\"Cobra Premium\",       \"lager\",    \"India\",        \"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600&q=80\"),
    (\"Simba Stout Imperial\",\"stout\",    \"India\",        \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"Bira 91 Strong\",      \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=600&q=80\"),
    (\"Heineken Silver\",     \"lager\",    \"Netherlands\",  \"https://images.unsplash.com/photo-1577897267749-50b5d5a3f8a3?w=600&q=80\"),
    (\"Carlsberg Elephant\",  \"strong\",   \"Denmark\",      \"https://images.unsplash.com/photo-1546158243-2d3f86317c80?w=600&q=80\"),
    (\"Tuborg Strong\",       \"strong\",   \"Denmark\",      \"https://images.unsplash.com/photo-1626078297693-c47b67f7b95e?w=600&q=80\"),
    (\"Budweiser Magnum\",    \"strong\",   \"USA\",          \"https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=600&q=80\"),
    (\"Asahi Black\",         \"stout\",    \"Japan\",        \"https://images.unsplash.com/photo-1600788907416-456578634209?w=600&q=80\"),
    (\"Hoegaarden Citrus\",   \"wheat\",    \"Belgium\",      \"https://images.unsplash.com/photo-1607344645866-009c320b63e0?w=600&q=80\"),
    (\"Kingfisher Buzz\",     \"strong\",   \"India\",        \"https://images.unsplash.com/photo-1618183479302-1e0aa382c36b?w=600&q=80\"),
    (\"Bira 91 Hill Station\",\"craft\",    \"India\",        \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=600&q=80\"),
    (\"Doolally Apple Cider\",\"craft\",    \"India\",        \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=600&q=80\"),
    (\"Simba Trippy Hippy\",  \"ipa\",      \"India\",        \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=600&q=80\"),
]

DESCRIPTIONS = [
    \"Crisp, refreshing taste with a balanced malt body and clean finish.\",
    \"Smooth, easy-drinking lager with subtle hop notes and citrus zest.\",
    \"Bold and robust flavor with caramel undertones and a creamy head.\",
    \"A premium brew crafted with imported hops for an unmistakable character.\",
    \"Light, golden and effortlessly smooth — perfect for any occasion.\",
    \"Rich, full-bodied with hints of roasted barley and dark chocolate.\",
    \"Bright, hoppy and aromatic with floral and tropical fruit notes.\",
    \"Refreshing wheat beer with banana, clove and a hazy, silky body.\",
    \"Strong and assertive with deep amber color and lasting warmth.\",
    \"Award-winning craft brew with complex layers and artisanal finesse.\",
]

FAQS = [
    (\"Do you deliver beer to my location?\", \"Yes, we offer same-day home delivery within a 12 km radius. Orders above ₹999 ship free. We also offer scheduled deliveries up to 7 days in advance.\"),
    (\"What are your store hours?\", \"We are open Monday to Sunday from 10:30 AM to 11:00 PM. On dry days and public restrictions, delivery may be paused as per local regulations.\"),
    (\"Do you stock imported & craft beers?\", \"Absolutely. We carry 150+ imported labels from 14 countries plus 90+ Indian craft beers across IPA, wheat, lager, stout and pilsner.\"),
    (\"Is identity verification required?\", \"Yes. Customers must be 21+ (or as per state law) and present a valid government-issued ID at purchase or delivery. No ID, no service.\"),
    (\"Do you sell chilled beer?\", \"Every fridge in the store is set between 2-4°C. You can choose chilled, room-temp or party-pack pre-chilled crates at checkout.\"),
    (\"Can I bulk-order for parties or weddings?\", \"Yes — we specialise in party catering. Get up to 18% off on orders of 10+ crates. Call our events team to plan your bash.\"),
    (\"What payment methods are accepted?\", \"We accept UPI, all major credit/debit cards, net banking, paper currency and cash on delivery.\"),
    (\"Do you offer a loyalty program?\", \"Yes — every ₹100 spent earns you 5 Daaru Points. Redeem for discounts, free merch, or exclusive limited-batch beers.\"),
    (\"Can I return or exchange a bottle?\", \"Sealed, unopened bottles can be exchanged within 24 hours of delivery in case of a manufacturing defect. We unfortunately cannot accept opened bottles.\"),
    (\"Are non-alcoholic beers available?\", \"Yes — we proudly stock 12+ non-alcoholic and 0.0% labels including Heineken 0.0, Erdinger Alkoholfrei and Coolberg.\"),
]

REVIEWS = [
    (\"Rohit Sharma\",    \"Daily customer\", \"Best collection of imported beers in the entire city. The staff knows their brews and the chilled bottles never disappoint. Cheers, Taau!\"),
    (\"Priya Mehra\",     \"Event planner\",  \"Booked three weddings through them last year. Pricing, variety and on-time delivery were absolutely top notch. Will use again.\"),
    (\"Amit Singh\",      \"Craft enthusiast\",\"Their craft section is unreal. Found three labels I couldn't get anywhere else in town. Taau actually recommends pairings — that's love.\"),
    (\"Karan Kapoor\",    \"Bartender\",      \"I order all my home stock from here. Crates always sealed, prices fair, delivery faster than pizza. 10/10.\"),
    (\"Sneha Iyer\",      \"Regular\",        \"Absolutely premium experience. Glass-front fridges, polite staff, clean shop. Feels more like a wine boutique than a beer shop.\"),
    (\"Aditya Verma\",    \"Beer Blogger\",   \"I review beer shops for a living. Taau Daaru Baaz is one of the cleanest, best-curated outlets I've visited in North India.\"),
    (\"Neha Gupta\",      \"Foodie\",         \"Their pairing suggestions changed how I host. Now my dinner parties have a proper beer menu.\"),
    (\"Vikram Rathod\",   \"Corporate buyer\",\"We source quarterly stock for our office lounge. Invoices, GST, bulk pricing — all sorted in one call. Reliable.\"),
    (\"Ishita Bhatt\",    \"First-timer\",    \"I knew nothing about beer. They walked me through styles, ABVs and gave me a small tasting flight to try. Customer for life.\"),
]

GALLERY = [
    \"https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=900&q=80\",
    \"https://images.unsplash.com/photo-1535958636474-b021ee887b13?w=900&q=80\",
    \"https://images.unsplash.com/photo-1571767454098-246b94fbcf70?w=900&q=80\",
    \"https://images.unsplash.com/photo-1608270586620-248524c67de9?w=900&q=80\",
    \"https://images.unsplash.com/photo-1566633806327-68e152aaf26d?w=900&q=80\",
    \"https://images.unsplash.com/photo-1571613316887-6f8d5cbf7ef7?w=900&q=80\",
    \"https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=900&q=80\",
    \"https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=900&q=80\",
    \"https://images.unsplash.com/photo-1577897267749-50b5d5a3f8a3?w=900&q=80\",
    \"https://images.unsplash.com/photo-1546158243-2d3f86317c80?w=900&q=80\",
    \"https://images.unsplash.com/photo-1626078297693-c47b67f7b95e?w=900&q=80\",
    \"https://images.unsplash.com/photo-1623091410901-00e2d268901f?w=900&q=80\",
]

# ---------------------- TEMPLATES ----------------------

def build_product_card(i, name, cat, origin, img):
    price_now = 120 + (i * 17) % 580 + 60
    price_old = price_now + 40 + (i * 7) % 80
    rating = round(3.8 + ((i * 13) % 13) / 10, 1)
    if rating > 5.0: rating = 5.0
    reviews_count = 24 + (i * 11) % 400
    desc = DESCRIPTIONS[i % len(DESCRIPTIONS)]
    badges = []
    if i % 6 == 0: badges.append('<span class=\"badge badge--new\">NEW</span>')
    if i % 7 == 0: badges.append('<span class=\"badge badge--hot\">HOT</span>')
    if i % 5 == 0: badges.append('<span class=\"badge badge--featured\">FEATURED</span>')
    disc_pct = int(((price_old - price_now) / price_old) * 100)
    if disc_pct > 0: badges.append(f'<span class=\"badge badge--discount\">-{disc_pct}%</span>')
    badges_html = '\n        '.join(badges)
    stars = ''.join(['<i class=\"fa-solid fa-star\"></i>' for _ in range(int(rating))])
    if rating - int(rating) >= 0.4: stars += '<i class=\"fa-solid fa-star-half-stroke\"></i>'

    return f'''
  <article class=\"product reveal\" data-name=\"{name.lower()}\" data-category=\"{cat}\"
           data-price=\"₹{price_now}\" data-desc=\"{desc} Origin: {origin}.\">
    <div class=\"product-media\">
      <div class=\"product-badges\">
        {badges_html}
      </div>
      <button class=\"product-fav\" aria-label=\"Add to favorites\" data-testid=\"fav-btn-{i}\">
        <i class=\"fa-regular fa-heart\"></i>
      </button>
      <img loading=\"lazy\" src=\"{img}\" alt=\"{name} — {origin}\">
      <div class=\"product-quick\">
        <button data-quick-view data-testid=\"quick-view-{i}\"><i class=\"fa-regular fa-eye\"></i> Quick View</button>
        <button data-add-cart data-testid=\"add-cart-{i}\"><i class=\"fa-solid fa-cart-plus\"></i> Add</button>
      </div>
    </div>
    <div class=\"product-body\">
      <div class=\"product-category\">{cat.replace('ipa','IPA').title()} • {origin}</div>
      <h3 class=\"product-name\">{name}</h3>
      <p class=\"product-desc\">{desc}</p>
      <div class=\"product-meta\">
        <div class=\"product-price\">
          <span class=\"now\">₹{price_now}</span>
          <span class=\"was\">₹{price_old}</span>
        </div>
        <div class=\"product-rating\">
          {stars}
          <span class=\"count\">({reviews_count})</span>
        </div>
      </div>
    </div>
  </article>
'''


def build_brands():
    parts = []
    for i, (name, origin, letter) in enumerate(BRANDS):
        parts.append(f'''
  <div class=\"brand-card reveal\">
    <div class=\"brand-logo\">{letter}</div>
    <div class=\"brand-name-c\">{name}</div>
    <div class=\"brand-origin\">{origin}</div>
  </div>''')
    return '\n'.join(parts)


def build_categories():
    parts = []
    for i, (name, icon, count) in enumerate(CATEGORIES):
        parts.append(f'''
  <a href=\"#beers\" class=\"cat-card reveal\">
    <div class=\"cat-icon\"><i class=\"fa-solid {icon}\"></i></div>
    <div>
      <div class=\"cat-name\">{name}</div>
      <div class=\"cat-count\">{count} products</div>
    </div>
    <div class=\"cat-arrow\"><i class=\"fa-solid fa-arrow-right\"></i></div>
  </a>''')
    return '\n'.join(parts)


def build_reviews():
    parts = []
    for i, (name, role, text) in enumerate(REVIEWS):
        initial = name[0].upper()
        parts.append(f'''
  <article class=\"testi-card\">
    <div class=\"testi-stars\">
      <i class=\"fa-solid fa-star\"></i><i class=\"fa-solid fa-star\"></i>
      <i class=\"fa-solid fa-star\"></i><i class=\"fa-solid fa-star\"></i>
      <i class=\"fa-solid fa-star\"></i>
    </div>
    <p class=\"testi-text\">\"{text}\"</p>
    <div class=\"testi-author\">
      <div class=\"testi-avatar\">{initial}</div>
      <div>
        <div class=\"testi-name\">{name}</div>
        <div class=\"testi-role\">{role}</div>
      </div>
    </div>
  </article>''')
    return '\n'.join(parts)


def build_faqs():
    parts = []
    for i, (q, a) in enumerate(FAQS):
        parts.append(f'''
  <div class=\"faq-item reveal\">
    <button class=\"faq-q\" aria-expanded=\"false\">
      <span>{q}</span>
      <span class=\"ic\"><i class=\"fa-solid fa-plus\"></i></span>
    </button>
    <div class=\"faq-a\"><p>{a}</p></div>
  </div>''')
    return '\n'.join(parts)


def build_gallery():
    classes = [\"g-wide\", \"\", \"\", \"g-tall\", \"\", \"\", \"g-wide\", \"\", \"\", \"\", \"\", \"g-tall\"]
    labels = [\"Tap Room\", \"Imported Shelf\", \"Craft Corner\", \"Premium Lounge\",
              \"Glass-Front Fridges\", \"VIP Tasting\", \"Party Crates\", \"Beer Sommelier\",
              \"Walk-In Cellar\", \"Signature Mugs\", \"Private Tastings\", \"Late-Night Counter\"]
    parts = []
    for i, img in enumerate(GALLERY):
        cls = classes[i] if i < len(classes) else \"\"
        lbl = labels[i] if i < len(labels) else \"Gallery\"
        parts.append(f'''
  <div class=\"g-item {cls} reveal\">
    <img loading=\"lazy\" src=\"{img}\" alt=\"{lbl}\">
    <div class=\"g-label\">{lbl}</div>
  </div>''')
    return '\n'.join(parts)


# Build product grid
def build_products():
    cards = []
    for i, (name, cat, origin, img) in enumerate(PRODUCT_NAMES):
        cards.append(build_product_card(i, name, cat, origin, img))
    return '\n'.join(cards)


# Featured (first 8) & New Arrivals (last 8)
def build_featured():
    cards = []
    for i, (name, cat, origin, img) in enumerate(PRODUCT_NAMES[:8]):
        cards.append(build_product_card(i, name, cat, origin, img))
    return '\n'.join(cards)


def build_new_arrivals():
    cards = []
    for j, item in enumerate(PRODUCT_NAMES[-8:]):
        i = len(PRODUCT_NAMES) - 8 + j
        cards.append(build_product_card(i, *item))
    return '\n'.join(cards)


def build_premium():
    # Premium = strong + craft + imported feel
    items = [p for p in PRODUCT_NAMES if p[1] in ('craft', 'strong', 'stout', 'ipa')][:8]
    cards = []
    for j, item in enumerate(items):
        cards.append(build_product_card(100 + j, *item))
    return '\n'.join(cards)


# ----------------------- HTML ASSEMBLY ----------------------

HTML_HEAD = '''<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, viewport-fit=cover\">
  <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
  <title>Taau Daaru Baaz Beer Shop — Premium Beers, Craft Brews & Imported Labels</title>
  <meta name=\"description\" content=\"Taau Daaru Baaz Beer Shop — North India's largest curated beer destination. 500+ premium, imported and craft beers with same-day delivery, expert pairing and party catering.\">
  <meta name=\"keywords\" content=\"beer shop, premium beer, imported beer, craft beer, IPA, lager, stout, wheat beer, beer delivery, Taau Daaru Baaz\">
  <meta name=\"author\" content=\"Taau Daaru Baaz Beer Shop\">
  <meta name=\"theme-color\" content=\"#0a0c11\">
  <meta property=\"og:title\" content=\"Taau Daaru Baaz Beer Shop — Premium Beers & Craft Brews\">
  <meta property=\"og:description\" content=\"500+ premium, imported and craft beers. Same-day delivery & party catering.\">
  <meta property=\"og:type\" content=\"website\">
  <meta property=\"og:image\" content=\"https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=1200&q=80\">
  <link rel=\"icon\" type=\"image/svg+xml\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23E5A93C'/%3E%3Ctext x='32' y='44' text-anchor='middle' font-family='Georgia' font-size='34' font-weight='bold' fill='%231a1206'%3ET%3C/text%3E%3C/svg%3E\">
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
  <link href=\"https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,700&family=Manrope:wght@300;400;500;600;700;800&family=Azeret+Mono:wght@400;500;600&display=swap\" rel=\"stylesheet\">
  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css\">
  <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>

<!-- ============================== LOADER ============================== -->
<div class=\"loader\" aria-hidden=\"true\">
  <div class=\"loader-mug\">
    <div class=\"loader-fill\"></div>
    <div class=\"loader-foam\"></div>
    <div class=\"loader-label\">TAAU DAARU BAAZ</div>
  </div>
</div>

<!-- ============================== AGE GATE ============================== -->
<div class=\"age-gate\" role=\"dialog\" aria-modal=\"true\" aria-label=\"Age verification\">
  <div class=\"age-box\">
    <div class=\"brand-mark\" style=\"margin:0 auto 14px;\">T</div>
    <h3>Are you of <span class=\"accent\">legal drinking age?</span></h3>
    <p>This website contains products intended for adults of legal drinking age. By entering, you confirm you are 21+ (or as per local law).</p>
    <div class=\"age-buttons\">
      <button class=\"btn btn--primary\" data-age-yes data-testid=\"age-yes-btn\">Yes, I am 21+</button>
      <button class=\"btn btn--ghost\" data-age-no data-testid=\"age-no-btn\">Not yet</button>
    </div>
  </div>
</div>

<!-- ============================== HEADER ============================== -->
<header class=\"header\" role=\"banner\">
  <div class=\"container\">
    <nav class=\"nav\" aria-label=\"Primary\">
      <a href=\"#top\" class=\"brand\" aria-label=\"Home\">
        <div class=\"brand-mark\">T</div>
        <div class=\"brand-text\">
          <div class=\"brand-name\">Taau Daaru Baaz</div>
          <div class=\"brand-tag\">Premium Beer Co.</div>
        </div>
      </a>
      <ul class=\"nav-links\">
        <li><a href=\"#home\" data-testid=\"nav-home\">Home</a></li>
        <li><a href=\"#about\" data-testid=\"nav-about\">About</a></li>
        <li><a href=\"#beers\" data-testid=\"nav-beers\">Beers</a></li>
        <li><a href=\"#brands\" data-testid=\"nav-brands\">Brands</a></li>
        <li><a href=\"#offers\" data-testid=\"nav-offers\">Offers</a></li>
        <li><a href=\"#gallery\" data-testid=\"nav-gallery\">Gallery</a></li>
        <li><a href=\"#contact\" data-testid=\"nav-contact\">Contact</a></li>
      </ul>
      <div class=\"nav-cta\">
        <button class=\"icon-btn\" aria-label=\"Search\" data-testid=\"header-search-btn\"><i class=\"fa-solid fa-magnifying-glass\"></i></button>
        <button class=\"icon-btn\" aria-label=\"Cart\" data-testid=\"header-cart-btn\" style=\"position:relative;\">
          <i class=\"fa-solid fa-bag-shopping\"></i>
          <span data-cart-count style=\"position:absolute;top:-6px;right:-6px;background:var(--gold-400);color:#1a1206;font-size:10px;font-weight:700;border-radius:999px;min-width:18px;height:18px;display:grid;place-items:center;padding:0 5px;\">0</span>
        </button>
        <button class=\"hamburger\" aria-label=\"Open menu\" data-testid=\"hamburger-btn\"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>

<!-- ============================== MOBILE MENU ============================== -->
<nav class=\"mobile-menu\" aria-label=\"Mobile\">
  <a href=\"#home\">Home</a>
  <a href=\"#about\">About</a>
  <a href=\"#beers\">Beers</a>
  <a href=\"#brands\">Brands</a>
  <a href=\"#offers\">Offers</a>
  <a href=\"#categories\">Categories</a>
  <a href=\"#reviews\">Reviews</a>
  <a href=\"#gallery\">Gallery</a>
  <a href=\"#faq\">FAQ</a>
  <a href=\"#contact\">Contact</a>
</nav>
'''

HERO = '''
<!-- ============================== HERO ============================== -->
<section class=\"hero\" id=\"home\">
  <span class=\"hero-orb hero-orb--1\"></span>
  <span class=\"hero-orb hero-orb--2\"></span>
  <div class=\"container\">
    <div class=\"hero-grid\">
      <div class=\"reveal-left\">
        <div class=\"hero-tag\"><span class=\"dot\"></span> North India's Premium Beer Destination</div>
        <h1 class=\"hero-title\">
          Brewed for the <span class=\"accent\">connoisseur</span>,<br>
          poured for the <span class=\"accent\">legend</span>.
        </h1>
        <p class=\"hero-sub\">Discover 500+ hand-curated beers from 14 countries — chilled to perfection, delivered to your door, served with stories the Taau himself would approve of.</p>
        <div class=\"hero-cta\">
          <a href=\"#beers\" class=\"btn btn--primary\" data-testid=\"hero-shop-btn\">Explore Collection <i class=\"fa-solid fa-arrow-right\"></i></a>
          <a href=\"#about\" class=\"btn btn--ghost\" data-testid=\"hero-story-btn\">Our Story <i class=\"fa-solid fa-circle-play\"></i></a>
        </div>
        <div class=\"hero-stats\">
          <div class=\"stat\">
            <div class=\"stat-num\"><span data-counter=\"500\" data-duration=\"2200\">0</span><span class=\"plus\">+</span></div>
            <div class=\"stat-label\">Beer Labels</div>
          </div>
          <div class=\"stat\">
            <div class=\"stat-num\"><span data-counter=\"14\" data-duration=\"1800\">0</span><span class=\"plus\">+</span></div>
            <div class=\"stat-label\">Countries</div>
          </div>
          <div class=\"stat\">
            <div class=\"stat-num\"><span data-counter=\"25000\" data-duration=\"2600\">0</span><span class=\"plus\">+</span></div>
            <div class=\"stat-label\">Happy Patrons</div>
          </div>
          <div class=\"stat\">
            <div class=\"stat-num\"><span data-counter=\"12\" data-duration=\"1700\">0</span><span class=\"plus\">+</span></div>
            <div class=\"stat-label\">Years of Trust</div>
          </div>
        </div>
      </div>
      <div class=\"hero-art reveal-right\">
        <div class=\"hero-floating hero-floating--1\">
          <div class=\"hf-icon\"><i class=\"fa-solid fa-truck-fast\"></i></div>
          <div class=\"hf-text\"><strong>30-min delivery</strong><span>Within city</span></div>
        </div>
        <div class=\"hero-floating hero-floating--2\">
          <div class=\"hf-icon\"><i class=\"fa-solid fa-snowflake\"></i></div>
          <div class=\"hf-text\"><strong>Always chilled</strong><span>Fresh stock daily</span></div>
        </div>
        <div class=\"hero-floating hero-floating--3\">
          <div class=\"hf-icon\"><i class=\"fa-solid fa-medal\"></i></div>
          <div class=\"hf-text\"><strong>100% original</strong><span>Authenticity guaranteed</span></div>
        </div>
        <div class=\"hero-bottle\">
          <div class=\"bottle-label\">
            <div class=\"crest\">T</div>
            <div class=\"name\">TAAU</div>
            <div class=\"sub\">DAARU BAAZ</div>
            <div class=\"est\">EST. 2013</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============================== MARQUEE ============================== -->
<div class=\"marquee\" aria-hidden=\"true\">
  <div class=\"marquee-track\">
    <span>Cold &amp; Crafted <span class=\"dot\">●</span> Hand-Curated <span class=\"dot\">●</span> Delivered Fast <span class=\"dot\">●</span> Aged to Please <span class=\"dot\">●</span> 500+ Labels <span class=\"dot\">●</span> 14 Countries <span class=\"dot\">●</span></span>
    <span>Cold &amp; Crafted <span class=\"dot\">●</span> Hand-Curated <span class=\"dot\">●</span> Delivered Fast <span class=\"dot\">●</span> Aged to Please <span class=\"dot\">●</span> 500+ Labels <span class=\"dot\">●</span> 14 Countries <span class=\"dot\">●</span></span>
  </div>
</div>
'''

ABOUT = '''
<!-- ============================== ABOUT ============================== -->
<section class=\"section\" id=\"about\">
  <div class=\"container\">
    <div class=\"about-grid\">
      <div class=\"about-media reveal-left\">
        <img src=\"https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=900&q=80\" alt=\"Premium beer shop interior\">
        <div class=\"about-badge\">
          <div class=\"num\">12+</div>
          <div class=\"lbl\">Years brewing <br>relationships</div>
        </div>
      </div>
      <div class=\"reveal-right\">
        <div class=\"eyebrow\">Our Story</div>
        <h2 class=\"section-title\" style=\"text-align:left;\">A neighborhood <span class=\"accent\">institution</span><br>turned beer cathedral.</h2>
        <p style=\"color:var(--text-2); margin-bottom:18px;\">It started in 2013 when Taau, a third-generation merchant with a stubborn love for proper beer, refused to stock the same six brands every other shop carried. He flew to Munich for one weekend and came back with 40 cases of lager nobody in town had tasted.</p>
        <p style=\"color:var(--text-2); margin-bottom:18px;\">Twelve years later, that one weekend has grown into North India's most respected beer destination — 500+ labels across 14 countries, a temperature-controlled cellar, a private tasting room, and a team that can pair a beer to your biryani better than your mother-in-law can argue.</p>
        <p style=\"color:var(--text-2);\">We're not just a shop. We are a culture. A pilgrimage. A second home for anyone who believes good beer deserves better treatment.</p>
        <div class=\"about-features\">
          <div class=\"about-feature\">
            <i class=\"fa-solid fa-temperature-low\"></i>
            <h4>Cold-Chain Imported</h4>
            <p>Every imported bottle moves through certified cold storage, never above 8°C.</p>
          </div>
          <div class=\"about-feature\">
            <i class=\"fa-solid fa-hand-holding-heart\"></i>
            <h4>Hand-Picked Inventory</h4>
            <p>Each label is personally tasted and approved before it earns shelf space.</p>
          </div>
          <div class=\"about-feature\">
            <i class=\"fa-solid fa-shield-halved\"></i>
            <h4>100% Authentic</h4>
            <p>Direct importer relationships. No grey market, no compromise.</p>
          </div>
          <div class=\"about-feature\">
            <i class=\"fa-solid fa-people-group\"></i>
            <h4>Expert Sommeliers</h4>
            <p>Two certified Cicerones on staff to help you pair, plan and discover.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

FOOTER = '''
<!-- ============================== FOOTER ============================== -->
<footer class=\"footer\" id=\"footer\">
  <div class=\"container\">
    <div class=\"footer-grid\">
      <div class=\"footer-brand\">
        <a href=\"#top\" class=\"brand\">
          <div class=\"brand-mark\">T</div>
          <div class=\"brand-text\">
            <div class=\"brand-name\">Taau Daaru Baaz</div>
            <div class=\"brand-tag\">Premium Beer Co.</div>
          </div>
        </a>
        <p>North India's most-loved beer destination. 500+ curated labels, certified cold-chain storage, and a Taau-approved welcome for every patron.</p>
        <div class=\"contact-socials\">
          <a href=\"#\" aria-label=\"Instagram\"><i class=\"fa-brands fa-instagram\"></i></a>
          <a href=\"#\" aria-label=\"Facebook\"><i class=\"fa-brands fa-facebook-f\"></i></a>
          <a href=\"#\" aria-label=\"X / Twitter\"><i class=\"fa-brands fa-x-twitter\"></i></a>
          <a href=\"#\" aria-label=\"YouTube\"><i class=\"fa-brands fa-youtube\"></i></a>
          <a href=\"#\" aria-label=\"WhatsApp\"><i class=\"fa-brands fa-whatsapp\"></i></a>
        </div>
      </div>
      <div>
        <h5>Quick Links</h5>
        <ul>
          <li><a href=\"#home\">Home</a></li>
          <li><a href=\"#about\">About Us</a></li>
          <li><a href=\"#beers\">All Beers</a></li>
          <li><a href=\"#brands\">Brands</a></li>
          <li><a href=\"#offers\">Offers</a></li>
          <li><a href=\"#contact\">Contact</a></li>
        </ul>
      </div>
      <div>
        <h5>Help</h5>
        <ul>
          <li><a href=\"#faq\">FAQ</a></li>
          <li><a href=\"#contact\">Delivery Info</a></li>
          <li><a href=\"#contact\">Return Policy</a></li>
          <li><a href=\"#contact\">Bulk Orders</a></li>
          <li><a href=\"#contact\">Privacy Policy</a></li>
          <li><a href=\"#contact\">Terms of Service</a></li>
        </ul>
      </div>
      <div>
        <h5>Opening Hours</h5>
        <ul class=\"footer-hours\">
          <li>Monday <span>10:30 — 23:00</span></li>
          <li>Tuesday <span>10:30 — 23:00</span></li>
          <li>Wednesday <span>10:30 — 23:00</span></li>
          <li>Thursday <span>10:30 — 23:00</span></li>
          <li>Friday <span>10:30 — 23:30</span></li>
          <li>Saturday <span>10:30 — 23:30</span></li>
          <li>Sunday <span>11:00 — 22:30</span></li>
        </ul>
      </div>
    </div>
    <div class=\"footer-bottom\">
      <div>© <span data-year>2025</span> Taau Daaru Baaz Beer Shop. All rights reserved. Drink responsibly.</div>
      <div class=\"pay\">
        <span>VISA</span><span>MASTERCARD</span><span>UPI</span><span>PAYTM</span><span>COD</span>
      </div>
    </div>
  </div>
</footer>

<!-- ============================== SCROLL TOP ============================== -->
<button class=\"scroll-top\" aria-label=\"Scroll to top\" data-testid=\"scroll-top-btn\">
  <i class=\"fa-solid fa-arrow-up\"></i>
</button>

<!-- ============================== QUICK VIEW MODAL ============================== -->
<div class=\"modal\" id=\"productModal\" role=\"dialog\" aria-modal=\"true\">
  <button class=\"modal-close\" aria-label=\"Close\" data-testid=\"modal-close\"><i class=\"fa-solid fa-xmark\"></i></button>
  <div class=\"modal-box\">
    <div class=\"modal-img\">
      <img src=\"\" alt=\"Product preview\">
    </div>
    <div class=\"modal-body\">
      <div class=\"product-category\" data-mt-cat></div>
      <h3 class=\"product-name\" data-mt-name style=\"font-size:1.6rem;margin-bottom:10px;\"></h3>
      <div class=\"product-rating\" style=\"margin-bottom:14px;\">
        <i class=\"fa-solid fa-star\"></i><i class=\"fa-solid fa-star\"></i><i class=\"fa-solid fa-star\"></i>
        <i class=\"fa-solid fa-star\"></i><i class=\"fa-solid fa-star-half-stroke\"></i>
        <span class=\"count\">(248 reviews)</span>
      </div>
      <p class=\"product-desc\" data-mt-desc style=\"font-size:.95rem; margin-bottom:24px;\"></p>
      <div style=\"display:flex; align-items:center; justify-content:space-between; margin-bottom:24px;\">
        <div class=\"product-price\">
          <span class=\"now\" data-mt-price>₹0</span>
        </div>
        <div class=\"product-rating\"><i class=\"fa-solid fa-truck-fast\"></i><span style=\"color:var(--text-2);font-size:.85rem;\">Free delivery</span></div>
      </div>
      <div style=\"display:flex; gap:10px;\">
        <button class=\"btn btn--primary\" style=\"flex:1;\" data-testid=\"modal-add-cart\"><i class=\"fa-solid fa-cart-plus\"></i> Add to Cart</button>
        <button class=\"btn btn--outline\" data-testid=\"modal-buy-now\"><i class=\"fa-solid fa-bolt\"></i> Buy Now</button>
      </div>
    </div>
  </div>
</div>

<script src=\"script.js\"></script>
</body>
</html>
'''


def section_wrap(id_, eyebrow, title_main, title_accent, sub, body, extra_class=\"\"):
    return f'''
<!-- ============================== {id_.upper()} ============================== -->
<section class=\"section {extra_class}\" id=\"{id_}\">
  <div class=\"container\">
    <div class=\"section-head reveal\">
      <div class=\"eyebrow\">{eyebrow}</div>
      <h2 class=\"section-title\">{title_main} <span class=\"accent\">{title_accent}</span></h2>
      <p class=\"section-sub\">{sub}</p>
    </div>
    {body}
  </div>
</section>
'''


def main():
    featured_body = f'<div class=\"product-grid\">{build_featured()}</div>'
    featured = section_wrap(\"featured\", \"Hand-Picked\", \"Featured\", \"Beers\",
                            \"The Taau's personal selection — a rotating shelf of the best beers we're pouring this season.\",
                            featured_body)

    premium_body = f'<div class=\"product-grid\">{build_premium()}</div>'
    premium = section_wrap(\"premium\", \"Top Shelf\", \"Premium\", \"Collection\",
                           \"Limited-batch, imported and craft favorites for collectors and connoisseurs.\",
                           premium_body)

    brands_body = f'<div class=\"brand-grid reveal-stagger\">{build_brands()}</div>'
    brands = section_wrap(\"brands\", \"World-Class Labels\", \"Popular\", \"Brands\",
                          \"From the snowy highlands of Bavaria to the deserts of Sonora — every brewery worth knowing, in one place.\",
                          brands_body)

    new_body = f'<div class=\"product-grid\">{build_new_arrivals()}</div>'
    new_arr = section_wrap(\"new\", \"Fresh Off The Truck\", \"New\", \"Arrivals\",
                           \"The latest additions to our cellar — first to taste, first to tell.\",
                           new_body)

    offers_body = '''
<div class=\"offer-strip\">
  <div class=\"offer-card offer-card--lg reveal-left\">
    <span class=\"offer-deco\"></span>
    <div>
      <div class=\"eyebrow\" style=\"margin-bottom:14px;\">Festive Offer</div>
      <h3>Flat <span class=\"accent\">30% off</span><br>on a curated party crate.</h3>
      <p>Mix &amp; match any 24 imported bottles. Free home delivery, glassware and a Taau-signed note.</p>
      <div class=\"code\">CODE: TAAU30</div>
    </div>
    <a href=\"#beers\" class=\"btn btn--primary\" style=\"align-self:flex-start;\">Claim Offer <i class=\"fa-solid fa-arrow-right\"></i></a>
  </div>
  <div class=\"offer-card offer-card--sm reveal-right\">
    <div>
      <div class=\"eyebrow\" style=\"margin-bottom:14px;\">Weekday Special</div>
      <h3>Buy 5<br>Get 1 <span class=\"accent\">free.</span></h3>
      <p>On every craft &amp; IPA Mon-Thu. Auto-applied at checkout.</p>
    </div>
    <a href=\"#beers\" class=\"btn btn--outline\" style=\"align-self:flex-start;\">Shop Craft <i class=\"fa-solid fa-arrow-right\"></i></a>
  </div>
</div>
'''
    offers = section_wrap(\"offers\", \"Limited Time\", \"Special\", \"Offers\",
                          \"Save more on your favorites. Limited stock, unlimited flavor.\",
                          offers_body)

    cats_body = f'<div class=\"cat-grid reveal-stagger\">{build_categories()}</div>'
    cats = section_wrap(\"categories\", \"Browse By Style\", \"Beer\", \"Categories\",
                        \"Lagers, ales, stouts, wheats, ciders and everything in between — find your style.\",
                        cats_body)

    all_beers_body = f'''
<div class=\"filter-bar reveal\">
  <div class=\"filter-chips\">
    <button class=\"chip is-active\" data-filter=\"all\" data-testid=\"chip-all\">All</button>
    <button class=\"chip\" data-filter=\"lager\" data-testid=\"chip-lager\">Lager</button>
    <button class=\"chip\" data-filter=\"wheat\" data-testid=\"chip-wheat\">Wheat</button>
    <button class=\"chip\" data-filter=\"ipa\" data-testid=\"chip-ipa\">IPA</button>
    <button class=\"chip\" data-filter=\"stout\" data-testid=\"chip-stout\">Stout</button>
    <button class=\"chip\" data-filter=\"pilsner\" data-testid=\"chip-pilsner\">Pilsner</button>
    <button class=\"chip\" data-filter=\"craft\" data-testid=\"chip-craft\">Craft</button>
    <button class=\"chip\" data-filter=\"strong\" data-testid=\"chip-strong\">Strong</button>
  </div>
  <div class=\"search-box\">
    <i class=\"fa-solid fa-magnifying-glass\"></i>
    <input id=\"productSearch\" type=\"search\" placeholder=\"Search any beer or brand...\" data-testid=\"product-search-input\" aria-label=\"Search products\">
  </div>
</div>
<div id=\"productGrid\" class=\"product-grid\">
{build_products()}
</div>
<div id=\"productEmpty\" style=\"display:none; text-align:center; padding:80px 24px; color:var(--text-3);\">
  <i class=\"fa-solid fa-mug-empty\" style=\"font-size:3rem; color:var(--gold-500); margin-bottom:14px;\"></i>
  <h3 style=\"color:var(--text-1); font-family:var(--font-display); font-size:1.5rem; margin-bottom:6px;\">No beers match your search</h3>
  <p>Try a different name, brand or category.</p>
</div>
'''
    all_beers = section_wrap(\"beers\", \"Full Catalog\", \"Browse Our\", \"Beers\",
                             \"Search, filter and discover from over 60 in-stock labels — chilled and ready.\",
                             all_beers_body)

    reviews_body = f'''
<div class=\"testi-wrap reveal\">
  <div class=\"testi-track\">
    {build_reviews()}
  </div>
  <div class=\"testi-controls\"></div>
</div>
'''
    reviews = section_wrap(\"reviews\", \"Word On The Street\", \"What Our\", \"Patrons Say\",
                           \"Twelve years, twenty-five thousand happy customers and one Taau who reads every review.\",
                           reviews_body)

    gallery_body = f'<div class=\"gallery-grid\">{build_gallery()}</div>'
    gallery = section_wrap(\"gallery\", \"Inside The Shop\", \"Our\", \"Gallery\",
                           \"A peek inside the temple of cold ones.\",
                           gallery_body)

    faq_body = f'<div class=\"faq-list\">{build_faqs()}</div>'
    faq = section_wrap(\"faq\", \"We Got Answers\", \"Frequently Asked\", \"Questions\",
                       \"Everything you wanted to ask the Taau but were too thirsty to remember.\",
                       faq_body)

    contact_body = '''
<div class=\"contact-grid\">
  <div class=\"contact-info reveal-left\">
    <h3>Drop by, dial in, or drop a line.</h3>
    <p>Whether you need a party crate, a pairing recommendation, or just want to chat about a Belgian Tripel — Taau is here.</p>
    <div class=\"contact-list\">
      <div class=\"contact-item\">
        <i class=\"fa-solid fa-location-dot\"></i>
        <div>
          <h4>Visit Our Store</h4>
          <p>Shop No. 12, Main Market, Sector 14<br>Gurugram, Haryana 122001, India</p>
        </div>
      </div>
      <div class=\"contact-item\">
        <i class=\"fa-solid fa-phone\"></i>
        <div>
          <h4>Call / WhatsApp</h4>
          <p><a href=\"tel:+919876543210\">+91 98765 43210</a> &nbsp;•&nbsp; <a href=\"tel:+911244567890\">0124 456 7890</a></p>
        </div>
      </div>
      <div class=\"contact-item\">
        <i class=\"fa-solid fa-envelope\"></i>
        <div>
          <h4>Email Us</h4>
          <p><a href=\"mailto:hello@taaudaarubaaz.com\">hello@taaudaarubaaz.com</a><br><a href=\"mailto:orders@taaudaarubaaz.com\">orders@taaudaarubaaz.com</a></p>
        </div>
      </div>
      <div class=\"contact-item\">
        <i class=\"fa-solid fa-clock\"></i>
        <div>
          <h4>Opening Hours</h4>
          <p>Mon–Thu: 10:30 — 23:00<br>Fri–Sat: 10:30 — 23:30 &nbsp;•&nbsp; Sun: 11:00 — 22:30</p>
        </div>
      </div>
    </div>
    <h4 style=\"color:var(--text-0); margin-bottom:14px;\">Follow us</h4>
    <div class=\"contact-socials\">
      <a href=\"#\" aria-label=\"Instagram\"><i class=\"fa-brands fa-instagram\"></i></a>
      <a href=\"#\" aria-label=\"Facebook\"><i class=\"fa-brands fa-facebook-f\"></i></a>
      <a href=\"#\" aria-label=\"X / Twitter\"><i class=\"fa-brands fa-x-twitter\"></i></a>
      <a href=\"#\" aria-label=\"YouTube\"><i class=\"fa-brands fa-youtube\"></i></a>
      <a href=\"#\" aria-label=\"WhatsApp\"><i class=\"fa-brands fa-whatsapp\"></i></a>
    </div>
  </div>
  <form class=\"contact-form reveal-right\" id=\"contactForm\" novalidate>
    <h3>Send us a message</h3>
    <div class=\"form-row\">
      <div class=\"form-group\">
        <label for=\"cf-name\">Full Name</label>
        <input id=\"cf-name\" type=\"text\" name=\"name\" placeholder=\"Rohit Sharma\" data-testid=\"contact-name\">
        <small class=\"form-error\"></small>
      </div>
      <div class=\"form-group\">
        <label for=\"cf-phone\">Phone</label>
        <input id=\"cf-phone\" type=\"tel\" name=\"phone\" placeholder=\"+91 98765 43210\" data-testid=\"contact-phone\">
        <small class=\"form-error\"></small>
      </div>
    </div>
    <div class=\"form-group\">
      <label for=\"cf-email\">Email</label>
      <input id=\"cf-email\" type=\"email\" name=\"email\" placeholder=\"you@example.com\" data-testid=\"contact-email\">
      <small class=\"form-error\"></small>
    </div>
    <div class=\"form-group\">
      <label for=\"cf-subject\">Subject</label>
      <select id=\"cf-subject\" name=\"subject\" data-testid=\"contact-subject\">
        <option value=\"\">— Select a topic —</option>
        <option>General Inquiry</option>
        <option>Bulk / Party Order</option>
        <option>Delivery Help</option>
        <option>Pairing Recommendation</option>
        <option>Wholesale &amp; Reseller</option>
      </select>
      <small class=\"form-error\"></small>
    </div>
    <div class=\"form-group\">
      <label for=\"cf-message\">Message</label>
      <textarea id=\"cf-message\" name=\"message\" placeholder=\"Tell us how we can help...\" data-testid=\"contact-message\"></textarea>
      <small class=\"form-error\"></small>
    </div>
    <button type=\"submit\" class=\"btn btn--primary\" style=\"width:100%;\" data-testid=\"contact-submit\">Send Message <i class=\"fa-solid fa-paper-plane\"></i></button>
    <div class=\"form-status\" role=\"status\"></div>
  </form>
</div>
'''
    contact = section_wrap(\"contact\", \"Get In Touch\", \"Let's\", \"Talk Beer\",
                           \"We respond to every message — even the ones that come at 11 PM with a craft question.\",
                           contact_body)

    map_body = '''
<div class=\"map-wrap reveal\">
  <iframe loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\" allowfullscreen
    src=\"https://www.google.com/maps?q=Gurugram%20Sector%2014&output=embed\"></iframe>
  <div class=\"map-overlay\">
    <h4>Taau Daaru Baaz</h4>
    <p>Shop No. 12, Main Market, Sector 14, Gurugram, Haryana 122001</p>
  </div>
</div>
'''
    map_sec = section_wrap(\"location\", \"Find Us\", \"Visit Our\", \"Store\",
                           \"Easy parking, walking-distance from the metro, and Taau usually behind the counter himself.\",
                           map_body)

    newsletter_body = '''
<div class=\"newsletter reveal\">
  <h3>Join the <span style=\"color:var(--gold-300);font-style:italic;\">Daaru Club</span></h3>
  <p>Subscribe for early-access drops, members-only discounts, tasting invites and zero spam — only good beer.</p>
  <form class=\"newsletter-form\" id=\"newsletterForm\">
    <input type=\"email\" placeholder=\"your.email@example.com\" required data-testid=\"newsletter-email\" aria-label=\"Email\">
    <button type=\"submit\" data-testid=\"newsletter-submit\">Subscribe</button>
  </form>
</div>
'''
    newsletter = section_wrap(\"newsletter\", \"Stay In The Loop\", \"The Daaru\", \"Club\",
                              \"Members get the best of Taau — every Friday.\",
                              newsletter_body, \"section--tight\")

    html = (
        HTML_HEAD
        + HERO
        + ABOUT
        + featured
        + premium
        + brands
        + new_arr
        + offers
        + cats
        + all_beers
        + reviews
        + gallery
        + faq
        + contact
        + map_sec
        + newsletter
        + FOOTER
    )

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f\"Wrote {OUT} — {len(html.splitlines())} lines, {len(html):,} bytes.\")


if __name__ == '__main__':
    main()
"
Observation: Create successful: /app/website/_generate.py
