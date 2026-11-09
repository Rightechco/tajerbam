<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر صفحه (Premium Header) ================= -->
    <div class="bg-gradient-to-br from-indigo-950 via-slate-900 to-slate-900 p-8 md:p-10 rounded-[2.5rem] border border-indigo-500/20 shadow-[0_20px_50px_-12px_rgba(30,27,75,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      
      <!-- افکت‌های نوری پس‌زمینه -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-indigo-500 rounded-full mix-blend-screen filter blur-[90px] opacity-30 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-fuchsia-600 rounded-full mix-blend-screen filter blur-[80px] opacity-20 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-[1.5rem] border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-indigo-500/20 rounded-[1.5rem] animate-pulse"></div>
          <svg class="w-10 h-10 text-indigo-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
        </div>
        <div>
          <h1 class="text-2xl md:text-3xl font-black text-white tracking-tight mb-2">بازار مناقصات و درخواست‌های خرید (RFQ)</h1>
          <div class="flex flex-wrap items-center gap-3">
            <span v-if="isVip" class="bg-amber-500/10 text-amber-400 border border-amber-500/20 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg>
              حساب کاربری طلایی (دسترسی نامحدود به خریداران)
            </span>
            <span v-else class="bg-slate-800 text-slate-400 border border-slate-700 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"></path></svg>
              حساب پایه (دسترسی محدود)
            </span>
          </div>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto shrink-0">
        <button @click="fetchRequests" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center disabled:opacity-50 tooltip cursor-pointer" title="به‌روزرسانی">
          <svg :class="{'animate-spin text-indigo-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button v-if="!isVip" @click="showUpgradeModal = true" class="flex-1 md:flex-none bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-black px-6 py-3.5 rounded-xl transition-all shadow-[0_10px_20px_rgba(245,158,11,0.3)] hover:-translate-y-1 flex items-center justify-center gap-2 text-sm cursor-pointer">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5 2a1 1 0 011 1v1h1a1 1 0 010 2H6v1a1 1 0 01-2 0V6H3a1 1 0 010-2h1V3a1 1 0 011-1zm0 10a1 1 0 011 1v1h1a1 1 0 110 2H6v1a1 1 0 11-2 0v-1H3a1 1 0 110-2h1v-1a1 1 0 011-1zM12 2a1 1 0 01.967.744L14.146 7.2 17.5 9.134a1 1 0 010 1.732l-3.354 1.935-1.18 4.455a1 1 0 01-1.933 0L9.854 12.8 6.5 10.866a1 1 0 010-1.732l3.354-1.935 1.18-4.455A1 1 0 0112 2z" clip-rule="evenodd"></path></svg>
          ارتقا به فروشنده VIP
        </button>
      </div>
    </div>

    <!-- ================= آمار و فیلترها ================= -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center relative z-10">
      <!-- باکس جستجو و فیلتر -->
      <div class="md:col-span-8 bg-white p-4 rounded-[1.5rem] border border-slate-100 shadow-sm flex flex-col sm:flex-row gap-4 h-full">
        <div class="relative w-full">
          <input type="text" v-model="searchQuery" placeholder="جستجوی کالای درخواستی (مثلاً: لپ‌تاپ، پسته، سیمان)..." class="w-full h-full bg-slate-50 border border-slate-200 text-sm font-black text-slate-800 px-4 py-3.5 pr-12 rounded-xl focus:bg-white focus:border-indigo-400 outline-none transition-all shadow-inner">
          <svg class="w-5 h-5 text-slate-400 absolute right-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        <select v-model="selectedCategory" class="w-full sm:w-56 bg-slate-50 border border-slate-200 text-sm font-bold text-slate-600 px-4 py-3.5 rounded-xl outline-none focus:border-indigo-400 cursor-pointer shadow-sm">
          <option value="all">همه دسته‌بندی‌ها</option>
          <option value="digital">کالای دیجیتال و الکترونیک</option>
          <option value="tools">ابزارآلات و ماشین‌آلات</option>
          <option value="agri">کشاورزی و مواد غذایی</option>
          <option value="construction">مصالح ساختمانی</option>
        </select>
      </div>

      <!-- کارت آمار کوچک -->
      <div class="md:col-span-4 bg-gradient-to-l from-indigo-600 to-blue-600 p-5 rounded-[1.5rem] border border-indigo-500 shadow-lg text-white flex justify-between items-center h-full relative overflow-hidden group">
        <div class="absolute -right-4 -top-10 w-24 h-24 bg-white rounded-full mix-blend-overlay opacity-10 group-hover:scale-150 transition-transform duration-500"></div>
        <div>
          <p class="text-indigo-100 text-xs font-bold mb-1 uppercase tracking-widest">فرصت‌های فعال فروش B2B</p>
          <div class="text-2xl font-black">{{ requests.length }} <span class="text-[10px] font-bold text-indigo-200">استعلام باز</span></div>
        </div>
        <div class="w-12 h-12 bg-white/20 backdrop-blur-md rounded-xl flex items-center justify-center border border-white/20 shadow-inner">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
      </div>
    </div>

    <!-- ================= گرید کارت‌های درخواست خرید ================= -->
    <div class="relative z-10 min-h-[400px]">
      
      <!-- لودینگ -->
      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 gap-4 bg-white/50 rounded-[2.5rem] border border-slate-100 shadow-sm">
        <div class="w-12 h-12 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
        <span class="text-sm font-black text-slate-500 animate-pulse">در حال فراخوانی استعلام‌های زنده از بک‌اند...</span>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- کارت درخواست خرید -->
        <div v-for="request in filteredRequests" :key="request.id" class="bg-white border border-slate-200/80 rounded-[2.5rem] p-6 shadow-sm hover:shadow-[0_15px_40px_rgba(79,70,229,0.08)] hover:border-indigo-200 transition-all duration-500 flex flex-col h-full group relative overflow-hidden">
          
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-indigo-500 to-blue-500 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          
          <!-- هدر کارت (همیشه واضح) -->
          <div class="mb-4 border-b border-slate-100 pb-4 relative z-10">
            <div class="flex justify-between items-start mb-3">
              <h4 class="font-black text-slate-800 text-lg leading-relaxed group-hover:text-indigo-600 transition-colors line-clamp-2">
                {{ request.title }}
              </h4>
              <span v-if="request.isUrgent" class="bg-rose-50 text-rose-600 border border-rose-100 px-2.5 py-1 rounded-lg text-[9px] font-black flex items-center gap-1 shadow-sm shrink-0 mt-1">
                <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse"></span> فوری
              </span>
            </div>
            
            <div class="flex flex-wrap gap-2 text-[11px] font-black">
              <span class="bg-slate-50 border border-slate-200 text-slate-600 px-3 py-1.5 rounded-xl flex items-center gap-1.5 shadow-sm">
                تعداد: <span class="text-indigo-600 font-mono text-xs">{{ formatPrice(request.qty) }}</span> عدد
              </span>
              <span class="bg-slate-50 border border-slate-200 text-slate-500 px-3 py-1.5 rounded-xl flex items-center gap-1.5 shadow-sm">
                مهلت: {{ request.deadline }} روز
              </span>
            </div>
          </div>

          <!-- بدنه کارت (دارای Paywall / Blur Effect) -->
          <div class="relative flex-grow flex flex-col z-10">
            <div :class="{'filter blur-[6px] select-none pointer-events-none opacity-40': !isVip, 'transition-all duration-700 h-full flex flex-col': true}">
              
              <!-- اطلاعات شرکت خریدار -->
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 rounded-xl bg-slate-100 flex items-center justify-center font-black text-slate-500 border border-slate-200 shadow-inner shrink-0">
                  {{ request.company ? request.company.charAt(0) : 'خ' }}
                </div>
                <div>
                  <h3 class="font-black text-slate-700 text-sm flex items-center gap-1">
                    {{ request.company || 'خریدار معتبر B2B' }}
                    <svg v-if="request.verified" class="w-3.5 h-3.5 text-blue-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                  </h3>
                  <p class="text-[10px] font-bold text-slate-400 mt-0.5 flex items-center gap-1">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                    تحویل: {{ request.location || 'سراسر کشور' }}
                  </p>
                </div>
              </div>

              <!-- توضیحات و بودجه -->
              <div class="bg-indigo-50/50 rounded-2xl p-4 border border-indigo-100/50 mb-6 flex-grow shadow-inner">
                <p class="text-[11px] text-slate-600 font-bold mb-4 line-clamp-3 leading-relaxed text-justify">
                  "{{ request.description }}"
                </p>
                <div class="flex items-center justify-between mt-auto border-t border-indigo-100 pt-3">
                  <span class="block text-[10px] font-black text-slate-400 uppercase tracking-widest">بودجه مدنظر</span>
                  <span class="font-black text-indigo-700 text-sm tracking-tight">{{ request.targetPrice ? formatPrice(request.targetPrice) + ' تومان' : 'توافقی' }}</span>
                </div>
              </div>

              <!-- دکمه اکشن VIP -->
              <button v-if="!request.hasQuoted" @click="openQuoteModal(request)" class="w-full mt-auto bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl transition-all hover:-translate-y-1 shadow-[0_10px_20px_rgba(15,23,42,0.2)] flex items-center justify-center gap-2 text-sm cursor-pointer">
                ارسال پیشنهاد قیمت (صدور فاکتور)
                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </button>
              <button v-else disabled class="w-full mt-auto bg-emerald-50 border border-emerald-200 text-emerald-600 font-black py-4 rounded-xl cursor-not-allowed flex items-center justify-center gap-2 text-sm shadow-sm">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                پیشنهاد شما روی میز خریدار قرار دارد
              </button>
            </div>

            <!-- Overlay قفل برای کاربران عادی (Paywall) -->
            <div v-if="!isVip" class="absolute inset-x-0 bottom-0 top-[15%] flex flex-col items-center justify-center z-20 bg-gradient-to-t from-white via-white/95 to-transparent rounded-b-[2rem] p-4 text-center">
               <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-amber-500 shadow-[0_10px_30px_rgba(0,0,0,0.1)] mb-3 border border-slate-100">
                 <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
               </div>
               <span class="text-sm font-black text-slate-800 mb-1">مخصوص فروشندگان طلایی (VIP)</span>
               <p class="text-[11px] font-bold text-slate-500 mb-4 px-4 leading-relaxed">جهت مشاهده نام خریدار، جزئیات کامل و ارسال مستقیم پیش‌فاکتور، حساب خود را ارتقا دهید.</p>
               
               <button @click="showUpgradeModal = true" class="bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-black text-xs px-6 py-3 rounded-xl shadow-lg shadow-amber-500/30 transition-all hover:-translate-y-0.5 cursor-pointer">
                 خرید اشتراک طلایی VIP
               </button>
            </div>
          </div>
        </div>

        <!-- حالت خالی -->
        <div v-if="filteredRequests.length === 0" class="col-span-full py-20 text-center bg-white rounded-[3rem] border border-slate-200 border-dashed">
          <div class="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center mx-auto mb-6 text-slate-300">
            <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <h3 class="text-xl font-black text-slate-800 mb-2">استعلام یا مناقصه‌ای یافت نشد</h3>
          <p class="text-slate-500 font-bold text-sm">خریداران B2B به صورت مداوم در حال ثبت درخواست‌های جدید در پلتفرم هستند.</p>
        </div>

      </div>
    </div>

    <!-- ================= MODAL: ارتقا به حساب طلایی VIP ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="showUpgradeModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-md rounded-[3rem] shadow-2xl relative overflow-hidden font-sans border border-white/20">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-amber-400 via-orange-500 to-amber-600 z-10"></div>
            
            <button @click="showUpgradeModal = false" class="absolute top-6 left-6 z-20 w-10 h-10 bg-slate-50 hover:bg-red-50 text-slate-400 hover:text-red-500 rounded-full flex items-center justify-center transition-colors border border-slate-100 cursor-pointer">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>

            <div class="p-8 text-center relative z-10 pb-6">
              <div class="w-20 h-20 bg-amber-100 text-amber-600 rounded-[2rem] flex items-center justify-center mx-auto mb-5 shadow-inner border border-amber-200">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
              <h2 class="text-2xl font-black text-slate-800 mb-2">باز کردن قفل کامل مناقصات</h2>
              <p class="text-slate-500 font-bold text-xs leading-relaxed mb-6">
                با ارتقاء به فروشنده طلایی، شماره تماس تمامی خریداران عمده را ببینید، حذف کمیسیون فروش دریافت کنید و بدون محدودیت پیش‌فاکتور ارسال کنید.
              </p>
            </div>

            <div class="bg-slate-50 border-t border-slate-100 p-6 space-y-3 relative z-10">
              <button @click="navigateToPlans" class="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-black py-4 rounded-2xl shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center gap-2 text-sm cursor-pointer">
                <span>مشاهده تعرفه‌ها و ارتقاء حساب</span>
                <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </button>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>

    <!-- ================= MODAL: فرم ثبت پیشنهاد قیمت (Quote) ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="activeRequest" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-2xl max-h-[95vh] overflow-y-auto rounded-[2.5rem] shadow-2xl relative font-sans flex flex-col custom-scrollbar border border-slate-200">
            
            <!-- هدر مودال -->
            <div class="bg-white border-b border-slate-100 p-6 flex justify-between items-center sticky top-0 z-20">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-indigo-50 rounded-[1.2rem] border border-indigo-100 flex items-center justify-center text-indigo-600 shrink-0">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                </div>
                <div>
                  <h2 class="text-lg font-black text-slate-800 mb-0.5">صدور پیش‌فاکتور رسمی</h2>
                  <p class="text-xs font-bold text-slate-500">درخواست: {{ activeRequest.title }} (تعداد: {{ formatPrice(activeRequest.qty) }} عدد)</p>
                </div>
              </div>
              <button @click="closeQuoteModal" class="w-9 h-9 bg-slate-50 border border-slate-200 rounded-full flex items-center justify-center text-slate-400 hover:text-red-500 hover:bg-red-50 transition-colors cursor-pointer">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <!-- بدنه فرم -->
            <div class="p-6 md:p-8 space-y-6">
              
              <div class="bg-slate-50 border border-slate-200 p-4 rounded-2xl flex items-start gap-3 shadow-inner">
                <svg class="w-5 h-5 text-indigo-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <div>
                  <p class="text-xs font-black text-slate-700 mb-1 leading-relaxed text-justify">{{ activeRequest.description }}</p>
                  <p class="text-[10px] font-bold text-slate-500">بودجه پیشنهادی خریدار: <span class="text-indigo-600 font-black">{{ activeRequest.targetPrice ? formatPrice(activeRequest.targetPrice) + ' تومان' : 'توافقی' }}</span></p>
                </div>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- قیمت پیشنهادی واحد -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-black text-slate-600 mb-2">قیمت پیشنهادی شما برای هر واحد (تومان) <span class="text-red-500">*</span></label>
                  <div class="relative">
                    <input type="number" v-model="quoteForm.unitPrice" placeholder="مثلاً: ۳۸۵۰۰۰۰۰" class="w-full bg-white border-2 border-slate-200 text-lg font-black text-indigo-700 py-3.5 pl-16 pr-5 rounded-2xl outline-none focus:border-indigo-500 transition-all shadow-sm font-mono text-left" dir="ltr">
                    <span class="absolute left-5 top-4 text-xs font-bold text-slate-400">تومان</span>
                  </div>
                  <p v-if="quoteForm.unitPrice" class="text-xs font-black text-emerald-600 mt-2.5 flex items-center gap-1.5 bg-emerald-50 w-fit px-3 py-1.5 rounded-lg border border-emerald-100">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    مبلغ کل پیش‌فاکتور: {{ formatPrice(quoteForm.unitPrice * activeRequest.qty) }} تومان
                  </p>
                </div>

                <!-- زمان تحویل -->
                <div>
                  <label class="block text-xs font-black text-slate-600 mb-2">زمان آماده‌سازی و تحویل <span class="text-red-500">*</span></label>
                  <select v-model="quoteForm.deliveryTime" class="w-full bg-white border-2 border-slate-200 text-sm font-bold text-slate-700 py-3.5 px-4 rounded-2xl outline-none focus:border-indigo-500 shadow-sm cursor-pointer">
                    <option value="2">فوری (۱ تا ۲ روز کاری)</option>
                    <option value="5">عادی (۳ تا ۵ روز کاری)</option>
                    <option value="10">سفارشی (بیش از یک هفته)</option>
                  </select>
                </div>

                <!-- نحوه ارسال -->
                <div>
                  <label class="block text-xs font-black text-slate-600 mb-2">نحوه ارسال پیشنهادی</label>
                  <select v-model="quoteForm.shipping" class="w-full bg-white border-2 border-slate-200 text-sm font-bold text-slate-700 py-3.5 px-4 rounded-2xl outline-none focus:border-indigo-500 shadow-sm cursor-pointer">
                    <option value="cargo">باربری سنگین (پس‌کرایه)</option>
                    <option value="express">پست پیشتاز ویژه</option>
                    <option value="free">ارسال رایگان اختصاصی</option>
                  </select>
                </div>

                <!-- توضیحات -->
                <div class="md:col-span-2">
                  <label class="block text-xs font-black text-slate-600 mb-2">پیام یا شرایط فروش برای خریدار</label>
                  <textarea v-model="quoteForm.note" rows="3" placeholder="مزایای رقابتی، گارانتی، یا توضیحات ارسال را بنویسید..." class="w-full bg-white border-2 border-slate-200 text-sm font-medium text-slate-800 p-4 rounded-2xl outline-none focus:border-indigo-500 transition-all resize-none shadow-sm leading-relaxed"></textarea>
                </div>
              </div>
            </div>

            <!-- فوتر -->
            <div class="bg-slate-50 border-t border-slate-200 p-6 flex flex-col sm:flex-row items-center justify-between gap-4 sticky bottom-0 z-20">
              <p class="text-[10px] font-bold text-slate-500 sm:w-1/2 leading-relaxed">پس از ثبت، پیش‌فاکتور شما در پنل خریدار قرار گرفته و در صورت تایید، سفارش صادر می‌گردد.</p>
              <button @click="submitQuote" :disabled="isSubmittingQuote || !quoteForm.unitPrice" class="w-full sm:w-auto bg-slate-900 hover:bg-black text-white font-black px-8 py-3.5 rounded-xl shadow-lg transition-all hover:-translate-y-0.5 disabled:opacity-50 flex items-center justify-center gap-2 cursor-pointer">
                <svg v-if="isSubmittingQuote" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>صدور و ارسال پیش‌فاکتور</span>
              </button>
            </div>

          </div>
        </div>
      </transition>
    </Teleport>

    <!-- توست اطلاع‌رسانی -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[100000] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-4 font-sans border', toast.type === 'error' ? 'bg-rose-600 border-rose-500' : 'bg-slate-900 border-slate-700']" dir="rtl">
          <div :class="['w-10 h-10 rounded-xl flex items-center justify-center border shrink-0', toast.type === 'error' ? 'bg-white/20 border-white/30' : 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30']">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm mb-0.5">{{ toast.title }}</h4>
            <p class="text-xs text-slate-300 font-bold leading-relaxed">{{ toast.message }}</p>
          </div>
        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';

const router = useRouter();

const isLoading = ref(true);
const isVip = ref(false);
const showUpgradeModal = ref(false);
const searchQuery = ref('');
const selectedCategory = ref('all');
const requests = ref([]);

const activeRequest = ref(null);
const isSubmittingQuote = ref(false);
const quoteForm = ref({
  unitPrice: null,
  deliveryTime: '5',
  shipping: 'cargo',
  note: ''
});

const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

// فراخوانی استعلام‌ها و وضعیت VIP فروشنده از بک‌اند
const fetchRequests = async () => {
  isLoading.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/rfqs`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    
    if (res.ok) {
      const data = await res.json();
      requests.value = data.rfqs || [];
      isVip.value = data.is_vip || false;
    } else {
      showToast('خطا', 'عدم دریافت لیست مناقصات از سرور.', 'error');
    }
  } catch (error) {
    console.error("Fetch RFQ error:", error);
    showToast('خطا', 'مشکلی در ارتباط با سرور رخ داد.', 'error');
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchRequests();
});

const filteredRequests = computed(() => {
  return requests.value.filter(r => {
    const matchQuery = !searchQuery.value || 
      r.title.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
      (r.company && r.company.toLowerCase().includes(searchQuery.value.toLowerCase()));
    
    return matchQuery;
  });
});

const openQuoteModal = (request) => {
  activeRequest.value = request;
  quoteForm.value = {
    unitPrice: request.targetPrice ? request.targetPrice : null,
    deliveryTime: '5',
    shipping: 'cargo',
    note: ''
  };
};

const closeQuoteModal = () => {
  activeRequest.value = null;
};

const submitQuote = async () => {
  if (!activeRequest.value || !quoteForm.value.unitPrice) return;
  isSubmittingQuote.value = true;

  try {
    const payload = {
      rfq_id: activeRequest.value.db_id || activeRequest.value.id,
      offered_price: Number(quoteForm.value.unitPrice),
      delivery_days: Number(quoteForm.value.deliveryTime),
      shipping: quoteForm.value.shipping,
      note: quoteForm.value.note
    };

    const res = await fetch(`${API_BASE_URL}/api/seller/rfqs/quote`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok && data.success) {
      activeRequest.value.hasQuoted = true;
      closeQuoteModal();
      showToast('پیشنهاد ثبت شد!', 'پیش‌فاکتور شما با موفقیت برای خریدار ارسال گردید.');
    } else {
      showToast('خطا در ثبت', data.detail || data.message || 'ثبت پیشنهاد انجام نشد.', 'error');
    }
  } catch (e) {
    showToast('خطا', 'ارتباط با سرور برقرار نشد.', 'error');
  } finally {
    isSubmittingQuote.value = false;
  }
};

const navigateToPlans = () => {
  showUpgradeModal.value = false;
  router.push('/plans');
};

const formatPrice = (price) => {
  if (!price) return '۰';
  return Number(price).toLocaleString('fa-IR');
};
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.tooltip { position: relative; }
</style>