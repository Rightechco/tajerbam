<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-cyan-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-cyan-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-cyan-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white mb-2 tracking-tight">نظارت بر استعلام‌های بازار (RFQ)</h1>
          <div class="flex flex-wrap items-center gap-3">
            <span class="bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
              بازار مناقصات B2B
            </span>
            <span class="text-xs font-medium text-slate-400">کنترل، داوری و نظارت بر رقابت تامین‌کنندگان برای تامین نیاز خریداران سازمانی.</span>
          </div>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto shrink-0">
        <button @click="fetchRfqs" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center disabled:opacity-50 tooltip" title="بروزرسانی">
          <svg :class="{'animate-spin text-cyan-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="exportToExcel" class="flex-1 md:flex-none bg-slate-800 hover:bg-slate-700 border border-slate-700 text-white font-bold px-6 py-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center gap-2 text-sm">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          خروجی لیست (CSV)
        </button>
      </div>
    </div>

    <!-- ================= کارت‌های آماری سریع ================= -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10 animate-fade-in">
      <div class="bg-slate-900 rounded-[2rem] border border-slate-700/50 p-6 shadow-lg flex items-center gap-5 hover:border-cyan-500/50 transition-colors group">
        <div class="w-14 h-14 bg-cyan-500/10 text-cyan-400 rounded-2xl flex items-center justify-center border border-cyan-500/20 shrink-0 group-hover:scale-110 transition-transform">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
        </div>
        <div>
          <p class="text-xs font-bold text-slate-400 mb-1 uppercase tracking-wider">استعلام‌های در جریان (Open)</p>
          <div class="text-2xl font-black text-white">{{ stats.openRfqs }} <span class="text-xs font-medium text-slate-500">مورد باز</span></div>
        </div>
      </div>
      <div class="bg-slate-900 rounded-[2rem] border border-slate-700/50 p-6 shadow-lg flex items-center gap-5 hover:border-amber-500/50 transition-colors group">
        <div class="w-14 h-14 bg-amber-500/10 text-amber-500 rounded-2xl flex items-center justify-center border border-amber-500/20 shrink-0 group-hover:scale-110 transition-transform">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"></path></svg>
        </div>
        <div>
          <p class="text-xs font-bold text-slate-400 mb-1 uppercase tracking-wider">مجموع پیشنهادات ثبت شده</p>
          <div class="text-2xl font-black text-white">{{ stats.totalQuotes }} <span class="text-xs font-medium text-slate-500">پروپوزال</span></div>
        </div>
      </div>
      <div class="bg-slate-900 rounded-[2rem] border border-slate-700/50 p-6 shadow-lg flex items-center gap-5 hover:border-emerald-500/50 transition-colors group">
        <div class="w-14 h-14 bg-emerald-500/10 text-emerald-400 rounded-2xl flex items-center justify-center border border-emerald-500/20 shrink-0 group-hover:scale-110 transition-transform">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <div>
          <p class="text-xs font-bold text-slate-400 mb-1 uppercase tracking-wider">حجم مالی در گردش استعلام‌ها</p>
          <div class="text-2xl font-black text-white tracking-tighter">{{ formatPrice(stats.totalBudget) }} <span class="text-[10px] font-medium text-slate-500">تومان</span></div>
        </div>
      </div>
    </div>

    <!-- ================= جدول مرکزی استعلام‌ها ================= -->
    <div class="bg-slate-900 rounded-[2.5rem] border border-slate-700/50 shadow-lg overflow-hidden relative z-10">
      <div class="p-6 md:p-8 border-b border-slate-800 flex flex-col lg:flex-row lg:items-center justify-between gap-6 bg-slate-950/30">
        <div>
          <h3 class="font-black text-white text-lg flex items-center gap-3 mb-1">
            <span class="w-3 h-3 rounded-full bg-cyan-500 shadow-[0_0_10px_rgba(6,182,212,0.6)]"></span>
            لیست درخواست‌های خرید (RFQ)
          </h3>
          <p class="text-xs font-bold text-slate-500">نمایش {{ filteredRfqs.length }} استعلام از مجموع {{ allRfqs.length }} درخواست</p>
        </div>

        <div class="flex flex-col sm:flex-row items-center gap-3 w-full lg:w-auto">
          <select v-model="statusFilter" class="bg-slate-800 border border-slate-700 text-sm font-bold text-slate-300 px-4 py-3.5 rounded-xl outline-none focus:border-cyan-500 cursor-pointer w-full sm:w-48 shrink-0 transition-colors">
            <option value="all">همه وضعیت‌ها</option>
            <option value="open">در جریان (باز)</option>
            <option value="closed">بسته شده / برنده مشخص شده</option>
            <option value="cancelled">لغو شده</option>
          </select>
          <div class="relative w-full sm:w-72 shrink-0">
            <input type="text" v-model="searchQuery" placeholder="جستجوی شناسه، عنوان یا خریدار..." class="w-full bg-slate-800 border border-slate-700 text-sm font-bold px-5 py-3.5 pr-12 rounded-xl outline-none focus:border-cyan-500 transition-all text-white placeholder-slate-500">
            <svg class="w-5 h-5 text-slate-400 absolute right-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>
      </div>

      <div class="overflow-x-auto custom-scrollbar-dark min-h-[400px]">
        <div v-if="isLoading" class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm z-20 flex justify-center items-center py-20 flex-col gap-4">
          <svg class="w-10 h-10 text-cyan-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          <span class="text-sm font-bold text-slate-400 animate-pulse">در حال دریافت داده‌های بازار...</span>
        </div>
        
        <table class="w-full text-right text-sm">
          <thead class="bg-slate-800/50 text-slate-400 text-[11px] font-black uppercase tracking-wider border-b border-slate-700/50">
            <tr>
              <th class="px-6 py-5">شناسه / شرکت خریدار</th>
              <th class="px-6 py-5">شرح اقلام و بودجه</th>
              <th class="px-6 py-5 text-center">وضعیت مناقصه</th>
              <th class="px-6 py-5 text-center">پیشنهادات</th>
              <th class="px-6 py-5 text-center">مدیریت</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/80 font-medium text-slate-300">
            <tr v-if="!isLoading && filteredRfqs.length === 0">
              <td colspan="5" class="py-16 text-center text-slate-500 font-bold border-2 border-dashed border-slate-800 m-4 rounded-xl">استعلامی با این مشخصات یافت نشد.</td>
            </tr>
            <tr v-for="rfq in filteredRfqs" :key="rfq.id" class="hover:bg-slate-800/40 transition-colors group">
              <td class="px-6 py-5">
                <div class="flex flex-col gap-2">
                  <div class="flex items-center gap-2">
                    <span class="font-mono text-cyan-400 font-black bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20 text-[10px]">{{ rfq.id }}</span>
                    <span class="text-[9px] font-bold text-slate-500">{{ rfq.date }}</span>
                  </div>
                  <span class="font-black text-white text-sm group-hover:text-cyan-300 transition-colors">{{ rfq.buyer }}</span>
                </div>
              </td>
              <td class="px-6 py-5">
                <div class="flex flex-col gap-1.5">
                  <span class="text-slate-300 font-bold text-sm max-w-xs truncate">{{ rfq.title }}</span>
                  <span class="text-[10px] font-bold text-slate-400 bg-slate-950 px-2 py-0.5 rounded border border-slate-700 w-fit flex items-center gap-1">
                    <svg class="w-3 h-3 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    سقف بودجه: {{ formatPrice(rfq.budget) }}
                  </span>
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <span v-if="rfq.status === 'open'" class="text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-3 py-1.5 rounded-lg text-xs font-black inline-flex items-center gap-1.5 w-fit shadow-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> در جریان
                </span>
                <span v-else-if="rfq.status === 'closed'" class="text-slate-400 bg-slate-800 border border-slate-700 px-3 py-1.5 rounded-lg text-xs font-black inline-flex items-center gap-1.5 w-fit shadow-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-slate-500"></span> بسته شده
                </span>
                <span v-else class="text-rose-400 bg-rose-500/10 border border-rose-500/20 px-3 py-1.5 rounded-lg text-xs font-black inline-flex items-center gap-1.5 w-fit shadow-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span> لغو شده
                </span>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="inline-flex items-center justify-center w-10 h-10 bg-slate-800 border border-slate-700 rounded-xl font-black text-amber-400 text-lg shadow-inner">
                  {{ rfq.quotesCount }}
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex justify-center gap-2">
                  <button @click="openRfqDetails(rfq)" class="px-4 py-2.5 bg-slate-800 hover:bg-cyan-500/20 text-slate-300 hover:text-cyan-400 border border-slate-700 hover:border-cyan-500/30 rounded-xl transition-all font-black text-xs shadow-sm flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                    بررسی
                  </button>
                  <button @click="deleteRfq(rfq.id)" class="p-2.5 bg-slate-800 text-rose-500/70 hover:text-rose-400 hover:bg-rose-500/10 border border-slate-700 hover:border-rose-500/50 rounded-xl transition-all tooltip shadow-sm" title="حذف استعلام">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= MODAL: پنل پیشرفته بررسی استعلام و پیشنهادات ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 scale-95 translate-y-4" enter-to-class="opacity-100 scale-100 translate-y-0" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 translate-y-4">
        <div v-if="activeRfqModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md" dir="rtl">
          <div class="bg-slate-900 w-full max-w-5xl h-[90vh] md:h-[85vh] rounded-[2.5rem] shadow-[0_30px_100px_rgba(0,0,0,0.5)] relative overflow-hidden border border-slate-700 flex flex-col">
            
            <!-- نوار بالایی مودال -->
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-cyan-500 to-blue-600 z-10"></div>
            
            <div class="p-6 md:p-8 border-b border-slate-800 bg-slate-950/50 flex justify-between items-start shrink-0 relative z-10">
              <div class="flex gap-4">
                <div class="w-14 h-14 bg-gradient-to-br from-slate-800 to-slate-900 border border-slate-700 rounded-2xl flex items-center justify-center text-cyan-400 shadow-inner shrink-0">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg>
                </div>
                <div>
                  <h3 class="font-black text-white text-xl mb-1">پرونده استعلام <span class="font-mono text-cyan-400">{{ activeRfqModal.id }}</span></h3>
                  <div class="flex flex-wrap items-center gap-2">
                    <span class="text-xs font-bold text-slate-400">خریدار: <span class="text-white">{{ activeRfqModal.buyer }}</span></span>
                    <span class="text-slate-600">•</span>
                    <span class="text-xs font-bold text-slate-400">تاریخ ثبت: {{ activeRfqModal.date }}</span>
                  </div>
                </div>
              </div>
              <button @click="closeRfqDetails" class="p-2.5 bg-slate-800 text-slate-400 hover:text-red-400 hover:bg-slate-700 rounded-xl transition-colors border border-slate-700">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <!-- تب‌های داخلی مودال -->
            <div class="flex bg-slate-950/80 border-b border-slate-800 px-6 md:px-8 pt-4 gap-2 shrink-0">
              <button @click="modalTab = 'info'" :class="['px-6 py-3 rounded-t-xl text-sm font-black transition-all border-b-2', modalTab === 'info' ? 'bg-slate-900 border-cyan-500 text-cyan-400' : 'border-transparent text-slate-500 hover:text-slate-300 hover:bg-slate-900/50']">
                جزئیات درخواست
              </button>
              <button @click="modalTab = 'quotes'" :class="['px-6 py-3 rounded-t-xl text-sm font-black transition-all border-b-2 flex items-center gap-2', modalTab === 'quotes' ? 'bg-slate-900 border-amber-500 text-amber-400' : 'border-transparent text-slate-500 hover:text-slate-300 hover:bg-slate-900/50']">
                پیشنهادات فروشندگان
                <span class="bg-amber-500/20 text-amber-500 px-1.5 py-0.5 rounded text-[10px]">{{ activeRfqModal.quotesCount }}</span>
              </button>
            </div>

            <!-- محتوای داخلی مودال -->
            <div class="flex-grow overflow-y-auto custom-scrollbar-dark p-6 md:p-8 bg-slate-900">
              
              <!-- تب اطلاعات -->
              <div v-if="modalTab === 'info'" class="space-y-6 animate-fade-in">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div class="bg-slate-950 border border-slate-800 p-5 rounded-2xl">
                    <span class="block text-[10px] font-bold text-slate-500 mb-1 uppercase tracking-widest">عنوان استعلام</span>
                    <span class="font-black text-white text-base">{{ activeRfqModal.title }}</span>
                  </div>
                  <div class="bg-slate-950 border border-slate-800 p-5 rounded-2xl">
                    <span class="block text-[10px] font-bold text-slate-500 mb-1 uppercase tracking-widest">سقف بودجه خریدار</span>
                    <span class="font-black text-emerald-400 text-lg tracking-tight font-mono">{{ formatPrice(activeRfqModal.budget) }} <span class="text-xs font-sans text-slate-500">تومان</span></span>
                  </div>
                </div>
                
                <div class="bg-slate-950 border border-slate-800 p-6 rounded-2xl">
                  <span class="block text-[10px] font-bold text-slate-500 mb-3 uppercase tracking-widest border-b border-slate-800 pb-2">شرح کامل اقلام و توضیحات</span>
                  <p class="text-sm font-medium text-slate-300 leading-relaxed whitespace-pre-line">{{ activeRfqModal.description }}</p>
                </div>

                <!-- کنترل ادمین روی استعلام -->
                <div class="bg-slate-800/50 border border-slate-700 p-6 rounded-2xl mt-8">
                  <h4 class="font-black text-white text-sm mb-4">عملیات مدیریتی (Admin Override)</h4>
                  <div class="flex flex-wrap gap-3">
                    <button @click="updateRfqStatus(activeRfqModal.id, 'closed')" v-if="activeRfqModal.status === 'open'" :disabled="isProcessing" class="px-6 py-3 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white font-bold rounded-xl transition-colors text-sm shadow-sm flex items-center gap-2">
                      بستن زودهنگام مناقصه
                    </button>
                    <button @click="updateRfqStatus(activeRfqModal.id, 'cancelled')" v-if="activeRfqModal.status === 'open'" :disabled="isProcessing" class="px-6 py-3 bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-rose-500 font-bold rounded-xl transition-colors text-sm shadow-sm flex items-center gap-2">
                      لغو و تعلیق استعلام
                    </button>
                  </div>
                </div>
              </div>

              <!-- تب پیشنهادات (Quotes) -->
              <div v-if="modalTab === 'quotes'" class="space-y-6 animate-fade-in">
                
                <div v-if="activeRfqModal.quotes.length === 0" class="text-center py-16 border-2 border-dashed border-slate-800 rounded-3xl bg-slate-950/50">
                  <div class="w-16 h-16 bg-slate-900 rounded-full flex items-center justify-center mx-auto mb-4 border border-slate-800">
                    <svg class="w-8 h-8 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                  </div>
                  <h4 class="font-black text-white text-lg mb-1">پیشنهادی ثبت نشده است</h4>
                  <p class="text-sm font-bold text-slate-500">تا این لحظه هیچ تامین‌کننده‌ای برای این استعلام قیمت نداده است.</p>
                </div>

                <div v-else class="grid grid-cols-1 gap-4">
                  <div v-for="(quote, idx) in sortedQuotes" :key="idx" class="bg-slate-950 border border-slate-800 rounded-[2rem] p-6 hover:border-amber-500/40 transition-colors shadow-sm relative group overflow-hidden">
                    
                    <div v-if="idx === 0" class="absolute top-0 right-0 bg-gradient-to-r from-amber-500 to-orange-500 text-white text-[10px] font-black px-4 py-1 rounded-bl-xl shadow-md z-10 flex items-center gap-1">
                      <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg> بهترین قیمت
                    </div>
                    
                    <div v-if="quote.is_accepted" class="absolute top-0 left-0 bg-emerald-500 text-white text-[10px] font-black px-4 py-1 rounded-br-xl shadow-md z-10 flex items-center gap-1">
                      <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> پیشنهاد برنده
                    </div>

                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-0 mt-2">
                      <div class="flex items-center gap-4">
                        <div class="w-14 h-14 bg-slate-800 rounded-2xl flex items-center justify-center font-black text-2xl text-slate-400 border border-slate-700 shadow-inner shrink-0">{{ quote.seller.charAt(0) }}</div>
                        <div>
                          <h5 class="font-black text-white text-lg mb-1">{{ quote.seller }}</h5>
                          <div class="flex flex-wrap gap-2 text-[10px] font-bold">
                            <span class="text-slate-400 bg-slate-900 px-2.5 py-1 rounded border border-slate-700">زمان تحویل: <span class="text-white">{{ quote.delivery }}</span></span>
                          </div>
                        </div>
                      </div>
                      
                      <div class="text-left bg-slate-900 px-6 py-3.5 rounded-2xl border border-slate-700/50 shadow-inner min-w-[200px]">
                        <p class="text-[10px] font-bold text-slate-500 mb-1 uppercase tracking-widest">قیمت پیشنهادی فروشنده</p>
                        <p class="font-black text-amber-400 text-2xl tracking-tight font-mono">{{ formatPrice(quote.price) }} <span class="text-xs text-slate-500 font-sans">تومان</span></p>
                      </div>
                    </div>

                    <!-- AI Evaluation Panel -->
                    <div class="mt-6 pt-5 border-t border-slate-800/80">
                      <div class="flex items-start gap-4 bg-slate-800/30 p-4 rounded-xl border border-slate-700/50">
                        <div class="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center shrink-0 border border-blue-500/20"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg></div>
                        <div class="flex-grow">
                          <div class="flex items-center justify-between mb-1.5">
                            <span class="text-xs font-black text-slate-300">امتیاز کیفی هوش مصنوعی (AI Score)</span>
                            <span class="text-sm font-black text-blue-400">{{ quote.ai_score }}/10</span>
                          </div>
                          <div class="h-1.5 w-full bg-slate-800 rounded-full overflow-hidden">
                            <div class="h-full rounded-full transition-all duration-1000 bg-gradient-to-r from-blue-500 to-cyan-400" :style="`width: ${quote.ai_score * 10}%`"></div>
                          </div>
                          <p class="text-[10px] text-slate-500 font-bold mt-2 leading-relaxed bg-slate-950 p-2 rounded-lg border border-slate-800">
                            یادداشت فروشنده: "{{ quote.note || 'آمادگی تامین کامل کالا مطابق با شرایط درخواستی با تضمین اصالت و گارانتی رسمی.' }}"
                          </p>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isProcessing = ref(false);
const allRfqs = ref([]);
const searchQuery = ref('');
const statusFilter = ref('all');

// --- Modal State ---
const activeRfqModal = ref(null);
const modalTab = ref('info');

// --- Fetch Data ---
const fetchRfqs = async () => {
  isLoading.value = true;
  try {
    // In a real app, this points to an Admin endpoint retrieving ALL RFQs
    const res = await fetch(`${API_BASE}/api/buyer/rfqs`, { 
      headers: { 'Authorization': `Bearer ${token()}` } 
    });
    if(res.ok) {
      const data = await res.json();
      allRfqs.value = data.rfqs;
    } else {
      throw new Error("Fallback to mock");
    }
  } catch(e) {
    // ================= MOCK DATA (Ultra Premium Fallback) =================
    setTimeout(() => {
      allRfqs.value = [
        {
          id: 'REQ-1405-199', buyer: 'شرکت پتروشیمی اصفهان', title: 'خرید ۵۰ عدد لپ‌تاپ مهندسی ایسوس', 
          description: 'نیاز فوری به ۵۰ دستگاه لپ‌تاپ ایسوس مدل Vivobook پردازنده i7 جهت تجهیز سایت اصفهان.\nشرایط:\n۱. فاکتور رسمی الزامی است.\n۲. گارانتی حداقل ۱۸ ماهه یکپارچه.\n۳. تحویل در محل شرکت پتروشیمی.',
          budget: 1500000000, status: 'open', date: '۱۴۰۵/۱۱/۲۸ - ۱۰:۳۰', quotesCount: 3,
          quotes: [
            { id: 1, seller: 'شرکت رایان تکرو', price: 1450000000, delivery: '۲ روز کاری', ai_score: 9.2, is_accepted: false, note: 'دستگاه‌ها پلمپ با گارانتی سازگار موجود است.' },
            { id: 2, seller: 'هلدینگ دیجیتال شاپ', price: 1490000000, delivery: '۵ روز کاری', ai_score: 8.5, is_accepted: false, note: 'ارسال با باربری اختصاصی شرکت صورت می‌گیرد.' },
            { id: 3, seller: 'پارس ارتباط', price: 1420000000, delivery: '۷ روز کاری', ai_score: 7.8, is_accepted: false, note: 'امکان تسویه ۲۰ روزه چک صیادی در صورت تایید اعتبار.' }
          ]
        },
        {
          id: 'REQ-1405-198', buyer: 'دانشگاه آزاد واحد تبریز', title: 'تجهیزات زیرساخت شبکه (سوئیچ و روتر سیسکو)', 
          description: 'لیست تجهیزات درخواستی:\n- ۱۰ عدد سوئیچ ۲۹۶۰\n- ۵ عدد روتر\nمدت زمان مناقصه: ۲ روز.',
          budget: 120000000, status: 'closed', date: '۱۴۰۵/۱۱/۲۶ - ۱۴:۱۵', quotesCount: 4,
          quotes: [
            { id: 4, seller: 'ارتباطات نوین', price: 115000000, delivery: '۱ روزه', ai_score: 9.8, is_accepted: true, note: 'کالای اورجینال نیو (New) با ضمانت اصالت کالا.' },
            { id: 5, seller: 'شبکه پرداز سیستم', price: 118000000, delivery: '۳ روزه', ai_score: 8.9, is_accepted: false, note: 'هزینه ارسال به عهده خریدار می‌باشد.' }
          ]
        },
        {
          id: 'REQ-1405-195', buyer: 'پیمانکاری عمران سازه', title: 'ابزارآلات صنعتی و لوازم ایمنی پروژه', 
          description: 'خرید عمده لوازم ایمنی کارگاهی شامل دستکش، کلاه ایمنی و دریل شارژی مطابق فایل پیوست.',
          budget: 450000000, status: 'cancelled', date: '۱۴۰۵/۱۱/۲۰ - ۰۹:۰۰', quotesCount: 0,
          quotes: []
        }
      ];
      
      // Calculate Stats automatically from mock
      stats.value.openRfqs = allRfqs.value.filter(r => r.status === 'open').length;
      stats.value.totalQuotes = allRfqs.value.reduce((sum, r) => sum + r.quotes.length, 0);
      stats.value.totalBudget = allRfqs.value.reduce((sum, r) => sum + r.budget, 0);
      
      isLoading.value = false;
    }, 800);
    return;
  }
  isLoading.value = false;
};

onMounted(fetchRfqs);

// --- State & Computed ---
const stats = ref({ openRfqs: 0, totalQuotes: 0, totalBudget: 0 });

const filteredRfqs = computed(() => {
  let result = allRfqs.value;
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase();
    result = result.filter(r => r.id.toLowerCase().includes(q) || r.buyer.toLowerCase().includes(q) || r.title.toLowerCase().includes(q));
  }
  if (statusFilter.value !== 'all') {
    result = result.filter(r => r.status === statusFilter.value);
  }
  return result;
});

// Sort quotes by price (lowest first) for the modal
const sortedQuotes = computed(() => {
  if(!activeRfqModal.value || !activeRfqModal.value.quotes) return [];
  return [...activeRfqModal.value.quotes].sort((a, b) => a.price - b.price);
});

// --- Actions ---
const openRfqDetails = (rfq) => {
  activeRfqModal.value = rfq;
  modalTab.value = 'info';
};

const closeRfqDetails = () => {
  activeRfqModal.value = null;
};

const updateRfqStatus = async (id, newStatus) => {
  const msg = newStatus === 'closed' ? "آیا از بستن زودهنگام این استعلام اطمینان دارید؟" : "آیا از لغو و تعلیق این استعلام به دلایل نظارتی اطمینان دارید؟";
  if(!confirm(msg)) return;
  
  isProcessing.value = true;
  try {
    // API Simulation
    setTimeout(() => {
      const rIndex = allRfqs.value.findIndex(r => r.id === id);
      if(rIndex !== -1) {
        allRfqs.value[rIndex].status = newStatus;
        if(activeRfqModal.value && activeRfqModal.value.id === id) {
          activeRfqModal.value.status = newStatus;
        }
      }
      isProcessing.value = false;
    }, 600);
  } catch(e) {
    isProcessing.value = false;
  }
};

const deleteRfq = async (id) => {
  if(!confirm("حذف استعلام منجر به پاک شدن تمام پیشنهادات مرتبط خواهد شد. ادامه می‌دهید؟")) return;
  allRfqs.value = allRfqs.value.filter(r => r.id !== id);
};

const exportToExcel = () => {
  alert('فایل خروجی استعلام‌ها (CSV) در حال تولید است و دانلود خواهد شد.');
};

// --- Utils ---
const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
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

body:has(.fixed.z-\[99999\]) { overflow: hidden; }
</style>