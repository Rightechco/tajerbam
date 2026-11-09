<template>
  <div class="space-y-8 max-w-[1200px] mx-auto pb-16 font-sans text-slate-800" dir="rtl">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- ================= کارت اعتباری شرکتی ================= -->
      <div class="lg:col-span-5 space-y-6 lg:sticky top-28">
        
        <div class="bg-gradient-to-tr from-violet-950 via-indigo-900 to-slate-900 rounded-[3rem] p-8 md:p-10 text-white shadow-[0_30px_60px_-15px_rgba(76,29,149,0.5)] relative overflow-hidden h-[260px] flex flex-col justify-between group">
          <div class="absolute right-10 top-10 w-14 h-10 bg-gradient-to-br from-yellow-200 via-yellow-400 to-yellow-600 rounded-lg opacity-90 shadow-inner overflow-hidden border border-yellow-300/50"></div>
          
          <div v-if="isLoading" class="absolute inset-0 bg-slate-900/50 flex justify-center items-center z-20">
            <svg class="w-8 h-8 text-white animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          </div>

          <div class="relative z-10 mt-2">
            <p class="text-violet-200 font-black text-[10px] mb-1 tracking-[0.2em] uppercase">موجودی کیف پول شرکتی</p>
            <div class="text-4xl md:text-5xl font-black tracking-tighter drop-shadow-lg flex items-end gap-2">
              {{ formatPrice(walletBalance) }} <span class="text-base font-bold text-fuchsia-400 mb-1">تومان</span>
            </div>
          </div>
        </div>

        <!-- فرم شارژ حساب -->
        <div class="bg-white rounded-[2rem] border border-slate-100 p-8 shadow-[0_8px_30px_rgb(0,0,0,0.03)]">
          <h2 class="text-lg font-black text-slate-800 mb-6 flex items-center gap-2 border-b border-slate-100 pb-4">
            <span class="w-2.5 h-2.5 rounded-full bg-violet-500"></span>
            افزایش اعتبار کیف پول
          </h2>
          
          <div class="space-y-5">
            <div>
              <label class="block text-xs font-bold text-slate-500 mb-2">مبلغ شارژ (تومان)</label>
              <input type="text" v-model="chargeAmount" placeholder="مثلاً: ۱۰۰,۰۰۰,۰۰۰" class="w-full bg-slate-50 border border-slate-200 text-lg font-black text-slate-800 py-3.5 px-5 rounded-xl outline-none focus:border-violet-400 transition-all text-left" dir="ltr">
            </div>
            
            <button @click="chargeWallet" :disabled="isCharging || !chargeAmount" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(0,0,0,0.15)] transition-all text-sm flex items-center justify-center gap-2 disabled:opacity-50">
              <svg v-if="isCharging" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              {{ isCharging ? 'در حال اتصال به درگاه...' : 'شارژ کیف پول' }}
            </button>
          </div>
        </div>
      </div>

      <!-- ================= تاریخچه مالی ================= -->
      <div class="lg:col-span-7 bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] overflow-hidden h-full flex flex-col">
        <div class="p-6 md:p-8 border-b border-slate-50 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            تراکنش‌ها و فاکتورهای پرداختی
          </h3>
        </div>
        
        <div class="flex-grow overflow-y-auto p-2 custom-scrollbar">
          <div v-if="isLoading" class="flex justify-center py-10"><svg class="w-8 h-8 text-violet-600 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg></div>
          
          <div class="divide-y divide-slate-100 px-4 md:px-6">
            <div v-for="t in transactions" :key="t.id" class="py-5 flex items-center justify-between group">
              <div class="flex items-center gap-4">
                <div :class="['w-12 h-12 rounded-[1rem] flex items-center justify-center shadow-sm', t.type === 'in' ? 'bg-emerald-50 text-emerald-600 border border-emerald-100' : 'bg-rose-50 text-rose-600 border border-rose-100']">
                  <svg v-if="t.type === 'in'" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                  <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path></svg>
                </div>
                <div>
                  <h4 class="font-black text-slate-800 text-sm mb-1 group-hover:text-violet-700 transition-colors">{{ t.title }}</h4>
                  <p class="text-[10px] font-bold text-slate-400">{{ t.date }} • {{ t.id }}</p>
                </div>
              </div>
              <div class="text-left flex flex-col items-end">
                <div :class="['font-black text-base md:text-lg tracking-tight mb-1.5', t.type === 'in' ? 'text-emerald-600' : 'text-slate-800']">
                  {{ t.type === 'in' ? '+' : '-' }} {{ formatPrice(t.amount) }} <span class="text-[10px] font-bold text-slate-400">تومان</span>
                </div>
              </div>
            </div>
            
            <div v-if="!isLoading && transactions.length === 0" class="text-center text-slate-500 py-10 font-bold">تراکنشی ثبت نشده است.</div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = localStorage.getItem('access_token') || 'test-token';

const isLoading = ref(true);
const isCharging = ref(false);
const walletBalance = ref(0);
const transactions = ref([]);
const chargeAmount = ref('');

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '۰';
};

const fetchWallet = async () => {
  try {
    isLoading.value = true;
    const response = await fetch(`${API_BASE}/api/buyer/wallet`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if(response.ok) {
      const data = await response.json();
      walletBalance.value = data.balance;
      transactions.value = data.transactions;
    }
  } catch (error) {
    console.error("Error fetching wallet data:", error);
  } finally {
    isLoading.value = false;
  }
};

const chargeWallet = async () => {
  // پاک‌سازی فرمت و تبدیل به عدد
  const rawAmount = Number(chargeAmount.value.replace(/\D/g, ''));
  if(!rawAmount || rawAmount <= 0) return;

  try {
    isCharging.value = true;
    const response = await fetch(`${API_BASE}/api/buyer/wallet/charge`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ amount: rawAmount })
    });
    
    if(response.ok) {
      const data = await response.json();
      alert(data.message);
      chargeAmount.value = '';
      fetchWallet(); // بارگذاری مجدد اطلاعات کیف پول و تراکنش‌ها
    }
  } catch (error) {
    console.error("Error charging wallet:", error);
  } finally {
    isCharging.value = false;
  }
};

onMounted(() => {
  fetchWallet();
});
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
</style>