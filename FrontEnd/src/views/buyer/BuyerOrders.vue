<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر و جستجو (Glassy Hero) ================= -->
    <div class="relative rounded-[2.5rem] bg-slate-900 border border-slate-800 shadow-[0_20px_60px_-15px_rgba(15,23,42,0.5)] overflow-hidden z-10 p-8 md:p-10 flex flex-col md:flex-row items-center justify-between gap-8">
      <div class="absolute -right-20 -top-20 w-72 h-72 bg-blue-600/30 rounded-full mix-blend-screen filter blur-[80px] pointer-events-none"></div>
      <div class="absolute -left-20 -bottom-20 w-72 h-72 bg-indigo-600/30 rounded-full mix-blend-screen filter blur-[80px] pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-[0_10px_25px_rgba(59,130,246,0.4)] text-white transform -rotate-3 hover:rotate-0 transition-transform duration-300 shrink-0">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
        </div>
        <div>
          <h1 class="text-2xl md:text-3xl font-black text-white mb-1 tracking-tight">سفارشات و پیگیری محموله‌ها</h1>
          <p class="text-xs md:text-sm font-bold text-slate-400">پیگیری وضعیت ارسال کالا، گفتگو مستقیم با تامین‌کننده و دریافت فاکتور رسمی.</p>
        </div>
      </div>

      <!-- جستجوی سفارشات -->
      <div class="relative w-full md:w-[380px] z-10 group">
        <div class="absolute inset-0 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-2xl blur opacity-20 group-hover:opacity-40 transition-opacity duration-300"></div>
        <div class="relative flex items-center bg-slate-900/90 border border-slate-700/80 rounded-2xl p-1.5 focus-within:border-blue-400 focus-within:ring-2 focus-within:ring-blue-500/20 transition-all">
          <input type="text" v-model="searchQuery" placeholder="جستجوی کد سفارش یا فروشنده..." class="w-full bg-transparent text-sm font-bold text-white px-4 py-2.5 outline-none placeholder-slate-500">
          <div class="w-10 h-10 bg-slate-800 text-slate-400 rounded-xl flex items-center justify-center shrink-0">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= فیلتر وضعیت‌ها ================= -->
    <div class="flex gap-2 p-1.5 bg-slate-100/80 backdrop-blur-xl rounded-2xl w-fit mx-auto md:mx-0 border border-slate-200/60 shadow-inner">
      <button @click="activeFilter = 'all'" :class="['px-6 py-2.5 rounded-xl text-xs md:text-sm font-black transition-all duration-300 cursor-pointer', activeFilter === 'all' ? 'bg-white text-blue-600 shadow-[0_4px_15px_rgba(0,0,0,0.05)]' : 'text-slate-500 hover:text-slate-800']">همه سفارشات</button>
      <button @click="activeFilter = 'active'" :class="['px-6 py-2.5 rounded-xl text-xs md:text-sm font-black transition-all duration-300 cursor-pointer', activeFilter === 'active' ? 'bg-white text-blue-600 shadow-[0_4px_15px_rgba(0,0,0,0.05)]' : 'text-slate-500 hover:text-slate-800']">در جریان</button>
      <button @click="activeFilter = 'delivered'" :class="['px-6 py-2.5 rounded-xl text-xs md:text-sm font-black transition-all duration-300 cursor-pointer', activeFilter === 'delivered' ? 'bg-white text-blue-600 shadow-[0_4px_15px_rgba(0,0,0,0.05)]' : 'text-slate-500 hover:text-slate-800']">تحویل شده</button>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 bg-white/50 rounded-[2.5rem] border border-slate-100 shadow-sm">
      <div class="relative w-16 h-16 mb-3">
        <div class="absolute inset-0 border-4 border-slate-200 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-blue-600 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-xs font-black text-slate-400 animate-pulse">در حال دریافت لیست سفارشات از سرور...</p>
    </div>

    <!-- ================= لیست سفارشات ================= -->
    <div v-else class="space-y-8 relative z-10">
      <transition-group name="list">
        <div v-for="order in filteredOrders" :key="order.db_id" class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_-10px_rgba(0,0,0,0.04)] overflow-hidden relative group hover:border-blue-200 transition-all duration-500">
          
          <!-- هدر کارت سفارش -->
          <div class="p-6 md:p-8 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6 bg-gradient-to-b from-slate-50/60 to-white">
            <div class="flex flex-wrap items-center gap-3 md:gap-4">
              <div class="bg-white text-slate-800 px-4 py-2 rounded-2xl text-xs font-mono font-black border border-slate-200 shadow-sm flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-blue-500"></span> {{ order.id }}
              </div>
              <div class="text-xs font-bold text-slate-500 flex items-center gap-1.5 bg-slate-50 px-3.5 py-2 rounded-2xl border border-slate-100">
                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg> {{ order.date }}
              </div>
              
              <div v-if="order.hasDispute" class="bg-rose-50 text-rose-600 border border-rose-200 px-3.5 py-2 rounded-2xl text-xs font-black flex items-center gap-2 shadow-sm">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-rose-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-rose-500"></span>
                </span>
                پرونده اختلاف در جریان
              </div>
            </div>

            <!-- دکمه‌های اکشن بالای کارت -->
            <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
              
              <!-- چت زنده با فروشنده -->
              <button @click="openChat(order)" class="flex-1 lg:flex-none text-xs font-black text-indigo-700 bg-indigo-50 border border-indigo-200 hover:bg-indigo-600 hover:text-white px-5 py-3 rounded-2xl transition-all shadow-sm flex items-center justify-center gap-2 cursor-pointer group">
                <svg class="w-4 h-4 text-indigo-600 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                چت زنده با تامین‌کننده
              </button>

              <!-- ثبت شکایت -->
              <button @click="openDisputeModal(order)" :disabled="order.hasDispute" class="flex-1 lg:flex-none text-xs font-black text-rose-600 bg-white border border-rose-200 px-5 py-3 rounded-2xl hover:bg-rose-50 hover:border-rose-300 transition-all shadow-sm flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg> 
                {{ order.hasDispute ? 'شکایت ثبت شد' : 'ثبت اختلاف' }}
              </button>

              <!-- فاکتور رسمی -->
              <button @click="openInvoice(order)" class="flex-1 lg:flex-none text-xs font-black text-white bg-slate-900 px-5 py-3 rounded-2xl hover:bg-black transition-all shadow-md flex items-center justify-center gap-2 cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg> 
                فاکتور B2B
              </button>
            </div>
          </div>

          <!-- خط تایم‌لاین انیمیشنی پیشرفت ارسال -->
          <div class="px-6 md:px-16 py-10 relative">
            <div class="absolute left-16 right-16 top-1/2 -translate-y-1/2 h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-blue-500 via-indigo-500 to-emerald-500 transition-all duration-1000 ease-out relative" :style="`width: ${calculateProgress(order.status)}%`"></div>
            </div>
            
            <div class="flex justify-between relative z-10">
              <div class="flex flex-col items-center gap-2">
                <div class="w-11 h-11 rounded-2xl flex items-center justify-center font-black shadow-md transition-all" :class="calculateProgress(order.status) >= 20 ? 'bg-blue-600 text-white scale-110' : 'bg-white border-2 border-slate-200 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg></div>
                <span class="text-[11px] font-black text-slate-700 bg-white px-2.5 py-0.5 rounded-full shadow-sm border border-slate-100">تایید سفارش</span>
              </div>
              <div class="flex flex-col items-center gap-2">
                <div class="w-11 h-11 rounded-2xl flex items-center justify-center font-black shadow-md transition-all" :class="calculateProgress(order.status) >= 60 ? 'bg-indigo-600 text-white scale-110' : 'bg-white border-2 border-slate-200 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg></div>
                <span class="text-[11px] font-black text-slate-700 bg-white px-2.5 py-0.5 rounded-full shadow-sm border border-slate-100">در حال ارسال</span>
              </div>
              <div class="flex flex-col items-center gap-2">
                <div class="w-11 h-11 rounded-2xl flex items-center justify-center font-black shadow-md transition-all" :class="calculateProgress(order.status) >= 100 ? 'bg-emerald-600 text-white scale-110' : 'bg-white border-2 border-slate-200 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
                <span class="text-[11px] font-black text-slate-700 bg-white px-2.5 py-0.5 rounded-full shadow-sm border border-slate-100">تحویل شد</span>
              </div>
            </div>
          </div>

          <!-- جزئیات اقلام و تامین‌کننده -->
          <div class="p-6 md:p-8 border-t border-slate-100 bg-white">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
              
              <div class="flex-1 min-w-0">
                <p class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2">اقلام سفارش</p>
                <div class="flex flex-wrap gap-2">
                  <span v-for="(item, index) in order.items" :key="index" class="inline-flex items-center gap-2 bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-1.5 text-xs font-black text-slate-700">
                    <span class="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
                    {{ item.name }} 
                    <span class="text-[10px] text-slate-500 font-bold bg-white px-2 py-0.5 rounded border border-slate-100">{{ item.qty }} عدد</span>
                  </span>
                </div>
              </div>

              <div class="hidden md:block w-px h-12 bg-slate-100 mx-2"></div>

              <div class="flex items-center gap-6 w-full md:w-auto">
                <div class="shrink-0">
                  <p class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">تامین‌کننده معتبر</p>
                  <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center font-black text-xs border border-indigo-100 shadow-sm">{{ order.seller ? order.seller.charAt(0) : 'ت' }}</div>
                    <p class="text-xs font-black text-slate-800">{{ order.seller }}</p>
                  </div>
                </div>
                
                <div class="text-left bg-slate-50 px-5 py-3 rounded-2xl border border-slate-200 shrink-0">
                  <p class="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-0.5">مبلغ کل فاکتور</p>
                  <p class="text-lg font-black text-indigo-700 tracking-tight">{{ formatPrice(order.total) }} <span class="text-[10px] font-bold text-slate-400">تومان</span></p>
                </div>
              </div>

            </div>
          </div>

        </div>
      </transition-group>
      
      <div v-if="!isLoading && filteredOrders.length === 0" class="bg-white border border-slate-200 border-dashed rounded-[2.5rem] py-20 flex flex-col items-center justify-center text-center">
        <div class="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center mb-3 text-slate-300">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
        </div>
        <h3 class="text-base font-black text-slate-800 mb-1">هیچ سفارشی یافت نشد</h3>
        <p class="text-xs font-bold text-slate-400">سفارشی مطابق با جستجو یا فیلتر انتخابی موجود نیست.</p>
      </div>
    </div>

    <!-- ================= MODAL: چت زنده با تامین‌کننده (Real-Time Live Chat) ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
        <div v-if="chatOrder" class="fixed bottom-0 left-0 md:bottom-6 md:left-6 z-[99999] w-full md:w-[420px] h-[600px] md:h-[550px] bg-white md:rounded-[2.5rem] rounded-t-[2.5rem] shadow-2xl flex flex-col font-sans border border-slate-200 overflow-hidden" dir="rtl">
          
          <!-- هدر چت -->
          <div class="bg-slate-900 text-white p-4 flex items-center justify-between shrink-0 relative overflow-hidden">
            <div class="absolute -left-10 -top-10 w-32 h-32 bg-indigo-500 rounded-full mix-blend-screen filter blur-[40px] opacity-20 pointer-events-none"></div>
            
            <div class="flex items-center gap-3 relative z-10">
              <div class="w-11 h-11 bg-indigo-600 rounded-2xl flex items-center justify-center font-black text-white shadow-inner text-base">
                {{ chatOrder.seller ? chatOrder.seller.charAt(0) : 'ت' }}
              </div>
              <div>
                <h3 class="font-black text-sm">{{ chatOrder.seller }}</h3>
                <p class="text-[10px] text-emerald-400 font-bold flex items-center gap-1.5 mt-0.5">
                  <span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></span> گفتگوی آنلاین سفارش {{ chatOrder.id }}
                </p>
              </div>
            </div>

            <button @click="closeChat" class="w-9 h-9 bg-white/10 hover:bg-white/20 rounded-full flex items-center justify-center transition-colors cursor-pointer relative z-10">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>

          <!-- بدنه پیام‌ها -->
          <div ref="chatContainer" class="flex-grow bg-slate-50/70 p-4 overflow-y-auto space-y-3 custom-scrollbar flex flex-col relative">
             <div v-if="isLoadingMessages" class="text-center py-10">
               <div class="w-6 h-6 border-2 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
               <span class="text-[11px] font-bold text-slate-400">در حال خواندن تاریخچه پیام‌ها...</span>
             </div>

             <div v-else-if="chatMessages.length === 0" class="text-center py-12 text-slate-400 text-xs font-bold leading-relaxed">
               هیچ پیامی ردوبدل نشده است.<br>سوالات خود در خصوص ارسال کالا را از فروشنده بپرسید.
             </div>
             
             <div v-else v-for="msg in chatMessages" :key="msg.id" :class="['flex flex-col', msg.sender === 'buyer' ? 'items-end' : 'items-start']">
               <div :class="['max-w-[85%] p-3.5 rounded-2xl text-xs font-medium leading-relaxed shadow-sm', msg.sender === 'buyer' ? 'bg-indigo-600 text-white rounded-tl-none' : 'bg-white text-slate-800 border border-slate-200 rounded-tr-none']">
                 <p>{{ msg.text }}</p>
                 <span :class="['block text-[9px] mt-1 text-left font-mono opacity-70', msg.sender === 'buyer' ? 'text-indigo-100' : 'text-slate-400']">{{ msg.time || 'هم‌اکنون' }}</span>
               </div>
             </div>
          </div>

          <!-- پیش‌فرض‌های سریع -->
          <div class="bg-white px-3 py-2 border-t border-slate-100 flex gap-2 overflow-x-auto hide-scrollbar shrink-0">
            <button @click="newMessage = 'سلام، زمان دقیق تحویل باربری کی هست؟'" class="text-[10px] font-bold bg-slate-100 hover:bg-indigo-50 hover:text-indigo-600 text-slate-600 px-3 py-1.5 rounded-xl whitespace-nowrap transition-colors cursor-pointer">زمان دقیق تحویل؟</button>
            <button @click="newMessage = 'لطفاً کد رهگیری بارنامه را بفرستید.'" class="text-[10px] font-bold bg-slate-100 hover:bg-indigo-50 hover:text-indigo-600 text-slate-600 px-3 py-1.5 rounded-xl whitespace-nowrap transition-colors cursor-pointer">کد بارنامه؟</button>
          </div>

          <!-- فرم ارسال پیام -->
          <div class="p-3 bg-white border-t border-slate-200 flex items-center gap-2 shrink-0">
            <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="پیام خود را بنویسید..." class="flex-grow bg-slate-50 border border-slate-200 text-xs font-bold px-4 py-3 rounded-full outline-none focus:border-indigo-500 transition-colors">
            <button @click="sendMessage" :disabled="!newMessage.trim()" class="w-10 h-10 bg-indigo-600 hover:bg-indigo-700 text-white rounded-full flex items-center justify-center shadow-md disabled:opacity-50 cursor-pointer shrink-0">
              <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            </button>
          </div>

        </div>
      </transition>
    </Teleport>

    <!-- ================= MODAL: ثبت شکایت و اختلاف (Dispute) ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="disputeModal.show" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6" dir="rtl">
          <div class="absolute inset-0 bg-slate-900/70 backdrop-blur-sm" @click="closeDisputeModal"></div>
          
          <div class="bg-white w-full max-w-lg rounded-[2.5rem] shadow-2xl relative z-10 overflow-hidden font-sans border border-slate-200">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-rose-500 to-red-600"></div>
            
            <div class="p-6 border-b border-slate-100 bg-slate-50 flex justify-between items-center">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-rose-100 text-rose-600 rounded-xl flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                </div>
                <div>
                  <h3 class="font-black text-slate-800 text-base">طرح دعوی و ثبت شکایت</h3>
                  <p class="text-[10px] font-bold text-slate-400">سفارش: {{ disputeModal.order?.id }}</p>
                </div>
              </div>
              <button @click="closeDisputeModal" class="w-8 h-8 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-400 hover:text-red-500 transition-colors cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="p-6 space-y-4">
              <div class="bg-rose-50 border border-rose-100 p-4 rounded-2xl text-xs font-bold text-rose-800 leading-relaxed text-justify">
                با ثبت شکایت، مبلغ پرداختی تا بررسی پرونده توسط تیم پشتیبانی تاجربام در حساب امانی (Escrow) مسدود خواهد ماند.
              </div>

              <div>
                <label class="block text-xs font-black text-slate-600 mb-1.5">علت اصلی شکایت</label>
                <select v-model="disputeForm.reason" class="w-full bg-slate-50 border border-slate-200 text-xs font-bold text-slate-700 py-3 px-3.5 rounded-xl outline-none focus:bg-white focus:border-rose-400 transition-all cursor-pointer">
                  <option value="" disabled selected>انتخاب مورد...</option>
                  <option value="damaged">کالای معیوب یا آسیب‌دیده فیزیکی</option>
                  <option value="wrong_item">مغایرت کالا با توضیحات و پیش‌فاکتور</option>
                  <option value="delay">تاخیر غیرمجاز در ارسال محموله</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-600 mb-1.5">توضیحات تکمیلی</label>
                <textarea v-model="disputeForm.description" rows="3" placeholder="جزئیات کامل را بنویسید..." class="w-full bg-slate-50 border border-slate-200 text-xs font-medium text-slate-800 p-3.5 rounded-xl outline-none focus:bg-white focus:border-rose-400 transition-all resize-none"></textarea>
              </div>
            </div>

            <div class="bg-slate-50 border-t border-slate-100 p-4 flex justify-end gap-3">
              <button @click="closeDisputeModal" class="px-5 py-2.5 rounded-xl font-bold bg-white border border-slate-200 text-slate-600 text-xs cursor-pointer">انصراف</button>
              <button @click="submitDispute" :disabled="!disputeForm.reason || isSubmittingDispute" class="px-6 py-2.5 rounded-xl font-black bg-rose-600 hover:bg-rose-700 text-white text-xs disabled:opacity-50 cursor-pointer">
                {{ isSubmittingDispute ? 'در حال ثبت...' : 'ارسال به میز قضاوت' }}
              </button>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>

    <!-- توست اطلاع‌رسانی -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-10" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-10">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[100000] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-3 border font-sans', toast.type === 'error' ? 'bg-rose-600 border-rose-500' : 'bg-slate-900 border-slate-700']" dir="rtl">
          <div :class="['w-8 h-8 rounded-full flex items-center justify-center shrink-0', toast.type === 'error' ? 'bg-white/20' : 'bg-emerald-500/20 text-emerald-400']">
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
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';

const orders = ref([]);
const isLoading = ref(true);
const searchQuery = ref('');
const activeFilter = ref('all');

// توست اطلاع‌رسانی
const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

// فراخوانی سفارشات خریدار از بک‌اند
const fetchOrders = async () => {
  isLoading.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/buyer/orders`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (res.ok) {
      const data = await res.json();
      orders.value = (data.orders || []).map(o => ({
        db_id: o.db_id || o.id,
        id: o.id || `ORD-${o.db_id}`,
        seller: o.seller || o.seller_name || 'تامین‌کننده معتبر B2B',
        date: o.date || '۱۴۰۵/۰۵/۰۱',
        status: o.status || 'pending',
        total: o.total || 0,
        hasDispute: o.has_dispute || false,
        items: o.items || []
      }));
    }
  } catch (error) {
    console.error("Error fetching buyer orders:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchOrders();
});

const calculateProgress = (status) => {
  if (status === 'delivered') return 100;
  if (status === 'shipped') return 60;
  if (status === 'processing') return 40;
  return 20; // pending
};

const filteredOrders = computed(() => {
  let result = orders.value;
  
  if (activeFilter.value === 'active') {
    result = result.filter(o => o.status !== 'delivered');
  } else if (activeFilter.value === 'delivered') {
    result = result.filter(o => o.status === 'delivered');
  }

  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase();
    result = result.filter(o => 
      o.id.toLowerCase().includes(q) || 
      (o.seller && o.seller.toLowerCase().includes(q))
    );
  }

  return result;
});

// ================= چت زنده real-time با فروشنده =================
const chatOrder = ref(null);
const chatMessages = ref([]);
const newMessage = ref('');
const isLoadingMessages = ref(false);
const chatContainer = ref(null);
let chatInterval = null;

const openChat = async (order) => {
  chatOrder.value = order;
  await fetchChatMessages();
  chatInterval = setInterval(fetchChatMessages, 3000);
};

const closeChat = () => {
  chatOrder.value = null;
  if (chatInterval) clearInterval(chatInterval);
};

const fetchChatMessages = async () => {
  if (!chatOrder.value) return;
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

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/orders/${chatOrder.value.db_id}/messages`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ text: textToSend, sender: 'buyer' })
    });
    if (res.ok) {
      await fetchChatMessages();
    }
  } catch (e) {
    showToast('خطا', 'پیام ارسال نشد.', 'error');
  }
};

// ================= مدیریت شکایات =================
const disputeModal = ref({ show: false, order: null });
const disputeForm = ref({ reason: '', description: '' });
const isSubmittingDispute = ref(false);

const openDisputeModal = (order) => {
  disputeModal.value = { show: true, order };
  disputeForm.value = { reason: '', description: '' };
};

const closeDisputeModal = () => {
  disputeModal.value.show = false;
};

const submitDispute = async () => {
  if (!disputeModal.value.order) return;
  isSubmittingDispute.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/buyer/orders/${disputeModal.value.order.db_id}/dispute`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(disputeForm.value)
    });
    if (res.ok) {
      disputeModal.value.order.hasDispute = true;
      showToast('شکایت ثبت شد', 'پرونده اختلاف جهت داوری به مدیریت ارجاع گردید.');
      closeDisputeModal();
    }
  } catch (e) {
    showToast('خطا', 'ثبت شکایت امکان‌پذیر نبود.', 'error');
  } finally {
    isSubmittingDispute.value = false;
  }
};

const openInvoice = (order) => {
  showToast('فاکتور B2B', `فاکتور رسمی سفارش ${order.id} آماده چاپ می‌باشد.`);
};

const formatPrice = (val) => {
  if (!val) return '۰';
  return Number(val).toLocaleString('fa-IR');
};

onUnmounted(() => {
  if (chatInterval) clearInterval(chatInterval);
});
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 5px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateY(15px); }
</style>