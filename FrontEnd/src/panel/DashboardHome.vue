<template>
  <div class="space-y-8 max-w-7xl mx-auto pb-12 font-sans" dir="rtl">
    
    <!-- ================= هدر داشبورد و خوش‌آمدگویی ================= -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 bg-white p-6 rounded-[2rem] border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.02)]">
      <div class="flex items-center gap-5">
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 p-0.5 shadow-lg shadow-blue-500/20">
          <div class="w-full h-full bg-white rounded-[14px] flex items-center justify-center font-black text-2xl text-blue-600">ر</div>
        </div>
        <div>
          <div class="flex items-center gap-2 mb-1">
            <h1 class="text-2xl font-black text-slate-800 tracking-tight">سلام، رایان تکرو! 👋</h1>
            <span class="bg-amber-100 text-amber-700 text-[10px] font-black px-2 py-0.5 rounded-md flex items-center gap-1">
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> فروشنده طلایی
            </span>
          </div>
          <p class="text-sm font-bold text-slate-500">خلاصه وضعیت فروشگاه شما در ۳۰ روز گذشته.</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <button class="bg-slate-50 border border-slate-200 text-slate-700 hover:bg-slate-100 font-bold px-5 py-3 rounded-xl transition-colors flex items-center gap-2 text-sm shadow-sm">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          گزارش اکسل
        </button>
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold px-5 py-3 rounded-xl transition-colors flex items-center gap-2 text-sm shadow-lg shadow-blue-500/30">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
          افزودن محصول جدید
        </button>
      </div>
    </div>

    <!-- ================= کارت‌های آماری (Stats) ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      
      <!-- کارت ویژه کیف پول (پریمیوم هولوگرافیک) -->
      <div class="bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 rounded-[2rem] p-7 text-white shadow-[0_15px_40px_-10px_rgba(30,58,138,0.5)] relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-40 h-40 bg-blue-500 rounded-full mix-blend-screen filter blur-[50px] opacity-40 group-hover:opacity-60 transition-opacity duration-700"></div>
        <div class="absolute bottom-0 left-0 w-32 h-32 bg-indigo-500 rounded-full mix-blend-screen filter blur-[40px] opacity-30"></div>
        <div class="relative z-10">
          <div class="flex items-center justify-between mb-6">
            <span class="text-indigo-200 text-sm font-bold flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              موجودی قابل برداشت
            </span>
            <div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center backdrop-blur-md border border-white/10"><svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg></div>
          </div>
          <div class="text-3xl lg:text-4xl font-black mb-1 tracking-tight drop-shadow-sm">۱۲۴,۵۰۰,۰۰۰</div>
          <div class="text-sm font-medium text-indigo-200 mb-6">تومان</div>
          <button class="w-full text-sm font-bold text-white bg-white/20 hover:bg-white/30 backdrop-blur-md py-3 rounded-xl transition-colors border border-white/10">درخواست تسویه حساب</button>
        </div>
      </div>

      <!-- کارت سفارشات -->
      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] hover:shadow-lg transition-shadow flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">سفارشات موفق عمده</span>
            <div class="w-10 h-10 bg-emerald-50 rounded-xl flex items-center justify-center text-emerald-600 group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800 mb-1">۴۸ <span class="text-sm font-bold text-slate-400">سفارش</span></div>
        </div>
        <div class="text-xs font-bold text-emerald-600 flex items-center gap-1.5 bg-emerald-50 w-fit px-2.5 py-1.5 rounded-lg mt-4">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> ۱۲٪ رشد از ماه قبل
        </div>
      </div>

      <!-- کارت بازدید -->
      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] hover:shadow-lg transition-shadow flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">بازدید از محصولات شما</span>
            <div class="w-10 h-10 bg-blue-50 rounded-xl flex items-center justify-center text-blue-600 group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800 mb-1">۲,۴۵۰ <span class="text-sm font-bold text-slate-400">بازدید</span></div>
        </div>
        <div class="text-xs font-bold text-emerald-600 flex items-center gap-1.5 bg-emerald-50 w-fit px-2.5 py-1.5 rounded-lg mt-4">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> ۲۴٪ رشد از ماه قبل
        </div>
      </div>
      
      <!-- کارت امتیاز -->
      <div class="bg-white rounded-[2rem] p-7 border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.03)] hover:shadow-lg transition-shadow flex flex-col justify-between group">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-sm font-bold">میانگین رضایت خریداران</span>
            <div class="w-10 h-10 bg-amber-50 rounded-xl flex items-center justify-center text-amber-500 group-hover:scale-110 transition-transform"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg></div>
          </div>
          <div class="text-3xl font-black text-slate-800 mb-1">۴.۸ <span class="text-sm font-bold text-slate-400">از ۵</span></div>
        </div>
        <div class="text-xs font-bold text-slate-500 bg-slate-50 w-fit px-2.5 py-1.5 rounded-lg mt-4">
          بر اساس ۱۲۴ رای ثبت شده
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- ================= نمودار فروش (شبیه‌سازی شده) ================= -->
      <div class="lg:col-span-2 bg-white border border-slate-100 rounded-[2rem] shadow-[0_4px_20px_rgb(0,0,0,0.02)] p-6 md:p-8">
        <div class="flex items-center justify-between mb-8">
          <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-indigo-500"></span> آمار فروش ۳۰ روز گذشته
          </h3>
          <select class="bg-slate-50 border border-slate-200 text-sm font-bold text-slate-600 px-3 py-2 rounded-xl outline-none focus:border-indigo-400">
            <option>ماه جاری</option>
            <option>ماه قبل</option>
            <option>سه ماهه</option>
          </select>
        </div>
        
        <!-- یک چارت میله‌ای فیک و زیبا با CSS -->
        <div class="h-64 flex items-end justify-between gap-2 md:gap-4 pt-4 border-b border-slate-100 relative">
          <!-- خطوط راهنما -->
          <div class="absolute w-full top-0 border-t border-dashed border-slate-200"></div>
          <div class="absolute w-full top-1/2 border-t border-dashed border-slate-200"></div>
          
          <!-- ستون‌ها -->
          <div v-for="i in 10" :key="i" class="w-full relative group cursor-pointer flex flex-col items-center justify-end h-full z-10">
            <!-- Tooltip فیک -->
            <div class="absolute -top-10 opacity-0 group-hover:opacity-100 transition-opacity bg-slate-800 text-white text-[10px] font-bold px-2 py-1 rounded-lg pointer-events-none">
              {{ Math.floor(Math.random() * 50) + 10 }} میلیون
            </div>
            <!-- میله -->
            <div class="w-full max-w-[2rem] bg-indigo-100 group-hover:bg-indigo-200 rounded-t-lg transition-all duration-500" :style="`height: ${Math.floor(Math.random() * 70) + 20}%`">
              <div class="w-full bg-indigo-500 rounded-t-lg absolute bottom-0" :style="`height: ${Math.floor(Math.random() * 60) + 20}%`"></div>
            </div>
          </div>
        </div>
        <div class="flex justify-between mt-4 text-xs font-bold text-slate-400">
          <span>۱ بهمن</span>
          <span>۱۵ بهمن</span>
          <span>۳۰ بهمن</span>
        </div>
      </div>

      <!-- ================= محصولات رو به اتمام ================= -->
      <div class="lg:col-span-1 bg-white border border-slate-100 rounded-[2rem] shadow-[0_4px_20px_rgb(0,0,0,0.02)] p-6 md:p-8">
        <h3 class="font-black text-slate-800 text-lg flex items-center gap-2 mb-6">
          <span class="w-3 h-3 rounded-full bg-orange-500 animate-pulse"></span> هشدارهای انبار
        </h3>
        
        <div class="space-y-4">
          <div class="flex items-center gap-4 p-3 rounded-2xl border border-slate-100 hover:bg-slate-50 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-slate-100 p-1 flex-shrink-0"><img src="https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png" class="w-full h-full object-contain"></div>
            <div class="flex-grow">
              <h4 class="text-sm font-bold text-slate-800 line-clamp-1">لپ‌تاپ ایسوس Vivobook</h4>
              <p class="text-xs font-bold text-orange-500 mt-1">فقط ۳ عدد در انبار!</p>
            </div>
            <button class="text-xs font-bold bg-white border border-slate-200 px-3 py-1.5 rounded-lg hover:text-blue-600 transition-colors">شارژ</button>
          </div>
          
          <div class="flex items-center gap-4 p-3 rounded-2xl border border-slate-100 hover:bg-slate-50 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-slate-100 p-1 flex-shrink-0"><img src="https://freepngimg.com/thumb/mouse/10-mouse-png-image.png" class="w-full h-full object-contain"></div>
            <div class="flex-grow">
              <h4 class="text-sm font-bold text-slate-800 line-clamp-1">موس بی‌سیم تسکو</h4>
              <p class="text-xs font-bold text-red-500 mt-1">اتمام موجودی</p>
            </div>
            <button class="text-xs font-bold bg-white border border-slate-200 px-3 py-1.5 rounded-lg hover:text-blue-600 transition-colors">شارژ</button>
          </div>
        </div>
        
        <button class="w-full mt-6 text-sm font-bold text-blue-600 bg-blue-50 py-3 rounded-xl hover:bg-blue-100 transition-colors">مدیریت انبار و کالاها</button>
      </div>

    </div>

    <!-- ================= جدول آخرین سفارشات B2B ================= -->
    <div class="bg-white border border-slate-100 rounded-[2rem] shadow-[0_4px_20px_rgb(0,0,0,0.02)] overflow-hidden">
      <div class="p-6 md:p-8 border-b border-slate-100 flex items-center justify-between">
        <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-blue-500"></span> آخرین سفارشات دریافتی
        </h3>
        <a href="#" class="text-sm font-bold text-blue-600 hover:text-blue-800 flex items-center gap-1">مشاهده همه <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg></a>
      </div>
      
      <div class="overflow-x-auto custom-scrollbar pb-4">
        <table class="w-full text-right text-sm min-w-[800px]">
          <thead class="bg-slate-50/80 text-slate-500 text-xs font-black">
            <tr>
              <th class="px-8 py-5">شناسه سفارش</th>
              <th class="px-8 py-5">شرح محصول</th>
              <th class="px-8 py-5 text-center">تعداد (بسته)</th>
              <th class="px-8 py-5">مبلغ کل (تومان)</th>
              <th class="px-8 py-5">وضعیت</th>
              <th class="px-8 py-5">عملیات</th>
            </tr>
          </thead>
          <tbody class="font-medium text-slate-700 divide-y divide-slate-50">
            <!-- ردیف 1 -->
            <tr class="hover:bg-slate-50/50 transition-colors group">
              <td class="px-8 py-5 font-mono font-bold text-slate-500">#TJB-4589</td>
              <td class="px-8 py-5">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-slate-100 p-1 flex-shrink-0"><img src="https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png" class="w-full h-full object-contain"></div>
                  <span class="font-bold text-slate-800">لپ‌تاپ ایسوس Vivobook i7</span>
                </div>
              </td>
              <td class="px-8 py-5 text-center"><span class="bg-slate-100 text-slate-700 px-3 py-1.5 rounded-lg font-bold text-xs">۲۰ عدد</span></td>
              <td class="px-8 py-5 font-black text-slate-800">۷۶۴,۰۰۰,۰۰۰</td>
              <td class="px-8 py-5"><span class="bg-amber-50 text-amber-600 px-3 py-1.5 rounded-lg text-[10px] font-black border border-amber-100 shadow-sm flex items-center w-fit gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> در انتظار تایید شما</span></td>
              <td class="px-8 py-5">
                <button class="bg-white border border-slate-200 text-blue-600 hover:border-blue-400 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm">بررسی و تایید</button>
              </td>
            </tr>
            <!-- ردیف 2 -->
            <tr class="hover:bg-slate-50/50 transition-colors group">
              <td class="px-8 py-5 font-mono font-bold text-slate-500">#TJB-4588</td>
              <td class="px-8 py-5">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-slate-100 p-1 flex-shrink-0"><img src="https://freepngimg.com/thumb/usb_cable/1-2-usb-cable-png.png" class="w-full h-full object-contain"></div>
                  <span class="font-bold text-slate-800">کابل شارژر Type-C تسکو</span>
                </div>
              </td>
              <td class="px-8 py-5 text-center"><span class="bg-slate-100 text-slate-700 px-3 py-1.5 rounded-lg font-bold text-xs">۱۵۰ عدد</span></td>
              <td class="px-8 py-5 font-black text-slate-800">۶,۳۰۰,۰۰۰</td>
              <td class="px-8 py-5"><span class="bg-blue-50 text-blue-600 px-3 py-1.5 rounded-lg text-[10px] font-black border border-blue-100 shadow-sm flex items-center w-fit gap-1"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> در حال پردازش انبار</span></td>
              <td class="px-8 py-5">
                <button class="bg-slate-100 text-slate-500 px-4 py-2 rounded-xl text-xs font-bold transition-all">مشاهده</button>
              </td>
            </tr>
            <!-- ردیف 3 -->
            <tr class="hover:bg-slate-50/50 transition-colors group">
              <td class="px-8 py-5 font-mono font-bold text-slate-500">#TJB-4581</td>
              <td class="px-8 py-5">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-slate-100 p-1 flex-shrink-0"><img src="https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png" class="w-full h-full object-contain"></div>
                  <span class="font-bold text-slate-800">مانیتور ۲۴ اینچ ال‌جی</span>
                </div>
              </td>
              <td class="px-8 py-5 text-center"><span class="bg-slate-100 text-slate-700 px-3 py-1.5 rounded-lg font-bold text-xs">۱۰ عدد</span></td>
              <td class="px-8 py-5 font-black text-slate-800">۵۸,۰۰۰,۰۰۰</td>
              <td class="px-8 py-5"><span class="bg-emerald-50 text-emerald-600 px-3 py-1.5 rounded-lg text-[10px] font-black border border-emerald-100 shadow-sm flex items-center w-fit gap-1"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg> تحویل داده شده</span></td>
              <td class="px-8 py-5">
                <button class="bg-slate-100 text-slate-500 px-4 py-2 rounded-xl text-xs font-bold transition-all">فاکتور</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</template>

<script setup>
// در اینجا می‌توانیم دیتاهای داینامیک چارت و سفارشات را مدیریت کنیم.
</script>

<style scoped>
/* استایل اسکرول‌بار اختصاصی جداول */
.custom-scrollbar::-webkit-scrollbar { height: 8px; }
.custom-scrollbar::-webkit-scrollbar-track { background: #f8fafc; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>