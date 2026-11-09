<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-blue-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-indigo-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-blue-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-blue-500 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مدیریت انبار (WMS)</h1>
          <p class="text-sm font-bold text-slate-400">کنترل موجودی، قفسه‌بندی و پایش هشدار اتمام کالا</p>
        </div>
      </div>

      <div class="relative z-10 flex flex-wrap gap-3 w-full md:w-auto">
        <div class="relative w-full md:w-64">
          <input v-model="searchQuery" type="text" placeholder="جستجوی کالا یا SKU..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 pr-11 rounded-xl focus:outline-none focus:border-blue-500 transition-colors text-sm font-medium">
          <svg class="w-5 h-5 text-slate-500 absolute right-4 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        
        <button @click="fetchInventoryData" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی اطلاعات">
          <svg :class="{'animate-spin text-blue-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-blue-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-blue-500 animate-pulse">در حال ارتباط با پایگاه داده انبار...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in">
      
      <!-- ================= کارت‌های آماری کلیدی ================= -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-blue-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">اقلام موجود در انبار</span>
            <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.totalItems }} <span class="text-sm text-slate-500 font-sans font-bold">کالا (SKU)</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-amber-500/30 p-6 relative overflow-hidden group hover:border-amber-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">موجودی رو به اتمام</span>
            <div class="w-10 h-10 bg-amber-500/10 text-amber-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-amber-400 mb-1">{{ stats.lowStock }} <span class="text-sm text-amber-500/50 font-sans font-bold">هشدار</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-rose-500/30 p-6 relative overflow-hidden group hover:border-rose-500/50 transition-all shadow-[0_0_15px_rgba(244,63,94,0.1)]">
          <div class="absolute top-0 left-0 w-32 h-32 bg-rose-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-rose-400 text-xs font-bold uppercase tracking-wider">ناموجود (Out of Stock)</span>
            <div class="w-10 h-10 bg-rose-500/10 text-rose-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-rose-400 mb-1">{{ stats.outOfStock }} <span class="text-sm text-rose-500/50 font-sans font-bold">کالا</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-indigo-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-indigo-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">رزرو شده در سبد خرید</span>
            <div class="w-10 h-10 bg-indigo-500/10 text-indigo-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.reserved }} <span class="text-sm text-slate-500 font-sans font-bold">عدد کالا</span></div>
        </div>

      </div>

      <!-- ================= جدول انبار ================= -->
      <div class="bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg overflow-hidden relative">
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-blue-500 to-indigo-500"></div>
        
        <div class="overflow-x-auto custom-scrollbar-dark p-2">
          <table class="w-full text-right border-collapse whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/50 text-slate-400 text-xs font-bold border-b border-slate-800">
                <th class="p-5 font-normal rounded-tr-xl">نام محصول / شناسه</th>
                <th class="p-5 font-normal text-center">کد SKU</th>
                <th class="p-5 font-normal text-center">موجودی کل</th>
                <th class="p-5 font-normal text-center">رزرو شده</th>
                <th class="p-5 font-normal text-center">قابل فروش</th>
                <th class="p-5 font-normal text-center">موقعیت فیزیکی (Rack)</th>
                <th class="p-5 font-normal text-center">وضعیت</th>
                <th class="p-5 font-normal text-left rounded-tl-xl">عملیات</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr v-if="filteredInventory.length === 0">
                <td colspan="8" class="py-12 text-center text-slate-500 font-bold">هیچ کالایی در انبار یافت نشد.</td>
              </tr>
              <tr v-for="item in filteredInventory" :key="item.id" class="border-b border-slate-800/50 hover:bg-slate-800/30 transition-colors group">
                <td class="p-5">
                  <div class="flex flex-col">
                    <span class="font-bold text-white text-sm" :title="item.product_name">{{ item.product_name.length > 35 ? item.product_name.substring(0,35) + '...' : item.product_name }}</span>
                    <span class="text-xs text-slate-500 mt-1">ID: #{{ item.product_id }}</span>
                  </div>
                </td>
                <td class="p-5 text-center font-mono text-xs text-slate-400 bg-slate-950/30 rounded">{{ item.sku }}</td>
                <td class="p-5 text-center font-black text-lg text-white">{{ formatPrice(item.stock_total) }}</td>
                <td class="p-5 text-center text-rose-400 font-bold">{{ item.stock_reserved }}</td>
                <td class="p-5 text-center font-bold text-emerald-400">{{ formatPrice(item.stock_total - item.stock_reserved) }}</td>
                <td class="p-5 text-center">
                  <span class="bg-slate-800 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-lg text-xs font-mono font-bold">{{ item.rack_location }}</span>
                </td>
                <td class="p-5 text-center">
                  <span :class="getStatusBadge(item.stock_total, item.min_threshold)" class="px-3 py-1.5 rounded-lg text-[11px] font-bold border flex items-center justify-center w-fit mx-auto gap-1">
                    <div class="w-1.5 h-1.5 rounded-full" :class="getStatusDot(item.stock_total, item.min_threshold)"></div>
                    {{ getStatusText(item.stock_total, item.min_threshold) }}
                  </span>
                </td>
                <td class="p-5 text-left">
                  <button @click="openEditModal(item)" class="bg-blue-600/10 hover:bg-blue-600 text-blue-500 hover:text-white border border-blue-600/30 px-4 py-2 rounded-xl transition-all text-xs font-bold shadow-sm">
                    بروزرسانی انبار
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ================= Modal: ویرایش موجودی ================= -->
    <div v-if="editModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="closeEditModal"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2rem] w-full max-w-md relative z-10 shadow-2xl overflow-hidden animate-fade-in">
        <div class="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-blue-500 to-cyan-500"></div>
        <div class="p-8">
          <h2 class="text-2xl font-black text-white mb-2">اصلاح موجودی کالا</h2>
          <p class="text-xs text-slate-400 mb-6 font-bold leading-relaxed">{{ editModal.data.product_name }}</p>
          
          <div class="space-y-5 mb-8">
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">موجودی کل در انبار (عدد):</label>
              <div class="relative">
                <input v-model="editModal.form.stock_total" type="number" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-blue-500 transition-colors font-black text-lg text-left" dir="ltr" />
                <span class="absolute right-4 top-3 text-slate-500 text-sm font-bold">QTY</span>
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">موقعیت فیزیکی / شماره قفسه (Rack):</label>
              <input v-model="editModal.form.rack_location" type="text" placeholder="مثال: A-12-Rack4" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-blue-500 transition-colors font-mono font-bold text-left" dir="ltr" />
            </div>
          </div>

          <div class="flex gap-4">
            <button @click="closeEditModal" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 rounded-xl transition-colors text-sm">انصراف</button>
            <button @click="submitEdit" :disabled="isSaving" class="flex-[2] bg-blue-600 hover:bg-blue-500 text-white font-bold py-3.5 rounded-xl transition-all shadow-lg shadow-blue-500/20 disabled:opacity-50 flex justify-center items-center gap-2 text-sm">
              <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span v-else>ذخیره در دیتابیس</span>
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
        <h4 class="text-white font-bold text-sm">بروزرسانی انبار</h4>
        <p class="text-slate-400 text-xs mt-0.5">اطلاعات کالا با موفقیت در پایگاه داده WMS ثبت شد.</p>
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
const toastShow = ref(false);
const searchQuery = ref('');

const allInventory = ref([]);

const stats = ref({
  totalItems: 0,
  lowStock: 0,
  outOfStock: 0,
  reserved: 0
});

const editModal = ref({
  show: false,
  data: null,
  form: {
    stock_total: 0,
    rack_location: ''
  }
});

// ================= FETCH INVENTORY FROM API =================
const fetchInventoryData = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/inventory`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if(response.ok) {
      const data = await response.json();
      if(data.success) {
        allInventory.value = data.inventory;
        calculateStats();
      }
    } else {
      if (response.status === 401) {
        alert("لطفا مجددا وارد سیستم شوید.");
      } else {
        throw new Error('Server error');
      }
    }
  } catch (error) {
    console.error("خطا در دریافت اطلاعات انبارداری:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchInventoryData();
});

// ================= BUSINESS LOGIC & FILTERING =================
const calculateStats = () => {
  let low = 0;
  let out = 0;
  let rsv = 0;
  
  allInventory.value.forEach(item => {
    rsv += item.stock_reserved || 0;
    if (item.stock_total <= 0) {
      out++;
    } else if (item.stock_total <= item.min_threshold) {
      low++;
    }
  });

  stats.value = {
    totalItems: allInventory.value.length,
    lowStock: low,
    outOfStock: out,
    reserved: rsv
  };
};

const filteredInventory = computed(() => {
  if (!searchQuery.value) return allInventory.value;
  const query = searchQuery.value.toLowerCase();
  return allInventory.value.filter(item => 
    item.product_name.toLowerCase().includes(query) || 
    item.sku.toLowerCase().includes(query)
  );
});

// ================= UPDATE INVENTORY =================
const openEditModal = (item) => {
  editModal.value.data = item;
  editModal.value.form = {
    stock_total: item.stock_total,
    rack_location: item.rack_location || ''
  };
  editModal.value.show = true;
};

const closeEditModal = () => {
  editModal.value.show = false;
  editModal.value.data = null;
};

const submitEdit = async () => {
  isSaving.value = true;
  const payload = {
    stock_total: Number(editModal.value.form.stock_total),
    rack_location: editModal.value.form.rack_location
  };

  try {
    const response = await fetch(`${API_BASE}/api/admin/inventory/${editModal.value.data.id}`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (response.ok) {
      // بروزرسانی محلی دیتای جدول بدون نیاز به رفرش کامل
      const index = allInventory.value.findIndex(p => p.id === editModal.value.data.id);
      if(index !== -1) {
        allInventory.value[index].stock_total = payload.stock_total;
        allInventory.value[index].rack_location = payload.rack_location;
      }
      
      calculateStats();
      closeEditModal();
      toastShow.value = true;
      setTimeout(() => { toastShow.value = false; }, 3500);
    } else {
      const errData = await response.json();
      throw new Error(errData.detail || 'خطا در ثبت اطلاعات');
    }
  } catch (error) {
    console.error("خطا در بروزرسانی انبار:", error);
    alert("بروزرسانی با شکست مواجه شد. " + error.message);
  } finally {
    isSaving.value = false;
  }
};

// ================= UTILS & BADGES =================
const formatPrice = (price) => {
  return price !== undefined && price !== null ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

const getStatusBadge = (stock, minThreshold) => {
  if (stock <= 0) return 'bg-rose-500/10 text-rose-400 border-rose-500/20';
  if (stock <= minThreshold) return 'bg-amber-500/10 text-amber-500 border-amber-500/20 animate-pulse';
  return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
};

const getStatusDot = (stock, minThreshold) => {
  if (stock <= 0) return 'bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.8)]';
  if (stock <= minThreshold) return 'bg-amber-500 shadow-[0_0_8px_rgba(245,158,11,0.8)]';
  return 'bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.8)]';
};

const getStatusText = (stock, minThreshold) => {
  if (stock <= 0) return 'ناموجود';
  if (stock <= minThreshold) return 'رو به اتمام';
  return 'موجود در انبار';
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

/* Hide arrows in number input */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

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