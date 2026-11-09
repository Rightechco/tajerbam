<template>
  <div class="min-h-screen bg-slate-50/80 flex font-sans text-slate-800 selection:bg-blue-100 selection:text-blue-900" dir="rtl">
    
    <!-- ================= سایدبار پریمیوم (فروشنده) ================= -->
    <aside :class="['fixed inset-y-0 right-0 z-50 w-72 bg-white/95 backdrop-blur-2xl border-l border-slate-200/60 shadow-[10px_0_40px_rgba(0,0,0,0.03)] transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static flex flex-col', isSidebarOpen ? 'translate-x-0' : 'translate-x-full']">
      
      <!-- لوگوی پنل -->
      <div class="h-24 flex items-center gap-4 px-6 border-b border-slate-100/80 flex-shrink-0 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-blue-600 to-indigo-500"></div>
        <div class="w-12 h-12 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-500/20">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
        </div>
        <div>
          <h2 class="font-black text-lg tracking-tight text-slate-800">تاجربام</h2>
          <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest">B2B SELLER PORTAL</p>
        </div>
        <button @click="isSidebarOpen = false" class="lg:hidden absolute left-4 text-slate-500 hover:text-red-500 bg-slate-50 hover:bg-red-50 p-2 rounded-xl transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <!-- منوی اصلی -->
      <nav class="flex-1 overflow-y-auto p-4 space-y-1 custom-scrollbar mt-2">
        <p class="px-4 text-[10px] font-black text-slate-400 mb-2 mt-2 tracking-wider">مدیریت فروشگاه</p>
        
        <router-link to="/panel" exact-active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
          پیشخوان فروشنده
        </router-link>

        <router-link to="/panel/add-product" active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          تعریف محصول جدید
        </router-link>

        <router-link to="/panel/products" active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path></svg>
          لیست محصولات من
        </router-link>

        <div class="h-px bg-slate-200/60 my-4 mx-4"></div>
        <p class="px-4 text-[10px] font-black text-slate-400 mb-2 mt-4 tracking-wider">فروش و ارتباطات</p>

        <router-link to="/panel/orders" active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center justify-between px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group relative">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            سفارشات عمده
          </div>
          <span class="absolute left-4 bg-amber-100 text-amber-600 group-[.router-link-active]:bg-white/20 group-[.router-link-active]:text-white px-2 py-0.5 rounded-md text-[10px] font-black shadow-sm">۲ جدید</span>
        </router-link>

        <router-link to="/panel/requests" active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center justify-between px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            درخواست‌های خریداران
          </div>
        </router-link>

        <div class="h-px bg-slate-200/60 my-4 mx-4"></div>
        <p class="px-4 text-[10px] font-black text-slate-400 mb-2 mt-4 tracking-wider">ابزارهای حرفه‌ای</p>

        <router-link to="/panel/marketing" active-class="bg-blue-600 text-white shadow-lg shadow-blue-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-slate-600 hover:bg-slate-50 hover:text-blue-700 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
          بازاریابی هوشمند
        </router-link>

        <router-link to="/panel/plans" active-class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-lg shadow-indigo-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl font-bold text-sm transition-all text-indigo-600 hover:bg-indigo-50 group border border-transparent hover:border-indigo-100">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
          ارتقاء پلن و تعرفه‌ها
        </router-link>
      </nav>

      <div class="p-4 mt-auto space-y-2">
        <button @click="$router.push('/')" class="w-full flex items-center justify-center gap-2 bg-slate-50 hover:bg-slate-100 text-slate-600 font-bold py-3.5 rounded-xl transition-colors text-sm border border-slate-200">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          بازگشت به فروشگاه
        </button>
      </div>

    </aside>

    <div v-if="isSidebarOpen" @click="isSidebarOpen = false" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-40 lg:hidden transition-opacity"></div>

    <!-- ================= محتوای اصلی (Header + Main) ================= -->
    <div class="flex-1 flex flex-col min-w-0 transition-all duration-300 h-screen overflow-hidden">
      
      <!-- هدر داشبورد -->
      <header class="h-20 bg-white/80 backdrop-blur-2xl border-b border-slate-200/60 sticky top-0 z-40 px-4 lg:px-8 flex items-center justify-between shadow-[0_2px_10px_rgba(0,0,0,0.02)]">
        
        <div class="flex items-center gap-4">
          <button @click="isSidebarOpen = !isSidebarOpen" class="lg:hidden text-slate-500 hover:text-blue-600 bg-slate-50 p-2.5 rounded-xl border border-slate-200 shadow-sm transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path></svg>
          </button>
          <div class="hidden md:flex items-center gap-2 bg-slate-50 border border-slate-200 px-4 py-2.5 rounded-xl min-w-[250px] shadow-sm">
            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            <input type="text" placeholder="جستجوی محصول، سفارش..." class="bg-transparent text-sm outline-none w-full font-bold text-slate-700 placeholder-slate-400">
          </div>
        </div>

        <div class="flex items-center gap-4 lg:gap-5">
          
          <button @click="clearNotification" class="relative p-2.5 text-slate-500 hover:text-blue-600 transition-colors bg-slate-50 border border-slate-200 rounded-xl hover:bg-blue-50 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            <span v-if="hasNotification" class="absolute top-1 right-1.5 w-2.5 h-2.5 bg-red-500 border-2 border-white rounded-full animate-bounce"></span>
          </button>

          <!-- دکمه خروج -->
          <button @click="logout" class="p-2.5 text-slate-500 hover:text-red-500 transition-colors bg-slate-50 border border-slate-200 rounded-xl hover:bg-red-50 shadow-sm tooltip" title="خروج امن">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          </button>
          
          <div class="w-px h-6 bg-slate-200"></div>

          <div class="flex items-center gap-3 cursor-pointer pl-1.5 pr-2 py-1.5 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-100 rounded-full hover:shadow-md transition-all shadow-sm">
            <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-blue-600 to-indigo-500 text-white flex items-center justify-center font-black text-sm shadow-sm">{{ userInitial }}</div>
            <div class="hidden sm:block text-left mr-2">
              <p class="text-xs font-black text-blue-900 truncate max-w-[120px]">{{ userName }}</p>
            </div>
            <svg class="w-4 h-4 text-slate-400 ml-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>
        </div>
      </header>

      <!-- محتوای متغیر پنل -->
      <main class="flex-1 overflow-y-auto p-4 lg:p-8 relative custom-scrollbar bg-[#f8fafc]">
        <router-view />
      </main>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const isSidebarOpen = ref(false);
const hasNotification = ref(true);

const userName = ref('فروشنده سیستم');
const userInitial = ref('ف');

onMounted(() => {
  const name = localStorage.getItem('full_name') || localStorage.getItem('user_name');
  if (name && name !== 'null' && name !== 'undefined' && name !== 'کاربر سیستم') {
    userName.value = name;
    userInitial.value = name.charAt(0);
  }
});

const clearNotification = () => {
  hasNotification.value = false;
};

const logout = () => {
  localStorage.removeItem('tajerbam_token');
  localStorage.removeItem('user_role');
  localStorage.removeItem('user_name');
  localStorage.removeItem('full_name');
  router.push('/login');
};
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>