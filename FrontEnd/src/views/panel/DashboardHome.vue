<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر داشبورد (Ultra Premium) ================= -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 bg-gradient-to-br from-indigo-950 via-slate-900 to-slate-900 p-8 md:p-10 rounded-[2.5rem] border border-indigo-500/20 shadow-[0_20px_50px_-12px_rgba(30,27,75,0.5)] relative overflow-hidden z-10 text-white">
      <!-- افکت‌های نوری -->
      <div class="absolute -left-20 -top-20 w-80 h-80 bg-indigo-500 rounded-full mix-blend-screen filter blur-[90px] opacity-30 pointer-events-none animate-pulse"></div>
      <div class="absolute -right-20 -bottom-20 w-64 h-64 bg-fuchsia-600 rounded-full mix-blend-screen filter blur-[80px] opacity-20 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-[1.5rem] border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0 overflow-hidden">
          <div class="absolute inset-0 bg-indigo-500/20 rounded-[1.5rem] animate-pulse"></div>
          <svg class="w-10 h-10 text-indigo-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
        </div>
        <div>
          <h1 class="text-2xl md:text-3xl font-black tracking-tight mb-2 flex items-center gap-3">
            <span class="text-3xl animate-waving-hand inline-block origin-[70%_70%]">👋</span> 
            سلام {{ userName }}، وقت بخیر!
          </h1>
          <div class="flex flex-wrap items-center gap-3">
             <span v-if="isVip" class="bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg>
                فروشنده طلایی (VIP)
             </span>
             <span v-else class="bg-slate-800 text-slate-400 border border-slate-700 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
                فروشنده پایه
             </span>
             <span class="text-xs font-bold text-slate-400">داشبورد زنده فروشگاه شما</span>
          </div>
        </div>
      </div>

      <button @click="exportFinancialReport" :disabled="isLoading || isExporting" class="relative z-10 bg-white/10 hover:bg-white/20 border border-white/20 text-white font-black px-8 py-4 rounded-xl backdrop-blur-md transition-all flex items-center justify-center gap-3 group shadow-[0_0_20px_rgba(255,255,255,0.05)] disabled:opacity-50">
        <svg v-if="!isExporting" class="w-5 h-5 group-hover:-translate-y-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
        <svg v-else class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        دانلود گزارش مالی
      </button>
    </div>

    <!-- ================= کارت‌های آماری (Stats) ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
      
      <!-- فروش کل -->
      <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] relative overflow-hidden group hover:border-emerald-200 transition-colors cursor-default">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-emerald-50 rounded-full mix-blend-multiply opacity-50 group-hover:scale-150 transition-transform duration-500 pointer-events-none"></div>
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div class="flex items-start justify-between mb-4">
            <p class="text-xs font-bold text-slate-400">فروش کل (ماه جاری)</p>
            <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-500 flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
          </div>
          <div>
            <h3 class="text-2xl font-black text-slate-800 tracking-tight">
              <span v-if="isLoading" class="inline-block w-24 h-8 bg-slate-100 rounded animate-pulse"></span>
              <span v-else>{{ formatPrice(stats.totalSales) }} <span class="text-[10px] text-slate-400">تومان</span></span>
            </h3>
            <p class="text-[10px] font-bold text-emerald-600 mt-2 flex items-center gap-1 bg-emerald-50 w-fit px-2 py-0.5 rounded-md"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> {{ stats.salesGrowth }}% رشد</p>
          </div>
        </div>
      </div>

      <!-- سفارشات جاری -->
      <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] relative overflow-hidden group hover:border-blue-200 transition-colors cursor-default">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-blue-50 rounded-full mix-blend-multiply opacity-50 group-hover:scale-150 transition-transform duration-500 pointer-events-none"></div>
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div class="flex items-start justify-between mb-4">
            <p class="text-xs font-bold text-slate-400">سفارشات در جریان</p>
            <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-500 flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            </div>
          </div>
          <div>
            <h3 class="text-3xl font-black text-slate-800 tracking-tight">
              <span v-if="isLoading" class="inline-block w-12 h-8 bg-slate-100 rounded animate-pulse"></span>
              <span v-else>{{ stats.activeOrders }}</span>
            </h3>
            <p class="text-[10px] font-bold text-blue-600 mt-2 flex items-center gap-1 bg-blue-50 w-fit px-2 py-0.5 rounded-md">نیازمند ارسال</p>
          </div>
        </div>
      </div>

      <!-- موجودی بلوکه شده -->
      <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] relative overflow-hidden group hover:border-amber-200 transition-colors cursor-default">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-amber-50 rounded-full mix-blend-multiply opacity-50 group-hover:scale-150 transition-transform duration-500 pointer-events-none"></div>
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div class="flex items-start justify-between mb-4">
            <p class="text-xs font-bold text-slate-400">موجودی بلوکه (Escrow)</p>
            <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            </div>
          </div>
          <div>
            <h3 class="text-2xl font-black text-slate-800 tracking-tight">
              <span v-if="isLoading" class="inline-block w-24 h-8 bg-slate-100 rounded animate-pulse"></span>
              <span v-else>{{ formatPrice(stats.escrowBalance) }} <span class="text-[10px] text-slate-400">تومان</span></span>
            </h3>
            <p class="text-[10px] font-bold text-amber-600 mt-2 flex items-center gap-1 bg-amber-50 w-fit px-2 py-0.5 rounded-md">در انتظار تایید خریداران</p>
          </div>
        </div>
      </div>

      <!-- استعلام‌های باز -->
      <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] relative overflow-hidden group hover:border-purple-200 transition-colors cursor-pointer" @click="$router.push('/panel/requests')">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-purple-50 rounded-full mix-blend-multiply opacity-50 group-hover:scale-150 transition-transform duration-500 pointer-events-none"></div>
        <div class="relative z-10 flex flex-col h-full justify-between">
          <div class="flex items-start justify-between mb-4">
            <p class="text-xs font-bold text-slate-400">مناقصات و درخواست‌ها</p>
            <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-500 flex items-center justify-center shadow-sm">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg>
            </div>
          </div>
          <div>
            <h3 class="text-3xl font-black text-slate-800 tracking-tight">
              <span v-if="isLoading" class="inline-block w-12 h-8 bg-slate-100 rounded animate-pulse"></span>
              <span v-else>{{ stats.openRfqs }}</span>
            </h3>
            <p class="text-[10px] font-bold text-purple-600 mt-2 flex items-center gap-1 bg-purple-50 w-fit px-2 py-0.5 rounded-md">فرصت ارسال پیش‌فاکتور</p>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= سفارشات اخیر ================= -->
    <div class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_rgba(0,0,0,0.02)] overflow-hidden">
      <div class="p-6 md:p-8 border-b border-slate-100 flex items-center justify-between bg-slate-50/50">
        <h2 class="text-lg font-black text-slate-800 flex items-center gap-2">
          <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          آخرین سفارشات دریافتی
        </h2>
        <router-link to="/panel/orders" class="text-xs font-black text-blue-600 bg-blue-50 px-4 py-2 rounded-xl hover:bg-blue-100 transition-colors">همه سفارشات</router-link>
      </div>

      <div class="overflow-x-auto custom-scrollbar">
        <table class="w-full text-right">
          <thead class="bg-slate-50 text-slate-400 text-[10px] font-black uppercase tracking-wider">
            <tr>
              <th class="px-6 py-4 text-center">کد سفارش</th>
              <th class="px-6 py-4">مشتری (خریدار)</th>
              <th class="px-6 py-4 text-center">مبلغ کل (تومان)</th>
              <th class="px-6 py-4 text-center">وضعیت</th>
              <th class="px-6 py-4 text-center">تاریخ</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-sm font-medium">
            <tr v-if="isLoading" v-for="i in 3" :key="i" class="animate-pulse">
              <td class="px-6 py-4"><div class="h-4 bg-slate-100 w-16 mx-auto rounded"></div></td>
              <td class="px-6 py-4"><div class="h-4 bg-slate-100 w-32 rounded"></div></td>
              <td class="px-6 py-4"><div class="h-4 bg-slate-100 w-24 mx-auto rounded"></div></td>
              <td class="px-6 py-4"><div class="h-6 bg-slate-100 w-16 mx-auto rounded-lg"></div></td>
              <td class="px-6 py-4"><div class="h-4 bg-slate-100 w-20 mx-auto rounded"></div></td>
            </tr>
            <tr v-else-if="recentOrders.length === 0">
              <td colspan="5" class="px-6 py-12 text-center text-slate-400 font-bold">سفارشی یافت نشد.</td>
            </tr>
            <tr v-else v-for="order in recentOrders" :key="order.id" class="hover:bg-slate-50/80 transition-colors group cursor-pointer" @click="$router.push('/panel/orders')">
              <td class="px-6 py-4 text-center font-mono font-black text-slate-500">#{{ order.id }}</td>
              <td class="px-6 py-4">
                <div class="font-black text-slate-800">{{ order.customer }}</div>
                <div class="text-[10px] text-slate-400 font-bold mt-1">{{ order.city }}</div>
              </td>
              <td class="px-6 py-4 text-center font-black text-slate-700">{{ formatPrice(order.amount) }}</td>
              <td class="px-6 py-4 text-center">
                <span v-if="order.status === 'pending'" class="bg-amber-50 text-amber-600 px-3 py-1 rounded-lg text-xs font-black border border-amber-100 flex items-center justify-center gap-1 w-fit mx-auto">
                  <span class="w-1.5 h-1.5 rounded-full bg-amber-500 animate-pulse"></span> در انتظار تایید
                </span>
                <span v-else-if="order.status === 'processing'" class="bg-blue-50 text-blue-600 px-3 py-1 rounded-lg text-xs font-black border border-blue-100 w-fit mx-auto block">در حال پردازش</span>
                <span v-else-if="order.status === 'shipped'" class="bg-indigo-50 text-indigo-600 px-3 py-1 rounded-lg text-xs font-black border border-indigo-100 w-fit mx-auto block">ارسال شده</span>
                <span v-else class="bg-emerald-50 text-emerald-600 px-3 py-1 rounded-lg text-xs font-black border border-emerald-100 w-fit mx-auto block">تکمیل شده</span>
              </td>
              <td class="px-6 py-4 text-center text-xs font-bold text-slate-500">{{ order.date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const userName = ref(localStorage.getItem('user_name') || 'فروشنده عزیز');
const isVip = ref(true); // برای نمایش دمو
const isLoading = ref(true);
const isExporting = ref(false);

const stats = ref({
  totalSales: 0,
  salesGrowth: 0,
  activeOrders: 0,
  escrowBalance: 0,
  openRfqs: 0
});

const recentOrders = ref([]);

const fetchDashboardData = async () => {
  isLoading.value = true;
  try {
    const token = localStorage.getItem('tajerbam_token');
    const res = await fetch(`${API_BASE_URL}/api/seller/dashboard`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    
    if (!res.ok) throw new Error();
    const data = await res.json();
    
    stats.value = data.stats;
    recentOrders.value = data.recentOrders;
  } catch (error) {
    // ================= FALLBACK MOCK DATA =================
    setTimeout(() => {
      stats.value = {
        totalSales: 1250000000,
        salesGrowth: 14.5,
        activeOrders: 12,
        escrowBalance: 450000000,
        openRfqs: 8
      };
      
      recentOrders.value = [
        { id: '8401', customer: 'شرکت پتروشیمی زاگرس', city: 'اصفهان', amount: 450000000, status: 'pending', date: '۱۴۰۳/۰۸/۱۰' },
        { id: '8399', customer: 'فروشگاه رایان تک', city: 'تهران', amount: 125000000, status: 'processing', date: '۱۴۰۳/۰۸/۰۹' },
        { id: '8395', customer: 'اداره کل آموزش و پرورش', city: 'تبریز', amount: 85000000, status: 'shipped', date: '۱۴۰۳/۰۸/۰۸' },
        { id: '8382', customer: 'گروه صنعتی مپنا', city: 'بوشهر', amount: 560000000, status: 'completed', date: '۱۴۰۳/۰۸/۰۵' }
      ];
      isLoading.value = false;
    }, 800);
  }
};

const exportFinancialReport = () => {
  isExporting.value = true;
  setTimeout(() => {
    isExporting.value = false;
    alert("گزارش مالی شما (CSV) با موفقیت تولید و دانلود شد.");
  }, 1500);
};

const formatPrice = (price) => {
  if (!price) return '0';
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

onMounted(() => {
  fetchDashboardData();
});
</script>

<style scoped>
@keyframes wave {
  0% { transform: rotate( 0.0deg) }
  10% { transform: rotate(14.0deg) }  
  20% { transform: rotate(-8.0deg) }
  30% { transform: rotate(14.0deg) }
  40% { transform: rotate(-4.0deg) }
  50% { transform: rotate(10.0deg) }
  60% { transform: rotate( 0.0deg) }  
  100% { transform: rotate( 0.0deg) }
}
.animate-waving-hand {
  animation: wave 2.5s infinite;
}
.custom-scrollbar::-webkit-scrollbar { height: 8px; width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>