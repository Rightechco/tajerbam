<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر صفحه ================= -->
    <div class="bg-white p-6 md:p-10 rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col md:flex-row items-start md:items-center justify-between gap-6 relative overflow-hidden z-10">
      <div class="absolute right-0 top-0 w-2.5 h-full bg-gradient-to-b from-blue-500 to-indigo-600"></div>
      <div class="absolute -left-20 -top-20 w-80 h-80 bg-blue-100 rounded-full mix-blend-multiply opacity-50 blur-[60px] pointer-events-none"></div>
      
      <div class="relative z-10">
        <h1 class="text-2xl md:text-4xl font-black text-slate-800 mb-3 flex items-center gap-4 tracking-tight">
          <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-indigo-50 text-blue-600 rounded-2xl flex items-center justify-center shadow-inner border border-blue-200">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
          </div>
          مرکز دراپ‌شیپینگ <span class="bg-blue-600 text-white text-xs px-2.5 py-1 rounded-lg ml-2 shadow-sm font-sans uppercase">VIP Only</span>
        </h1>
        <p class="text-sm font-bold text-slate-500 max-w-2xl leading-relaxed">سفارشات مشتریان خود را با قیمت همکار ثبت کنید. کالا مستقیماً از انبار تامین‌کننده و با نام شما برای مشتری نهایی ارسال می‌شود.</p>
      </div>
    </div>

    <!-- ================= بخش 1: تامین‌کنندگان همکار و محصولاتشان ================= -->
    <div class="bg-slate-900 rounded-[3rem] p-8 md:p-12 shadow-[0_30px_60px_-15px_rgba(15,23,42,0.6)] relative overflow-hidden">
      <!-- افکت‌های نوری -->
      <div class="absolute -left-20 -top-20 w-80 h-80 bg-blue-600 rounded-full mix-blend-screen filter blur-[90px] opacity-40 pointer-events-none"></div>
      
      <h2 class="text-xl md:text-2xl font-black text-white mb-8 relative z-10 flex items-center gap-3">
        <span class="w-3 h-3 rounded-full bg-emerald-400 shadow-[0_0_15px_rgba(52,211,153,0.8)] animate-pulse"></span>
        تامین‌کنندگان طرف قرارداد شما
      </h2>

      <!-- لودینگ فروشندگان -->
      <div v-if="isLoadingSellers" class="relative z-10 flex justify-center py-10">
         <svg class="w-10 h-10 text-blue-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
      </div>

      <!-- لیست افقی فروشندگان -->
      <div v-else class="flex gap-5 overflow-x-auto custom-scrollbar pb-6 relative z-10 snap-x pt-2">
        <div v-for="seller in partneredSellers" :key="seller.id" 
             @click="activeSeller = seller"
             :class="['flex-shrink-0 w-56 p-5 rounded-[1.5rem] border-2 cursor-pointer transition-all duration-300 snap-start flex flex-col items-center text-center gap-4', 
                      activeSeller?.id === seller.id ? 'bg-gradient-to-b from-blue-600 to-indigo-600 border-blue-400 shadow-[0_15px_30px_rgba(37,99,235,0.5)] -translate-y-2' : 'bg-white/5 border-white/10 hover:bg-white/10 hover:-translate-y-1']">
          <div class="w-16 h-16 rounded-[1.2rem] bg-white text-slate-800 flex items-center justify-center font-black text-2xl shadow-inner">
            {{ seller.name.charAt(0) }}
          </div>
          <div>
            <h3 class="font-black text-white text-base mb-1">{{ seller.name }}</h3>
            <p class="text-xs text-blue-200 font-bold bg-white/10 px-2 py-1 rounded-md">{{ seller.productCount }} کالا برای فروش</p>
          </div>
        </div>
      </div>

      <!-- محصولات فروشنده انتخاب شده -->
      <transition enter-active-class="transition duration-500 ease-out" enter-from-class="opacity-0 translate-y-8" enter-to-class="opacity-100 translate-y-0">
        <div v-if="activeSeller" class="mt-10 pt-10 border-t border-white/10 relative z-10">
          <h3 class="text-xl font-black text-white mb-8">کاتالوگ محصولات: <span class="text-blue-400">{{ activeSeller.name }}</span></h3>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="product in activeSeller.products" :key="product.id" class="bg-white rounded-[2rem] p-5 flex flex-col group border-2 border-transparent hover:border-blue-300 hover:shadow-[0_15px_30px_rgba(0,0,0,0.2)] transition-all duration-300">
              <div class="w-full h-40 bg-slate-50/80 border border-slate-100 rounded-[1.5rem] p-4 mb-4 flex items-center justify-center group-hover:bg-blue-50/50 transition-colors">
                <img :src="product.img" class="max-h-full object-contain mix-blend-multiply transition-transform duration-500 group-hover:scale-110 group-hover:rotate-2">
              </div>
              <h4 class="font-black text-slate-800 text-sm leading-relaxed line-clamp-2 mb-4 group-hover:text-blue-700 transition-colors">{{ product.name }}</h4>
              
              <div class="bg-slate-50 rounded-xl p-3 mb-4 mt-auto border border-slate-100 flex justify-between items-center">
                <span class="text-[10px] font-black text-slate-500">قیمت خرید همکار:</span>
                <span class="font-black text-blue-700 text-base tracking-tight">{{ formatPrice(product.price) }} <span class="text-[10px]">ت</span></span>
              </div>
              
              <button @click="addToCart(product, activeSeller.name)" class="w-full bg-slate-900 hover:bg-blue-600 text-white font-black py-3.5 rounded-xl transition-all shadow-md group-hover:shadow-[0_8px_20px_rgba(37,99,235,0.3)] text-xs flex items-center justify-center gap-2 group-hover:-translate-y-1">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                افزودن به سبد مشتری
              </button>
            </div>
          </div>
        </div>
      </transition>
    </div>

    <!-- ================= بخش 2: سبد خرید و ثبت نهایی ================= -->
    <div v-if="cartItems.length > 0" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start relative z-10 animate-fade-in pt-4">
      
      <!-- ستون راست: فرم اطلاعات مشتری -->
      <div class="lg:col-span-5 space-y-6 lg:sticky top-28">
        <div class="bg-white rounded-[2.5rem] border border-slate-200/60 p-8 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-blue-500 to-indigo-600"></div>
          <h2 class="text-xl font-black text-slate-800 mb-6 flex items-center gap-3 border-b border-slate-100 pb-5">
            <div class="w-10 h-10 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
            </div>
            اطلاعات مشتری (گیرنده)
          </h2>
          
          <div class="space-y-5">
            <div>
              <label class="block text-xs font-black text-slate-600 mb-2">نام کامل مشتری نهایی</label>
              <input type="text" placeholder="مثلاً: محمد حسینی" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-800 px-5 py-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all shadow-sm">
            </div>
            <div>
              <label class="block text-xs font-black text-slate-600 mb-2">شماره تماس مشتری</label>
              <input type="tel" dir="ltr" placeholder="0912..." class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-800 text-right px-5 py-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all shadow-sm">
            </div>
            <div>
              <label class="block text-xs font-black text-slate-600 mb-2">آدرس دقیق پستی</label>
              <textarea rows="3" placeholder="استان، شهر، خیابان، پلاک، واحد..." class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-800 px-5 py-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all resize-none shadow-sm"></textarea>
            </div>
            <div class="bg-blue-50/80 border border-blue-200 p-5 rounded-2xl flex items-start gap-3 mt-4">
              <svg class="w-6 h-6 text-blue-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <p class="text-xs font-bold text-blue-900 leading-relaxed text-justify">
                محموله ارسالی دقیقاً با نام و برند شما (به عنوان فرستنده) بسته‌بندی و ارسال می‌شود. مشتری هیچ اطلاعی از تامین‌کننده اصلی نخواهد داشت.
              </p>
            </div>
          </div>
        </div>

        <!-- باکس تسویه حساب -->
        <div class="bg-gradient-to-b from-slate-900 to-slate-800 rounded-[2.5rem] p-8 md:p-10 text-white shadow-2xl relative overflow-hidden border border-slate-700">
          <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-500 rounded-full mix-blend-screen filter blur-[60px] opacity-20 pointer-events-none"></div>
          
          <h3 class="font-black text-xl mb-6 border-b border-slate-700/60 pb-5">تسویه حساب دراپ‌شیپینگ</h3>
          
          <div class="space-y-4 text-sm font-medium text-slate-300 mb-8">
            <div class="flex justify-between items-center bg-white/5 p-4 rounded-xl border border-white/10">
              <span class="font-bold">ارزش کل اقلام (قیمت همکار):</span>
              <span class="font-black text-white tracking-tight">{{ formatPrice(cartTotal) }} <span class="text-[10px]">تومان</span></span>
            </div>
          </div>

          <div class="border-t border-slate-700/60 pt-6 mb-8 flex justify-between items-end">
            <span class="text-sm font-black text-slate-400">مبلغ پرداختی از کیف پول شما:</span>
            <span class="text-3xl font-black text-emerald-400 tracking-tighter">{{ formatPrice(cartTotal) }} <span class="text-sm font-bold">تومان</span></span>
          </div>

          <button @click="handleCheckout" class="w-full bg-emerald-500 hover:bg-emerald-400 text-slate-900 font-black py-4.5 rounded-2xl transition-all shadow-[0_10px_25px_rgba(16,185,129,0.3)] hover:-translate-y-1 flex items-center justify-center gap-2 text-base">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            کسر از موجودی و ارسال سفارش
          </button>
        </div>
      </div>

      <!-- ستون چپ: اقلام سبد خرید -->
      <div class="lg:col-span-7 space-y-6">
        <h2 class="text-2xl font-black text-slate-800 flex items-center gap-3 px-2 mb-8">
          <div class="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center text-slate-500 border border-slate-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
          </div>
          جزئیات سبد خرید 
        </h2>

        <!-- تفکیک بر اساس فروشنده -->
        <transition-group name="list" tag="div" class="space-y-6">
          <div v-for="(group, sellerName) in groupedCart" :key="sellerName" class="bg-white rounded-[2.5rem] border border-slate-200/60 shadow-sm overflow-hidden group">
            
            <div class="bg-slate-50 border-b border-slate-100 p-5 px-8 flex items-center justify-between">
              <div class="flex items-center gap-4">
                <span class="w-10 h-10 rounded-[1rem] bg-white border border-slate-200 flex items-center justify-center text-base font-black text-slate-400 shadow-sm">{{ sellerName.charAt(0) }}</span>
                <div>
                  <span class="font-black text-slate-800 text-base">تامین‌کننده: {{ sellerName }}</span>
                  <p class="text-[10px] font-bold text-slate-500 mt-1">سفارشات این فروشنده در یک پکیج ارسال می‌شود.</p>
                </div>
              </div>
            </div>

            <div class="p-6 md:p-8 space-y-6">
              <div v-for="item in group" :key="item.cartId" class="flex flex-col md:flex-row md:items-center gap-6 relative p-4 rounded-2xl hover:bg-slate-50 transition-colors border border-transparent hover:border-slate-100">
                <button @click="removeFromCart(item.cartId)" class="absolute top-2 left-2 md:-top-2 md:-left-2 w-8 h-8 bg-red-50 text-red-500 rounded-full flex items-center justify-center hover:bg-red-500 hover:text-white transition-all shadow-sm tooltip" title="حذف کالا">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                
                <div class="w-24 h-24 bg-white rounded-[1.2rem] p-3 border border-slate-200 shrink-0 shadow-sm flex items-center justify-center">
                  <img :src="item.img" class="max-w-full max-h-full object-contain mix-blend-multiply">
                </div>
                
                <div class="flex-grow">
                  <h4 class="font-black text-slate-800 text-base line-clamp-2 mb-4">{{ item.name }}</h4>
                  <div class="flex flex-col md:flex-row md:justify-between md:items-end gap-4">
                    
                    <!-- کنترل تعداد -->
                    <div class="flex items-center bg-white border-2 border-slate-200 rounded-xl p-1 w-fit shadow-sm">
                      <button @click="item.qty > 1 ? item.qty-- : null" class="w-10 h-10 flex items-center justify-center font-black text-slate-500 hover:bg-slate-100 rounded-lg transition-colors">-</button>
                      <input type="number" v-model="item.qty" readonly class="w-12 text-center bg-transparent font-black text-slate-800 text-lg outline-none pointer-events-none">
                      <button @click="item.qty++" class="w-10 h-10 flex items-center justify-center font-black text-slate-500 hover:bg-slate-100 rounded-lg transition-colors">+</button>
                    </div>
                    
                    <div class="text-left bg-slate-50 px-4 py-2 rounded-xl border border-slate-100">
                      <span class="block text-[10px] font-bold text-slate-500 mb-1">جمع این قلم:</span>
                      <span class="font-black text-blue-700 text-lg tracking-tight">{{ formatPrice(item.price * item.qty) }} <span class="text-[10px]">تومان</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition-group>
      </div>
    </div>
    
    <!-- اگر سبد خالی بود -->
    <div v-else-if="!activeSeller && !isLoadingSellers" class="text-center py-20 text-slate-400 font-bold animate-fade-in bg-white rounded-[2rem] border border-slate-100 border-dashed">
      ابتدا از لیست تامین‌کنندگان بالا، شریک تجاری خود را انتخاب کرده و محصولات را به سبد مشتری اضافه کنید.
    </div>

    <!-- ================= MODAL: Paywall Checkout (ارتقا پلن) ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 scale-95 translate-y-4" enter-to-class="opacity-100 scale-100 translate-y-0" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 translate-y-4">
        <div v-if="showUpgradeModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-md rounded-[3rem] shadow-2xl relative overflow-hidden border border-white/20">
            <div class="absolute top-0 right-0 w-full h-3 bg-gradient-to-r from-amber-400 to-orange-500 z-10"></div>
            <div class="absolute -right-16 -top-16 w-64 h-64 bg-amber-400 rounded-full mix-blend-screen filter blur-[70px] opacity-20 pointer-events-none"></div>
            
            <button @click="showUpgradeModal = false" class="absolute top-6 left-6 z-20 w-10 h-10 bg-slate-50 hover:bg-red-50 text-slate-400 hover:text-red-500 rounded-full flex items-center justify-center transition-colors border border-slate-100">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>

            <div class="p-8 md:p-10 text-center relative z-10">
              <div class="w-24 h-24 bg-gradient-to-tr from-amber-100 to-orange-100 rounded-[2rem] flex items-center justify-center mx-auto mb-6 shadow-inner border border-amber-200">
                <svg class="w-12 h-12 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
              <h2 class="text-2xl font-black text-slate-800 mb-3 tracking-tight">سیستم ثبت سفارش قفل است!</h2>
              <p class="text-slate-500 font-bold text-sm leading-relaxed mb-8 px-2">
                برای استفاده از سیستم دراپ‌شیپینگ (ثبت سفارش مستقیم با قیمت همکار و ارسال به نام خودتان برای مشتری)، باید اشتراک VIP بازاریابان را فعال کنید.
              </p>
              
              <button @click="$router.push('/marketer/plans')" class="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-black py-4.5 rounded-2xl shadow-[0_10px_25px_rgba(245,158,11,0.4)] transition-all hover:-translate-y-1 flex items-center justify-center gap-2 text-base">
                مشاهده پلن‌ها و ارتقاء آنی حساب
                <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </button>
            </div>
          </div>

        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const hasActivePlan = ref(false); // در حالت تستی false است
const showUpgradeModal = ref(false);
const isLoadingSellers = ref(false);

const partneredSellers = ref([]);
const activeSeller = ref(null);
const cartItems = ref([]);

const fetchPartners = () => {
  isLoadingSellers.value = true;
  // Mock Data
  setTimeout(() => {
    partneredSellers.value = [
      { 
        id: 1, name: 'رایان تکرو', productCount: 45, 
        products: [
          { id: 101, name: 'لپ‌تاپ ایسوس Vivobook X1502 پردازنده i7 نسل ۱۲', img: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png', price: 39800000 },
          { id: 102, name: 'موس بی‌سیم تسکو مدل TM 120', img: 'https://freepngimg.com/thumb/mouse/10-mouse-png-image.png', price: 180000 }
        ]
      },
      { 
        id: 2, name: 'دیجیتال شاپ مرکزی', productCount: 120, 
        products: [
          { id: 201, name: 'مانیتور ۲۴ اینچ ال‌جی پنل IPS', img: 'https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png', price: 5620000 },
          { id: 202, name: 'گوشی موبایل سامسونگ Galaxy S23 Ultra', img: 'https://freepngimg.com/thumb/smartphone/133618-smart-phone-apple-free-photo.png', price: 48500000 }
        ]
      }
    ];
    // انتخاب پیش‌فرض اگر فروشنده‌ای بود
    if(partneredSellers.value.length > 0) activeSeller.value = partneredSellers.value[0];
    
    isLoadingSellers.value = false;
  }, 800);
};

onMounted(() => {
  fetchPartners();
});

const addToCart = (product, sellerName) => {
  const existing = cartItems.value.find(i => i.id === product.id && i.seller === sellerName);
  if (existing) {
    existing.qty++;
  } else {
    cartItems.value.push({ ...product, seller: sellerName, qty: 1, cartId: Date.now() + Math.random() });
  }
};

const removeFromCart = (cartId) => {
  cartItems.value = cartItems.value.filter(i => i.cartId !== cartId);
};

const groupedCart = computed(() => {
  return cartItems.value.reduce((acc, item) => {
    if (!acc[item.seller]) acc[item.seller] = [];
    acc[item.seller].push(item);
    return acc;
  }, {});
});

const cartTotal = computed(() => {
  return cartItems.value.reduce((sum, item) => sum + (item.price * item.qty), 0);
});

const handleCheckout = () => {
  if (!hasActivePlan.value) {
    showUpgradeModal.value = true;
  } else {
    alert('مبلغ از کیف پول شما کسر و سفارش با موفقیت ثبت شد و به تفکیک برای تامین‌کنندگان ارسال گردید.');
    cartItems.value = []; // خالی کردن سبد
  }
};

const formatPrice = (price) => {
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { height: 8px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }

.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateX(30px) scale(0.98); }

body:has(.fixed.z-\[99999\]) { overflow: hidden; }

/* مخفی کردن فلش‌های input number */
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}
</style>