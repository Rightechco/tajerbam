<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-8 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-cyan-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-cyan-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-cyan-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مدیریت محتوا (CMS)</h1>
          <p class="text-sm font-bold text-slate-400">مدیریت بنرهای تبلیغاتی، اسلایدرها و محتوای بصری پلتفرم</p>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto">
        <button @click="fetchBanners" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی">
          <svg :class="{'animate-spin text-cyan-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="openAddBannerModal" class="flex-grow md:flex-grow-0 bg-cyan-600 hover:bg-cyan-500 text-white px-6 py-3.5 rounded-xl transition-all font-bold flex items-center justify-center gap-2 text-sm shadow-[0_0_15px_rgba(6,182,212,0.4)]">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
          افزودن بنر جدید
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-cyan-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-cyan-500 animate-pulse">در حال دریافت محتوای بصری پلتفرم...</p>
    </div>

    <!-- ================= لیست بنرها ================= -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 animate-fade-in">
      <div v-if="banners.length === 0" class="col-span-full bg-slate-900 border border-slate-800 rounded-[2rem] p-12 text-center text-slate-500 font-bold">
        هیچ بنری در سیستم ثبت نشده است.
      </div>

      <div v-for="banner in banners" :key="banner.id" class="bg-slate-900 border border-slate-800 rounded-[2rem] overflow-hidden shadow-lg group hover:border-cyan-500/50 transition-all flex flex-col">
        <!-- تصویر بنر -->
        <div class="h-48 w-full bg-slate-800 relative overflow-hidden">
          <img :src="banner.img" :alt="banner.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" @error="handleImageError" />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-transparent to-transparent opacity-80"></div>
          
          <div class="absolute top-4 right-4">
            <span v-if="banner.status === 'active'" class="bg-emerald-500/90 text-white backdrop-blur-md px-3 py-1 rounded-lg text-xs font-bold shadow-sm">فعال</span>
            <span v-else class="bg-slate-600/90 text-white backdrop-blur-md px-3 py-1 rounded-lg text-xs font-bold shadow-sm">غیرفعال</span>
          </div>
          
          <div class="absolute bottom-4 right-4 left-4">
            <span class="bg-slate-900/80 backdrop-blur-md text-cyan-300 border border-cyan-500/30 px-2.5 py-1 rounded text-[10px] font-bold mb-2 inline-block">
              {{ banner.position === 'home_main' ? 'اسلایدر اصلی صفحه اول' : 'بنر تبلیغاتی سایدبار' }}
            </span>
          </div>
        </div>

        <!-- اطلاعات و عملیات -->
        <div class="p-6 flex flex-col flex-grow justify-between">
          <div>
            <h3 class="text-white font-black text-lg mb-2 line-clamp-1" :title="banner.title">{{ banner.title }}</h3>
            <p class="text-xs text-slate-500 font-mono line-clamp-1 mb-4" dir="ltr">{{ banner.url || 'بدون لینک' }}</p>
          </div>
          
          <div class="flex gap-3 mt-auto pt-4 border-t border-slate-800/80">
            <button class="flex-1 bg-slate-800 hover:bg-slate-700 text-white py-2.5 rounded-xl text-xs font-bold transition-colors">ویرایش</button>
            <button @click="deleteBanner(banner.id)" class="flex-1 bg-rose-500/10 hover:bg-rose-500 text-rose-500 hover:text-white border border-rose-500/20 py-2.5 rounded-xl text-xs font-bold transition-all flex items-center justify-center gap-1">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
              حذف
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= Modal: افزودن بنر ================= -->
    <div v-if="modals.banner" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="modals.banner = false"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2rem] w-full max-w-xl relative z-10 shadow-2xl overflow-hidden animate-fade-in">
        <div class="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-cyan-500 to-blue-500"></div>
        <div class="p-8">
          <h2 class="text-2xl font-black text-white mb-2">ثبت بنر تبلیغاتی جدید</h2>
          <p class="text-xs text-slate-400 mb-6 font-bold leading-relaxed border-b border-slate-800 pb-4">تصویر و مشخصات بنر جهت نمایش در وب‌سایت اصلی را وارد نمایید.</p>
          
          <div class="space-y-5 mb-8">
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">عنوان بنر (Alt / Title)</label>
              <input v-model="newBanner.title" type="text" placeholder="مثال: جشنواره فروش پاییزه..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-cyan-500 transition-colors text-sm" />
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">مکان نمایش (Position)</label>
                <select v-model="newBanner.position" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-cyan-500 transition-colors text-sm cursor-pointer">
                  <option value="home_main">اسلایدر اصلی (Home Main)</option>
                  <option value="home_sidebar">بنر کناری (Home Sidebar)</option>
                </select>
              </div>
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">وضعیت (Status)</label>
                <select v-model="newBanner.status" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-cyan-500 transition-colors text-sm cursor-pointer">
                  <option value="active">فعال (انتشار فوری)</option>
                  <option value="inactive">غیرفعال (پیش‌نویس)</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">لینک ارجاع (URL - اختیاری)</label>
              <input v-model="newBanner.url" type="text" placeholder="https://..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-cyan-500 transition-colors text-sm font-mono text-left" dir="ltr" />
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">آدرس تصویر (Image URL)</label>
              <input v-model="newBanner.img" type="text" placeholder="https://..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-cyan-500 transition-colors text-sm font-mono text-left" dir="ltr" />
            </div>
            
            <!-- پیش‌نمایش عکس در فرم -->
            <div v-if="newBanner.img" class="mt-4 w-full h-32 bg-slate-950 rounded-xl border border-slate-700 overflow-hidden flex items-center justify-center">
                <img :src="newBanner.img" class="max-w-full max-h-full object-contain" @error="handleImageError" alt="پیش‌نمایش">
            </div>
          </div>

          <div class="flex gap-4">
            <button @click="modals.banner = false" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 rounded-xl transition-colors text-sm">انصراف</button>
            <button @click="submitBanner" :disabled="isModalsSubmitting" class="flex-[2] bg-cyan-600 hover:bg-cyan-500 text-white font-bold py-3.5 rounded-xl transition-all shadow-[0_0_15px_rgba(6,182,212,0.3)] disabled:opacity-50 flex justify-center items-center gap-2 text-sm">
              <svg v-if="isModalsSubmitting" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span v-else>ذخیره و انتشار بنر</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= Toast Notification ================= -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-800 border border-cyan-500/30 shadow-[0_10px_30px_rgba(0,0,0,0.5)] rounded-2xl p-4 flex items-center gap-4 z-50 animate-fade-in max-w-sm">
      <div class="w-10 h-10 bg-cyan-500/10 rounded-full flex items-center justify-center shrink-0">
        <svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
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
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isModalsSubmitting = ref(false);
const banners = ref([]);
const modals = ref({ banner: false });

const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

const newBanner = ref({
  title: '',
  url: '',
  position: 'home_main',
  img: '',
  status: 'active'
});

const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 4000);
};

// ================= دریافت لیست بنرها از بک‌اند =================
const fetchBanners = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/cms/banners`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      const data = await response.json();
      if (data.success) {
        banners.value = data.banners;
      }
    } else {
      if(response.status === 401) alert('لطفاً مجددا لاگین کنید.');
    }
  } catch (error) {
    console.error("خطا در دریافت بنرها:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchBanners();
});

// ================= ثبت بنر جدید در دیتابیس =================
const openAddBannerModal = () => {
  newBanner.value = { title: '', url: '', position: 'home_main', img: '', status: 'active' };
  modals.value.banner = true;
};

const submitBanner = async () => {
  if (!newBanner.value.title || !newBanner.value.img) {
    alert("وارد کردن عنوان و آدرس تصویر الزامی است.");
    return;
  }

  isModalsSubmitting.value = true;
  try {
    const payload = {
      title: newBanner.value.title,
      url: newBanner.value.url,
      position: newBanner.value.position,
      img: newBanner.value.img,
      status: newBanner.value.status
    };

    const response = await fetch(`${API_BASE}/api/admin/cms/banners`, {
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
      modals.value.banner = false;
      await fetchBanners(); // بروزرسانی مجدد لیست
    } else {
      throw new Error(result.detail || 'خطا در ثبت بنر');
    }
  } catch (error) {
    console.error("Error creating banner:", error);
    alert(error.message);
  } finally {
    isModalsSubmitting.value = false;
  }
};

// ================= حذف بنر از دیتابیس =================
const deleteBanner = async (id) => {
  if (!confirm("آیا از حذف این بنر اطمینان دارید؟")) return;

  try {
    const response = await fetch(`${API_BASE}/api/admin/cms/banners/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    const result = await response.json();

    if (response.ok && result.success) {
      banners.value = banners.value.filter(b => b.id !== id);
      showToast('حذف موفق', result.message);
    } else {
      throw new Error(result.detail || 'خطا در حذف بنر');
    }
  } catch (error) {
    console.error("Error deleting banner:", error);
    alert(error.message);
  }
};

// ================= مدیریت خطای بارگذاری عکس =================
const handleImageError = (e) => {
  e.target.src = 'https://placehold.co/600x400/1e293b/475569?text=Image+Not+Found';
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.custom-scrollbar-dark::-webkit-scrollbar { width: 4px; height: 6px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: #475569; }

.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
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