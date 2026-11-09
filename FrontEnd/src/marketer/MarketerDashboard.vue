<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-12 font-sans text-slate-800" dir="rtl">
    
    <!-- ================= هدر و خوش‌آمدگویی (Glassy Hero) ================= -->
    <div class="relative rounded-[2.5rem] overflow-hidden bg-slate-900 p-8 md:p-10 shadow-[0_20px_50px_-12px_rgba(15,23,42,0.5)]">
      <!-- افکت‌های نوری پس‌زمینه -->
      <div class="absolute -right-20 -top-20 w-96 h-96 bg-emerald-500 rounded-full mix-blend-screen filter blur-[100px] opacity-40 animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-72 h-72 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-30"></div>
      
      <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-8">
        <div class="flex items-center gap-6">
          <div class="w-20 h-20 rounded-full bg-white/10 backdrop-blur-xl border border-white/20 p-1 shadow-2xl flex-shrink-0">
            <div class="w-full h-full bg-gradient-to-tr from-emerald-400 to-teal-500 rounded-full flex items-center justify-center font-black text-3xl text-slate-900">ع</div>
          </div>
          <div>
            <div class="flex items-center gap-3 mb-2">
              <h1 class="text-3xl font-black text-white tracking-tight">سلام علی، خوش برگشتی!</h1>
              <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-black px-3 py-1 rounded-full shadow-sm backdrop-blur-md">VIP Affiliate</span>
            </div>
            <p class="text-slate-300 font-medium text-sm md:text-base">این ماه عملکرد فوق‌العاده‌ای داشتی. <span class="text-emerald-400 font-bold">۲۴٪ رشد</span> نسبت به ماه قبل!</p>
          </div>
        </div>
        
        <div class="flex gap-3">
          <button class="bg-white/10 hover:bg-white/20 backdrop-blur-md border border-white/10 text-white font-bold px-6 py-3.5 rounded-2xl transition-all shadow-lg flex items-center gap-2 text-sm">
            <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
            گزارش عملکرد
          </button>
        </div>
      </div>
    </div>

    <!-- ================= کارت‌های آماری (Bento Grid) ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-6">
      
      <!-- کارت موجودی (Big Card) -->
      <div class="lg:col-span-5 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-[2.5rem] p-8 text-white shadow-[0_20px_40px_-10px_rgba(16,185,129,0.5)] relative overflow-hidden flex flex-col justify-between group cursor-pointer" @click="$router.push('/marketer/wallet')">
        <div class="absolute top-0 right-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-10 mix-blend-overlay"></div>
        <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-white rounded-full mix-blend-overlay filter blur-[40px] opacity-20 group-hover:scale-150 transition-transform duration-700"></div>
        
        <div class="relative z-10 flex items-center justify-between mb-8">
          <div class="bg-white/20 backdrop-blur-md border border-white/30 px-4 py-2 rounded-xl flex items-center gap-2 text-sm font-bold">
            <span class="w-2 h-2 rounded-full bg-white animate-ping"></span>
            موجودی قابل برداشت
          </div>
          <div class="w-12 h-12 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center border border-white/20"><svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg></div>
        </div>
        <div class="relative z-10">
          <div class="text-5xl font-black mb-2 tracking-tight drop-shadow-md">۱۲,۴۵۰,۰۰۰</div>
          <div class="text-emerald-100 font-bold text-lg mb-6">تومان</div>
          <div class="flex items-center gap-2 text-sm font-black bg-white text-teal-700 w-fit px-4 py-2.5 rounded-xl shadow-lg hover:shadow-xl transition-shadow">
            درخواست تسویه آنی <svg class="w-4 h-4 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </div>
        </div>
      </div>

      <!-- شبکه کارت‌های کوچک (Small Cards) -->
      <div class="lg:col-span-7 grid grid-cols-2 gap-6">
        
        <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform">
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-xs md:text-sm font-bold">کلیک‌های ارجاعی (ماه)</span>
            <div class="w-10 h-10 bg-blue-50 text-blue-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"></path></svg></div>
          </div>
          <div>
            <div class="text-2xl md:text-3xl font-black text-slate-800">۴,۸۹۲</div>
            <div class="text-[11px] font-bold text-emerald-600 flex items-center gap-1 mt-2 bg-emerald-50 w-fit px-2 py-1 rounded-md">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> +۱۲.۵٪ رشد
            </div>
          </div>
        </div>

        <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-between hover:-translate-y-1 transition-transform">
          <div class="flex items-center justify-between mb-4">
            <span class="text-slate-500 text-xs md:text-sm font-bold">خریدهای قطعی شده</span>
            <div class="w-10 h-10 bg-indigo-50 text-indigo-500 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg></div>
          </div>
          <div>
            <div class="text-2xl md:text-3xl font-black text-slate-800">۱۵۶ <span class="text-xs text-slate-400">سفارش</span></div>
            <div class="text-[11px] font-bold text-emerald-600 flex items-center gap-1 mt-2 bg-emerald-50 w-fit px-2 py-1 rounded-md">
              ۸ سفارش در حال پردازش
            </div>
          </div>
        </div>

        <div class="col-span-2 bg-slate-900 rounded-[2rem] p-6 shadow-xl relative overflow-hidden flex items-center justify-between border border-slate-800">
          <div class="absolute right-0 top-0 w-32 h-full bg-gradient-to-l from-emerald-500/20 to-transparent"></div>
          <div class="relative z-10">
            <p class="text-slate-400 text-xs font-bold mb-1">نرخ تبدیل (Conversion Rate)</p>
            <div class="text-2xl font-black text-white">۳.۲٪ <span class="text-[10px] text-emerald-400 ml-2">بسیار عالی 🎯</span></div>
          </div>
          <div class="relative z-10 w-1/2 h-10 flex items-end justify-between gap-1">
             <!-- مینی چارت فیک با CSS -->
             <div class="w-full bg-emerald-500 rounded-t-sm" style="height: 30%"></div>
             <div class="w-full bg-emerald-500 rounded-t-sm" style="height: 50%"></div>
             <div class="w-full bg-emerald-500 rounded-t-sm" style="height: 40%"></div>
             <div class="w-full bg-emerald-500 rounded-t-sm" style="height: 70%"></div>
             <div class="w-full bg-emerald-400 rounded-t-sm" style="height: 90%"></div>
             <div class="w-full bg-emerald-400 rounded-t-sm shadow-[0_0_10px_#34d399]" style="height: 100%"></div>
          </div>
        </div>

      </div>
    </div>

    <!-- ================= بخش ابزار سریع و جدول ================= -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <!-- ساخت لینک جادویی -->
      <div class="lg:col-span-1 bg-white border border-slate-100 rounded-[2.5rem] shadow-sm p-8 relative overflow-hidden flex flex-col justify-center">
        <div class="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center text-white mb-6 shadow-lg shadow-blue-500/30">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
        </div>
        <h3 class="font-black text-slate-800 text-xl mb-2">لینک‌ساز سریع</h3>
        <p class="text-xs font-bold text-slate-500 mb-6 leading-relaxed">لینک هر محصول یا دسته‌بندی از تاجربام را اینجا قرار دهید تا لینک درآمدزای شما ساخته شود.</p>
        
        <div class="space-y-4">
          <div class="relative">
            <input type="text" v-model="linkInput" placeholder="https://tajerbam.com/..." class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-medium text-slate-800 px-4 py-4 rounded-xl focus:bg-white focus:border-blue-500 outline-none transition-all" dir="ltr">
          </div>
          <button @click="generateLink" :disabled="!linkInput" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl transition-all shadow-xl shadow-slate-900/20 disabled:opacity-50 text-sm">
            تولید لینک جادویی
          </button>

          <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4" enter-to-class="opacity-100 translate-y-0">
            <div v-if="generatedLink" class="mt-4 p-1 bg-gradient-to-r from-emerald-400 to-teal-500 rounded-xl">
              <div class="bg-white rounded-lg p-3 flex items-center justify-between gap-2">
                <input type="text" readonly :value="generatedLink" class="w-full text-xs font-mono text-slate-600 bg-transparent outline-none truncate" dir="ltr">
                <button @click="copyLink" class="bg-emerald-50 text-emerald-600 hover:bg-emerald-500 hover:text-white p-2 rounded-md transition-colors flex-shrink-0">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                </button>
              </div>
            </div>
          </transition>
        </div>
      </div>

      <!-- جدول زنده کمیسیون‌ها -->
      <div class="lg:col-span-2 bg-white border border-slate-100 rounded-[2.5rem] shadow-sm overflow-hidden flex flex-col">
        <div class="p-6 md:p-8 border-b border-slate-100 flex items-center justify-between">
          <h3 class="font-black text-slate-800 text-lg flex items-center gap-3">
            <div class="w-3 h-3 bg-emerald-500 rounded-full animate-pulse shadow-[0_0_10px_#10b981]"></div>
            جریان درآمدی زنده (Live)
          </h3>
          <router-link to="/marketer/wallet" class="text-xs font-bold text-blue-600 hover:bg-blue-50 px-3 py-1.5 rounded-lg transition-colors">مشاهده کامل</router-link>
        </div>
        
        <div class="overflow-x-auto custom-scrollbar flex-grow p-2">
          <table class="w-full text-right text-sm">
            <tbody class="divide-y divide-slate-50 font-medium text-slate-700">
              
              <tr class="hover:bg-slate-50/80 transition-colors group" v-for="i in 4" :key="i">
                <td class="px-6 py-4">
                  <div class="flex items-center gap-4">
                    <div class="w-12 h-12 bg-white rounded-xl p-1 border border-slate-200 shadow-sm group-hover:shadow transition-shadow">
                      <img :src="i%2===0 ? 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png' : 'https://freepngimg.com/thumb/smartphone/133618-smart-phone-apple-free-photo.png'" class="w-full h-full object-contain mix-blend-multiply">
                    </div>
                    <div>
                      <p class="font-black text-slate-800 text-sm mb-1">{{ i%2===0 ? 'لپ‌تاپ ایسوس (عمده)' : 'گوشی سامسونگ (خرده)' }}</p>
                      <p class="text-[10px] font-bold text-slate-400">مشتری: کاربر {{ Math.floor(Math.random() * 9000) + 1000 }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4">
                  <div class="text-left">
                    <span class="block text-[10px] font-bold text-slate-400 mb-1">پورسانت شما</span>
                    <span class="font-black text-emerald-600 text-base tracking-tight">+ {{ i%2===0 ? '۲,۵۰۰,۰۰۰' : '۴۵۰,۰۰۰' }} <span class="text-[10px]">تومان</span></span>
                  </div>
                </td>
                <td class="px-6 py-4 text-center">
                  <span class="bg-emerald-50 border border-emerald-100 text-emerald-700 px-3 py-1.5 rounded-lg text-[10px] font-black shadow-sm flex items-center justify-center gap-1 w-fit mx-auto">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> واریز شد
                  </span>
                </td>
              </tr>
              
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const linkInput = ref('');
const generatedLink = ref('');

const generateLink = () => {
  const base = linkInput.value.split('?')[0];
  generatedLink.value = `${base}?ref=ali_karimi_89_vip`;
};

const copyLink = () => {
  navigator.clipboard.writeText(generatedLink.value).then(() => {
    // در واقعیت یک توست نشان می‌دهیم
    alert('لینک کپی شد!');
  });
};
</script>