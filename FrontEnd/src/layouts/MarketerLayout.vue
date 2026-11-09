<template>
  <div class="min-h-screen bg-[#f8fafc] flex font-sans text-slate-800 selection:bg-emerald-100 selection:text-emerald-900" dir="rtl">
    
    <!-- ================= سایدبار بازاریاب ================= -->
    <aside :class="['fixed inset-y-0 right-0 z-50 w-72 bg-white/95 backdrop-blur-2xl border-l border-slate-200/60 shadow-[10px_0_40px_rgba(0,0,0,0.03)] transform transition-transform duration-300 ease-in-out lg:translate-x-0 lg:static flex flex-col', isSidebarOpen ? 'translate-x-0' : 'translate-x-full']">
      
      <!-- لوگو -->
      <div class="h-24 flex items-center gap-4 px-6 border-b border-slate-100/80 flex-shrink-0 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
        <div class="w-12 h-12 bg-gradient-to-tr from-emerald-500 to-teal-500 rounded-2xl flex items-center justify-center shadow-lg shadow-emerald-500/20">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <div>
          <span class="text-xl font-black tracking-tight text-slate-800">مرکز <span class="text-emerald-600">بازاریابان</span></span>
          <p class="text-[10px] font-bold text-slate-400 mt-0.5 tracking-wider uppercase">Affiliate Panel</p>
        </div>
        <button @click="isSidebarOpen = false" class="lg:hidden mr-auto p-2 bg-slate-50 rounded-xl text-slate-500 hover:text-red-500 hover:bg-red-50 transition-colors"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
      </div>

      <!-- منوها -->
      <div class="p-4 flex-1 overflow-y-auto custom-scrollbar space-y-2 mt-4">
        
        <router-link to="/marketer" exact-active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"></path></svg>
          داشبورد درآمد
        </router-link>

        <router-link to="/marketer/products" active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center justify-between px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group relative">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            محصولات سودآور
          </div>
          <span class="bg-orange-100 text-orange-600 group-[.router-link-active]:bg-white/20 group-[.router-link-active]:text-white text-[10px] font-black px-2 py-0.5 rounded-md shadow-sm">Hot</span>
        </router-link>

        <router-link to="/marketer/requests" active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"></path></svg>
          ارتباط با فروشندگان
        </router-link>

        <router-link to="/marketer/cart" active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group relative">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
          ثبت سفارش مشتری
        </router-link>

        <router-link to="/marketer/links" active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
          لینک‌ها و بنرها
        </router-link>

        <router-link to="/marketer/wallet" active-class="bg-emerald-500 text-white shadow-lg shadow-emerald-500/30 font-black" class="flex items-center gap-3 px-4 py-3.5 rounded-2xl text-slate-600 font-bold hover:bg-slate-50 hover:text-emerald-600 transition-all group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
          کیف پول و تسویه
        </router-link>

        <div class="h-px bg-slate-200/60 my-4 mx-4"></div>

        <router-link to="/marketer/plans" active-class="bg-gradient-to-r from-amber-400 to-orange-500 text-white shadow-lg shadow-orange-500/30 font-black" class="flex items-center justify-between px-4 py-3.5 rounded-2xl text-amber-600 font-bold hover:bg-amber-50 transition-all group border border-amber-200/50">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 group-[.router-link-active]:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
            ارتقاء حساب (VIP)
          </div>
        </router-link>

      </div>

      <div class="p-4 mt-auto space-y-2">
        <button @click="$router.push('/')" class="w-full flex items-center justify-center gap-2 bg-slate-50 hover:bg-slate-100 text-slate-600 font-bold py-3.5 rounded-xl transition-colors text-sm border border-slate-200">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          بازگشت به فروشگاه
        </button>
      </div>
    </aside>

    <div v-if="isSidebarOpen" @click="isSidebarOpen = false" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-40 lg:hidden transition-opacity"></div>

    <!-- ================= محتوای اصلی ================= -->
    <div class="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
      <header class="h-20 bg-white/80 backdrop-blur-2xl border-b border-slate-200/60 flex items-center justify-between px-4 lg:px-8 z-30 sticky top-0 shadow-[0_2px_10px_rgba(0,0,0,0.02)]">
        <div class="flex items-center gap-4">
          <button @click="isSidebarOpen = true" class="lg:hidden p-2.5 bg-slate-50 rounded-xl text-slate-600 hover:text-emerald-600 transition-colors"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path></svg></button>
          
          <div class="hidden md:flex items-center gap-2 bg-slate-50 border border-slate-200 px-4 py-2.5 rounded-xl min-w-[200px] shadow-sm">
             <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_8px_rgba(16,185,129,0.6)]"></span>
             <span class="text-sm font-bold text-slate-700 truncate">وضعیت حساب: عالی</span>
          </div>
        </div>

        <div class="flex items-center gap-4 lg:gap-5">
          
          <button @click="clearNotification" class="relative p-2.5 text-slate-500 hover:text-emerald-600 transition-colors bg-slate-50 border border-slate-200 rounded-xl hover:bg-emerald-50 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            <span v-if="hasNotification" class="absolute top-1 right-1.5 w-2.5 h-2.5 bg-red-500 border-2 border-white rounded-full animate-bounce"></span>
          </button>

          <button @click="logout" class="p-2.5 text-slate-500 hover:text-red-500 transition-colors bg-slate-50 border border-slate-200 rounded-xl hover:bg-red-50 shadow-sm tooltip" title="خروج">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          </button>

          <div class="w-px h-6 bg-slate-200"></div>

          <div class="flex items-center gap-3 cursor-pointer pl-2 pr-2 py-1.5 bg-gradient-to-r from-emerald-50 to-teal-50 border border-emerald-100 rounded-full shadow-sm hover:shadow-md transition-all">
            <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-emerald-500 to-teal-500 text-white flex items-center justify-center font-black text-sm shadow-sm">{{ marketerInitial }}</div>
            <div class="hidden sm:block text-left mr-1">
              <p class="text-xs font-black text-emerald-900">{{ marketerName }}</p>
            </div>
          </div>
        </div>
      </header>

      <main class="flex-1 overflow-y-auto p-4 lg:p-8 relative custom-scrollbar">
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

const marketerName = ref('بازاریاب سیستم');
const marketerInitial = ref('ب');

onMounted(() => {
  const name = localStorage.getItem('full_name') || localStorage.getItem('user_name');
  if (name && name !== 'null' && name !== 'undefined') {
    marketerName.value = name;
    marketerInitial.value = name.charAt(0);
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

<style>
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>