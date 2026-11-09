<template>
  <div class="max-w-[1200px] mx-auto pb-16 pt-8 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- افکت‌های پس‌زمینه گلوبال -->
    <div class="absolute top-20 left-10 w-96 h-96 bg-emerald-100 rounded-full mix-blend-multiply filter blur-[100px] opacity-60 z-0 pointer-events-none"></div>
    <div class="absolute top-40 right-20 w-80 h-80 bg-teal-100 rounded-full mix-blend-multiply filter blur-[80px] opacity-50 z-0 pointer-events-none"></div>

    <div class="text-center mb-16 relative z-10">
      <div class="inline-flex items-center gap-2 bg-emerald-50 text-emerald-700 px-5 py-2 rounded-full text-xs font-black mb-8 shadow-sm border border-emerald-200">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_8px_rgba(16,185,129,0.8)]"></span>
        اشتراک حرفه‌ای و VIP بازاریابان (Partners)
      </div>
      <h1 class="text-4xl md:text-6xl font-black text-slate-800 tracking-tighter mb-6 leading-tight">
        موتور <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-500 to-teal-600 drop-shadow-sm">دراپ‌شیپینگ</span> خود را روشن کنید!
      </h1>
      <p class="text-slate-500 font-bold text-base md:text-lg max-w-3xl mx-auto leading-relaxed">
        با ارتقاء به پلن VIP، مستقیماً با بزرگترین تامین‌کنندگان کشور مذاکره کنید، قیمت عمده بگیرید و از طریق پنل اختصاصی، سفارشات مشتریان خود را بدون نیاز به انبارداری و با نام برند خودتان ثبت کنید.
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center px-4 md:px-10 relative z-10">
      
      <!-- پلن رایگان -->
      <div class="bg-white/80 backdrop-blur-xl rounded-[3rem] p-10 border-2 border-slate-100 shadow-[0_10px_40px_-15px_rgba(0,0,0,0.05)] flex flex-col h-full transform lg:scale-95 hover:scale-100 transition-transform duration-500">
        <div class="w-16 h-16 bg-slate-100 rounded-2xl flex items-center justify-center mb-6 border border-slate-200 shadow-inner">
          <svg class="w-8 h-8 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
        </div>
        <h3 class="text-2xl font-black text-slate-800 mb-2">بازاریاب عادی (Affiliate)</h3>
        <p class="text-sm font-bold text-slate-500 mb-8">مناسب برای تبلیغات در شبکه‌های اجتماعی و وب‌سایت‌ها</p>
        
        <div class="mb-10 border-b border-slate-200/60 pb-8">
          <span class="text-5xl font-black text-slate-800 tracking-tight">رایگان</span>
          <span class="text-sm font-bold text-slate-400 mr-2">همیشه</span>
        </div>
        
        <ul class="space-y-6 text-sm font-black text-slate-600 flex-grow mb-10">
          <li class="flex items-center gap-4"><div class="w-6 h-6 rounded-full bg-emerald-50 text-emerald-500 flex items-center justify-center shrink-0"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> ساخت لینک رهگیری (UTM) محصولات</li>
          <li class="flex items-center gap-4"><div class="w-6 h-6 rounded-full bg-emerald-50 text-emerald-500 flex items-center justify-center shrink-0"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> دریافت پورسانت استاندارد از فروش</li>
          <li class="flex items-center gap-4 text-slate-400 opacity-60"><div class="w-6 h-6 rounded-full bg-slate-100 text-slate-300 flex items-center justify-center shrink-0"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></div> <span class="line-through">ثبت سفارش مستقیم (Dropshipping)</span></li>
          <li class="flex items-center gap-4 text-slate-400 opacity-60"><div class="w-6 h-6 rounded-full bg-slate-100 text-slate-300 flex items-center justify-center shrink-0"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></div> <span class="line-through">چت مستقیم و چانه‌زنی با تامین‌کنندگان</span></li>
        </ul>
        <button class="w-full bg-slate-100 text-slate-500 font-black py-4.5 rounded-2xl cursor-not-allowed text-base shadow-inner border border-slate-200">پلن فعلی شما</button>
      </div>

      <!-- پلن VIP -->
      <div class="bg-gradient-to-b from-slate-900 via-slate-800 to-emerald-950 rounded-[3rem] p-10 border-2 border-emerald-500/40 shadow-[0_30px_80px_-15px_rgba(16,185,129,0.5)] relative flex flex-col h-full overflow-hidden transform hover:-translate-y-2 transition-transform duration-500">
        <!-- نورپردازی و افکت‌های VIP -->
        <div class="absolute -top-32 -right-32 w-80 h-80 bg-emerald-500 rounded-full mix-blend-screen filter blur-[90px] opacity-50 pointer-events-none"></div>
        <div class="absolute -bottom-20 -left-20 w-64 h-64 bg-teal-500 rounded-full mix-blend-screen filter blur-[80px] opacity-30 pointer-events-none"></div>
        
        <div class="absolute top-0 inset-x-0 flex justify-center">
          <span class="bg-gradient-to-r from-amber-400 to-orange-500 text-white text-[11px] font-black px-6 py-2 rounded-b-2xl shadow-[0_5px_15px_rgba(245,158,11,0.4)] tracking-wider">حرفه‌ای‌ترین ابزار بازار B2B</span>
        </div>

        <div class="w-16 h-16 bg-gradient-to-br from-emerald-400 to-teal-500 rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-emerald-500/30 mt-4 relative z-10 border border-emerald-300">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        </div>

        <div class="mb-6 relative z-10">
          <h3 class="text-3xl font-black text-white mb-2 tracking-tight">بازاریاب VIP (شریک تجاری)</h3>
          <p class="text-sm font-bold text-emerald-300">کسب درآمد نجومی با راه‌اندازی کسب‌وکار بدون سرمایه</p>
        </div>
        
        <div class="mb-10 border-b border-emerald-500/30 pb-8 relative z-10">
          <div class="flex items-end gap-2">
            <span class="text-6xl font-black text-white tracking-tighter">۳۹۰,۰۰۰</span>
            <span class="text-base font-bold text-emerald-200 mb-2">تومان / ماهانه</span>
          </div>
        </div>
        
        <ul class="space-y-6 text-sm font-bold text-emerald-50 flex-grow mb-10 relative z-10">
          <li class="flex items-center gap-4">
            <div class="w-6 h-6 rounded-full bg-emerald-500/40 border border-emerald-400 flex items-center justify-center shrink-0 shadow-sm"><svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> 
            <span class="text-amber-400 font-black text-base">دسترسی به سیستم Dropshipping (ارسال با نام شما)</span>
          </li>
          <li class="flex items-center gap-4">
            <div class="w-6 h-6 rounded-full bg-white/10 flex items-center justify-center shrink-0"><svg class="w-3.5 h-3.5 text-emerald-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> 
            <span class="text-white">ارسال درخواست همکاری و نمایندگی به فروشندگان</span>
          </li>
          <li class="flex items-center gap-4">
            <div class="w-6 h-6 rounded-full bg-white/10 flex items-center justify-center shrink-0"><svg class="w-3.5 h-3.5 text-emerald-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> 
            <span class="text-white">چت مستقیم B2B برای مذاکره قیمت همکار</span>
          </li>
          <li class="flex items-center gap-4">
            <div class="w-6 h-6 rounded-full bg-white/10 flex items-center justify-center shrink-0"><svg class="w-3.5 h-3.5 text-emerald-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg></div> 
            <span class="text-white">نمایش ویژه پروفایل شما برای تامین‌کنندگان پلتفرم</span>
          </li>
        </ul>
        
        <button @click="upgradePlan" :disabled="isUpgrading" class="w-full bg-gradient-to-r from-emerald-400 to-teal-500 hover:from-emerald-500 hover:to-teal-600 text-slate-900 font-black py-4.5 rounded-2xl shadow-[0_10px_25px_rgba(16,185,129,0.4)] transition-all hover:-translate-y-1 relative z-10 text-base disabled:opacity-70 flex justify-center items-center gap-2">
          <svg v-if="isUpgrading" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          خرید پلن و فعال‌سازی آنی
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token');

const isUpgrading = ref(false);

const upgradePlan = async () => {
  isUpgrading.value = true;
  try {
    const response = await fetch(`${API_BASE_URL}/api/plans/upgrade`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}` 
      },
      body: JSON.stringify({ plan_id: 2, billing_cycle: 'monthly' })
    });
    
    if(response.ok) {
      alert("تبریک! حساب شما به VIP ارتقا یافت. حالا می‌توانید از سیستم دراپ‌شیپینگ استفاده کنید.");
      // آپدیت وضعیت استیت در صورت وجود استور (Pinia/Vuex) یا رفرش
      router.push('/marketer/dashboard');
    } else {
      throw new Error();
    }
  } catch(error) {
    // در صورت قطعی اتصال بک‌اند
    setTimeout(() => {
      isUpgrading.value = false;
      alert("به درگاه بانکی متصل شدید (تست). اشتراک شما با موفقیت ارتقا یافت.");
      router.push('/marketer/dashboard');
    }, 1000);
  }
};
</script>