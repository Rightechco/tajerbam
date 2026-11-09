<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- Rendering Header and System Status... -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 rounded-[2.5rem] border border-slate-700/50 p-8 md:p-10 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.7)] relative overflow-hidden flex flex-col md:flex-row md:items-center justify-between gap-6 z-10">
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-amber-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-amber-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-amber-500 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">داشبورد فرماندهی پلتفرم</h1>
          <div class="flex flex-wrap items-center gap-3">
            <span class="bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-bold px-3 py-1 rounded-lg flex items-center gap-1.5 shadow-sm">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span> تمام سرویس‌ها در وضعیت پایدار
            </span>
            <span class="text-xs font-medium text-slate-400 bg-slate-800 px-3 py-1 rounded-lg border border-slate-700">آخرین بروزرسانی: هم‌اکنون</span>
          </div>
        </div>
      </div>

      <div class="relative z-10 flex gap-3 w-full md:w-auto">
        <button @click="refreshData" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center disabled:opacity-50 tooltip" title="بروزرسانی اطلاعات">
          <svg :class="{'animate-spin text-amber-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="logout" class="bg-rose-500/10 text-rose-400 border border-rose-500/30 px-6 py-3.5 rounded-xl hover:bg-rose-500/20 transition-all font-bold flex items-center gap-2 text-sm shadow-sm">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          خروج از سیستم
        </button>
      </div>
    </div>

    <!-- Loading State... -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-32 z-20 relative">
      <div class="relative w-20 h-20 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-amber-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-black text-amber-500 animate-pulse tracking-widest">در حال دریافت و تحلیل داده‌های کلان پلتفرم...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in relative z-10">
      
      <!-- Rendering KPI Cards (DYNAMIC FROM main.py) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- درآمد پلتفرم -->
        <div class="bg-slate-900 rounded-[2rem] border border-slate-800 p-6 shadow-lg relative overflow-hidden group hover:border-amber-500/50 transition-colors cursor-default flex flex-col justify-between h-full">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full z-0 mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10">
            <div class="flex items-center justify-between mb-4">
              <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">گردش مالی کل پلتفرم</span>
              <div class="w-10 h-10 bg-amber-500/10 text-amber-500 rounded-xl flex items-center justify-center border border-amber-500/20"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
            </div>
            <div class="text-3xl font-black text-white mb-1 tracking-tighter">{{ formatPrice(stats.total_revenue) }} <span class="text-sm font-bold text-slate-500 font-sans">تومان</span></div>
          </div>
          <div class="relative z-10 text-[11px] font-bold text-emerald-400 flex items-center gap-1 mt-4 bg-emerald-500/10 w-fit px-2.5 py-1.5 rounded-lg border border-emerald-500/20">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> درآمد کل سیستم
          </div>
        </div>

        <!-- تعداد سفارشات -->
        <div class="bg-slate-900 rounded-[2rem] border border-slate-800 p-6 shadow-lg relative overflow-hidden group hover:border-emerald-500/50 transition-colors cursor-default flex flex-col justify-between h-full">
          <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500 rounded-br-full z-0 mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10">
            <div class="flex items-center justify-between mb-4">
              <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">تعداد کل سفارشات</span>
              <div class="w-10 h-10 bg-emerald-500/10 text-emerald-500 rounded-xl flex items-center justify-center border border-emerald-500/20"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg></div>
            </div>
            <div class="text-3xl font-black text-white mb-1 tracking-tighter">{{ formatPrice(stats.total_orders) }} <span class="text-sm font-bold text-slate-500 font-sans">سفارش</span></div>
          </div>
          <div class="relative z-10 text-[11px] font-bold text-emerald-400 flex items-center gap-1 mt-4 bg-emerald-500/10 w-fit px-2.5 py-1.5 rounded-lg border border-emerald-500/20">
            وضعیت پایدار لجستیک
          </div>
        </div>

        <!-- کل کاربران -->
        <div class="bg-slate-900 rounded-[2rem] border border-slate-800 p-6 shadow-lg relative overflow-hidden group hover:border-indigo-500/50 transition-colors cursor-default flex flex-col justify-between h-full">
          <div class="absolute top-0 left-0 w-32 h-32 bg-indigo-500 rounded-br-full z-0 mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10">
            <div class="flex items-center justify-between mb-4">
              <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">کاربران فعال (پلتفرم)</span>
              <div class="w-10 h-10 bg-indigo-500/10 text-indigo-400 rounded-xl flex items-center justify-center border border-indigo-500/20"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg></div>
            </div>
            <div class="text-3xl font-black text-white mb-1 tracking-tighter">{{ formatPrice(stats.total_users) }} <span class="text-sm font-bold text-slate-500 font-sans">نفر</span></div>
          </div>
          <div class="relative z-10 flex gap-2 mt-4">
            <span class="text-[10px] font-bold text-indigo-300 bg-indigo-500/10 px-2 py-1 rounded-md border border-indigo-500/20">مجموع اعضای سایت</span>
          </div>
        </div>

        <!-- کل محصولات -->
        <div class="bg-gradient-to-br from-blue-900/40 to-slate-900 rounded-[2rem] border border-blue-900/50 p-6 shadow-lg relative overflow-hidden group hover:border-blue-500/50 transition-colors flex flex-col justify-between h-full">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full z-0 mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10">
            <div class="flex items-center justify-between mb-4">
              <span class="text-blue-400 text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
                محصولات کاتالوگ
              </span>
              <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center border border-blue-500/20"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg></div>
            </div>
            <div class="text-3xl font-black text-white mb-1 tracking-tighter">{{ formatPrice(stats.total_products) }} <span class="text-sm font-bold text-slate-400 font-sans">کالا</span></div>
          </div>
          <div class="relative z-10 mt-4">
            <span class="text-[10px] font-bold text-blue-300 bg-blue-500/10 px-2 py-1 rounded-md border border-blue-500/20">تایید شده در پلتفرم</span>
          </div>
        </div>
      </div>

      <!-- Rendering Charts and Live Feed... -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- چارت درآمد (8 ستون) -->
        <div class="lg:col-span-8 bg-slate-900 rounded-[2.5rem] border border-slate-800 shadow-lg p-6 md:p-8 flex flex-col relative overflow-hidden">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-10 relative z-10">
            <div>
              <h3 class="font-black text-white text-lg flex items-center gap-2 mb-1">
                <div class="w-3 h-3 rounded-full bg-blue-500 shadow-[0_0_10px_rgba(59,130,246,0.6)]"></div>
                روند رشد درآمد پلتفرم (تحلیل سالانه)
              </h3>
              <p class="text-xs font-bold text-slate-500">مجموع کمیسیون‌های کسر شده از فروش و اشتراک‌های VIP فروخته شده.</p>
            </div>
            <select class="bg-slate-950 text-white border border-slate-700 text-xs font-bold px-4 py-2.5 rounded-xl outline-none focus:border-blue-500 transition-colors cursor-pointer shadow-sm w-full sm:w-auto">
              <option>سال مالی ۱۴۰۵</option>
              <option>سال مالی ۱۴۰۴</option>
            </select>
          </div>
          
          <!-- پیاده‌سازی چارت با CSS -->
          <div class="flex-grow flex items-end justify-between gap-1 sm:gap-4 relative z-10 h-72 border-b border-slate-700/80 pb-2">
            <div class="absolute w-full top-0 border-t border-dashed border-slate-800 -z-10 flex items-center justify-end"><span class="text-[9px] text-slate-600 font-mono -translate-y-3 bg-slate-900 pl-2">Max</span></div>
            <div class="absolute w-full top-1/4 border-t border-dashed border-slate-800 -z-10"></div>
            <div class="absolute w-full top-2/4 border-t border-dashed border-slate-800 -z-10"></div>
            <div class="absolute w-full top-3/4 border-t border-dashed border-slate-800 -z-10"></div>
            
            <div v-for="(item, index) in chartData" :key="index" class="w-full relative group flex flex-col items-center justify-end h-full">
              <!-- Tooltip -->
              <div class="absolute -top-12 opacity-0 group-hover:opacity-100 transition-all duration-300 bg-slate-800 text-white text-[11px] font-black px-3 py-1.5 rounded-lg pointer-events-none shadow-xl z-20 whitespace-nowrap border border-slate-600 flex items-center gap-1 transform translate-y-2 group-hover:translate-y-0">
                {{ item.value }} <span class="text-slate-400 font-sans text-[9px]">میلیون</span>
              </div>
              
              <div class="w-full max-w-[3rem] bg-slate-800/50 rounded-t-xl group-hover:bg-slate-700/80 transition-colors duration-300 relative overflow-hidden" :style="`height: ${item.percent}%`">
                <div class="absolute bottom-0 w-full rounded-t-xl transition-all duration-700" :class="item.color" :style="`height: ${item.fill}%`"></div>
                <div class="absolute top-0 left-0 w-1/2 h-full bg-white/5"></div>
              </div>
              <div class="text-[10px] font-bold mt-3 transition-colors duration-300" :class="item.isCurrent ? 'text-white bg-slate-800 px-2 py-0.5 rounded' : 'text-slate-500 group-hover:text-slate-300'">{{ item.month }}</div>
            </div>
          </div>
        </div>

        <!-- فید زنده (Live Activity Feed - 4 ستون) -->
        <div class="lg:col-span-4 bg-slate-900 rounded-[2.5rem] border border-slate-800 shadow-lg flex flex-col overflow-hidden relative">
          <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-emerald-500 to-teal-500"></div>
          <div class="p-6 md:p-8 border-b border-slate-800/80 flex justify-between items-center bg-slate-950/30">
            <h3 class="font-black text-white text-base flex items-center gap-2">
              <svg class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              جریان زنده پلتفرم
            </h3>
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse shadow-[0_0_8px_rgba(16,185,129,0.8)]"></span>
          </div>
          
          <div class="flex-grow overflow-y-auto custom-scrollbar-dark p-6 space-y-6 max-h-[400px]">
            <div v-if="activities.length === 0" class="text-center text-slate-500 font-bold py-10">رویدادی ثبت نشده است.</div>
            
            <div v-for="activity in activities" :key="activity.id" class="flex gap-4 relative group">
              <!-- Timeline Line -->
              <div class="w-px h-full bg-slate-800 absolute right-[15px] top-8 group-last:hidden"></div>
              
              <div :class="activity.iconBg" class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 z-10 border border-slate-700 shadow-sm">
                <!-- استفاده از تگ استاندارد برای آیکون به جای v-html مستقیم -->
                <svg class="w-4 h-4" :class="activity.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24" v-html="activity.svg"></svg>
              </div>
              
              <div class="bg-slate-950/50 border border-slate-800/80 p-3.5 rounded-2xl flex-grow hover:border-slate-700 transition-colors">
                <p class="text-sm font-black text-slate-200 mb-1.5 flex justify-between items-center">
                  {{ activity.title }}
                  <span class="text-[9px] font-mono text-slate-500 bg-slate-900 px-1.5 py-0.5 rounded">{{ activity.time }}</span>
                </p>
                <p class="text-xs text-slate-400 leading-relaxed font-medium" v-html="activity.desc"></p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Actionable Tasks List... -->
      <div class="bg-slate-900 rounded-[2.5rem] border border-slate-800 shadow-lg p-6 md:p-8">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 gap-4 border-b border-slate-800 pb-6">
          <h3 class="font-black text-white text-xl flex items-center gap-3">
            <svg class="w-6 h-6 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
            تسک‌های عملیاتی مدیر (Pending Actions)
          </h3>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="task in pendingTasks" :key="task.id" @click="$router.push(task.link)" class="bg-slate-950 border border-slate-800 p-6 rounded-3xl flex flex-col justify-between group hover:border-indigo-500/50 hover:bg-slate-800/50 transition-all cursor-pointer shadow-sm relative overflow-hidden">
            <div class="absolute -right-10 -top-10 w-24 h-24 rounded-full mix-blend-screen opacity-10 group-hover:opacity-30 transition-opacity" :class="task.glowColor"></div>
            
            <div class="relative z-10 flex items-center justify-between mb-6">
              <div class="w-12 h-12 rounded-2xl flex items-center justify-center font-black text-xl border shadow-inner transition-colors" :class="task.iconClass">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" v-html="task.iconSvg"></svg>
              </div>
              <svg class="w-6 h-6 text-slate-600 group-hover:text-indigo-400 transition-colors transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </div>
            
            <div class="relative z-10">
              <h4 class="font-black text-white text-base mb-1.5 group-hover:text-indigo-300 transition-colors">{{ task.title }}</h4>
              <p class="text-xs font-bold text-slate-500 leading-relaxed">{{ task.subtitle }}</p>
            </div>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);

// اتصال به دیتابیس (اطلاعات کلان)
const stats = ref({
  total_revenue: 0,
  total_orders: 0,
  total_users: 0,
  total_products: 0
});

// داده‌های نمایشی هیبریدی (بخش‌هایی که هنوز API ندارند)
const chartData = ref([]);
const activities = ref([]);
const pendingTasks = ref([]);

// فرمت دهی اعداد و قیمت
const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

// خروج از حساب کاربری
const logout = () => {
  localStorage.removeItem('tajerbam_token');
  router.push('/login');
};

const refreshData = () => {
  fetchDashboardData();
};

// بارگذاری اطلاعات نمایشی گرافیکی (بخش پایین داشبورد)
const populateMockVisuals = () => {
  // Chart Data
  const months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'];
  const values = [45, 52, 68, 74, 60, 85, 90, 110, 105, 125, 140, 160]; 
  const maxVal = Math.max(...values);
  
  chartData.value = values.map((val, i) => {
    const percent = Math.floor((val / maxVal) * 100);
    return {
      month: months[i],
      value: val,
      percent: percent,
      fill: Math.floor(percent * 0.8),
      color: i === 10 ? 'bg-gradient-to-t from-amber-600 to-yellow-400' : 'bg-gradient-to-t from-blue-600 to-indigo-400',
      isCurrent: i === 10
    };
  });

  // Live Feed
  activities.value = [
    { 
      id: 1, title: 'ثبت‌نام فروشنده جدید', time: '5 دقیقه پیش', 
      desc: 'شرکت <b>رایان تکرو</b> مدارک هویتی خود را برای فعالیت در پلتفرم ارسال کرد.', 
      iconBg: 'bg-slate-900', iconColor: 'text-blue-400', 
      svg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path>'
    },
    { 
      id: 2, title: 'خرید اشتراک VIP', time: '12 دقیقه پیش', 
      desc: 'بازاریاب <b>علی کریمی</b> اشتراک یک‌ساله دراپ‌شیپینگ را خریداری نمود.', 
      iconBg: 'bg-slate-900', iconColor: 'text-amber-400', 
      svg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path>'
    },
    { 
      id: 3, title: 'ثبت استعلام (RFQ)', time: '28 دقیقه پیش', 
      desc: 'سازمان <b>دانشگاه آزاد</b> یک استعلام خرید برای ۵۰ قلم کالای دیجیتال ثبت کرد.', 
      iconBg: 'bg-slate-900', iconColor: 'text-violet-400', 
      svg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>'
    },
    { 
      id: 4, title: 'درخواست تسویه پایا', time: '1 ساعت پیش', 
      desc: 'تامین‌کننده <b>دیجیتال شاپ</b> درخواست برداشت ۱۲۰,۰۰۰,۰۰۰ تومان ثبت کرد.', 
      iconBg: 'bg-slate-900', iconColor: 'text-emerald-400', 
      svg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>'
    },
    { 
      id: 5, title: 'شکایت خریدار', time: '2 ساعت پیش', 
      desc: 'خریدار <b>پیمانکاری حسینی</b> برای سفارش ORD-9811 درخواست داوری ثبت کرد.', 
      iconBg: 'bg-rose-950', iconColor: 'text-rose-400', 
      svg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>'
    },
  ];

  // Pending Tasks
  pendingTasks.value = [
    { id: 1, title: 'احراز هویت و KYC', subtitle: 'بررسی مدارک کاربران جدید', link: '/admin/users', glowColor: 'bg-blue-500', iconClass: 'bg-slate-900 text-blue-400 border-blue-500/30', iconSvg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"></path>' },
    { id: 2, title: 'محصولات در انتظار', subtitle: 'تایید کالاهای جدید فروشندگان', link: '/admin/products', glowColor: 'bg-cyan-500', iconClass: 'bg-slate-900 text-cyan-400 border-cyan-500/30', iconSvg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>' },
    { id: 3, title: 'درخواست‌های تسویه', subtitle: 'واریز وجه پایا به کاربران', link: '/admin/finance', glowColor: 'bg-emerald-500', iconClass: 'bg-slate-900 text-emerald-400 border-emerald-500/30', iconSvg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>' },
    { id: 4, title: 'پرونده‌های اختلاف', subtitle: 'شکایات باز روی میز قضاوت', link: '/admin/orders', glowColor: 'bg-rose-500', iconClass: 'bg-rose-950 text-rose-500 border-rose-500/30', iconSvg: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path>' },
  ];
};

// دریافت اطلاعات واقعی از بک اند FastAPI
const fetchDashboardData = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/dashboard`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });
    
    if(response.ok) {
      const data = await response.json();
      if(data.success && data.stats) {
        // مپ کردن داده‌های بک اند به فرانت اند
        stats.value = {
          total_revenue: data.stats.total_revenue || 0,
          total_orders: data.stats.total_orders || 0,
          total_users: data.stats.total_users || 0,
          total_products: data.stats.total_products || 0
        };
      }
    } else {
      // اگر توکن نامعتبر یا منقضی شده بود به صفحه لاگین منتقل شود
      if (response.status === 401 || response.status === 403) {
        logout();
        return;
      }
      throw new Error(`Server responded with ${response.status}`);
    }
  } catch (error) {
    console.error("خطا در دریافت اطلاعات داشبورد سیستم:", error);
  } finally {
    populateMockVisuals();
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchDashboardData();
});
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.5s ease-out forwards; }
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
</style>