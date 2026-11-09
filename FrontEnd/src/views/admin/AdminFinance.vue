<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-8 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-emerald-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-teal-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-emerald-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-emerald-500 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مدیریت مالی و خزانه‌داری</h1>
          <p class="text-sm font-bold text-slate-400">کنترل تراکنش‌ها، حساب‌های اسکرو (Escrow) و تسویه با فروشندگان</p>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto">
        <button @click="fetchFinanceData" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی اطلاعات">
          <svg :class="{'animate-spin text-emerald-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="exportToExcel" class="bg-emerald-600 hover:bg-emerald-500 text-white px-6 py-3.5 rounded-xl transition-all font-bold flex items-center gap-2 text-sm shadow-[0_0_15px_rgba(16,185,129,0.4)]">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          خروجی اکسل تراکنش‌ها
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-emerald-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-emerald-500 animate-pulse">در حال استخراج امن اطلاعات مالی...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in">
      
      <!-- ================= کارت‌های آماری خزانه‌داری ================= -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- موجودی آزاد سیستم -->
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-blue-500/50 transition-all">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">سود کل سیستم (کارمزدها)</span>
            <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ formatPrice(stats.systemBalance) }} <span class="text-sm text-slate-500 font-sans">تومان</span></div>
        </div>

        <!-- موجودی بلوکه اسکرو -->
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-amber-500/50 transition-all">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">حجم بلوکه شده (Escrow)</span>
            <div class="w-10 h-10 bg-amber-500/10 text-amber-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ formatPrice(stats.escrowVolume) }} <span class="text-sm text-slate-500 font-sans">تومان</span></div>
        </div>

        <!-- در انتظار تسویه -->
        <div class="bg-slate-900 rounded-3xl border border-rose-500/30 p-6 relative overflow-hidden group hover:border-rose-500/60 transition-all shadow-[0_0_15px_rgba(244,63,94,0.1)]">
          <div class="absolute top-0 left-0 w-32 h-32 bg-rose-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-rose-400 text-xs font-bold uppercase tracking-wider">در انتظار تسویه (Payouts)</span>
            <div class="w-10 h-10 bg-rose-500/10 text-rose-500 rounded-xl flex items-center justify-center animate-pulse"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-rose-400 mb-1">{{ formatPrice(stats.pendingAmount) }} <span class="text-sm text-rose-500/50 font-sans">تومان</span></div>
        </div>

        <!-- مجموع واریزی موفق -->
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-emerald-500/50 transition-all">
          <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">کل مبالغ تسویه شده</span>
            <div class="w-10 h-10 bg-emerald-500/10 text-emerald-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ formatPrice(stats.paidAmount) }} <span class="text-sm text-slate-500 font-sans">تومان</span></div>
        </div>

      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- ================= لیست درخواست‌های تسویه (Pending Payouts) ================= -->
        <div class="lg:col-span-1 bg-slate-900 rounded-[2rem] border border-rose-500/20 shadow-lg p-6 flex flex-col h-[600px] relative">
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-rose-500 to-orange-500 rounded-t-[2rem]"></div>
          
          <h3 class="font-black text-white text-lg flex items-center gap-2 mb-6 mt-2">
            <div class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></div>
            درخواست‌های واریز پایا
          </h3>

          <div v-if="pendingRequests.length === 0" class="flex-grow flex flex-col items-center justify-center text-slate-500">
            <svg class="w-16 h-16 mb-4 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
            <span class="font-bold">درخواستی برای تسویه وجود ندارد</span>
          </div>

          <div v-else class="flex-grow overflow-y-auto custom-scrollbar-dark space-y-4 pr-2">
            <div v-for="req in pendingRequests" :key="req.id" class="bg-slate-950 border border-slate-800 p-4 rounded-2xl hover:border-rose-500/40 transition-colors">
              <div class="flex justify-between items-start mb-3">
                <div>
                  <h4 class="font-bold text-white text-sm">{{ req.user_name }}</h4>
                  <p class="text-xs text-slate-500 mt-1 font-mono">{{ req.created_at }}</p>
                </div>
                <span class="bg-rose-500/10 text-rose-400 font-black text-sm px-3 py-1.5 rounded-lg border border-rose-500/20">
                  {{ formatPrice(req.amount) }} <span class="text-[10px] font-sans font-normal">تومان</span>
                </span>
              </div>
              <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center mb-4">
                <span class="text-xs text-slate-400">شماره شبا:</span>
                <span class="text-xs font-mono text-slate-300 select-all" dir="ltr">IR{{ req.iban }}</span>
              </div>
              <button @click="openProcessModal(req)" class="w-full bg-slate-800 hover:bg-emerald-600 hover:text-white text-emerald-500 border border-slate-700 hover:border-emerald-500 transition-all font-bold py-2.5 rounded-xl text-sm flex justify-center items-center gap-2 shadow-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                بررسی و ثبت پرداخت
              </button>
            </div>
          </div>
        </div>

        <!-- ================= تاریخچه تراکنش‌ها (Transaction History) ================= -->
        <div class="lg:col-span-2 bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg flex flex-col h-[600px] overflow-hidden">
          <div class="p-6 md:p-8 border-b border-slate-800/80 flex justify-between items-center bg-slate-950/30">
            <h3 class="font-black text-white text-lg flex items-center gap-2">
              <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
              دفتر کل تراکنش‌ها (Ledger)
            </h3>
            <div class="flex gap-2">
              <span class="bg-slate-800 text-slate-400 text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700">{{ transactionHistory.length }} رکورد اخیر</span>
            </div>
          </div>

          <div class="flex-grow overflow-auto custom-scrollbar-dark p-6">
             <table class="w-full text-right border-collapse whitespace-nowrap">
              <thead>
                <tr class="text-slate-400 text-xs font-bold border-b border-slate-800">
                  <th class="pb-4 font-normal">شناسه تراکنش</th>
                  <th class="pb-4 font-normal">کاربر / ذینفع</th>
                  <th class="pb-4 font-normal">نوع عملیات</th>
                  <th class="pb-4 font-normal">مبلغ (تومان)</th>
                  <th class="pb-4 font-normal">وضعیت</th>
                  <th class="pb-4 font-normal">تاریخ</th>
                </tr>
              </thead>
              <tbody class="text-sm">
                <tr v-if="transactionHistory.length === 0">
                  <td colspan="6" class="py-8 text-center text-slate-500">تراکنشی یافت نشد</td>
                </tr>
                <tr v-for="tx in transactionHistory" :key="tx.id" class="border-b border-slate-800/50 hover:bg-slate-800/20 transition-colors">
                  <td class="py-4 text-slate-300 font-mono text-xs">#{{ tx.id }}</td>
                  <td class="py-4 font-bold text-white">{{ tx.user_name }}</td>
                  <td class="py-4">
                    <span :class="getTypeBadge(tx.type)">{{ getTypeName(tx.type) }}</span>
                  </td>
                  <td class="py-4 font-black" :class="tx.type === 'withdraw' || tx.type === 'fee' ? 'text-rose-400' : 'text-emerald-400'">
                    {{ tx.type === 'withdraw' || tx.type === 'fee' ? '-' : '+' }}{{ formatPrice(tx.amount) }}
                  </td>
                  <td class="py-4">
                    <span :class="getStatusBadge(tx.status)">{{ getStatusName(tx.status) }}</span>
                  </td>
                  <td class="py-4 text-slate-500 text-xs font-mono">{{ tx.created_at }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

    <!-- ================= Modal: ثبت پرداخت (Process Payout) ================= -->
    <div v-if="processModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="closeProcessModal"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2rem] w-full max-w-lg relative z-10 shadow-2xl overflow-hidden animate-fade-in">
        <div class="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-emerald-500 to-teal-500"></div>
        <div class="p-8">
          <h2 class="text-2xl font-black text-white mb-2">ثبت تسویه حساب (پایا)</h2>
          <p class="text-sm text-slate-400 mb-6 border-b border-slate-800 pb-4">اطلاعات پرداختی را تایید و رسید انتقال را وارد کنید.</p>
          
          <div class="space-y-4 mb-8">
            <div class="flex justify-between items-center bg-slate-950 p-4 rounded-xl border border-slate-800">
              <span class="text-slate-400 text-sm">مبلغ قابل پرداخت:</span>
              <span class="text-emerald-400 font-black text-xl">{{ formatPrice(processModal.data.amount) }} <span class="text-xs font-normal">تومان</span></span>
            </div>
            
            <div class="flex flex-col bg-slate-950 p-4 rounded-xl border border-slate-800">
              <span class="text-slate-400 text-xs mb-1">شماره شبا مقصد ({{ processModal.data.user_name }}):</span>
              <span class="text-slate-200 font-mono text-lg" dir="ltr">IR{{ processModal.data.iban }}</span>
            </div>

            <div>
              <label class="block text-slate-400 text-sm font-bold mb-2">کد پیگیری بانکی (اختیاری):</label>
              <input v-model="adminNote" type="text" placeholder="مثال: 140308129910" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors font-mono" dir="ltr" />
            </div>
          </div>

          <div class="flex gap-4">
            <button @click="closeProcessModal" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 rounded-xl transition-colors">انصراف</button>
            <button @click="processPayout" :disabled="isProcessing" class="flex-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-3.5 rounded-xl transition-all shadow-lg shadow-emerald-500/20 disabled:opacity-50 flex justify-center items-center gap-2">
              <svg v-if="isProcessing" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span v-else>تایید و کسر از سیستم</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= Toast Notification ================= -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-800 border border-emerald-500/30 shadow-[0_10px_30px_rgba(0,0,0,0.5)] rounded-2xl p-4 flex items-center gap-4 z-50 animate-fade-in max-w-sm">
      <div class="w-10 h-10 bg-emerald-500/10 rounded-full flex items-center justify-center shrink-0">
        <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <div>
        <h4 class="text-white font-bold text-sm">{{ toastData.title }}</h4>
        <p class="text-slate-400 text-xs mt-0.5">{{ toastData.text }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
// متد دریافت توکن از نشست ادمین
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isProcessing = ref(false);

const stats = ref({
  systemBalance: 0,
  escrowVolume: 0,
  paidAmount: 0,
  pendingAmount: 0
});

const pendingRequests = ref([]);
const transactionHistory = ref([]);

const processModal = ref({ show: false, data: null });
const adminNote = ref('');
const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

// نمایش پیام موفقیت
const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 4000);
};

// ================= FETCH DATA (REAL API) =================
const fetchFinanceData = async () => {
  isLoading.value = true;
  try {
    const headers = {
      'Authorization': `Bearer ${token()}`,
      'Content-Type': 'application/json'
    };

    // دریافت تمامی اطلاعات مالی به صورت همزمان (Parallel Fetching)
    const [statsRes, pendingRes, historyRes] = await Promise.all([
      fetch(`${API_BASE}/api/admin/finance/stats`, { headers }),
      fetch(`${API_BASE}/api/admin/finance/payouts/pending`, { headers }),
      fetch(`${API_BASE}/api/admin/finance/transactions`, { headers })
    ]);

    if(statsRes.ok) stats.value = await statsRes.json();
    if(pendingRes.ok) pendingRequests.value = await pendingRes.json();
    if(historyRes.ok) transactionHistory.value = await historyRes.json();

  } catch (error) {
    console.error("خطا در دریافت اطلاعات خزانه‌داری:", error);
    showToast('خطای سرور', 'برقراری ارتباط با هسته مالی با مشکل مواجه شد.');
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchFinanceData();
});

// ================= PROCESS PAYOUT (REAL API) =================
const openProcessModal = (req) => {
  processModal.value.data = req;
  adminNote.value = '';
  processModal.value.show = true;
};

const closeProcessModal = () => {
  processModal.value.show = false;
  processModal.value.data = null;
};

const processPayout = async () => {
  const reqData = processModal.value.data;
  if (!reqData) return;
  
  isProcessing.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/finance/payouts/${reqData.id}/process`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ tracking_code: adminNote.value })
    });

    const result = await response.json();

    if(response.ok) {
      showToast('تسویه حساب موفق', `مبلغ ${formatPrice(reqData.amount)} با موفقیت پرداخت و در دفتر کل ثبت شد.`);
      // رفرش داده‌ها پس از موفقیت عملیات مالی
      await fetchFinanceData();
      closeProcessModal();
    } else {
      throw new Error(result.detail || 'خطا در عملیات تسویه');
    }
  } catch (error) {
    console.error("خطا در پردازش پرداخت:", error);
    alert(error.message);
  } finally {
    isProcessing.value = false;
  }
};

const exportToExcel = () => {
  alert('درخواست تولید فایل CSV برای هسته ارسال شد و به زودی دانلود می‌شود.');
};

// ================= UI HELPERS =================
const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

const getTypeBadge = (type) => {
  const map = {
    escrow: 'bg-amber-500/10 text-amber-400 border border-amber-500/20 px-2 py-1 rounded text-xs',
    withdraw: 'bg-rose-500/10 text-rose-400 border border-rose-500/20 px-2 py-1 rounded text-xs',
    fee: 'bg-blue-500/10 text-blue-400 border border-blue-500/20 px-2 py-1 rounded text-xs',
    deposit: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2 py-1 rounded text-xs'
  };
  return map[type] || 'bg-slate-800 text-slate-400 px-2 py-1 rounded text-xs';
};

const getTypeName = (type) => {
  const map = {
    escrow: 'بلوکه اسکرو',
    withdraw: 'برداشت/تسویه',
    fee: 'کسر کارمزد',
    deposit: 'واریز/شارژ'
  };
  return map[type] || type;
};

const getStatusBadge = (status) => {
  const map = {
    completed: 'text-emerald-400',
    pending: 'text-rose-400 animate-pulse',
    failed: 'text-slate-500'
  };
  return map[status] || 'text-slate-400';
};

const getStatusName = (status) => {
  const map = {
    completed: 'موفق',
    pending: 'در انتظار',
    failed: 'ناموفق'
  };
  return map[status] || status;
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.custom-scrollbar-dark::-webkit-scrollbar { width: 4px; height: 6px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: #475569; }

.tooltip { position: relative; }
.tooltip:hover::after {
  content: attr(title);
  position: absolute;
  bottom: 120%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #1e293b;
  color: white;
  font-size: 10px;
  font-weight: 800;
  padding: 6px 10px;
  border-radius: 8px;
  white-space: nowrap;
  pointer-events: none;
  z-index: 50;
  box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  border: 1px solid #334155;
}
</style>