<template>
  <div class="min-h-screen bg-[#0f172a] flex font-sans text-slate-300 selection:bg-amber-500/30 selection:text-amber-200" dir="rtl">
    
    <!-- ================= سایدبار ادمین (Dark Enterprise Theme) ================= -->
    <aside :class="['fixed inset-y-0 right-0 z-50 w-72 bg-slate-950/95 backdrop-blur-3xl text-white shadow-[15px_0_50px_rgba(0,0,0,0.5)] transform transition-all duration-400 ease-in-out lg:translate-x-0 lg:static flex flex-col border-l border-slate-800/80', isSidebarOpen ? 'translate-x-0' : 'translate-x-full']">
      
      <!-- هدر سایدبار و لوگو -->
      <div class="h-24 flex items-center gap-4 px-6 border-b border-slate-800/80 flex-shrink-0 relative overflow-hidden bg-slate-950/50">
        <!-- نوار گرادیان نوری بالای سایدبار -->
        <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-amber-400 to-orange-600"></div>
        
        <div class="w-12 h-12 bg-gradient-to-tr from-amber-500 to-orange-600 rounded-2xl flex items-center justify-center shadow-[0_0_20px_rgba(245,158,11,0.4)] relative group cursor-default">
          <div class="absolute inset-0 bg-white/20 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity"></div>
          <svg class="w-6 h-6 text-white relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        
        <div class="flex flex-col justify-center">
          <span class="text-xl font-black tracking-tight text-white leading-none">مدیریت <span class="text-amber-500">پلتفرم</span></span>
          <p class="text-[10px] font-bold text-slate-500 mt-1 tracking-widest uppercase">Super Admin</p>
        </div>

        <!-- دکمه بستن سایدبار در موبایل -->
        <button @click="isSidebarOpen = false" class="lg:hidden mr-auto p-2.5 bg-slate-900 rounded-xl text-slate-400 hover:text-red-400 hover:bg-red-500/10 transition-colors border border-slate-800">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <!-- ================= منوهای ناوبری ================= -->
      <nav class="p-4 flex-1 overflow-y-auto custom-scrollbar-dark space-y-1.5">
        
        <div class="text-[10px] font-black text-slate-500 mb-3 px-2 tracking-widest uppercase mt-2">مرکز کنترل و مالی</div>

        <router-link to="/admin" exact-active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">داشبورد کلان</span>
        </router-link>

        <router-link to="/admin/finance" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center justify-between px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span class="group-hover:-translate-x-1 transition-transform">تسویه‌ها (خزانه‌داری)</span>
          </div>
          <span class="bg-red-500 text-white text-[10px] font-black px-2 py-0.5 rounded-md shadow-sm group-[.router-link-active]:bg-red-600 animate-pulse">۵</span>
        </router-link>

        <router-link to="/admin/accounting" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">حسابداری و گزارشات</span>
        </router-link>

        <div class="h-px bg-slate-800/80 my-5 mx-4 relative"><div class="absolute left-1/2 -translate-x-1/2 -top-1 w-2 h-2 bg-slate-900 border border-slate-800 rounded-full"></div></div>
        
        <div class="text-[10px] font-black text-slate-500 mb-3 px-2 tracking-widest uppercase mt-4">نظارت و عملیات تجاری</div>

        <router-link to="/admin/users" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">مدیریت کاربران (KYC)</span>
        </router-link>

        <router-link to="/admin/categories" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center justify-between px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
            <span class="group-hover:-translate-x-1 transition-transform">مدیریت دسته‌بندی‌ها</span>
          </div>
          <span class="text-[10px] font-black px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 group-[.router-link-active]:bg-emerald-950 group-[.router-link-active]:text-emerald-300">جدید</span>
        </router-link>

        <router-link to="/admin/products" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center justify-between px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            <span class="group-hover:-translate-x-1 transition-transform">نظارت بر کالاها</span>
          </div>
          <span class="text-[10px] font-black px-2 py-0.5 rounded-md bg-slate-800 text-slate-400 group-[.router-link-active]:bg-amber-950 group-[.router-link-active]:text-amber-800 border border-slate-700 group-[.router-link-active]:border-amber-900">۱۴</span>
        </router-link>

        <router-link to="/admin/rfq" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">نظارت بر استعلام‌ها (RFQ)</span>
        </router-link>

        <router-link to="/admin/orders" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center justify-between px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
            <span class="group-hover:-translate-x-1 transition-transform">سفارشات و اختلافات</span>
          </div>
          <span class="w-2 h-2 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.6)]"></span>
        </router-link>

        <router-link to="/admin/inventory" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">انبار و موجودی کالا</span>
        </router-link>

        <div class="h-px bg-slate-800/80 my-5 mx-4 relative"><div class="absolute left-1/2 -translate-x-1/2 -top-1 w-2 h-2 bg-slate-900 border border-slate-800 rounded-full"></div></div>
        
        <div class="text-[10px] font-black text-slate-500 mb-3 px-2 tracking-widest uppercase mt-4">سیستم و پیکربندی</div>

        <router-link to="/admin/cms" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 01-2-2h10a2 2 0 012 2v12a2 2 0 01-2 2zM9 15h6"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">محتوا و بنرها (CMS)</span>
        </router-link>

        <router-link to="/admin/settings" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center gap-3 px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          <span class="group-hover:-translate-x-1 transition-transform">تنظیمات پلتفرم</span>
        </router-link>

        <router-link to="/admin/notifications" active-class="bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/20 font-black border-transparent" class="flex items-center justify-between px-4 py-3.5 rounded-xl text-slate-400 font-bold hover:bg-slate-900 hover:text-white transition-all duration-300 border border-transparent hover:border-slate-800 group">
          <div class="flex items-center gap-3">
            <svg class="w-5 h-5 opacity-70 group-[.router-link-active]:opacity-100 group-[.router-link-active]:text-slate-900 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"></path></svg>
            <span class="group-hover:-translate-x-1 transition-transform">سیستم اطلاعیه‌ها</span>
          </div>
        </router-link>

      </nav>

      <!-- ================= دکمه خروج ================= -->
      <div class="p-4 mt-auto border-t border-slate-800/80 bg-slate-950/50">
        <button @click="logout" class="w-full flex items-center justify-center gap-2 bg-slate-900 hover:bg-rose-600/90 text-slate-400 hover:text-white font-bold py-4 rounded-xl transition-colors duration-300 text-sm border border-slate-800 hover:border-rose-500 shadow-sm group">
          <svg class="w-5 h-5 transition-transform group-hover:-translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          خروج از سیستم
        </button>
      </div>
    </aside>

    <!-- Overlay موبایل -->
    <div v-if="isSidebarOpen" @click="isSidebarOpen = false" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-40 lg:hidden transition-opacity"></div>

    <!-- ================= محتوای اصلی (هدر + روتر ویو) ================= -->
    <div class="flex-1 flex flex-col min-w-0 h-screen overflow-hidden bg-slate-950 relative">
      <!-- گرید بک‌گراند اختصاصی پنل ادمین -->
      <div class="absolute inset-0 z-0 pointer-events-none" style="background-image: radial-gradient(#1e293b 1px, transparent 1px); background-size: 24px 24px; opacity: 0.4;"></div>
      
      <!-- هدر تاپ‌بار -->
      <header class="h-20 bg-slate-950/80 backdrop-blur-2xl border-b border-slate-800/80 flex items-center justify-between px-4 lg:px-8 z-30 sticky top-0 shadow-sm relative">
        <div class="flex items-center gap-4">
          <button @click="isSidebarOpen = true" class="lg:hidden p-2.5 bg-slate-900 rounded-xl text-slate-300 hover:text-amber-500 border border-slate-800 transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path></svg>
          </button>
          
          <div class="hidden md:flex items-center gap-2 bg-emerald-500/10 border border-emerald-500/20 px-4 py-2.5 rounded-xl shadow-inner">
             <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_10px_rgba(16,185,129,0.8)]"></span>
             <span class="text-xs font-black text-emerald-400 tracking-wider">سیستم در وضعیت پایدار (OK)</span>
          </div>
        </div>

        <div class="flex items-center gap-4 lg:gap-5">
          
          <!-- دکمه نوتیفیکیشن -->
          <button @click="clearNotification" class="relative p-2.5 text-slate-400 hover:text-amber-400 transition-colors bg-slate-900 border border-slate-800 rounded-xl hover:border-amber-500/50 shadow-sm group">
            <svg class="w-5 h-5 group-hover:animate-swing" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
            <span v-if="hasNotification" class="absolute top-0 right-0 w-3 h-3 bg-rose-500 border-2 border-slate-900 rounded-full animate-pulse shadow-[0_0_10px_rgba(244,63,94,0.8)]"></span>
          </button>
          
          <!-- دکمه خروج هدر -->
          <button @click="logout" class="p-2.5 text-slate-400 hover:text-rose-500 transition-colors bg-slate-900 border border-slate-800 rounded-xl hover:border-rose-500/50 shadow-sm tooltip" title="خروج از سیستم">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          </button>

          <div class="w-px h-8 bg-slate-800/80"></div>

          <!-- پروفایل ادمین -->
          <div class="flex items-center gap-3 pl-2 pr-3 py-1.5 bg-slate-900/80 border border-slate-800 rounded-2xl shadow-inner cursor-pointer hover:bg-slate-800 transition-colors">
            <div class="text-left mr-2">
              <p class="text-xs font-black text-white">{{ adminName }}</p>
              <p class="text-[9px] font-bold text-slate-500 mt-0.5 uppercase tracking-widest">Admin Role</p>
            </div>
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-400 to-orange-600 text-slate-950 flex items-center justify-center font-black text-lg shadow-md border border-amber-300/30">
              <svg v-if="adminName === 'Super Admin'" class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12zm8.706-1.442c1.146-.573 2.437.463 2.126 1.706l-.709 2.836.042-.02a.75.75 0 01.67 1.34l-.04.022c-1.147.573-2.438-.463-2.127-1.706l.71-2.836-.042.02a.75.75 0 11-.671-1.34l.041-.022zM12 9a.75.75 0 100-1.5.75.75 0 000 1.5z" clip-rule="evenodd"></path></svg>
              <span v-else>{{ adminInitial }}</span>
            </div>
          </div>
        </div>
      </header>

      <!-- محل قرارگیری ویوها -->
      <main class="flex-1 overflow-y-auto p-4 lg:p-8 relative custom-scrollbar-dark z-10">
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

const adminName = ref('Super Admin');
const adminInitial = ref('S');

onMounted(() => {
  const name = localStorage.getItem('full_name') || localStorage.getItem('user_name');
  if (name && name !== 'null' && name !== 'undefined' && name !== 'کاربر سیستم') {
    adminName.value = name;
    adminInitial.value = name.charAt(0);
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
/* استایل‌های اختصاصی دارک مود ادمین */
.custom-scrollbar-dark::-webkit-scrollbar { width: 6px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; border: 1px solid #0f172a; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: #475569; }

/* انیمیشن زنگوله نوتیفیکیشن */
@keyframes swing {
  20% { transform: rotate(15deg); }
  40% { transform: rotate(-10deg); }
  60% { transform: rotate(5deg); }
  80% { transform: rotate(-5deg); }
  100% { transform: rotate(0deg); }
}
.animate-swing { animation: swing 1s ease-in-out; }

/* Tooltip (در صورت عدم استفاده از لایبرری اکسترنال) */
.tooltip { position: relative; }
.tooltip:hover::after {
  content: attr(title);
  position: absolute;
  top: 120%;
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
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  border: 1px solid #334155;
}
</style>