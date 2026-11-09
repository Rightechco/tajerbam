"""
=========================================================================================
   TAJERBAM B2B ECOSYSTEM - ADVANCED DATA SEEDER
   Version: 7.0.0
   Description: این اسکریپت برای تزریق انبوه داده‌های تستی (محصولات، سفارشات، بازاریابان و 
   کاربران VIP) به دیتابیس استفاده می‌شود تا گرافیک پنل‌ها در بهترین حالت دمو داده شود.
=========================================================================================
"""

import random
import time
from datetime import datetime, timedelta
from backend.main import (
    SessionLocal, User, Category, Product, Inventory, ProductPriceTier, 
    engine, Base, UserRole, SubscriptionPlan, Transaction, Order, 
    MarketerLink, Dispute, RFQ
)

def seed_enterprise_database():
    print("="*60)
    print("🚀 Starting Enterprise Data Seeder for TajerBam V7.0.0...")
    print("="*60)
    
    # 1. اطمینان از وجود جداول
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        # ==================== 1. Categories ====================
        print("📁 1. Syncing Categories...")
        categories_data = [
            {"name": "کالای دیجیتال و قطعات", "slug": "digital", "icon": "computer"},
            {"name": "موبایل و تبلت", "slug": "mobile", "icon": "phone"},
            {"name": "ابزارآلات صنعتی", "slug": "tools", "icon": "tool"},
            {"name": "تجهیزات پزشکی", "slug": "medical", "icon": "heart"}
        ]
        
        for c_data in categories_data:
            if not db.query(Category).filter(Category.slug == c_data["slug"]).first():
                db.add(Category(**c_data))
        db.commit()

        # ==================== 2. Users (IAM) ====================
        print("👥 2. Generating VIP Users, Sellers & Marketers...")
        
        # Super Admin
        admin = db.query(User).filter(User.phone == "09999999999").first()
        if not admin:
            admin = User(
                phone="09999999999", full_name="مدیریت کلان تاجربام", role=UserRole.ADMIN,
                wallet_balance=5000000000.0, is_verified=True, is_vip=True
            )
            db.add(admin)

        # VIP Seller
        seller = db.query(User).filter(User.phone == "09121111111").first()
        if not seller:
            seller = User(
                phone="09121111111", full_name="شرکت رایان تکرو", role=UserRole.SELLER,
                wallet_balance=85000000.0, is_verified=True, is_vip=True,
                company_name="رایان تکرو", sheba_number="012345678912345678912345"
            )
            db.add(seller)
            
        # Top Marketer
        marketer = db.query(User).filter(User.phone == "09142222222").first()
        if not marketer:
            marketer = User(
                phone="09142222222", full_name="علی کریمی (Affiliate)", role=UserRole.MARKETER,
                wallet_balance=12450000.0, total_earned=45000000.0, is_verified=True, is_vip=True
            )
            db.add(marketer)
            
        # VIP Buyer
        buyer = db.query(User).filter(User.phone == "09153333333").first()
        if not buyer:
            buyer = User(
                phone="09153333333", full_name="خرید سازمانی پتروشیمی", role=UserRole.BUYER,
                wallet_balance=1200000000.0, is_verified=True, company_name="پتروشیمی خلیج فارس"
            )
            db.add(buyer)

        db.commit()

        # ==================== 3. Products & Inventory ====================
        print("📦 3. Populating Warehouse and Product Catalog...")
        seller_id = db.query(User).filter(User.phone == "09121111111").first().id
        cat_id = db.query(Category).filter(Category.slug == "digital").first().id
        
        products_data = [
            {"title": "لپ‌تاپ گیمینگ ایسوس ROG Strix G15", "sku": "AS-ROG-15", "price": 68000000, "comm": 4.5, "img": "https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png"},
            {"title": "گوشی هوشمند سامسونگ Galaxy S24 Ultra", "sku": "SM-S24U", "price": 71000000, "comm": 2.5, "img": "https://freepngimg.com/thumb/smartphone/133618-smart-phone-apple-free-photo.png"},
            {"title": "مانیتور 27 اینچ خمیده سامسونگ", "sku": "SM-M27C", "price": 12500000, "comm": 8.0, "img": "https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png"},
            {"title": "موس بی‌سیم تسکو (پک 50 عددی)", "sku": "TS-M-101", "price": 280000, "comm": 12.0, "img": "https://freepngimg.com/thumb/mouse/10-mouse-png-image.png"}
        ]
        
        added_prods = 0
        for pd in products_data:
            if not db.query(Product).filter(Product.sku == pd["sku"]).first():
                product = Product(
                    title=pd["title"], sku=pd["sku"], price_retail=pd["price"], 
                    category_id=cat_id, seller_id=seller_id, 
                    commission_percent=pd["comm"], image_url=pd["img"],
                    is_dropship_enabled=True, has_insurance=True
                )
                db.add(product)
                db.flush()
                
                # Price Tiers
                db.add(ProductPriceTier(product_id=product.id, min_qty=5, max_qty=19, price_per_unit=pd["price"]*0.95))
                db.add(ProductPriceTier(product_id=product.id, min_qty=20, max_qty=None, price_per_unit=pd["price"]*0.88))
                
                # Inventory
                db.add(Inventory(product_id=product.id, stock_total=random.randint(50, 500), min_threshold=10, rack_location=f"RACK-{random.randint(1,10)}"))
                added_prods += 1
                
        db.commit()
        print(f"   -> Added {added_prods} new premium products.")

        # ==================== 4. Fake Ledger & Orders ====================
        print("💸 4. Simulating Double-Entry Ledger and Orders...")
        if db.query(Transaction).count() < 5:
            admin_id = db.query(User).filter(User.role == UserRole.ADMIN).first().id
            marketer_id = db.query(User).filter(User.role == UserRole.MARKETER).first().id
            
            # Withdrawal request for admin panel
            db.add(Transaction(
                user_id=seller_id, transaction_id=f"TRX-WD-{int(time.time())}", 
                type="out", category="withdraw", amount=15000000, status="pending", title="درخواست تسویه فروشنده"
            ))
            
            # Commission for marketer
            db.add(Transaction(
                user_id=marketer_id, transaction_id=f"TRX-COM-{int(time.time())+1}", 
                type="in", category="commission", amount=2500000, status="success", title="پورسانت فروش لپ‌تاپ"
            ))
            
            # A dispute case
            ord_num = f"ORD-{random.randint(10000, 99999)}"
            order = Order(
                order_number=ord_num, buyer_id=buyer.id, seller_id=seller_id, 
                product_name="مانیتور 27 اینچ خمیده", qty=50, total_amount=625000000, 
                status="disputed", progress=100
            )
            db.add(order)
            db.flush()
            
            db.add(Dispute(
                order_id=order.id, plaintiff_id=buyer.id, reason="damaged", 
                description="چندین عدد از مانیتورها در حین باربری آسیب فیزیکی دیده‌اند.", status="open"
            ))
            
            db.commit()
            
        print("="*60)
        print("✅ SUCCESS! Enterprise Database is successfully populated and ready.")
        print("="*60)

    except Exception as e:
        db.rollback()
        print(f"❌ FATAL ERROR During Seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_enterprise_database()