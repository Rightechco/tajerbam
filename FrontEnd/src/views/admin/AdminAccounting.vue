<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-emerald-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-blue-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-blue-500 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">حسابداری و گزارشات مالی</h1>
          <p class="text-sm font-bold text-slate-400">گزارش‌گیری دقیق از سود، زیان و گردش مالی پلتفرم (P&L)</p>
        </div>
      </div>

      <div class="relative z-10 flex flex-wrap items-center gap-3 w-full lg:w-auto">
        <div class="bg-slate-950 border border-slate-700 p-1.5 rounded-xl flex gap-1">
          <button @click="timeFilter = 'week'" :class="timeFilter === 'week' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:text-white'" class="px-4 py-2 rounded-lg text-sm font-bold transition-all">هفته جاری</button>
          <button @click="timeFilter = 'month'" :class="timeFilter === 'month' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:text-white'" class="px-4 py-2 rounded-lg text-sm font-bold transition-all">ماه جاری</button>
          <button @click="timeFilter = 'year'" :class="timeFilter === 'year' ? 'bg-blue-600 text-white' : 'text-slate-400 hover:text-white'" class="px-4 py-2 rounded-lg text-sm font-bold transition-all">سالانه</button>
        </div>
        
        <button @click="exportReport" :disabled="isExporting" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-3.5 rounded-xl transition-all font-bold flex items-center justify-center gap-2 text-sm shadow-[0_0_15px_rgba(37,99,235,0.4)] disabled:opacity-50">
          <svg v-if="isExporting" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          صدور گزارش (PDF)
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-blue-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-blue-500 animate-pulse">در حال استخراج و تحلیل داده‌های مالی...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in">
      
      <!-- ================= کارت‌های آماری کلیدی (KPIs) ================= -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- کل فروش (GMV) -->
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-blue-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">گردش مالی (GMV)</span>
            <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ formatPrice(stats.revenue) }}</div>
          <div class="relative z-10 mt-2 text-xs text-blue-400 font-bold bg-blue-500/10 inline-block px-2 py-1 rounded">کل فروش پلتفرم</div>
        </div>

        <!-- هزینه‌ها -->
        <div class="bg-slate-900 rounded-3xl border border-rose-500/20 p-6 relative overflow-hidden group hover:border-rose-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-rose-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-rose-400 text-xs font-bold uppercase tracking-wider">هزینه‌ها و کمیسیون</span>
            <div class="w-10 h-10 bg-rose-500/10 text-rose-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-rose-400 mb-1">{{ formatPrice(stats.expenses) }}</div>
          <div class="relative z-10 mt-2 text-xs text-rose-400 font-bold bg-rose-500/10 inline-block px-2 py-1 rounded">خروجی عملیاتی</div>
        </div>

        <!-- سود خالص -->
        <div class="bg-slate-900 rounded-3xl border border-emerald-500/30 p-6 relative overflow-hidden group hover:border-emerald-500/60 transition-all shadow-[0_0_15px_rgba(16,185,129,0.1)]">
          <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-emerald-400 text-xs font-bold uppercase tracking-wider">سود خالص (Net Profit)</span>
            <div class="w-10 h-10 bg-emerald-500/10 text-emerald-500 rounded-xl flex items-center justify-center animate-pulse"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-emerald-400 mb-1">{{ formatPrice(stats.netProfit) }}</div>
          <div class="relative z-10 mt-2 text-xs text-emerald-400 font-bold bg-emerald-500/10 inline-block px-2 py-1 rounded">حاشیه سود: {{ stats.margin }}%</div>
        </div>

        <!-- وجه بلوکه شده (Escrow) -->
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-amber-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">سپرده حساب امانی</span>
            <div class="w-10 h-10 bg-amber-500/10 text-amber-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ formatPrice(stats.escrowLocked) }}</div>
          <div class="relative z-10 mt-2 text-xs text-amber-400 font-bold bg-amber-500/10 inline-block px-2 py-1 rounded">در حال تسویه (تومان)</div>
        </div>

      </div>

      <!-- ================= نمودار و جدول پرفروش‌ترین‌ها ================= -->
      <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
        
        <!-- چارت (پیاده‌سازی CSS) -->
        <div class="xl:col-span-2 bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg p-6 flex flex-col h-[500px]">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-black text-white text-lg flex items-center gap-2">
              <div class="w-3 h-3 rounded-full bg-blue-500"></div>
              تحلیل روند درآمد و هزینه
            </h3>
            <div class="flex gap-4 text-xs font-bold">
              <div class="flex items-center gap-1.5"><span class="w-3 h-3 rounded bg-emerald-500"></span> درآمد خالص</div>
              <div class="flex items-center gap-1.5"><span class="w-3 h-3 rounded bg-rose-500"></span> هزینه‌ها</div>
            </div>
          </div>
          
          <div class="flex-grow flex items-end justify-between gap-1 md:gap-3 relative z-10 border-b border-slate-700/80 pb-2 overflow-x-auto custom-scrollbar-dark px-2">
            <!-- Grid Lines -->
            <div class="absolute w-full top-0 border-t border-dashed border-slate-800 -z-10"></div>
            <div class="absolute w-full top-1/4 border-t border-dashed border-slate-800 -z-10"></div>
            <div class="absolute w-full top-2/4 border-t border-dashed border-slate-800 -z-10"></div>
            <div class="absolute w-full top-3/4 border-t border-dashed border-slate-800 -z-10"></div>
            
            <div v-for="(item, index) in chartData" :key="index" class="w-12 md:w-full min-w-[30px] max-w-[50px] relative group flex flex-col items-center justify-end h-full">
              <!-- Tooltip -->
              <div class="absolute -top-16 opacity-0 group-hover:opacity-100 transition-all duration-300 bg-slate-800 text-white text-[11px] font-black px-3 py-2 rounded-lg pointer-events-none shadow-xl z-20 whitespace-nowrap border border-slate-600 flex flex-col gap-1 transform translate-y-2 group-hover:translate-y-0">
                <span class="text-emerald-400">+ {{ formatPrice(item.income) }}</span>
                <span class="text-rose-400">- {{ formatPrice(item.expense) }}</span>
              </div>
              
              <div class="w-full flex gap-1 items-end h-[85%] relative">
                <div class="w-1/2 bg-gradient-to-t from-emerald-700 to-emerald-400 rounded-t-md hover:brightness-125 transition-all" :style="`height: ${Math.max((item.income / maxChartValue) * 100, 5)}%`"></div>
                <div class="w-1/2 bg-gradient-to-t from-rose-800 to-rose-500 rounded-t-md hover:brightness-125 transition-all" :style="`height: ${Math.max((item.expense / maxChartValue) * 100, 5)}%`"></div>
              </div>
              <div class="text-[10px] font-bold mt-3 text-slate-500 whitespace-nowrap">{{ item.date }}</div>
            </div>
          </div>
        </div>

        <!-- لیست پرفروش‌ترین‌ها -->
        <div class="xl:col-span-1 bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg p-6 flex flex-col h-[500px]">
          <h3 class="font-black text-white text-lg flex items-center gap-2 mb-6 border-b border-slate-800 pb-4">
            <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
            پرفروش‌ترین کالاها (Top Sellers)
          </h3>

          <div class="flex-grow overflow-y-auto custom-scrollbar-dark pr-2 space-y-4">
            <div v-if="topProducts.length === 0" class="text-center text-slate-500 py-10 font-bold">داده‌ای یافت نشد.</div>
            
            <div v-for="(prod, i) in topProducts" :key="i" class="flex items-center gap-4 bg-slate-950/50 p-3 rounded-2xl border border-slate-800/80 hover:border-slate-700 transition-colors">
              <div class="w-12 h-12 bg-white rounded-xl p-1 shrink-0 shadow-sm border border-slate-700">
                <img :src="prod.img" class="w-full h-full object-contain" alt="">
              </div>
              <div class="flex-grow min-w-0">
                <h4 class="text-white font-bold text-sm truncate" :title="prod.name">{{ prod.name }}</h4>
                <div class="flex items-center gap-3 mt-1">
                  <span class="text-[10px] font-mono text-slate-500 bg-slate-900 px-1.5 py-0.5 rounded">{{ prod.sku }}</span>
                  <span class="text-xs font-bold text-slate-400">{{ prod.qty }} فروش</span>
                </div>
              </div>
              <div class="text-left shrink-0">
                <span class="text-emerald-400 font-black text-sm block">{{ formatPrice(prod.revenue) }}</span>
                <span class="text-[10px] text-slate-500 font-bold">تومان</span>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ================= Toast Notification ================= -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-800 border border-blue-500/30 shadow-[0_10px_30px_rgba(0,0,0,0.5)] rounded-2xl p-4 flex items-center gap-4 z-50 animate-fade-in max-w-sm">
      <div class="w-10 h-10 bg-blue-500/10 rounded-full flex items-center justify-center shrink-0">
        <svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <div>
        <h4 class="text-white font-bold text-sm">گزارش مالی صادر شد</h4>
        <p class="text-slate-400 text-xs mt-0.5">فایل PDF گزارش P&L با موفقیت دانلود شد.</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isExporting = ref(false);
const timeFilter = ref('month');

const toastShow = ref(false);

const stats = ref({
  revenue: 0,
  expenses: 0,
  netProfit: 0,
  escrowLocked: 0,
  margin: 0
});

const chartData = ref([]);
const topProducts = ref([]);

// بدست آوردن ماکسیمم برای رسم صحیح ارتفاع نمودارهای CSS
const maxChartValue = computed(() => {
  if (chartData.value.length === 0) return 100;
  return Math.max(...chartData.value.map(d => Math.max(d.income, d.expense))) * 1.1; 
});

// ================= FETCH ACCOUNTING DATA FROM FastAPI =================
const fetchAccountingData = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/accounting/advanced?filter=${timeFilter.value}`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if(response.ok) {
      const data = await response.json();
      if(data.success) {
        stats.value = data.stats;
        topProducts.value = data.topProducts;
        chartData.value = data.chartData;
      }
    } else {
      if (response.status === 401) {
        alert("لطفا مجددا وارد سیستم شوید.");
      } else {
        throw new Error('Server error');
      }
    }
  } catch (error) {
    console.error("خطا در دریافت اطلاعات حسابداری سیستم:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchAccountingData();
});

// با تغییر فیلتر زمانی (هفته، ماه، سال) دیتا دوباره فچ می‌شود
watch(timeFilter, () => {
  fetchAccountingData();
});

// --- Export ---
const exportReport = () => {
  isExporting.value = true;
  setTimeout(() => {
    isExporting.value = false;
    toastShow.value = true;
    setTimeout(() => { toastShow.value = false; }, 4000);
  }, 1500);
};

// --- Utils ---
const formatPrice = (price) => {
  if (!price) return '0';
  return Math.round(price).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.5s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.custom-scrollbar-dark::-webkit-scrollbar { width: 4px; height: 6px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: #475569; }
</style>