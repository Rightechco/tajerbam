<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-amber-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-rose-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-amber-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-amber-500 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مدیریت سفارشات و داوری</h1>
          <p class="text-sm font-bold text-slate-400">پایش لجستیک، تغییر وضعیت سفارشات و مرکز حل اختلاف (Escrow)</p>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto">
        <div class="relative w-full md:w-64">
          <input v-model="searchQuery" type="text" placeholder="جستجوی شماره سفارش..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 pr-11 rounded-xl focus:outline-none focus:border-amber-500 transition-colors text-sm font-medium">
          <svg class="w-5 h-5 text-slate-500 absolute right-4 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        
        <button @click="fetchData" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی اطلاعات">
          <svg :class="{'animate-spin text-amber-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-amber-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-amber-500 animate-pulse">در حال ارتباط با پایگاه داده سفارشات...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in">
      
      <!-- ================= کارت‌های آماری کلیدی ================= -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-blue-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">کل سفارشات سیستم</span>
            <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.total }} <span class="text-sm text-slate-500 font-sans font-bold">سفارش</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-amber-500/30 p-6 relative overflow-hidden group hover:border-amber-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">در حال پردازش (Pending)</span>
            <div class="w-10 h-10 bg-amber-500/10 text-amber-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-amber-400 mb-1">{{ stats.processing }} <span class="text-sm text-amber-500/50 font-sans font-bold">مورد</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-emerald-500/30 p-6 relative overflow-hidden group hover:border-emerald-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-emerald-400 text-xs font-bold uppercase tracking-wider">تحویل شده (Completed)</span>
            <div class="w-10 h-10 bg-emerald-500/10 text-emerald-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-emerald-400 mb-1">{{ stats.completed }} <span class="text-sm text-emerald-500/50 font-sans font-bold">مورد</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-rose-500/40 p-6 relative overflow-hidden group hover:border-rose-500/60 transition-all shadow-[0_0_15px_rgba(244,63,94,0.15)]">
          <div class="absolute top-0 left-0 w-32 h-32 bg-rose-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-rose-400 text-xs font-bold uppercase tracking-wider">پرونده اختلاف باز</span>
            <div class="w-10 h-10 bg-rose-500/10 text-rose-500 rounded-xl flex items-center justify-center animate-pulse"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-rose-400 mb-1">{{ disputes.length }} <span class="text-sm text-rose-500/50 font-sans font-bold">پرونده</span></div>
        </div>

      </div>

      <!-- ================= میز قضاوت و حل اختلاف (Resolution Center) ================= -->
      <div class="bg-slate-900 rounded-[2rem] border border-rose-500/30 shadow-lg overflow-hidden relative">
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-rose-500 to-orange-500"></div>
        <div class="p-6 md:p-8 border-b border-slate-800/80 flex justify-between items-center bg-slate-950/30">
          <h3 class="font-black text-white text-lg flex items-center gap-2">
            <svg class="w-6 h-6 text-rose-500 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
            میز قضاوت مدیریت (Resolution Center)
          </h3>
          <span v-if="disputes.length > 0" class="bg-rose-500/10 text-rose-400 text-xs font-bold px-3 py-1.5 rounded border border-rose-500/20">نیازمند مداخله فوری</span>
          <span v-else class="bg-emerald-500/10 text-emerald-400 text-xs font-bold px-3 py-1.5 rounded border border-emerald-500/20">وضعیت پایدار</span>
        </div>
        
        <div class="p-6 space-y-4">
          <!-- پیام حالت خالی -->
          <div v-if="disputes.length === 0" class="flex flex-col items-center justify-center py-10 text-center">
            <div class="w-20 h-20 bg-slate-800/50 rounded-full flex items-center justify-center mb-4 border border-slate-700">
              <svg class="w-10 h-10 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
            <h4 class="text-lg font-black text-white mb-2">پرونده بازی وجود ندارد</h4>
            <p class="text-slate-500 text-sm max-w-md">در حال حاضر هیچ خریداری در پلتفرم ثبت شکایت و درخواست داوری نکرده است.</p>
          </div>

          <!-- لیست اختلافات -->
          <div v-else v-for="dispute in disputes" :key="dispute.id" class="bg-slate-950 border border-rose-500/20 p-5 rounded-2xl relative hover:border-rose-500/50 transition-colors">
            <div class="flex flex-col lg:flex-row justify-between lg:items-center gap-4">
              <div class="space-y-2">
                <div class="flex items-center gap-3">
                  <h4 class="font-bold text-white text-base">پرونده اختلاف شماره: #{{ dispute.id }}</h4>
                  <span class="text-xs font-mono bg-slate-800 text-slate-300 px-2 py-0.5 rounded border border-slate-700">سفارش: {{ dispute.order_id }}</span>
                </div>
                <p class="text-sm text-rose-400 font-bold bg-rose-500/10 inline-block px-2 py-1 rounded">علت: {{ dispute.reason }}</p>
                <p class="text-xs text-slate-400 mt-2 max-w-2xl leading-relaxed">{{ dispute.description }}</p>
              </div>
              
              <div class="flex flex-col sm:flex-row gap-2 shrink-0 w-full lg:w-auto">
                <button @click="resolveDispute(dispute.id, 'buyer', 'رای مدیریت: بازگشت وجه به خریدار به دلیل عدم تطابق کالا')" class="flex-1 lg:flex-none bg-blue-600/10 hover:bg-blue-600 text-blue-500 hover:text-white border border-blue-600/30 transition-all font-bold py-2.5 px-4 rounded-xl text-xs flex justify-center items-center gap-2 shadow-sm">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"></path></svg>
                  حق با خریدار (Refund)
                </button>
                <button @click="resolveDispute(dispute.id, 'seller', 'رای مدیریت: رد شکایت خریدار و واریز وجه به فروشنده')" class="flex-1 lg:flex-none bg-emerald-600/10 hover:bg-emerald-600 text-emerald-500 hover:text-white border border-emerald-600/30 transition-all font-bold py-2.5 px-4 rounded-xl text-xs flex justify-center items-center gap-2 shadow-sm">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                  حق با فروشنده (Payout)
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= جدول کل سفارشات ================= -->
      <div class="bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg overflow-hidden relative">
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-amber-500 to-orange-500"></div>
        
        <div class="overflow-x-auto custom-scrollbar-dark p-2">
          <table class="w-full text-right border-collapse whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/50 text-slate-400 text-xs font-bold border-b border-slate-800">
                <th class="p-5 font-normal rounded-tr-xl">شماره سفارش</th>
                <th class="p-5 font-normal">خریدار / مشتری</th>
                <th class="p-5 font-normal">نام محصول</th>
                <th class="p-5 font-normal text-center">تعداد</th>
                <th class="p-5 font-normal text-center">مبلغ کل (تومان)</th>
                <th class="p-5 font-normal text-center">درصد پیشرفت</th>
                <th class="p-5 font-normal text-center">وضعیت سیستم</th>
                <th class="p-5 font-normal text-left rounded-tl-xl">عملیات</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr v-if="filteredOrders.length === 0">
                <td colspan="8" class="py-12 text-center text-slate-500 font-bold">هیچ سفارشی یافت نشد.</td>
              </tr>
              <tr v-for="order in filteredOrders" :key="order.id" class="border-b border-slate-800/50 hover:bg-slate-800/30 transition-colors group">
                <td class="p-5 font-mono text-xs text-slate-300 font-bold">
                  <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full" :class="getStatusDot(order.status)"></div>
                    {{ order.order_number }}
                  </div>
                </td>
                <td class="p-5 font-bold text-white">{{ order.buyer_name }}</td>
                <td class="p-5 text-slate-400 truncate max-w-[200px]" :title="order.product_name">{{ order.product_name }}</td>
                <td class="p-5 text-center font-black text-white">{{ order.qty }}</td>
                <td class="p-5 text-center font-black text-emerald-400">{{ formatPrice(order.total_amount) }}</td>
                <td class="p-5 text-center">
                  <div class="flex items-center gap-2 justify-center">
                    <div class="w-16 h-1.5 bg-slate-800 rounded-full overflow-hidden">
                      <div class="h-full bg-amber-500 rounded-full" :style="`width: ${order.progress}%`"></div>
                    </div>
                    <span class="text-[10px] text-slate-400 font-mono">{{ order.progress }}%</span>
                  </div>
                </td>
                <td class="p-5 text-center">
                  <span :class="getStatusBadge(order.status)" class="px-3 py-1.5 rounded-lg text-[11px] font-bold shadow-sm inline-block min-w-[90px] text-center">
                    {{ getStatusName(order.status) }}
                  </span>
                </td>
                <td class="p-5 text-left">
                  <button @click="openEditModal(order)" class="bg-amber-500/10 hover:bg-amber-500 text-amber-500 hover:text-slate-900 border border-amber-500/30 transition-all font-bold px-4 py-2 rounded-xl text-xs flex items-center justify-center gap-2 shadow-sm mr-auto">
                    تغییر وضعیت
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ================= Modal: ویرایش وضعیت سفارش ================= -->
    <div v-if="editModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="closeEditModal"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2rem] w-full max-w-md relative z-10 shadow-2xl overflow-hidden animate-fade-in">
        <div class="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-amber-500 to-orange-500"></div>
        <div class="p-8">
          <h2 class="text-2xl font-black text-white mb-2">تغییر وضعیت لجستیک سفارش</h2>
          <p class="text-xs text-slate-400 mb-6 font-mono font-bold leading-relaxed border-b border-slate-800 pb-4">شماره پیگیری: {{ editModal.data.order_number }}</p>
          
          <div class="space-y-5 mb-8">
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">وضعیت سیستمی (Status):</label>
              <select v-model="editModal.form.status" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-amber-500 transition-colors text-sm cursor-pointer font-bold">
                <option value="pending">در انتظار تایید (Pending)</option>
                <option value="processing">در حال پردازش / بسته‌بندی (Processing)</option>
                <option value="shipped">ارسال شده (Shipped)</option>
                <option value="delivered">تحویل شده (Delivered)</option>
                <option value="disputed">دارای اختلاف / مسدود (Disputed)</option>
                <option value="cancelled">لغو شده (Cancelled)</option>
              </select>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2 flex justify-between">
                <span>درصد پیشرفت لجستیک (Progress):</span>
                <span class="text-amber-400 font-mono">{{ editModal.form.progress }}%</span>
              </label>
              <input v-model="editModal.form.progress" type="range" min="0" max="100" step="5" class="w-full accent-amber-500 mt-2" />
            </div>
          </div>

          <div class="flex gap-4">
            <button @click="closeEditModal" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 rounded-xl transition-colors text-sm">انصراف</button>
            <button @click="submitOrderStatus" :disabled="isSaving" class="flex-[2] bg-amber-500 hover:bg-amber-400 text-slate-900 font-black py-3.5 rounded-xl transition-all shadow-[0_0_15px_rgba(245,158,11,0.3)] disabled:opacity-50 flex justify-center items-center gap-2 text-sm">
              <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span v-else>ذخیره در پایگاه داده</span>
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
import { ref, computed, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isSaving = ref(false);
const searchQuery = ref('');

const orders = ref([]);
const disputes = ref([]);

const stats = ref({
  total: 0,
  processing: 0,
  completed: 0
});

const editModal = ref({
  show: false,
  data: null,
  form: {
    status: 'pending',
    progress: 0
  }
});

const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 4000);
};

// ================= FETCH DATA =================
const fetchData = async () => {
  isLoading.value = true;
  try {
    const headers = {
      'Authorization': `Bearer ${token()}`,
      'Content-Type': 'application/json'
    };

    // Parallel Fetching for Orders and Disputes
    const [ordersRes, disputesRes] = await Promise.all([
      fetch(`${API_BASE}/api/admin/orders`, { headers }),
      fetch(`${API_BASE}/admin/disputes/open`, { headers })
    ]);

    if (ordersRes.ok) {
      const ordersData = await ordersRes.json();
      if (ordersData.success) {
        orders.value = ordersData.orders;
        calculateStats();
      }
    } else if (ordersRes.status === 401) {
      alert("لطفا مجددا وارد سیستم شوید.");
    }

    if (disputesRes.ok) {
      disputes.value = await disputesRes.json();
    }
  } catch (error) {
    console.error("خطا در دریافت اطلاعات سفارشات:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchData();
});

const calculateStats = () => {
  stats.value.total = orders.value.length;
  stats.value.processing = orders.value.filter(o => ['pending', 'processing', 'shipped'].includes(o.status)).length;
  stats.value.completed = orders.value.filter(o => o.status === 'delivered' || o.status === 'completed').length;
};

const filteredOrders = computed(() => {
  if (!searchQuery.value) return orders.value;
  const q = searchQuery.value.toLowerCase();
  return orders.value.filter(o => 
    o.order_number.toLowerCase().includes(q) || 
    o.buyer_name.toLowerCase().includes(q)
  );
});

// ================= RESOLVE DISPUTE (Escrow) =================
const resolveDispute = async (disputeId, winner, resolutionText) => {
  const winnerName = winner === 'buyer' ? 'خریدار (برگشت وجه)' : 'فروشنده (آزادسازی وجه)';
  if(!confirm(`آیا مطمئن هستید؟ رای به نفع ${winnerName} صادر خواهد شد و عملیات مالی غیرقابل بازگشت است.`)) return;
  
  try {
    const payload = {
      winner: winner,
      resolution: resolutionText
    };

    // اصلاح لینک اتصال به بک‌اند (بدون /api/ مطابق ساختار main.py)
    const response = await fetch(`${API_BASE}/admin/disputes/${disputeId}/resolve`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    if (response.ok && result.success) {
      showToast('عملیات موفق', result.message);
      // Remove resolved dispute from list
      disputes.value = disputes.value.filter(d => d.id !== disputeId);
      // Refresh orders as status might have changed
      await fetchData();
    } else {
      throw new Error(result.detail || 'خطا در اعمال تغییرات مالی');
    }
  } catch (error) {
    console.error("Dispute Resolution Error:", error);
    alert(error.message);
  }
};

// ================= UPDATE ORDER STATUS =================
const openEditModal = (order) => {
  editModal.value.data = order;
  editModal.value.form = {
    status: order.status,
    progress: order.progress || 0
  };
  editModal.value.show = true;
};

const closeEditModal = () => {
  editModal.value.show = false;
  editModal.value.data = null;
};

const submitOrderStatus = async () => {
  isSaving.value = true;
  try {
    const payload = {
      status: editModal.value.form.status,
      progress: parseInt(editModal.value.form.progress)
    };

    const response = await fetch(`${API_BASE}/api/admin/orders/${editModal.value.data.id}/status`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    if (response.ok && result.success) {
      // Local update to avoid full refresh
      const index = orders.value.findIndex(o => o.id === editModal.value.data.id);
      if(index !== -1) {
        orders.value[index].status = payload.status;
        orders.value[index].progress = payload.progress;
      }
      calculateStats();
      closeEditModal();
      showToast('بروزرسانی موفق', result.message);
    } else {
      throw new Error(result.detail || 'خطا در ثبت وضعیت');
    }
  } catch (error) {
    console.error("Order Status Update Error:", error);
    alert(error.message);
  } finally {
    isSaving.value = false;
  }
};

// ================= UTILS & BADGES =================
const formatPrice = (price) => {
  return price !== undefined && price !== null ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

const getStatusName = (status) => {
  const map = {
    pending: 'در انتظار تایید',
    processing: 'در حال پردازش',
    shipped: 'ارسال شده',
    delivered: 'تحویل شده',
    completed: 'تحویل و تسویه',
    disputed: 'مورد اختلاف',
    cancelled: 'لغو شده'
  };
  return map[status] || status;
};

const getStatusBadge = (status) => {
  const map = {
    pending: 'bg-amber-500/10 text-amber-500 border border-amber-500/20',
    processing: 'bg-blue-500/10 text-blue-400 border border-blue-500/20',
    shipped: 'bg-indigo-500/10 text-indigo-400 border border-indigo-500/20',
    delivered: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20',
    completed: 'bg-emerald-500 text-slate-900 border border-emerald-500',
    disputed: 'bg-rose-500/10 text-rose-400 border border-rose-500/20 animate-pulse',
    cancelled: 'bg-slate-800 text-slate-400 border border-slate-700'
  };
  return map[status] || 'bg-slate-800 text-slate-400';
};

const getStatusDot = (status) => {
  const map = {
    pending: 'bg-amber-500',
    processing: 'bg-blue-400',
    shipped: 'bg-indigo-400',
    delivered: 'bg-emerald-400',
    completed: 'bg-emerald-500',
    disputed: 'bg-rose-500',
    cancelled: 'bg-slate-500'
  };
  return map[status] || 'bg-slate-500';
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