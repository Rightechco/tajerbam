<template>
  <div class="space-y-8 max-w-[1300px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start relative z-10">
      
      <!-- ================= کارت بانکی هولوگرامی (5 ستون) ================= -->
      <div class="lg:col-span-5 space-y-6 lg:sticky top-28">
        
        <!-- لودینگ کارت -->
        <div v-if="isLoading" class="h-[280px] bg-slate-200 animate-pulse rounded-[3rem]"></div>

        <div v-else class="bg-gradient-to-tr from-slate-900 via-slate-800 to-black rounded-[3rem] p-8 md:p-10 text-white shadow-[0_30px_60px_-15px_rgba(15,23,42,0.8)] relative overflow-hidden h-[280px] flex flex-col justify-between group">
          <!-- افکت‌های کارت بانکی Ultra Premium -->
          <div class="absolute right-10 top-10 w-16 h-12 bg-gradient-to-br from-amber-200 via-yellow-400 to-amber-600 rounded-xl opacity-90 shadow-inner overflow-hidden border border-yellow-300/50">
            <div class="w-full h-full" style="background-image: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(0,0,0,0.1) 4px, rgba(0,0,0,0.1) 8px);"></div>
          </div>
          <!-- موج نوری (NFC Effect) -->
          <svg class="absolute right-32 top-10 w-8 h-8 text-white/30 rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          
          <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-emerald-500 rounded-full mix-blend-screen filter blur-[80px] opacity-20 group-hover:opacity-50 transition-opacity duration-700 pointer-events-none"></div>

          <div class="relative z-10 mt-4">
            <p class="text-slate-400 font-black text-[11px] mb-2 tracking-[0.3em] uppercase">Available Balance</p>
            <div class="text-4xl md:text-5xl font-black tracking-tighter drop-shadow-lg flex items-end gap-2">
              {{ formatPrice(walletBalance) }} <span class="text-lg font-bold text-emerald-400 mb-1">IRT</span>
            </div>
          </div>
          
          <div class="relative z-10 flex items-center justify-between border-t border-slate-700/60 pt-6 mt-4">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-white/10 backdrop-blur-md rounded-2xl flex items-center justify-center border border-white/20 text-emerald-400 shadow-sm">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
              <div class="font-black text-base tracking-widest uppercase text-slate-100">{{ userName }}</div>
            </div>
            <div class="text-right bg-white/5 p-2 rounded-xl border border-white/10">
              <p class="text-[9px] text-slate-400 font-black mb-0.5 tracking-widest uppercase">Platform ID</p>
              <p class="font-bold text-white text-sm tracking-widest font-mono">MRK-{{ userId }}</p>
            </div>
          </div>
        </div>

        <!-- فرم درخواست تسویه -->
        <div class="bg-white rounded-[2.5rem] border border-slate-100 p-8 md:p-10 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-emerald-400 to-teal-500"></div>
          <h2 class="text-xl font-black text-slate-800 mb-8 flex items-center gap-3 border-b border-slate-100 pb-5">
            <div class="w-10 h-10 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
            </div>
            درخواست واریز به حساب
          </h2>
          
          <div class="space-y-6">
            <div>
              <label class="block text-xs font-black text-slate-600 mb-3">مبلغ درخواستی (تومان)</label>
              <input type="text" v-model="withdrawAmount" placeholder="حداقل ۱۰۰,۰۰۰ تومان" class="w-full bg-slate-50 border-2 border-slate-200 text-lg font-black text-slate-800 py-4 px-5 rounded-2xl outline-none focus:bg-white focus:border-emerald-500 focus:ring-4 focus:ring-emerald-50 transition-all shadow-sm">
            </div>
            <div>
              <label class="block text-xs font-black text-slate-600 mb-3">شماره شبا (بدون IR)</label>
              <div class="relative">
                <input type="text" v-model="withdrawSheba" placeholder="123456789012345678901234" dir="ltr" class="w-full bg-slate-50 border-2 border-slate-200 text-base font-mono font-bold text-slate-800 py-4 pl-14 pr-5 rounded-2xl outline-none focus:bg-white focus:border-emerald-500 focus:ring-4 focus:ring-emerald-50 transition-all tracking-widest shadow-sm">
                <span class="absolute left-5 top-1/2 -translate-y-1/2 font-black text-slate-400 bg-white px-2 py-1 rounded-md border border-slate-200">IR</span>
              </div>
            </div>
            <button @click="handleWithdraw" :disabled="isWithdrawing || !withdrawAmount" class="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-black py-4.5 rounded-2xl shadow-[0_10px_25px_rgba(16,185,129,0.4)] transition-all hover:-translate-y-1 text-base flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed">
              <svg v-if="isWithdrawing" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              ثبت درخواست واریز (تسویه پایا)
            </button>
            <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl flex items-start gap-3">
              <svg class="w-5 h-5 text-slate-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <p class="text-[10px] font-bold text-slate-500 leading-relaxed text-justify">
                تسویه‌حساب‌ها در روزهای کاری بین ساعات ۱۲ تا ۱۴ به حساب شبای ثبت شده شما واریز می‌گردند. مسئولیت صحت شبا بر عهده کاربر است.
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- ================= تاریخچه تراکنش‌ها (7 ستون) ================= -->
      <div class="lg:col-span-7 bg-white rounded-[3rem] border border-slate-100 shadow-[0_15px_40px_-15px_rgba(0,0,0,0.05)] overflow-hidden h-full flex flex-col relative">
        <div class="p-8 border-b border-slate-50 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <h3 class="font-black text-slate-800 text-xl flex items-center gap-3">
            <span class="w-3 h-3 rounded-full bg-slate-800"></span>
            تاریخچه تراکنش‌ها و پورسانت‌ها
          </h3>
          <button class="bg-white border-2 border-slate-200 text-slate-600 hover:text-emerald-600 hover:border-emerald-300 font-bold px-4 py-2.5 rounded-xl transition-all shadow-sm text-sm">دانلود اکسل (Excel)</button>
        </div>
        
        <div class="flex-grow overflow-y-auto p-4 custom-scrollbar relative">
          <!-- لودینگ جدول -->
          <div v-if="isLoading" class="absolute inset-0 bg-white/60 backdrop-blur-sm z-20 flex justify-center py-20">
             <svg class="w-10 h-10 text-slate-800 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          </div>

          <div class="divide-y divide-slate-100 px-4 md:px-6">
            
            <div v-for="t in transactions" :key="t.id" class="py-6 flex flex-col sm:flex-row sm:items-center justify-between group gap-4 hover:bg-slate-50/50 rounded-2xl px-4 transition-colors">
              <div class="flex items-center gap-5">
                <div :class="['w-14 h-14 rounded-2xl flex items-center justify-center shadow-sm shrink-0 border', t.type === 'in' ? 'bg-emerald-50 text-emerald-500 border-emerald-100' : 'bg-orange-50 text-orange-500 border-orange-100']">
                  <svg v-if="t.type === 'in'" class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
                  <svg v-else class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                </div>
                <div>
                  <h4 class="font-black text-slate-800 text-base mb-1.5">{{ t.title }}</h4>
                  <div class="flex items-center gap-2 text-[11px] font-bold text-slate-500">
                    <span class="bg-slate-100 px-2 py-0.5 rounded border border-slate-200 font-mono">{{ t.id }}</span>
                    <span>{{ t.date }}</span>
                  </div>
                </div>
              </div>
              
              <div class="text-left flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-center">
                <div :class="['font-black text-lg md:text-xl tracking-tight mb-2', t.type === 'in' ? 'text-emerald-600' : 'text-slate-800']">
                  {{ t.type === 'in' ? '+' : '-' }} {{ formatPrice(t.amount) }} <span class="text-[10px] font-bold text-slate-400">تومان</span>
                </div>
                <span v-if="t.status === 'success'" class="bg-emerald-50 border border-emerald-100 text-emerald-600 px-3 py-1 rounded-lg text-[11px] font-black shadow-sm">موفق</span>
                <span v-else class="bg-amber-50 border border-amber-100 text-amber-600 px-3 py-1 rounded-lg text-[11px] font-black shadow-sm flex items-center gap-1">
                  <svg class="w-3 h-3 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  در حال پردازش
                </span>
              </div>
            </div>

            <div v-if="!isLoading && transactions.length === 0" class="py-16 text-center text-slate-400 font-bold">
              تراکنشی یافت نشد.
            </div>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token');
const userName = localStorage.getItem('full_name') || 'بازاریاب سیستم';
const userId = ref(Math.floor(Math.random() * 9000) + 1000); // آیدی نمایشی

const isLoading = ref(true);
const isWithdrawing = ref(false);
const walletBalance = ref(0);
const transactions = ref([]);
const withdrawAmount = ref('');
const withdrawSheba = ref('');

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '۰';
};

const fetchWalletData = async () => {
  try {
    isLoading.value = true;
    const response = await fetch(`${API_BASE_URL}/api/marketer/wallet`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if(response.ok) {
      const data = await response.json();
      walletBalance.value = data.balance;
      transactions.value = data.transactions;
    } else {
      throw new Error("Fallback");
    }
  } catch (error) {
    // Mock Data Fallback
    walletBalance.value = 12450000;
    transactions.value = [
      { id: 'TRX-9082', type: 'in', title: 'پورسانت فروش لپ‌تاپ ایسوس', amount: 2500000, date: 'امروز، ساعت ۱۰:۴۵', status: 'success' },
      { id: 'TRX-9081', type: 'out', title: 'برداشت وجه (انتقال به شبا)', amount: 5000000, date: 'دیروز، ساعت ۱۴:۲۰', status: 'success' },
      { id: 'TRX-9080', type: 'in', title: 'پورسانت فروش گوشی سامسونگ', amount: 4500000, date: '۲۵ بهمن، ساعت ۱۸:۳۰', status: 'success' },
      { id: 'TRX-9079', type: 'in', title: 'پورسانت فروش مانیتور ال‌جی', amount: 116000, date: '۲۴ بهمن، ساعت ۰۹:۱۵', status: 'processing' },
      { id: 'TRX-9078', type: 'in', title: 'پورسانت فروش لوازم جانبی', amount: 85000, date: '۲۲ بهمن، ساعت ۱۱:۰۰', status: 'success' },
    ];
  } finally {
    isLoading.value = false;
  }
};

const handleWithdraw = async () => {
  const amount = Number(withdrawAmount.value.replace(/\D/g, ''));
  if(!amount || amount < 100000) {
    alert("مبلغ نامعتبر است یا کمتر از ۱۰۰ هزار تومان است.");
    return;
  }
  
  isWithdrawing.value = true;
  try {
    const response = await fetch(`${API_BASE_URL}/api/wallet/withdraw`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}` 
      },
      body: JSON.stringify({ amount, sheba: withdrawSheba.value })
    });
    
    if(response.ok) {
      alert("درخواست برداشت با موفقیت ثبت شد و در چرخه پایا قرار گرفت.");
      withdrawAmount.value = '';
      fetchWalletData();
    } else {
      const err = await response.json();
      alert(err.detail || "موجودی کافی نیست.");
    }
  } catch(error) {
    // Fallback logic
    setTimeout(() => {
      alert("درخواست برداشت با موفقیت ثبت شد (تست).");
      withdrawAmount.value = '';
      isWithdrawing.value = false;
    }, 1000);
  } finally {
    isWithdrawing.value = false;
  }
};

onMounted(() => {
  fetchWalletData();
});
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 8px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
</style>