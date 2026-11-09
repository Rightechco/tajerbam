<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- هدر پریمیوم -->
    <div class="bg-white p-6 md:p-10 rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col md:flex-row md:items-center justify-between gap-6 relative overflow-hidden">
      <div class="absolute right-0 top-0 w-2.5 h-full bg-gradient-to-b from-orange-400 to-red-500"></div>
      <div class="absolute -left-20 -top-20 w-80 h-80 bg-orange-100 rounded-full mix-blend-multiply opacity-50 blur-[60px] pointer-events-none"></div>
      
      <div class="relative z-10">
        <h1 class="text-2xl md:text-4xl font-black text-slate-800 mb-3 flex items-center gap-3 tracking-tight">
          <div class="w-14 h-14 bg-gradient-to-br from-orange-100 to-red-50 text-orange-600 rounded-2xl flex items-center justify-center shadow-inner border border-orange-200">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"></path></svg>
          </div>
          محصولات داغ و سودآور <span class="bg-red-500 text-white text-xs px-2 py-1 rounded-md ml-2 uppercase animate-pulse">Hot</span>
        </h1>
        <p class="text-sm font-bold text-slate-500 max-w-2xl leading-relaxed">کالاهایی که بالاترین نرخ تبدیل و بیشترین حاشیه سود تضمین‌شده را برای شبکه بازاریابان به همراه داشته‌اند.</p>
      </div>
      
      <div class="flex gap-3 relative z-10 w-full md:w-auto">
        <select class="w-full md:w-56 bg-white border-2 border-slate-100 hover:border-orange-300 text-sm font-black text-slate-700 px-5 py-4 rounded-2xl outline-none focus:border-orange-500 focus:ring-4 focus:ring-orange-50 cursor-pointer shadow-sm transition-all">
          <option>🔥 مرتب‌سازی: بیشترین سود</option>
          <option>📈 مرتب‌سازی: پرفروش‌ترین‌ها</option>
          <option>✨ مرتب‌سازی: جدیدترین‌ها</option>
        </select>
      </div>
    </div>

    <!-- گرید محصولات -->
    <div class="relative z-10 min-h-[400px]">
      <div v-if="isLoading" class="absolute inset-0 bg-white/50 backdrop-blur-sm z-20 flex justify-center py-20 rounded-[2rem]">
        <svg class="w-12 h-12 text-orange-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        
        <div v-for="product in products" :key="product.id" class="bg-white border border-slate-200/60 rounded-[2.5rem] p-6 shadow-sm hover:shadow-[0_25px_50px_-12px_rgba(249,115,22,0.2)] hover:border-orange-300 transition-all duration-500 flex flex-col group relative overflow-hidden">
          
          <!-- درخشش پس‌زمینه هاور -->
          <div class="absolute inset-0 bg-gradient-to-b from-transparent to-orange-50/30 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>

          <!-- برچسب کمیسیون -->
          <div class="absolute top-5 right-5 z-10">
            <div class="bg-gradient-to-r from-orange-500 to-red-500 text-white text-[11px] font-black px-3.5 py-1.5 rounded-xl shadow-lg shadow-orange-500/30 flex items-center gap-1.5 transform group-hover:scale-105 transition-transform">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              پورسانت: {{ product.commissionPercent }}٪
            </div>
          </div>

          <!-- تصویر کالا با افکت سه‌بعدی -->
          <div class="w-full h-56 bg-slate-50/80 rounded-[2rem] p-6 mb-6 flex items-center justify-center group-hover:bg-orange-50/50 transition-colors border border-slate-100 relative z-10">
            <img :src="product.img" class="max-h-full object-contain mix-blend-multiply group-hover:scale-110 group-hover:rotate-3 group-hover:drop-shadow-2xl transition-all duration-500 ease-out">
          </div>

          <div class="flex flex-wrap items-center gap-2 mb-3 text-[10px] font-bold text-slate-400 relative z-10">
            <span class="bg-slate-100 px-2.5 py-1 rounded-lg border border-slate-200">{{ product.category }}</span>
            <span class="bg-slate-50 px-2.5 py-1 rounded-lg border border-slate-200">فروشنده: <span class="text-slate-600">{{ product.seller }}</span></span>
          </div>
          
          <h3 class="font-black text-slate-800 text-sm md:text-base leading-relaxed mb-6 line-clamp-2 group-hover:text-orange-600 transition-colors relative z-10">{{ product.name }}</h3>
          
          <div class="mt-auto space-y-4 relative z-10">
            <div class="bg-emerald-50/80 rounded-2xl p-4 border border-emerald-100 flex justify-between items-center group-hover:border-emerald-200 group-hover:bg-emerald-100/50 transition-colors">
              <span class="text-[11px] font-black text-slate-600">سود هر فروش شما:</span>
              <span class="font-black text-emerald-600 text-lg tracking-tight">+ {{ formatPrice(product.profit) }} <span class="text-[10px]">تومان</span></span>
            </div>

            <button @click="copyLink(product.id)" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-2xl transition-all shadow-[0_8px_20px_rgba(0,0,0,0.15)] flex items-center justify-center gap-2 text-sm group-hover:-translate-y-1">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
              دریافت لینک جادویی
            </button>
          </div>
        </div>

      </div>
    </div>

    <!-- توست نوتیفیکیشن -->
    <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
      <div v-if="copiedToast.show" class="fixed bottom-6 left-6 md:left-10 z-[100000] bg-slate-900 text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-4 font-sans border border-slate-700" dir="rtl">
        <div class="w-10 h-10 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center border border-emerald-500/30">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
        </div>
        <div>
          <h4 class="font-black text-sm tracking-wide">لینک بازاریابی کپی شد!</h4>
          <p class="text-[11px] text-slate-300 mt-1 font-medium">لینک کپی شده در کلیپ‌بورد آماده انتشار است.</p>
        </div>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';
const userName = localStorage.getItem('full_name') || 'ali_karimi';

const isLoading = ref(true);
const products = ref([]);
const copiedToast = ref({ show: false });

const formatPrice = (price) => {
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

const fetchProducts = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE_URL}/api/seller/marketing`, { // استفاده از اندپوینت موجود پایتون
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (response.ok) {
      const data = await response.json();
      // مپ کردن داده‌های سرور به ساختار فرانت
      products.value = data.products.map(p => ({
        id: p.id, name: p.title, category: 'دسته عمومی', seller: 'تامین‌کننده مجاز', 
        img: p.image, commissionPercent: p.commission, profit: (p.price * (p.commission / 100))
      }));
    } else {
      throw new Error("fallback");
    }
  } catch (error) {
    // Mock Data Fallback
    products.value = [
      { id: 1, name: 'لپ‌تاپ ایسوس Vivobook X1502ZA پردازنده i7', category: 'کالای دیجیتال', seller: 'رایان تکرو', img: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png', commissionPercent: '۵', profit: 2100000 },
      { id: 2, name: 'گوشی موبایل سامسونگ Galaxy S23 Ultra', category: 'موبایل', seller: 'دیجیتال شاپ', img: 'https://freepngimg.com/thumb/smartphone/133618-smart-phone-apple-free-photo.png', commissionPercent: '۳', profit: 1500000 },
      { id: 3, name: 'مانیتور ۲۴ اینچ ال‌جی مدل FHD پنل IPS', category: 'قطعات کامپیوتر', seller: 'رایان تکرو', img: 'https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png', commissionPercent: '۸', profit: 464000 },
      { id: 4, name: 'ساعت هوشمند اپل واچ سری ۹ بند سیلیکونی', category: 'گجت هوشمند', seller: 'واردات مستقیم پارس', img: 'https://freepngimg.com/thumb/smart_watch/133618-watch-smart-apple-free-photo.png', commissionPercent: '۶', profit: 1320000 },
    ];
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchProducts();
});

const copyLink = (id) => {
  const generatedUrl = `tajerbam.com/p/${id}?ref=${userName.replace(/\s+/g, '_').toLowerCase()}`;
  navigator.clipboard.writeText(generatedUrl).then(() => {
    copiedToast.value.show = true;
    setTimeout(() => { copiedToast.value.show = false; }, 3000);
  });
};
</script>