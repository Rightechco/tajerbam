<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-8 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-violet-500 rounded-full mix-blend-screen filter blur-[100px] opacity-20 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-fuchsia-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-violet-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-violet-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مرکز پیام و اعلانات (Push & SMS)</h1>
          <p class="text-sm font-bold text-slate-400">ارسال پیامک انبوه، نوتیفیکیشن‌های سیستمی و پایش ارتباطات</p>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto">
        <button @click="fetchData" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی وضعیت">
          <svg :class="{'animate-spin text-violet-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ اولیه ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-violet-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-violet-400 animate-pulse">در حال دریافت تاریخچه ارتباطات و وضعیت پنل...</p>
    </div>

    <div v-else class="grid grid-cols-1 xl:grid-cols-12 gap-8 animate-fade-in">
      
      <!-- ================= ستون راست: فرم ارسال پیام و آمار ================= -->
      <div class="xl:col-span-5 space-y-6">
        
        <!-- کارت وضعیت پنل پیامک -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg p-6 relative overflow-hidden group">
          <div class="absolute right-0 top-0 w-1.5 h-full bg-blue-500 group-hover:bg-blue-400 transition-colors"></div>
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-white font-black text-base flex items-center gap-2">
              <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              اعتبار پنل پیامک (SMS)
            </h3>
            <span class="bg-blue-500/10 text-blue-400 font-bold px-2 py-1 rounded text-[10px] border border-blue-500/20 animate-pulse">متصل به اپراتور</span>
          </div>
          <div class="mb-3">
            <span class="text-3xl font-black text-white tracking-tight">{{ formatPrice(stats.smsCredit) }}</span>
            <span class="text-xs text-slate-500 mr-2 font-bold">تومان</span>
          </div>
          <!-- Progress Bar -->
          <div class="w-full bg-slate-800 rounded-full h-2 mb-2">
            <div class="bg-blue-500 h-2 rounded-full transition-all duration-1000" :style="`width: ${stats.smsCreditLevel}%`"></div>
          </div>
          <p class="text-[10px] text-slate-400 font-bold text-left">{{ stats.smsCreditLevel }}% ظرفیت مصرف شده</p>
        </div>

        <!-- کارت ارسال پیام جدید -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg p-6 relative">
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-violet-500 to-fuchsia-500 rounded-t-[2rem]"></div>
          <h3 class="text-white font-black text-lg mb-6 mt-2 flex items-center gap-2 border-b border-slate-800 pb-4">
            <svg class="w-5 h-5 text-violet-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            ایجاد اعلان جدید
          </h3>
          
          <form @submit.prevent="submitForm" class="space-y-5">
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">عنوان پیام (Subject)</label>
              <input v-model="form.title" type="text" placeholder="مثال: قطعی موقت درگاه بانکی..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 transition-colors text-sm" required />
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">نوع ارسال (Channel)</label>
                <select v-model="form.type" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 transition-colors text-sm cursor-pointer">
                  <option value="system">پاپ‌آپ سیستمی (Push)</option>
                  <option value="sms">ارسال پیامک (SMS)</option>
                </select>
              </div>
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">گروه هدف (Target)</label>
                <select v-model="form.target_group" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 transition-colors text-sm cursor-pointer">
                  <option value="all">تمامی کاربران سیستم</option>
                  <option value="seller">فقط تامین‌کنندگان</option>
                  <option value="buyer">فقط خریداران</option>
                  <option value="marketer">فقط بازاریابان</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">متن پیام (Content)</label>
              <textarea v-model="form.content" rows="4" placeholder="متن پیام خود را اینجا بنویسید..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 transition-colors text-sm resize-none custom-scrollbar-dark" required></textarea>
              <p class="text-[10px] text-slate-500 mt-1 text-left" dir="ltr">{{ form.content.length }} Chars</p>
            </div>

            <button type="submit" :disabled="isSending" class="w-full bg-violet-600 hover:bg-violet-500 text-white font-bold py-3.5 rounded-xl transition-all shadow-[0_0_15px_rgba(139,92,246,0.4)] disabled:opacity-50 flex justify-center items-center gap-2 text-sm mt-2">
              <svg v-if="isSending" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
              <span v-if="isSending">در حال توزیع پیام...</span>
              <span v-else>ارسال پیام به گروه هدف</span>
            </button>
          </form>
        </div>
      </div>

      <!-- ================= ستون چپ: تاریخچه پیام‌های ارسالی ================= -->
      <div class="xl:col-span-7">
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg flex flex-col h-full relative overflow-hidden min-h-[600px]">
          
          <div class="p-6 md:p-8 border-b border-slate-800 bg-slate-950/30 flex justify-between items-center">
            <h3 class="text-white font-black text-lg flex items-center gap-2">
              <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              تاریخچه پیام‌های صادر شده (Logs)
            </h3>
            <div class="bg-fuchsia-500/10 text-fuchsia-400 px-3 py-1 rounded-lg text-xs font-bold border border-fuchsia-500/20">
              کل ارسال‌ها: {{ notifications.length }}
            </div>
          </div>

          <div class="flex-grow p-6 overflow-y-auto custom-scrollbar-dark space-y-4">
            <div v-if="notifications.length === 0" class="text-center text-slate-500 py-10 font-bold">
              هیچ پیامی در تاریخچه یافت نشد.
            </div>

            <div v-for="note in notifications" :key="note.id" class="bg-slate-950 border border-slate-800/80 p-5 rounded-2xl flex flex-col gap-3 hover:border-slate-700 transition-colors">
              <div class="flex justify-between items-start">
                <div class="flex items-center gap-3">
                  <!-- آیکون نوع ارسال -->
                  <div class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 border" :class="note.type === 'sms' ? 'bg-blue-500/10 text-blue-500 border-blue-500/20' : 'bg-violet-500/10 text-violet-500 border-violet-500/20'">
                    <svg v-if="note.type === 'sms'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                    <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
                  </div>
                  <div>
                    <h4 class="text-white font-bold text-sm">{{ note.title }}</h4>
                    <div class="flex gap-2 mt-1">
                      <span class="text-[10px] text-slate-500 font-mono">{{ note.created_at }}</span>
                      <span class="text-[10px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded">{{ getTargetName(note.target_group) }}</span>
                    </div>
                  </div>
                </div>
                <span class="bg-emerald-500/10 text-emerald-400 px-2.5 py-1 rounded text-[10px] font-bold border border-emerald-500/20">انجام شده</span>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed bg-slate-900/50 p-3 rounded-xl">{{ note.content }}</p>
            </div>
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
        <h4 class="text-white font-bold text-sm">ارسال موفق</h4>
        <p class="text-slate-400 text-xs mt-0.5">پیام شما با موفقیت در صف توزیع سیستم قرار گرفت.</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isSending = ref(false);
const notifications = ref([]);

const stats = ref({
  smsCredit: 12500000,
  smsCreditLevel: 45
});

const form = ref({
  title: '',
  content: '',
  type: 'system',
  target_group: 'all'
});

const toastShow = ref(false);

// ================= دریافت اطلاعات از بک‌اند =================
const fetchData = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/notifications`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      const data = await response.json();
      if (data.success) {
        notifications.value = data.notifications;
      }
    } else {
      if(response.status === 401) alert('لطفاً مجددا لاگین کنید.');
    }
  } catch (error) {
    console.error("خطا در دریافت تاریخچه پیام‌ها:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchData();
});

// ================= ارسال اعلان/پیامک جدید =================
const submitForm = async () => {
  if (!form.value.title || !form.value.content) {
    alert("لطفا تمامی فیلدهای الزامی را پر کنید.");
    return;
  }

  isSending.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/notifications`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form.value)
    });

    const result = await response.json();

    if (response.ok && result.success) {
      // شبیه‌سازی کسر اعتبار پیامک در UI برای جلوه بهتر (اختیاری)
      if (form.value.type === 'sms') {
        stats.value.smsCredit = Math.max(0, stats.value.smsCredit - 150000); 
        stats.value.smsCreditLevel = Math.max(0, stats.value.smsCreditLevel - 1);
      }

      // بروزرسانی لیست لاگ‌ها
      await fetchData();

      // ریست فرم
      form.value.title = '';
      form.value.content = '';
      
      toastShow.value = true;
      setTimeout(() => { toastShow.value = false; }, 3500);
    } else {
      throw new Error(result.detail || 'خطا در ارسال پیام');
    }
  } catch (error) {
    console.error("Error sending notification:", error);
    alert("خطا در ارسال پیام. " + error.message);
  } finally {
    isSending.value = false;
  }
};

// ================= توابع کمکی (Helpers) =================
const getTargetName = (target) => {
  const map = {
    'all': 'سراسری (همه اعضا)',
    'seller': 'گروه تامین‌کنندگان',
    'buyer': 'گروه خریداران',
    'marketer': 'گروه بازاریابان'
  };
  return map[target] || 'نامشخص';
};

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
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