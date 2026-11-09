<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر صفحه ================= -->
    <div class="bg-white p-6 md:p-8 rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col md:flex-row items-center justify-between gap-6 relative overflow-hidden">
      <!-- افکت نوری پس‌زمینه -->
      <div class="absolute -right-10 -top-10 w-64 h-64 bg-blue-100 rounded-full mix-blend-multiply opacity-50 blur-[50px] pointer-events-none"></div>
      
      <div class="relative z-10">
        <h1 class="text-2xl md:text-3xl font-black text-slate-800 mb-2 flex items-center gap-3">
          <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center shadow-inner border border-blue-100">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
          </div>
          کمپین‌ها و لینک‌های اختصاصی
        </h1>
        <p class="text-sm font-bold text-slate-500 mr-2">عملکرد لینک‌های بازاریابی خود را رصد کنید و کمپین‌های هوشمند (UTM) جدید بسازید.</p>
      </div>

      <button @click="openNewCampaignModal" class="w-full md:w-auto bg-blue-600 hover:bg-blue-700 text-white font-black px-8 py-4.5 rounded-2xl shadow-[0_10px_25px_rgba(37,99,235,0.4)] transition-all hover:-translate-y-1 flex items-center justify-center gap-2 relative z-10 text-sm">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
        ایجاد کمپین جدید
      </button>
    </div>

    <!-- ================= جدول عملکرد لینک‌ها ================= -->
    <div class="bg-white rounded-[2.5rem] border border-slate-100 shadow-sm overflow-hidden relative z-10">
      <div class="p-6 md:p-8 border-b border-slate-50 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.5)]"></span>
          لیست لینک‌های فعال شما
        </h3>
        <div class="relative w-full sm:w-80">
          <input type="text" v-model="searchQuery" placeholder="جستجوی کمپین یا آدرس..." class="w-full bg-white border-2 border-slate-100 text-sm font-bold px-5 py-3 pr-12 rounded-xl outline-none focus:border-blue-400 transition-all shadow-sm">
          <svg class="w-5 h-5 text-slate-400 absolute right-4 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
      </div>

      <div class="overflow-x-auto custom-scrollbar min-h-[300px] relative">
        <!-- لودینگ -->
        <div v-if="isLoading" class="absolute inset-0 bg-white/50 backdrop-blur-sm z-20 flex justify-center py-10">
          <svg class="w-10 h-10 text-blue-600 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        </div>

        <table class="w-full text-right text-sm">
          <thead class="bg-white text-slate-400 text-[11px] font-black uppercase border-b border-slate-100">
            <tr>
              <th class="px-6 py-5">نام کمپین / لینک مقصد</th>
              <th class="px-6 py-5 text-center">آمار کلیک</th>
              <th class="px-6 py-5 text-center">خریدهای موفق</th>
              <th class="px-6 py-5 text-center">نرخ تبدیل (CR)</th>
              <th class="px-6 py-5 text-center">عملیات</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-50 font-medium text-slate-700">
            
            <tr v-if="!isLoading && filteredLinks.length === 0">
              <td colspan="5" class="py-12 text-center text-slate-500 font-bold">هیچ کمپینی یافت نشد.</td>
            </tr>

            <tr v-for="link in filteredLinks" :key="link.id" class="hover:bg-slate-50/80 transition-colors group">
              <td class="px-6 py-5">
                <div class="flex flex-col">
                  <span class="font-black text-slate-800 mb-2 group-hover:text-blue-600 transition-colors text-base">{{ link.title }}</span>
                  <div class="flex items-center gap-2">
                    <span class="text-[11px] font-mono font-bold text-blue-700 bg-blue-50 border border-blue-100 px-3 py-1 rounded-lg truncate max-w-[250px] shadow-sm" dir="ltr">{{ link.url }}</span>
                  </div>
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex flex-col items-center justify-center bg-slate-50 rounded-xl p-2 border border-slate-100 w-24 mx-auto">
                  <span class="font-black text-slate-800 text-lg">{{ link.clicks.toLocaleString() }}</span>
                  <span class="text-[10px] font-black text-emerald-600 flex items-center gap-0.5 mt-1 bg-emerald-100/50 px-1.5 py-0.5 rounded"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> {{ link.growth }}٪</span>
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <span class="font-black text-emerald-700 bg-emerald-50 px-4 py-2 rounded-xl border border-emerald-200 shadow-sm">{{ link.sales }} سفارش</span>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="w-full max-w-[100px] mx-auto">
                  <div class="flex justify-between items-center mb-1">
                    <span class="text-xs font-black text-slate-700">{{ link.cr }}٪</span>
                    <span class="text-[9px] text-slate-400 font-bold">عالی</span>
                  </div>
                  <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden shadow-inner">
                    <div class="bg-gradient-to-r from-blue-400 to-indigo-500 h-full rounded-full" :style="`width: ${Math.min(link.cr * 10, 100)}%`"></div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex justify-center gap-2">
                  <button @click="copyToClipboard(link.url)" class="bg-white border-2 border-slate-200 text-slate-500 hover:text-blue-600 hover:border-blue-300 hover:bg-blue-50 font-bold p-2.5 rounded-xl transition-all shadow-sm tooltip" title="کپی لینک">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                  </button>
                  <button class="bg-white border-2 border-slate-200 text-slate-500 hover:text-indigo-600 hover:border-indigo-300 hover:bg-indigo-50 font-bold p-2.5 rounded-xl transition-all shadow-sm tooltip" title="دریافت بنر QR">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm14 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z"></path></svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= MODALS ================= -->
    <Teleport to="body">
      
      <!-- مودال ایجاد کمپین جدید -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95 translate-y-4" enter-to-class="opacity-100 scale-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 translate-y-4">
        <div v-if="showNewCampaignModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-lg rounded-[2.5rem] shadow-2xl relative overflow-hidden font-sans border border-white/40">
            <!-- نوار تزئینی بالا -->
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-blue-500 to-indigo-600 z-10"></div>
            
            <div class="p-6 md:p-8 border-b border-slate-100 flex justify-between items-center relative z-10 bg-slate-50/50">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-white rounded-2xl shadow-sm border border-slate-200 flex items-center justify-center text-blue-600">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                </div>
                <div>
                  <h3 class="font-black text-slate-800 text-lg">ایجاد کمپین جدید</h3>
                  <p class="text-xs font-bold text-slate-500 mt-1">یک لینک رهگیری (UTM) اختصاصی بسازید</p>
                </div>
              </div>
              <button @click="closeNewCampaignModal" class="w-10 h-10 bg-white border-2 border-slate-200 rounded-full flex items-center justify-center text-slate-400 hover:text-red-500 hover:bg-red-50 hover:border-red-200 transition-colors shadow-sm">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>
            
            <div class="p-6 md:p-8 space-y-6 relative z-10">
              
              <!-- نام کمپین -->
              <div>
                <label class="block text-xs font-black text-slate-600 mb-2">نام کمپین (جهت شناسایی در پنل)</label>
                <input type="text" v-model="newCampaign.title" placeholder="مثلاً: تبلیغ در کانال تلگرام" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-800 py-4 px-5 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all shadow-sm">
              </div>

              <!-- انتخاب محصول یا صفحه -->
              <div>
                <label class="block text-xs font-black text-slate-600 mb-2">محصول یا صفحه هدف در تاجربام</label>
                <select v-model="newCampaign.target" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold text-slate-700 py-4 px-5 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all shadow-sm cursor-pointer">
                  <option value="p_123">لپ‌تاپ ایسوس Vivobook X1502ZA</option>
                  <option value="p_456">گوشی موبایل سامسونگ Galaxy S23</option>
                  <option value="c_digital">کل دسته‌بندی کالای دیجیتال</option>
                  <option value="home">صفحه اصلی سایت</option>
                </select>
              </div>

              <!-- پیش‌نمایش لینک -->
              <div v-if="newCampaign.title" class="bg-blue-50 border border-blue-200 rounded-2xl p-5 animate-fade-in shadow-inner">
                <p class="text-[10px] font-black text-blue-800 mb-3">پیش‌نمایش لینک رهگیری نهایی شما:</p>
                <div class="bg-white border border-blue-200/60 rounded-xl p-3 text-sm font-mono font-bold text-slate-600 truncate shadow-sm" dir="ltr">
                  tajerbam.com/{{ newCampaign.target.replace('_', '/') }}?ref={{ userName.replace(/\s+/g, '_').toLowerCase() }}&utm_source={{ newCampaign.title.replace(/\s+/g, '_') }}
                </div>
              </div>
            </div>

            <div class="p-6 md:p-8 bg-slate-50/80 border-t border-slate-100 flex gap-4">
              <button @click="saveCampaign" :disabled="!newCampaign.title || isSaving" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-black py-4 rounded-xl shadow-[0_10px_25px_rgba(37,99,235,0.4)] transition-all hover:-translate-y-1 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0 text-sm flex justify-center items-center gap-2">
                <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                ثبت و ایجاد لینک اختصاصی
              </button>
              <button @click="closeNewCampaignModal" class="px-6 py-4 bg-white border-2 border-slate-200 text-slate-600 font-bold rounded-xl hover:bg-slate-50 hover:text-slate-800 transition-colors text-sm shadow-sm">
                انصراف
              </button>
            </div>
          </div>

        </div>
      </transition>

      <!-- توست کپی شدن / موفقیت -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
        <div v-if="toast.show" class="fixed bottom-6 left-6 md:left-10 z-[100000] bg-slate-900 text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-4 font-sans border border-slate-700" dir="rtl">
          <div class="w-10 h-10 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center border border-emerald-500/30">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm tracking-wide">{{ toast.title }}</h4>
            <p class="text-xs text-slate-300 mt-1 font-medium">{{ toast.message }}</p>
          </div>
        </div>
      </transition>

    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';
const userName = localStorage.getItem('full_name') || 'ali_karimi';

const isLoading = ref(true);
const isSaving = ref(false);

// مدیریت توست نوتیفیکیشن
const toast = ref({ show: false, title: '', message: '' });
const showToast = (title, message) => {
  toast.value = { show: true, title, message };
  setTimeout(() => { toast.value.show = false; }, 3000);
};

// داده‌های جدول لینک‌ها
const linksData = ref([]);

const fetchLinks = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE_URL}/api/marketer/links`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (response.ok) {
      const data = await response.json();
      linksData.value = data.links;
    } else {
      // Mock Data
      linksData.value = [
        { id: 1, title: 'کمپین فروش لپ‌تاپ‌های ایسوس', url: `tajerbam.com/p/123?ref=${userName}`, clicks: 1245, growth: 12, sales: 18, cr: 1.4 },
        { id: 2, title: 'بنر اینستاگرام - گوشی سامسونگ', url: `tajerbam.com/p/456?ref=${userName}`, clicks: 890, growth: 5, sales: 8, cr: 0.9 },
        { id: 3, title: 'لینک معرفی ابزارآلات صنعتی', url: `tajerbam.com/p/789?ref=${userName}`, clicks: 432, growth: 24, sales: 15, cr: 3.4 },
        { id: 4, title: 'کمپین تخفیف مانیتور', url: `tajerbam.com/p/101?ref=${userName}`, clicks: 150, growth: 2, sales: 1, cr: 0.6 },
      ];
    }
  } catch (error) {
    console.error("Links Fetch Error:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchLinks();
});

// جستجو
const searchQuery = ref('');
const filteredLinks = computed(() => {
  if (!searchQuery.value) return linksData.value;
  return linksData.value.filter(l => l.title.includes(searchQuery.value) || l.url.includes(searchQuery.value));
});

// کپی در کلیپ‌بورد
const copyToClipboard = (text) => {
  navigator.clipboard.writeText(text).then(() => {
    showToast('لینک کپی شد!', 'لینک در کلیپ‌بورد شما ذخیره شد.');
  });
};

// منطق مودال ایجاد کمپین
const showNewCampaignModal = ref(false);
const newCampaign = ref({ title: '', target: 'p_123' });

const openNewCampaignModal = () => {
  newCampaign.value = { title: '', target: 'p_123' };
  showNewCampaignModal.value = true;
};

const closeNewCampaignModal = () => {
  showNewCampaignModal.value = false;
};

const saveCampaign = () => {
  isSaving.value = true;
  // شبیه‌سازی ریکوئست POST
  setTimeout(() => {
    const generatedUrl = `tajerbam.com/${newCampaign.value.target.replace('_', '/')}?ref=${userName.replace(/\s+/g, '_').toLowerCase()}&utm_source=${newCampaign.value.title.replace(/\s+/g, '_')}`;
    
    linksData.value.unshift({
      id: Date.now(),
      title: newCampaign.value.title,
      url: generatedUrl,
      clicks: 0,
      growth: 0,
      sales: 0,
      cr: 0
    });

    isSaving.value = false;
    closeNewCampaignModal();
    showToast('کمپین ایجاد شد!', 'لینک جدید شما آماده استفاده و رهگیری است.');
  }, 800);
};
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

body:has(.fixed.z-\[99999\]) { overflow: hidden; }
</style>