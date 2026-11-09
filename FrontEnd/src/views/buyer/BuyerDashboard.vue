<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-12 font-sans" dir="rtl">
    
    <!-- ================= هدر و خوش‌آمدگویی (Glassy Hero) ================= -->
    <div class="relative rounded-[2.5rem] overflow-hidden bg-slate-900 p-8 md:p-10 shadow-[0_20px_50px_-12px_rgba(15,23,42,0.5)] border border-slate-800">
      <div class="absolute -right-20 -top-20 w-96 h-96 bg-violet-600 rounded-full mix-blend-screen filter blur-[100px] opacity-30 animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-72 h-72 bg-fuchsia-600 rounded-full mix-blend-screen filter blur-[80px] opacity-20"></div>
      
      <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-8">
        <div class="flex items-center gap-6">
          <div class="w-20 h-20 rounded-full bg-white/10 backdrop-blur-xl border border-white/20 p-1 shadow-2xl flex-shrink-0">
            <div class="w-full h-full bg-gradient-to-tr from-violet-500 to-fuchsia-500 rounded-full flex items-center justify-center font-black text-3xl text-white">
              <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            </div>
          </div>
          <div>
            <div class="flex items-center gap-3 mb-2">
              <h1 class="text-2xl md:text-3xl font-black text-white tracking-tight">سلام، مدیر خرید شرکت پارس تک!</h1>
            </div>
            <p class="text-slate-300 font-medium text-sm md:text-base leading-relaxed">خلاصه وضعیت خریدهای سازمانی و استعلام‌های اخیر شما.</p>
          </div>
        </div>
        
        <div class="flex gap-3 shrink-0">
          <button class="bg-violet-600 hover:bg-violet-500 text-white font-black px-6 py-4 rounded-2xl shadow-[0_10px_25px_rgba(124,58,237,0.4)] transition-all hover:-translate-y-1 flex items-center gap-2 text-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
            ثبت استعلام خرید (RFQ)
          </button>
        </div>
      </div>
    </div>

    <!-- ================= کارت‌های آماری (Bento Grid) ================= -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform relative overflow-hidden">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-blue-500"></div>
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">سفارشات در جریان</span>
            <div class="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg></div>
          </div>
          <div class="text-4xl font-black text-slate-800">۳ <span class="text-sm font-bold text-slate-400">محموله</span></div>
        </div>
        <div class="text-[11px] font-bold text-blue-700 bg-blue-50 px-3 py-1.5 rounded-lg w-fit mt-5 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-blue-500 animate-ping"></span> ۱ محموله در مسیر انبار شما
        </div>
      </div>

      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform relative overflow-hidden">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-emerald-500"></div>
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">مجموع خریدهای موفق</span>
            <div class="w-12 h-12 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="text-3xl md:text-4xl font-black text-slate-800">۸۵۰ <span class="text-sm font-bold text-slate-400">میلیون ت</span></div>
        </div>
        <div class="text-[11px] font-bold text-emerald-700 bg-emerald-50 px-3 py-1.5 rounded-lg w-fit mt-5">
          صرفه‌جویی با خرید عمده: ۴۵ میلیون
        </div>
      </div>

      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform relative overflow-hidden">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-violet-500"></div>
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">استعلام‌های باز (RFQ)</span>
            <div class="w-12 h-12 bg-violet-50 text-violet-600 rounded-xl flex items-center justify-center"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg></div>
          </div>
          <div class="text-4xl font-black text-slate-800">۲ <span class="text-sm font-bold text-slate-400">استعلام</span></div>
        </div>
        <div class="text-[11px] font-bold text-violet-700 bg-violet-50 px-3 py-1.5 rounded-lg w-fit mt-5">
          ۱۲ پیشنهاد قیمت جدید دریافت شد
        </div>
      </div>

    </div>

    <!-- ================= جدول پیشرفته سفارشات ================= -->
    <div class="bg-white rounded-[2.5rem] border border-slate-100 shadow-sm overflow-hidden">
      <div class="p-6 md:p-8 border-b border-slate-50 bg-slate-50/50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-violet-500"></span>
          آخرین پیش‌فاکتورها و سفارشات
        </h3>
        <button class="text-xs font-bold text-violet-600 bg-violet-50 hover:bg-violet-100 px-4 py-2 rounded-xl transition-colors">مشاهده همه سفارشات</button>
      </div>

      <div class="overflow-x-auto custom-scrollbar">
        <table class="w-full text-right text-sm">
          <thead class="bg-white text-slate-400 text-[11px] font-black uppercase border-b border-slate-100">
            <tr>
              <th class="px-6 py-5">شناسه / کالا</th>
              <th class="px-6 py-5">تامین‌کننده</th>
              <th class="px-6 py-5 text-center">مبلغ کل (تومان)</th>
              <th class="px-6 py-5 text-center">وضعیت پیگیری</th>
              <th class="px-6 py-5 text-center">عملیات</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-50 font-medium text-slate-700">
            
            <tr class="hover:bg-slate-50/80 transition-colors group">
              <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                  <div class="w-12 h-12 bg-white border border-slate-200 rounded-xl p-1 shadow-sm flex-shrink-0">
                    <img src="https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png" class="w-full h-full object-contain mix-blend-multiply">
                  </div>
                  <div class="flex flex-col">
                    <span class="font-black text-slate-800 text-sm mb-1 line-clamp-1">خرید ۵۰ عدد لپ‌تاپ ایسوس</span>
                    <span class="text-[10px] font-mono text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md w-fit">ORD-1405-9842</span>
                  </div>
                </div>
              </td>
              <td class="px-6 py-5">
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full bg-slate-200 flex items-center justify-center text-[10px] font-black">ر</div>
                  <span class="font-bold text-slate-600">شرکت رایان تکرو</span>
                </div>
              </td>
              <td class="px-6 py-5 text-center font-black text-slate-800 text-base">
                ۱,۹۹۰,۰۰۰,۰۰۰
              </td>
              <td class="px-6 py-5 text-center">
                <span class="bg-blue-50 text-blue-600 border border-blue-100 px-3 py-1.5 rounded-lg text-[11px] font-black inline-flex items-center gap-1 shadow-sm">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"></path></svg>
                  ارسال شده (باربری)
                </span>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex justify-center gap-2">
                  <button class="bg-white border border-slate-200 text-slate-500 hover:text-blue-600 hover:border-blue-300 font-bold px-3 py-2 rounded-xl transition-all shadow-sm text-xs">
                    رسید باربری
                  </button>
                  <button class="bg-slate-900 hover:bg-black text-white font-bold px-3 py-2 rounded-xl transition-all shadow-md text-xs">
                    فاکتور رسمی
                  </button>
                </div>
              </td>
            </tr>

            <tr class="hover:bg-slate-50/80 transition-colors group">
              <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                  <div class="w-12 h-12 bg-white border border-slate-200 rounded-xl p-1 shadow-sm flex-shrink-0">
                    <img src="https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png" class="w-full h-full object-contain mix-blend-multiply">
                  </div>
                  <div class="flex flex-col">
                    <span class="font-black text-slate-800 text-sm mb-1 line-clamp-1">تجهیز مانیتورهای سایت اداری</span>
                    <span class="text-[10px] font-mono text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md w-fit">ORD-1405-9830</span>
                  </div>
                </div>
              </td>
              <td class="px-6 py-5">
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full bg-slate-200 flex items-center justify-center text-[10px] font-black">د</div>
                  <span class="font-bold text-slate-600">دیجیتال شاپ</span>
                </div>
              </td>
              <td class="px-6 py-5 text-center font-black text-slate-800 text-base">
                ۱۷۴,۰۰۰,۰۰۰
              </td>
              <td class="px-6 py-5 text-center">
                <span class="bg-emerald-50 text-emerald-600 border border-emerald-100 px-3 py-1.5 rounded-lg text-[11px] font-black inline-flex items-center gap-1 shadow-sm">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                  تحویل شده
                </span>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex justify-center gap-2">
                  <button class="bg-white border border-slate-200 text-slate-500 hover:text-blue-600 hover:border-blue-300 font-bold px-3 py-2 rounded-xl transition-all shadow-sm text-xs">
                    خرید مجدد
                  </button>
                </div>
              </td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script setup>
// منطق‌های مربوط به داشبورد خریدار
</script>