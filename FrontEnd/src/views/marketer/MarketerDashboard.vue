<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-12 font-sans" dir="rtl">
    
    <!-- هدر خوش‌آمدگویی -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 bg-white p-6 md:p-8 rounded-[2.5rem] border border-slate-100 shadow-[0_20px_50px_-12px_rgba(16,185,129,0.1)] relative overflow-hidden">
      <div class="absolute top-0 left-0 w-72 h-72 bg-emerald-100 rounded-full mix-blend-multiply filter blur-[50px] opacity-70 animate-pulse z-0"></div>
      
      <div class="flex items-center gap-5 relative z-10">
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-emerald-500 to-teal-500 p-0.5 shadow-lg shadow-emerald-500/30">
          <div class="w-full h-full bg-white/90 backdrop-blur-sm rounded-[14px] flex items-center justify-center font-black text-2xl text-emerald-600">
            {{ userName.charAt(0) }}
          </div>
        </div>
        <div>
          <div class="flex items-center gap-2 mb-1">
            <h1 class="text-2xl font-black text-slate-800 tracking-tight">سلام {{ userName }} عزیز، خداقوت! 🚀</h1>
          </div>
          <p class="text-sm font-bold text-slate-500">لینک‌های شما در ۲۴ ساعت گذشته <span class="text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-lg border border-emerald-200">{{ stats.todayClicks }} کلیک</span> جدید داشته است.</p>
        </div>
      </div>
      
      <div class="relative z-10 flex gap-3">
        <button class="bg-white border-2 border-slate-200 text-slate-700 hover:border-emerald-400 hover:text-emerald-600 font-bold px-6 py-3.5 rounded-2xl transition-all shadow-sm flex items-center gap-2 text-sm group">
          <svg class="w-5 h-5 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          آکادمی فروش
        </button>
      </div>
    </div>

    <!-- کارت‌های آماری -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative">
      <!-- لودینگ آماری -->
      <div v-if="isLoading" class="absolute inset-0 bg-white/50 backdrop-blur-sm z-20 flex justify-center py-10 rounded-[2rem]">
        <svg class="w-10 h-10 text-emerald-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
      </div>

      <!-- درآمد کل -->
      <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 rounded-[2.5rem] p-7 text-white shadow-xl relative overflow-hidden group hover:-translate-y-1 transition-all">
        <div class="absolute -right-10 -top-10 w-40 h-40 bg-emerald-500 rounded-full mix-blend-screen filter blur-[50px] opacity-30 group-hover:opacity-60 transition-opacity"></div>
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-slate-300 text-sm font-bold">موجودی قابل برداشت</span>
              <div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center border border-white/10"><svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
            </div>
            <div class="text-3xl font-black mb-1 tracking-tight">{{ formatPrice(stats.balance) }} <span class="text-xs font-bold text-emerald-300">تومان</span></div>
          </div>
          <button @click="$router.push('/marketer/wallet')" class="w-full mt-5 bg-emerald-500 hover:bg-emerald-400 text-slate-900 font-black py-3 rounded-xl transition-colors text-sm shadow-[0_5px_15px_rgba(16,185,129,0.3)]">تسویه حساب</button>
        </div>
      </div>

      <div class="bg-white rounded-[2.5rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">کلیک روی لینک‌ها</span>
            <div class="w-10 h-10 bg-blue-50 text-blue-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800">{{ stats.totalClicks }}</div>
        </div>
        <div class="text-xs font-bold text-blue-700 bg-blue-50 px-3 py-1.5 rounded-lg w-fit mt-4 border border-blue-100">+{{ stats.clicksGrowth }}٪ نسبت به ماه قبل</div>
      </div>

      <div class="bg-white rounded-[2.5rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">خریدهای موفق</span>
            <div class="w-10 h-10 bg-indigo-50 text-indigo-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800">{{ stats.successfulSales }} <span class="text-sm font-bold text-slate-400">سفارش</span></div>
        </div>
        <div class="text-xs font-bold text-indigo-700 bg-indigo-50 px-3 py-1.5 rounded-lg w-fit mt-4 border border-indigo-100">در حال پردازش: {{ stats.pendingSales }} سفارش</div>
      </div>

      <div class="bg-white rounded-[2.5rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">نرخ تبدیل (CR)</span>
            <div class="w-10 h-10 bg-orange-50 text-orange-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800">{{ stats.conversionRate }}٪</div>
        </div>
        <div class="text-xs font-bold text-orange-700 bg-orange-50 px-3 py-1.5 rounded-lg w-fit mt-4 border border-orange-100">عملکرد شما: عالی 🎯</div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- ابزار ساخت لینک سریع -->
      <div class="lg:col-span-1 bg-white border border-slate-100 rounded-[2.5rem] shadow-sm p-6 md:p-8 relative overflow-hidden flex flex-col justify-center">
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-emerald-400 to-teal-500"></div>
        <h3 class="font-black text-slate-800 text-lg flex items-center gap-2 mb-6">
          <svg class="w-6 h-6 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
          تولید لینک بازاریابی سریع
        </h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-slate-500 mb-2">لینک صفحه محصول یا فروشگاه را وارد کنید:</label>
            <input type="text" v-model="linkInput" placeholder="https://tajerbam.com/product/..." class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-800 px-4 py-3.5 rounded-xl focus:bg-white focus:border-emerald-400 outline-none transition-all" dir="ltr">
          </div>
          <button @click="generateLink" :disabled="!linkInput || isGenerating" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl transition-all shadow-[0_10px_20px_rgba(0,0,0,0.15)] disabled:opacity-50 text-sm flex justify-center items-center gap-2">
            <svg v-if="isGenerating" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            ساخت لینک اختصاصی من
          </button>

          <!-- نتیجه لینک -->
          <div v-if="generatedLink" class="mt-4 p-4 bg-emerald-50 border border-emerald-200 rounded-xl animate-fade-in shadow-inner">
            <p class="text-[10px] font-bold text-emerald-800 mb-2">لینک شما آماده کپی است:</p>
            <div class="flex items-center gap-2 bg-white border border-emerald-200 p-2 rounded-lg shadow-sm">
              <input type="text" readonly :value="generatedLink" class="w-full text-xs font-mono font-bold text-slate-600 bg-transparent outline-none" dir="ltr">
              <button @click="copyLink" class="bg-emerald-100 text-emerald-700 hover:bg-emerald-500 hover:text-white p-2.5 rounded-lg transition-colors tooltip shrink-0" title="کپی کردن">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- جدول آخرین تراکنش‌های بازاریابی -->
      <div class="lg:col-span-2 bg-white border border-slate-100 rounded-[2.5rem] shadow-sm overflow-hidden flex flex-col">
        <div class="p-6 md:p-8 border-b border-slate-50 bg-slate-50/50 flex items-center justify-between">
          <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-indigo-500 shadow-[0_0_10px_rgba(99,102,241,0.6)]"></span> آخرین پورسانت‌های دریافتی
          </h3>
          <button class="text-xs font-bold text-indigo-600 hover:text-indigo-800 bg-indigo-50 px-3 py-1.5 rounded-lg transition-colors border border-indigo-100">مشاهده کیف پول</button>
        </div>
        
        <div class="overflow-x-auto custom-scrollbar flex-grow relative">
          <div v-if="isLoading" class="absolute inset-0 bg-white/50 backdrop-blur-sm z-20 flex justify-center py-10">
            <svg class="w-8 h-8 text-indigo-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          </div>

          <table class="w-full text-right text-sm">
            <thead class="bg-white text-slate-400 text-[11px] font-black uppercase border-b border-slate-100">
              <tr>
                <th class="px-6 py-5">محصول فروخته شده</th>
                <th class="px-6 py-5 text-center">مبلغ کل خرید</th>
                <th class="px-6 py-5 text-center">پورسانت شما</th>
                <th class="px-6 py-5 text-center">وضعیت</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-50 font-medium text-slate-700">
              <tr v-for="t in recentTransactions" :key="t.id" class="hover:bg-slate-50/80 transition-colors group">
                <td class="px-6 py-5">
                  <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-white border border-slate-200 rounded-xl p-1 shadow-sm shrink-0">
                      <img :src="t.img" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                      <p class="font-black text-slate-800 text-sm mb-1 group-hover:text-indigo-600 transition-colors">{{ t.product }}</p>
                      <p class="text-[10px] font-bold text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md w-fit">تامین‌کننده: {{ t.seller }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-5 text-center font-mono font-bold">{{ formatPrice(t.orderTotal) }}</td>
                <td class="px-6 py-5 text-center font-black text-emerald-600 text-base">+ {{ formatPrice(t.commission) }}</td>
                <td class="px-6 py-5 text-center">
                  <span v-if="t.status === 'paid'" class="bg-emerald-50 border border-emerald-100 text-emerald-600 px-3 py-1.5 rounded-lg text-[11px] font-black shadow-sm">واریز به کیف پول</span>
                  <span v-else class="bg-amber-50 border border-amber-100 text-amber-600 px-3 py-1.5 rounded-lg text-[11px] font-black shadow-sm">در انتظار تحویل</span>
                </td>
              </tr>
              <tr v-if="recentTransactions.length === 0">
                <td colspan="4" class="px-6 py-10 text-center text-slate-400 font-bold">هنوز فروشی ثبت نکرده‌اید.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';
const userName = localStorage.getItem('full_name') || 'بازاریاب عزیز';

const isLoading = ref(true);
const isGenerating = ref(false);
const stats = ref({ balance: 0, totalClicks: 0, clicksGrowth: 0, successfulSales: 0, pendingSales: 0, conversionRate: 0, todayClicks: 0 });
const recentTransactions = ref([]);

const linkInput = ref('');
const generatedLink = ref('');

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '۰';
};

const fetchData = async () => {
  try {
    isLoading.value = true;
    const response = await fetch(`${API_BASE_URL}/api/marketer/dashboard`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (response.ok) {
      const data = await response.json();
      stats.value = data.stats;
      recentTransactions.value = data.recent_transactions;
    } else {
      // Mock data for test
      stats.value = { balance: 4250000, totalClicks: 1842, clicksGrowth: 15, successfulSales: 28, pendingSales: 5, conversionRate: 1.5, todayClicks: 45 };
      recentTransactions.value = [
        { id: 1, product: 'لپ‌تاپ ایسوس (خرید عمده ۵ عدد)', seller: 'رایان تکرو', orderTotal: 195000000, commission: 2500000, status: 'paid', img: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png' },
        { id: 2, product: 'مانیتور ال‌جی ۲۴ اینچ', seller: 'دیجیتال شاپ', orderTotal: 5800000, commission: 116000, status: 'pending', img: 'https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png' }
      ];
    }
  } catch (error) {
    console.error("Dashboard Fetch Error", error);
  } finally {
    isLoading.value = false;
  }
};

const generateLink = () => {
  if(!linkInput.value) return;
  isGenerating.value = true;
  setTimeout(() => {
    const base = linkInput.value.split('?')[0];
    const usernameSlug = userName.replace(/\s+/g, '_').toLowerCase();
    generatedLink.value = `${base}?ref=${usernameSlug}&utm_source=panel`;
    isGenerating.value = false;
  }, 800);
};

const copyLink = () => {
  navigator.clipboard.writeText(generatedLink.value).then(() => {
    alert('لینک با موفقیت کپی شد. حالا می‌توانید آن را در شبکه‌های اجتماعی خود قرار دهید.');
  });
};

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { height: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>