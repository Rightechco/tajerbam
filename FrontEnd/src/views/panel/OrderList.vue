<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800" dir="rtl">
    
    <!-- ================= هدر صفحه ================= -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-5 md:p-6 rounded-[2rem] border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.02)] relative z-10">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center shadow-inner relative shrink-0">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
          <span v-if="!hasActivePlan" class="absolute -top-1 -right-1 w-3.5 h-3.5 bg-amber-500 border-2 border-white rounded-full"></span>
          <span v-if="totalUnreadMessages > 0" class="absolute -top-2 -left-2 w-5 h-5 bg-rose-500 text-white text-[10px] font-black flex items-center justify-center border-2 border-white rounded-full shadow-md animate-bounce">{{ totalUnreadMessages }}</span>
        </div>
        <div>
          <h1 class="text-xl md:text-2xl font-black text-slate-800 tracking-tight">مدیریت سفارشات B2B</h1>
          <p class="text-xs font-bold mt-1" :class="hasActivePlan ? 'text-emerald-600' : 'text-amber-600'">
            {{ hasActivePlan ? 'اشتراک طلایی شما فعال است (صفر درصد کمیسیون).' : `کارمزد پلتفرم: ${platformFeePercent}% - جهت دسترسی به مشتریان کمیسیون را تسویه کنید.` }}
          </p>
        </div>
      </div>
      <div class="flex flex-wrap items-center gap-3">
        <button @click="fetchOrders" :disabled="isLoading" class="bg-slate-50 border border-slate-200 text-slate-600 hover:bg-slate-100 font-bold p-2.5 rounded-xl transition-all shadow-sm flex items-center justify-center cursor-pointer" title="به‌روزرسانی">
          <svg :class="['w-5 h-5', {'animate-spin text-blue-600': isLoading}]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="exportExcel" :disabled="isExporting" class="bg-emerald-50 border border-emerald-200 text-emerald-700 hover:bg-emerald-100 font-bold px-5 py-2.5 rounded-xl transition-all shadow-sm flex items-center gap-2 text-sm disabled:opacity-70 cursor-pointer">
          <svg v-if="!isExporting" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 01-2-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          <svg v-else class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          {{ isExporting ? 'در حال خروجی...' : 'خروجی اکسل / CSV' }}
        </button>
      </div>
    </div>

    <!-- ================= کارت‌های آماری ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
      
      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-2 h-full bg-emerald-500"></div>
        <div class="flex items-center justify-between mb-4">
          <span class="text-slate-500 text-xs font-bold">جمع فروش قطعی</span>
          <div class="w-10 h-10 bg-emerald-50 text-emerald-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        </div>
        <div class="text-2xl font-black text-slate-800">{{ formatPrice(stats.totalRevenue) }} <span class="text-[10px] font-bold text-slate-400">تومان</span></div>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-2 h-full bg-blue-500"></div>
        <div class="flex items-center justify-between mb-4">
          <span class="text-slate-500 text-xs font-bold">سفارشات تحویل شده</span>
          <div class="w-10 h-10 bg-blue-50 text-blue-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        </div>
        <div class="text-2xl font-black text-slate-800">{{ stats.shippedCount }} <span class="text-[10px] font-bold text-slate-400">سفارش</span></div>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-2 h-full bg-amber-500"></div>
        <div class="flex items-center justify-between mb-4">
          <span class="text-slate-500 text-xs font-bold">در انتظار پردازش</span>
          <div class="w-10 h-10 bg-amber-50 text-amber-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
        </div>
        <div class="text-2xl font-black text-slate-800">{{ stats.pendingCount }} <span class="text-[10px] font-bold text-slate-400">سفارش</span></div>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-2 h-full bg-purple-500"></div>
        <div class="flex items-center justify-between mb-4">
          <span class="text-slate-500 text-xs font-bold">کل سفارشات B2B</span>
          <div class="w-10 h-10 bg-purple-50 text-purple-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg></div>
        </div>
        <div class="text-2xl font-black text-slate-800">{{ orders.length }} <span class="text-[10px] font-bold text-slate-400">سفارش</span></div>
      </div>
    </div>

    <!-- ================= فیلترها و عملیات گروهی ================= -->
    <div class="bg-white p-4 rounded-[1.5rem] border border-slate-100 shadow-sm flex flex-col lg:flex-row gap-4 justify-between items-center transition-all relative z-10">
      
      <div class="flex flex-col md:flex-row items-center gap-3 w-full lg:w-auto">
        <div class="relative w-full md:w-80">
          <input type="text" v-model="searchQuery" placeholder="جستجوی نام خریدار یا کد سفارش..." class="w-full bg-slate-50 border border-slate-200 text-sm font-medium text-slate-800 px-4 py-3 pr-10 rounded-xl focus:bg-white focus:border-blue-400 outline-none transition-all">
          <svg class="w-4 h-4 text-slate-400 absolute right-3 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        
        <select v-model="filterStatus" class="w-full md:w-48 bg-slate-50 border border-slate-200 text-sm font-bold text-slate-600 px-4 py-3 rounded-xl outline-none focus:border-blue-400 cursor-pointer">
          <option value="all">همه وضعیت‌ها</option>
          <option value="pending">در انتظار تایید</option>
          <option value="processing">در حال پردازش</option>
          <option value="shipped">ارسال شده (باربری)</option>
          <option value="delivered">تحویل شده</option>
        </select>
      </div>
      
      <transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100">
        <div v-if="selectedOrders.length > 0" class="flex flex-wrap items-center justify-center gap-2 bg-blue-50 border border-blue-100 px-4 py-2 rounded-xl w-full lg:w-auto">
          <span class="text-xs font-black text-blue-800 ml-2">{{ selectedOrders.length }} انتخاب</span>
          <button @click="openBulkLabels" class="text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg transition-colors shadow-sm flex items-center gap-1 cursor-pointer">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"></path></svg>
            چاپ گروهی لیبل‌ها
          </button>
        </div>
      </transition>
    </div>

    <!-- ================= جدول سفارشات ================= -->
    <div class="bg-white border border-slate-100 rounded-[2.5rem] shadow-[0_8px_30px_rgb(0,0,0,0.03)] overflow-hidden relative z-10">
      <div class="overflow-x-auto custom-scrollbar min-h-[400px]">
        <table class="w-full text-right text-sm">
          <thead class="bg-slate-50 text-slate-500 text-[11px] font-black uppercase tracking-wider border-b border-slate-200/80">
            <tr>
              <th class="px-6 py-5 w-12 text-center">
                <input type="checkbox" @change="toggleAll" :checked="selectedOrders.length === filteredOrders.length && filteredOrders.length > 0" class="w-4 h-4 rounded text-blue-600 border-slate-300 cursor-pointer">
              </th>
              <th class="px-6 py-5">اطلاعات خریدار (هوشمند)</th>
              <th class="px-6 py-5">نوع ارسال و تسویه</th>
              <th class="px-6 py-5">مبلغ نهایی (تومان)</th>
              <th class="px-6 py-5 text-center">وضعیت</th>
              <th class="px-6 py-5 text-center">عملیات</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100/80 font-medium text-slate-700">
            
            <tr v-if="isLoading" v-for="i in 3" :key="i" class="animate-pulse">
              <td class="px-6 py-5"></td>
              <td class="px-6 py-5"><div class="flex items-center gap-4"><div class="w-11 h-11 bg-slate-100 rounded-full"></div><div class="space-y-2"><div class="h-3 bg-slate-100 rounded w-24"></div><div class="h-2 bg-slate-100 rounded w-16"></div></div></div></td>
              <td class="px-6 py-5"><div class="space-y-2"><div class="h-3 bg-slate-100 rounded w-20"></div><div class="h-2 bg-slate-100 rounded w-16"></div></div></td>
              <td class="px-6 py-5"><div class="h-4 bg-slate-100 rounded w-20"></div></td>
              <td class="px-6 py-5 text-center"><div class="h-6 bg-slate-100 rounded-xl w-20 mx-auto"></div></td>
              <td class="px-6 py-5"><div class="flex justify-center gap-2"><div class="w-9 h-9 bg-slate-100 rounded-xl"></div><div class="w-9 h-9 bg-slate-100 rounded-xl"></div></div></td>
            </tr>

            <tr v-else-if="filteredOrders.length === 0">
              <td colspan="6" class="text-center py-16 text-slate-400 font-bold">هیچ سفارشی مطابق با جستجو یا فیلتر یافت نشد.</td>
            </tr>

            <tr v-else v-for="order in filteredOrders" :key="order.db_id" class="hover:bg-slate-50/50 transition-colors group" :class="{'bg-slate-50/30': !canViewDetails(order)}">
              <td class="px-6 py-5 text-center">
                <input type="checkbox" :value="order" v-model="selectedOrders" class="w-4 h-4 rounded text-blue-600 border-slate-300 cursor-pointer">
              </td>
              
              <!-- اطلاعات خریدار (قفل یا باز) -->
              <td class="px-6 py-5">
                <div class="flex items-start gap-4">
                  <div class="w-11 h-11 rounded-full flex items-center justify-center font-black text-lg shadow-inner shrink-0 border transition-all"
                       :class="canViewDetails(order) ? 'bg-gradient-to-tr from-blue-100 to-indigo-100 text-blue-600 border-blue-200' : 'bg-slate-100 text-slate-400 border-slate-200'">
                    <svg v-if="!canViewDetails(order)" class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                    <span v-else>{{ order.customer ? order.customer.charAt(0) : 'خ' }}</span>
                  </div>
                  
                  <div>
                    <h3 class="font-black text-sm flex items-center gap-2" :class="canViewDetails(order) ? 'text-slate-800' : 'text-slate-500'">
                      <template v-if="canViewDetails(order)">{{ order.customer }}</template>
                      <template v-else><span class="blur-[4px] select-none">شرکت خریدار مخفی</span></template>
                    </h3>
                    
                    <div class="flex items-center gap-2 mt-1.5">
                      <span class="text-[11px] font-mono font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded">ID: {{ order.id }}</span>
                      <span v-if="!canViewDetails(order)" class="text-[11px] font-mono text-slate-400 bg-slate-50 px-1.5 py-0.5 rounded border border-slate-200" dir="ltr">091X XXX XXXX</span>
                      <span v-else class="text-[11px] font-mono text-slate-600 bg-slate-50 px-1.5 py-0.5 rounded border border-slate-200" dir="ltr">{{ order.phone }}</span>
                    </div>

                    <div class="mt-3 flex items-center gap-2">
                      <button v-if="!canViewDetails(order)" @click="openUnlockModal(order)" class="text-[11px] font-bold bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-200 px-3 py-1.5 rounded-lg shadow-sm transition-all flex items-center gap-1.5 cursor-pointer">
                        تسویه کمیسیون و مشاهده
                      </button>
                      <button v-else @click="openChat(order)" class="relative text-[11px] font-bold bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 px-3 py-1.5 rounded-lg shadow-sm transition-all flex items-center gap-1.5 cursor-pointer">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                        چت زنده با خریدار
                        <span v-if="order.unread_count > 0" class="absolute -top-1.5 -right-1.5 w-4 h-4 bg-rose-500 text-white text-[9px] font-black flex items-center justify-center rounded-full border-2 border-white animate-pulse shadow-sm">{{ order.unread_count }}</span>
                      </button>
                    </div>
                  </div>
                </div>
              </td>
              
              <!-- ارسال و تسویه -->
              <td class="px-6 py-5">
                <div class="space-y-1.5">
                  <span v-if="order.paymentMethod === 'cod'" class="inline-flex items-center bg-amber-50 text-amber-700 text-[10px] font-black px-2 py-0.5 rounded border border-amber-200">
                    پرداخت در مقصد / پس‌کرایه
                  </span>
                  <span v-else class="inline-flex items-center bg-emerald-50 text-emerald-700 text-[10px] font-black px-2 py-0.5 rounded border border-emerald-200">
                    تسویه آنلاین / امانی (Escrow)
                  </span>
                  <div class="text-[11px] font-bold text-slate-500">
                    {{ order.shipping === 'cargo' ? 'باربری سنگین' : 'پست پیشتاز' }}
                  </div>
                </div>
              </td>
              
              <td class="px-6 py-5 font-black text-slate-800 text-base">
                {{ formatPrice(order.total) }}
              </td>

              <!-- وضعیت -->
              <td class="px-6 py-5 text-center">
                <span v-if="order.status === 'pending'" class="inline-flex bg-amber-50 text-amber-600 border border-amber-200 px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm">در انتظار تایید</span>
                <span v-else-if="order.status === 'processing'" class="inline-flex bg-blue-50 text-blue-600 border border-blue-200 px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm">در حال پردازش</span>
                <span v-else-if="order.status === 'shipped'" class="inline-flex bg-purple-50 text-purple-600 border border-purple-200 px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm">ارسال شده</span>
                <span v-else-if="order.status === 'delivered'" class="inline-flex bg-emerald-50 text-emerald-600 border border-emerald-200 px-3 py-1.5 rounded-xl text-xs font-bold shadow-sm">تحویل شده</span>
              </td>

              <!-- عملیات -->
              <td class="px-6 py-5 text-center">
                <div class="flex items-center justify-center gap-2">
                  <button @click="handleAction(order, 'details')" title="مشاهده جزئیات سفارش" class="w-9 h-9 flex items-center justify-center rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-indigo-600 hover:border-indigo-300 transition-all shadow-sm cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                  </button>
                  <button @click="handleAction(order, 'invoice')" title="چاپ فاکتور" class="w-9 h-9 flex items-center justify-center rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-blue-600 hover:border-blue-300 transition-all shadow-sm cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                  </button>
                  <button @click="handleAction(order, 'label')" title="چاپ لیبل پستی" class="w-9 h-9 flex items-center justify-center rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-emerald-600 hover:border-emerald-300 transition-all shadow-sm cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"></path></svg>
                  </button>
                  <button @click="openReportModal(order)" title="گزارش مشکل به ادمین" class="w-9 h-9 flex items-center justify-center rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-rose-600 hover:border-rose-300 hover:bg-rose-50 transition-all shadow-sm cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
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
      
      <!-- ۱. مودال آزادسازی اطلاعات و پرداخت کمیسیون -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="orderToUnlock" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-md rounded-[2.5rem] shadow-2xl relative overflow-hidden font-sans border border-slate-100">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-amber-400 via-orange-500 to-amber-600"></div>
            
            <div class="p-8 text-center relative">
              <button @click="closeUnlockModal" class="absolute top-6 left-6 text-slate-400 hover:text-slate-700 bg-slate-50 w-8 h-8 rounded-full flex items-center justify-center transition-colors cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
              <div class="w-16 h-16 bg-amber-100 text-amber-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-amber-200 shadow-inner">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              </div>
              <h2 class="text-xl font-black text-slate-800 mb-2">باز کردن قفل اطلاعات خریدار</h2>
              <p class="text-xs font-bold text-slate-500 leading-relaxed px-4">
                نرخ کارمزد پلتفرم <span class="text-amber-600 font-black">{{ platformFeePercent }}%</span> می‌باشد. جهت مشاهده شماره تماس، آدرس و شروع چت، کمیسیون سفارش را تسویه کنید.
              </p>
            </div>

            <div class="p-6 bg-slate-50 border-t border-slate-100 space-y-4">
              <div class="bg-amber-50/60 border border-amber-200 rounded-2xl p-4 flex justify-between items-center">
                <span class="text-xs font-bold text-slate-600">کمیسیون این سفارش:</span>
                <span class="font-black text-amber-600 text-lg">{{ formatPrice(calculateCommission(orderToUnlock.total)) }} <span class="text-xs font-bold text-slate-500">تومان</span></span>
              </div>

              <button @click="payCommission" :disabled="isUnlocking" class="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-black py-4 rounded-xl shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center gap-2 text-sm cursor-pointer disabled:opacity-50">
                <svg v-if="isUnlocking" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>پرداخت از کیف پول و آزادسازی آنی</span>
              </button>
            </div>
          </div>
        </div>
      </transition>

      <!-- ۲. مودال جزئیات و تغییر وضعیت -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="detailsOrder" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-4xl max-h-[90vh] overflow-y-auto rounded-[2.5rem] shadow-2xl relative font-sans flex flex-col custom-scrollbar border border-slate-200">
            
            <div class="bg-slate-50 border-b border-slate-200 p-6 flex justify-between items-center sticky top-0 z-20">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-slate-200 flex items-center justify-center text-blue-600">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
                </div>
                <div>
                  <h2 class="text-xl font-black text-slate-800">جزئیات سفارش {{ detailsOrder.id }}</h2>
                  <p class="text-xs font-bold text-slate-500 mt-1">خریدار: {{ detailsOrder.customer }} | ثبت: {{ detailsOrder.date }}</p>
                </div>
              </div>
              <button @click="detailsOrder = null" class="w-10 h-10 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 transition-colors cursor-pointer">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="p-6 md:p-8 flex-grow grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
              <div class="lg:col-span-2 space-y-6">
                <h3 class="font-black text-slate-800 border-b border-slate-100 pb-3 flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-blue-500"></span> اقلام سفارش داده شده
                </h3>
                <div class="space-y-4">
                  <div v-for="(item, idx) in detailsOrder.items" :key="idx" class="flex gap-4 p-4 border border-slate-100 rounded-2xl bg-white shadow-sm">
                    <div class="w-16 h-16 bg-slate-50 rounded-xl p-2 shrink-0 border border-slate-100 flex items-center justify-center">
                      <img :src="item.img || 'https://via.placeholder.com/150'" class="max-h-full max-w-full object-contain mix-blend-multiply">
                    </div>
                    <div class="flex-grow flex flex-col justify-between">
                      <h4 class="font-bold text-slate-800 text-sm">{{ item.name }}</h4>
                      <div class="flex justify-between items-end mt-2">
                        <span class="text-xs font-bold text-slate-500 bg-slate-100 px-2 py-1 rounded-md">{{ item.qty }} عدد</span>
                        <div class="text-left">
                          <span class="text-[10px] text-slate-400 block mb-0.5">قیمت واحد: {{ formatPrice(item.price) }}</span>
                          <span class="text-sm font-black text-blue-700">{{ formatPrice(item.price * item.qty) }} تومان</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="lg:col-span-1 space-y-6">
                <div class="bg-slate-50 border border-slate-200 p-5 rounded-2xl">
                  <h3 class="font-black text-slate-800 mb-3 text-sm">وضعیت ارسال و پردازش</h3>
                  <select v-model="detailsOrder.status" class="w-full bg-white border border-slate-300 text-sm font-bold text-slate-700 p-3 rounded-xl outline-none focus:border-blue-500 shadow-sm cursor-pointer">
                    <option value="pending">در انتظار تایید</option>
                    <option value="processing">در حال پردازش (بسته‌بندی)</option>
                    <option value="shipped">ارسال شده (تحویل باربری)</option>
                    <option value="delivered">تحویل شده به خریدار</option>
                  </select>
                </div>

                <div class="bg-emerald-50 border border-emerald-100 p-5 rounded-2xl">
                  <h3 class="font-black text-emerald-800 mb-3 flex items-center gap-1.5 text-sm">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                    اطلاعات گیرنده
                  </h3>
                  <p class="text-xs font-bold text-emerald-800 mb-1">{{ detailsOrder.customer }}</p>
                  <p class="text-xs font-mono font-bold text-emerald-700" dir="ltr">{{ detailsOrder.phone }}</p>
                  <p class="text-[11px] font-medium text-emerald-600 mt-2 pt-2 border-t border-emerald-200/60">آدرس: {{ detailsOrder.address }}</p>
                </div>
              </div>
            </div>
            
            <div class="p-6 bg-slate-50 border-t border-slate-200 flex justify-end gap-3">
              <button @click="detailsOrder = null" class="bg-white border border-slate-200 text-slate-600 font-bold px-6 py-3 rounded-xl hover:bg-slate-100 cursor-pointer">انصراف</button>
              <button @click="saveOrderDetails" :disabled="isUpdating" class="bg-slate-900 text-white font-bold px-8 py-3 rounded-xl hover:bg-black shadow-md flex items-center justify-center gap-2 cursor-pointer">
                <svg v-if="isUpdating" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                ذخیره وضعیت
              </button>
            </div>
          </div>
        </div>
      </transition>

      <!-- ۳. چت زنده و پریمیوم با خریدار -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
        <div v-if="chatOrder" class="fixed bottom-0 left-0 md:bottom-6 md:left-6 z-[99999] w-full md:w-[420px] h-[600px] md:h-[550px] bg-white md:rounded-[2rem] rounded-t-[2rem] shadow-2xl flex flex-col font-sans border border-slate-200 overflow-hidden" dir="rtl">
          <div class="bg-slate-900 text-white p-4 flex items-center justify-between shrink-0">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center font-black text-white shadow-inner">{{ chatOrder.customer ? chatOrder.customer.charAt(0) : 'C' }}</div>
              <div>
                <h3 class="font-black text-sm">{{ chatOrder.customer }}</h3>
                <p class="text-[10px] text-emerald-400 font-bold flex items-center gap-1"><span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></span> گفتگو آنلاین سفارش {{ chatOrder.id }}</p>
              </div>
            </div>
            <button @click="closeChat" class="w-8 h-8 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors cursor-pointer"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
          </div>

          <!-- بدنه پیام‌ها -->
          <div ref="chatContainer" class="flex-grow bg-slate-50 p-4 overflow-y-auto space-y-3 custom-scrollbar">
             <div v-if="isLoadingMessages" class="text-center py-8"><div class="w-6 h-6 border-2 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto"></div></div>
             <div v-else-if="chatMessages.length === 0" class="text-center py-10 text-slate-400 text-xs font-bold">هیچ پیامی تبادل نشده است. گفتگو را شروع کنید!</div>
             
             <div v-else v-for="msg in chatMessages" :key="msg.id" :class="['flex flex-col', msg.sender === 'seller' ? 'items-end' : 'items-start']">
               <div :class="['max-w-[85%] p-3.5 rounded-2xl text-xs font-medium leading-relaxed shadow-sm', msg.sender === 'seller' ? 'bg-indigo-600 text-white rounded-tl-none' : 'bg-white text-slate-800 border border-slate-200 rounded-tr-none']">
                 <p>{{ msg.text }}</p>
                 <span :class="['block text-[9px] mt-1 text-left font-mono opacity-70', msg.sender === 'seller' ? 'text-indigo-100' : 'text-slate-400']">{{ msg.time }}</span>
               </div>
             </div>
          </div>

          <!-- فرم ارسال پیام -->
          <div class="p-3 bg-white border-t border-slate-200 flex items-center gap-2 shrink-0">
            <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="پیام خود را بنویسید..." class="flex-grow bg-slate-50 border border-slate-200 text-xs font-bold px-4 py-3 rounded-full outline-none focus:border-indigo-500 transition-colors">
            <button @click="sendMessage" :disabled="!newMessage.trim()" class="w-10 h-10 bg-indigo-600 hover:bg-indigo-700 text-white rounded-full flex items-center justify-center shadow-md disabled:opacity-50 cursor-pointer">
              <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            </button>
          </div>
        </div>
      </transition>

      <!-- ۴. مودال فاکتور رسمی -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="activeInvoice" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm print:p-0 print:bg-transparent print:block" dir="rtl">
          <div class="bg-white w-full max-w-4xl max-h-[90vh] overflow-y-auto rounded-3xl shadow-2xl relative print:max-h-none print:shadow-none print:w-full print:m-0 flex flex-col print:block">
            
            <div class="p-8 md:p-10 flex-grow">
              <div class="flex justify-between items-center border-b-2 border-slate-800 pb-6 mb-8">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 bg-black rounded-xl flex items-center justify-center text-white font-black text-2xl">ت</div>
                  <div>
                    <h2 class="text-2xl font-black text-slate-800">فاکتور رسمی فروش B2B</h2>
                    <p class="text-xs font-bold text-slate-500 mt-1">پلتفرم تجارت عمده تاجربام</p>
                  </div>
                </div>
                <div class="text-left text-xs font-bold text-slate-600 space-y-1">
                  <p>شماره فاکتور: {{ activeInvoice.id }}</p>
                  <p>تاریخ صدور: {{ activeInvoice.date }}</p>
                </div>
              </div>
              
              <div class="grid grid-cols-2 gap-8 mb-8 border-2 border-slate-800 rounded-2xl p-6">
                <div>
                  <h3 class="font-black text-slate-800 mb-2 border-b border-slate-200 pb-2 text-xs">مشخصات فروشنده</h3>
                  <p class="text-xs font-bold text-slate-800">تامین‌کننده معتبر تاجربام</p>
                </div>
                <div>
                  <h3 class="font-black text-slate-800 mb-2 border-b border-slate-200 pb-2 text-xs">مشخصات خریدار</h3>
                  <p class="text-xs font-bold text-slate-800">نام: {{ activeInvoice.customer }}</p>
                  <p class="text-xs font-bold text-slate-800 mt-1">تلفن: {{ activeInvoice.phone }}</p>
                  <p class="text-xs font-bold text-slate-800 mt-1">آدرس: {{ activeInvoice.address }}</p>
                </div>
              </div>

              <table class="w-full text-right text-xs border-2 border-slate-800 mb-10">
                <thead class="bg-slate-100 font-black text-slate-800 border-b-2 border-slate-800">
                  <tr>
                    <th class="p-3 border-l border-slate-300 w-12 text-center">ردیف</th>
                    <th class="p-3 border-l border-slate-300">شرح کالا</th>
                    <th class="p-3 border-l border-slate-300 text-center">تعداد</th>
                    <th class="p-3 border-l border-slate-300">قیمت واحد (تومان)</th>
                    <th class="p-3">قیمت کل (تومان)</th>
                  </tr>
                </thead>
                <tbody class="font-bold text-slate-700">
                  <tr v-for="(item, idx) in activeInvoice.items" :key="idx" class="border-b border-slate-300">
                    <td class="p-3 border-l border-slate-300 text-center">{{ idx + 1 }}</td>
                    <td class="p-3 border-l border-slate-300">{{ item.name }}</td>
                    <td class="p-3 border-l border-slate-300 text-center">{{ item.qty }}</td>
                    <td class="p-3 border-l border-slate-300">{{ formatPrice(item.price) }}</td>
                    <td class="p-3">{{ formatPrice(item.price * item.qty) }}</td>
                  </tr>
                </tbody>
              </table>

              <div class="flex justify-end mb-12">
                <div class="w-1/2 bg-slate-50 border-2 border-slate-800 p-4 rounded-xl text-sm font-black text-slate-800 flex justify-between">
                  <span>مبلغ کل فاکتور:</span>
                  <span>{{ formatPrice(activeInvoice.total) }} تومان</span>
                </div>
              </div>
            </div>
            
            <div class="bg-slate-50 p-6 flex justify-end gap-3 print:hidden border-t border-slate-200">
              <button @click="activeInvoice = null" class="px-6 py-2.5 rounded-xl font-bold bg-white border border-slate-200 text-slate-600 text-xs">بستن</button>
              <button onclick="window.print()" class="px-6 py-2.5 rounded-xl font-bold bg-blue-600 text-white shadow-md text-xs flex items-center gap-2 cursor-pointer"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg> چاپ فاکتور</button>
            </div>
          </div>
        </div>
      </transition>

      <!-- ۵. چاپ لیبل پستی گروهی/تکی -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="labelsToPrint.length > 0" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm print:p-0 print:bg-transparent print:block" dir="rtl">
          <div class="bg-slate-100 w-full max-w-3xl max-h-[90vh] overflow-y-auto rounded-3xl shadow-2xl relative print:max-h-none print:shadow-none print:w-full print:m-0 print:bg-white flex flex-col print:block">
            
            <div class="bg-white p-4 border-b border-slate-200 flex justify-between items-center sticky top-0 z-10 print:hidden">
              <h3 class="font-black text-slate-800 text-sm">تعداد لیبل: {{ labelsToPrint.length }} ردیف</h3>
              <div class="flex gap-2">
                <button @click="labelsToPrint = []" class="px-4 py-2 rounded-lg font-bold bg-white border border-slate-200 text-slate-600 text-xs">لغو</button>
                <button onclick="window.print()" class="px-6 py-2 rounded-lg font-bold bg-indigo-600 text-white shadow-md text-xs cursor-pointer">چاپ نهایی</button>
              </div>
            </div>

            <div class="p-6 flex-grow space-y-8 print:p-0 print:space-y-0">
              <div v-for="label in labelsToPrint" :key="label.id" class="print-page bg-white border-2 border-black rounded-2xl p-8 shadow-sm mx-auto w-full max-w-2xl">
                
                <div class="flex justify-between items-start border-b-2 border-black pb-4 mb-6">
                  <div class="text-right">
                    <h2 class="text-2xl font-black mb-1">لیبل ارسال محموله</h2>
                    <p class="text-xs font-bold text-slate-600">پلتفرم تجارت عمده تاجربام</p>
                  </div>
                  <div class="w-40 h-12 border-2 border-black flex items-center justify-center font-mono font-black text-2xl tracking-widest">
                    ||| | || ||
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-6 mb-6 border-b-2 border-black pb-8">
                  <div class="border-l-2 border-black pr-2">
                    <span class="text-xs font-black bg-black text-white px-3 py-1 rounded">فرستنده</span>
                    <p class="mt-4 text-sm font-bold text-black">تامین‌کننده تاجربام</p>
                  </div>
                  <div class="pr-4">
                    <span class="text-xs font-black bg-black text-white px-3 py-1 rounded">گیرنده</span>
                    <div class="mt-4 space-y-1.5 text-sm font-bold text-black">
                      <p class="text-base font-black">{{ label.customer }}</p>
                      <p>تلفن: <span dir="ltr">{{ label.phone }}</span></p>
                      <p>آدرس: {{ label.address }}</p>
                    </div>
                  </div>
                </div>

                <div class="flex justify-between items-end font-bold text-black">
                  <p class="text-sm">کد سفارش: <span class="font-mono font-black">{{ label.id }}</span></p>
                  <div class="text-left border-2 border-black p-3 rounded-xl">
                    <p class="text-xs font-black">روش ارسال:</p>
                    <p class="text-xl font-black">{{ label.shipping === 'cargo' ? 'باربری (پس‌کرایه)' : 'پست پیشتاز' }}</p>
                  </div>
                </div>

              </div>
            </div>

          </div>
        </div>
      </transition>

      <!-- ۶. مودال گزارش مشکل به ادمین -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="reportModal.show" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6" dir="rtl">
          <div class="absolute inset-0 bg-slate-900/70 backdrop-blur-sm" @click="closeReportModal"></div>
          
          <div class="bg-white w-full max-w-lg rounded-[2.5rem] shadow-2xl relative z-10 overflow-hidden font-sans border border-slate-200">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-rose-500 to-red-600"></div>
            
            <div class="p-6 border-b border-slate-100 bg-slate-50 flex justify-between items-center">
              <h3 class="font-black text-slate-800 text-base">ثبت شکایات و گزارش اختلاف</h3>
              <button @click="closeReportModal" class="w-8 h-8 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-500 hover:text-red-500 transition-colors cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="p-6 space-y-4">
              <div>
                <label class="block text-xs font-black text-slate-600 mb-1.5">موضوع اختلاف</label>
                <select v-model="reportForm.reason" class="w-full bg-slate-50 border border-slate-200 text-xs font-bold text-slate-700 py-3 px-3.5 rounded-xl outline-none focus:bg-white focus:border-rose-400 transition-all cursor-pointer">
                  <option value="" disabled selected>انتخاب موضوع...</option>
                  <option value="fake_claim">ادعای کذب خریدار در خصوص کیفیت</option>
                  <option value="no_confirm">عدم تایید تحویل کالا با وجود بارنامه</option>
                  <option value="fraud">مشکل در تسویه یا عدم پاسخگویی</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-600 mb-1.5">توضیحات</label>
                <textarea v-model="reportForm.description" rows="3" placeholder="جزئیات موضوع را شرح دهید..." class="w-full bg-slate-50 border border-slate-200 text-xs font-medium text-slate-800 p-3.5 rounded-xl outline-none focus:bg-white focus:border-rose-400 transition-all resize-none"></textarea>
              </div>
            </div>

            <div class="bg-slate-50 border-t border-slate-100 p-4 flex justify-end gap-3">
              <button @click="closeReportModal" class="px-5 py-2.5 rounded-xl font-bold bg-white border border-slate-200 text-slate-600 text-xs">انصراف</button>
              <button @click="submitReport" :disabled="!reportForm.reason" class="px-6 py-2.5 rounded-xl font-black bg-rose-600 hover:bg-rose-700 text-white text-xs disabled:opacity-50 cursor-pointer">ارسال گزارش</button>
            </div>
          </div>
        </div>
      </transition>

      <!-- توست اطلاع‌رسانی -->
      <transition name="toast-fade">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[999999] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-3 border', toast.type === 'error' ? 'bg-rose-600 border-rose-500' : 'bg-slate-900 border-slate-700']">
          <div :class="['w-8 h-8 rounded-full flex items-center justify-center shrink-0', toast.type === 'error' ? 'bg-white/20' : 'bg-emerald-500/20 text-emerald-400']">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm">{{ toast.title }}</h4>
            <p class="text-xs text-slate-300 mt-0.5">{{ toast.message }}</p>
          </div>
        </div>
      </transition>

    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';

const getApiBaseUrl = () => {
  if (typeof window !== 'undefined' && window.location.origin) {
    if (window.location.origin.includes(':8000')) return window.location.origin;
  }
  return 'https://tajerbam.com';
};

const API_BASE_URL = getApiBaseUrl();

// دریافت دقیق توکن احراز هویت کاربر از تمامی کلیدهای احتمالی مرورگر
const getToken = () => {
  return localStorage.getItem('tajerbam_token') || 
         localStorage.getItem('access_token') || 
         localStorage.getItem('token') || 
         localStorage.getItem('auth_token') || 
         'test-token';
};

const hasActivePlan = ref(false);
const platformFeePercent = ref(5);
const isLoading = ref(true);
const isUpdating = ref(false);
const isExporting = ref(false);
const isUnlocking = ref(false);

const orders = ref([]);
const totalUnreadMessages = ref(0);
let pollingInterval = null;

// توست اطلاع‌رسانی
const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

// دریافت سفارشات واقعی تامین‌کننده از دیتابیس (بدون هیچ‌گونه ماک دیتا)
const fetchOrders = async () => {
  isLoading.value = true;
  const token = getToken();

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders`, {
      headers: { 
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });
    if (res.ok) {
      const data = await res.json();
      hasActivePlan.value = data.hasActivePlan || false;
      platformFeePercent.value = data.platform_fee_percent || 5;
      
      // مپینگ خالص داده‌های دیتابیس بدون مقادیر پیش‌فرض فرضی
      orders.value = (data.orders || []).map(o => ({
        db_id: o.db_id,
        id: o.id,
        customer: o.customer || o.buyer?.name || 'خریدار B2B',
        phone: o.phone || o.buyer?.phone || '---',
        address: o.address || o.buyer?.address || '---',
        type: o.type || 'wholesale',
        shipping: o.shipping || 'cargo',
        paymentMethod: o.payment_method || 'escrow',
        status: o.status || 'pending',
        total: o.total || 0,
        date: o.date || '---',
        isCommissionPaid: o.is_commission_paid || false,
        unread_count: o.unread_count || 0,
        items: o.items || []
      }));
      
      totalUnreadMessages.value = orders.value.reduce((sum, order) => sum + (order.unread_count || 0), 0);
    } else {
      orders.value = [];
      showToast('اطلاعیه', 'هیچ سفارشی در دیتابیس یافت نشد.', 'error');
    }
  } catch (e) {
    console.error("Fetch orders database error:", e);
    orders.value = [];
    showToast('خطای ارتباط', 'ارتباط با سرور دیتابیس برقرار نشد.', 'error');
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchOrders();
  startBackgroundPolling();
});

const startBackgroundPolling = () => {
  pollingInterval = setInterval(async () => {
    if (isUnlocking.value || isUpdating.value || isExporting.value) return; 
    
    try {
      const res = await fetch(`${API_BASE_URL}/api/seller/orders`, {
        headers: { 
          'Authorization': `Bearer ${getToken()}`,
          'Content-Type': 'application/json'
        }
      });
      
      if (res.ok) {
        const data = await res.json();
        let hasNewMessage = false;
        let newTotalUnread = 0;

        (data.orders || []).forEach(newOrder => {
          const existingOrder = orders.value.find(o => o.db_id === newOrder.db_id);
          const newUnread = newOrder.unread_count || 0;
          
          if (existingOrder) {
            if (chatOrder.value && chatOrder.value.db_id === existingOrder.db_id) {
               // کاربر در حال چت با همین سفارش است، بج افزایش پیدا نمی‌کند
            } else if (newUnread > (existingOrder.unread_count || 0)) {
              hasNewMessage = true;
              existingOrder.unread_count = newUnread;
              showToast('پیام جدید', `پیام جدیدی در گفتگو با خریدار "${existingOrder.customer || 'B2B'}" دریافت کردید.`, 'success');
            }
            newTotalUnread += existingOrder.unread_count || 0;
          }
        });
        
        if(hasNewMessage) {
          totalUnreadMessages.value = newTotalUnread;
        }
      }
    } catch (e) {
      // نادیده گرفتن خطاهای پس‌زمینه (برای جلوگیری از مزاحمت)
    }
  }, 10000); // چک کردن خاموش هر ۱۰ ثانیه
};

// محاسبات آماری بر اساس رکوردهای واقعی موجود
const stats = computed(() => {
  const shipped = orders.value.filter(o => o.status === 'shipped' || o.status === 'delivered');
  const pending = orders.value.filter(o => o.status === 'pending');
  return {
    shippedCount: shipped.length,
    pendingCount: pending.length,
    totalRevenue: shipped.reduce((acc, o) => acc + o.total, 0)
  };
});

const searchQuery = ref('');
const filterStatus = ref('all');
const selectedOrders = ref([]);

const filteredOrders = computed(() => {
  let result = orders.value;
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase();
    result = result.filter(o => String(o.id).toLowerCase().includes(q) || (o.customer && String(o.customer).toLowerCase().includes(q)));
  }
  if (filterStatus.value !== 'all') {
    result = result.filter(o => o.status === filterStatus.value);
  }
  return result;
});

const toggleAll = (e) => {
  if (e.target.checked) selectedOrders.value = [...filteredOrders.value];
  else selectedOrders.value = [];
};

const canViewDetails = (order) => {
  return hasActivePlan.value || order.isCommissionPaid;
};

const calculateCommission = (total) => {
  return Math.round((total * platformFeePercent.value) / 100);
};

// مدیریت مودال‌ها
const orderToUnlock = ref(null);
const detailsOrder = ref(null);
const chatOrder = ref(null);
const activeInvoice = ref(null);
const labelsToPrint = ref([]);

const openUnlockModal = (order) => { orderToUnlock.value = order; };
const closeUnlockModal = () => { orderToUnlock.value = null; };

const payCommission = async () => {
  if (!orderToUnlock.value) return;
  isUnlocking.value = true;
  const token = getToken();
  
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders/${orderToUnlock.value.db_id}/unlock-commission`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await res.json();
    if (res.ok && data.success) {
      orderToUnlock.value.isCommissionPaid = true;
      showToast('پرداخت موفق', 'کمیسیون کسر گردید و اطلاعات خریدار نمایان شد.');
      closeUnlockModal();
      await fetchOrders();
    } else {
      showToast('خطا', data.detail || data.message || 'موجودی کیف پول کافی نیست.', 'error');
    }
  } catch (e) {
    showToast('خطا', 'ارتباط با سرور برقرار نشد.', 'error');
  } finally {
    isUnlocking.value = false;
  }
};

const handleAction = (order, actionType) => {
  if (!canViewDetails(order)) {
    openUnlockModal(order);
    return;
  }
  if (actionType === 'details') detailsOrder.value = JSON.parse(JSON.stringify(order));
  if (actionType === 'invoice') activeInvoice.value = order;
  if (actionType === 'label') labelsToPrint.value = [order];
};

const saveOrderDetails = async () => {
  if (!detailsOrder.value) return;
  isUpdating.value = true;
  const token = getToken();

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders/${detailsOrder.value.db_id}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ status: detailsOrder.value.status, progress: 50 })
    });
    if (res.ok) {
      showToast('به‌روزرسانی موفق', 'وضعیت سفارش در دیتابیس ذخیره شد.');
      detailsOrder.value = null;
      await fetchOrders();
    }
  } catch (e) {
    showToast('خطا', 'مشکلی در بروزرسانی رخ داد.', 'error');
  } finally {
    isUpdating.value = false;
  }
};

// ================= چت زنده real-time =================
const chatMessages = ref([]);
const newMessage = ref('');
const isLoadingMessages = ref(false);
const chatContainer = ref(null);
let chatInterval = null;

const openChat = async (order) => {
  chatOrder.value = order;
  
  if (order.unread_count > 0) {
    totalUnreadMessages.value -= order.unread_count;
    if (totalUnreadMessages.value < 0) totalUnreadMessages.value = 0;
    order.unread_count = 0;
  }
  
  await fetchChatMessages();
  chatInterval = setInterval(fetchChatMessages, 3000);
};

const closeChat = () => {
  chatOrder.value = null;
  if (chatInterval) clearInterval(chatInterval);
};

const fetchChatMessages = async () => {
  if (!chatOrder.value) return;
  const token = getToken();

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders/${chatOrder.value.db_id}/messages`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (res.ok) {
      const data = await res.json();
      chatMessages.value = data.messages || [];
      await nextTick();
      if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    }
  } catch (e) {
    console.error("Chat error:", e);
  }
};

const sendMessage = async () => {
  if (!newMessage.value.trim() || !chatOrder.value) return;
  const textToSend = newMessage.value;
  newMessage.value = '';
  const token = getToken();

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders/${chatOrder.value.db_id}/messages`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ text: textToSend, sender: 'seller' })
    });
    if (res.ok) {
      await fetchChatMessages();
    }
  } catch (e) {
    showToast('خطا', 'پیام ارسال نشد.', 'error');
  }
};

// گزارش به ادمین
const reportModal = ref({ show: false, order: null });
const reportForm = ref({ reason: '', description: '' });

const openReportModal = (order) => { reportModal.value = { show: true, order }; reportForm.value = { reason: '', description: '' }; };
const closeReportModal = () => { reportModal.value.show = false; };
const submitReport = () => {
  showToast('گزارش ارسال شد', 'پرونده گزارش اختلاف جهت بررسی خریدار برای پشتیبانی ارسال گردید.');
  closeReportModal();
};

const openBulkLabels = () => {
  const valid = selectedOrders.value.filter(o => canViewDetails(o));
  if (valid.length > 0) labelsToPrint.value = valid;
  else showToast('هشدار', 'ابتدا کمیسیون سفارشات انتخابی را تسویه کنید.', 'error');
};

const exportExcel = () => {
  if (filteredOrders.value.length === 0) return;
  isExporting.value = true;
  
  let csvContent = "\uFEFFشناسه سفارش,خریدار,تلفن,مبلغ کل (تومان),وضعیت,تاریخ\n";
  filteredOrders.value.forEach(o => {
    csvContent += `"${o.id}","${o.customer}","${o.phone}","${o.total}","${o.status}","${o.date}"\n`;
  });

  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", `Orders_Report_${new Date().toISOString().slice(0, 10)}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  
  isExporting.value = false;
  showToast('دانلود فایل', 'گزارش سفارشات با موفقیت استخراج شد.');
};

const formatPrice = (val) => {
  if (!val) return '۰';
  return Number(val).toLocaleString('fa-IR');
};

onUnmounted(() => {
  if (chatInterval) clearInterval(chatInterval);
  if (pollingInterval) clearInterval(pollingInterval);
});
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 5px; height: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }

@media print {
  body * { visibility: hidden !important; }
  .fixed.z-\[99999\], .fixed.z-\[99999\] * { visibility: visible !important; }
  .fixed.z-\[99999\] { position: absolute; left: 0; top: 0; width: 100%; margin: 0; padding: 0; background: transparent; }
  .print-page { page-break-after: always; border: 2px solid black !important; }
}
</style>