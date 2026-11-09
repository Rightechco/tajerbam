<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-16 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر و کلید ذخیره نهایی ================= -->
    <div class="bg-slate-900 p-6 md:p-8 rounded-[2.5rem] border border-slate-700/50 shadow-2xl relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      <div class="absolute -right-20 -top-20 w-64 h-64 bg-amber-500 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-5">
        <div class="w-16 h-16 bg-gradient-to-br from-amber-500 to-orange-600 rounded-2xl flex items-center justify-center text-slate-900 shadow-[0_0_30px_rgba(245,158,11,0.3)] shrink-0">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-1">پیکربندی کلان سیستم و مالی</h1>
          <p class="text-sm font-bold text-slate-400">تنظیمات درگاه‌های پرداخت، هزینه‌های ارسال، مالیات و تعرفه‌های پلتفرم</p>
        </div>
      </div>

      <div class="relative z-10 w-full md:w-auto">
        <button @click="saveAllSettings" :disabled="isSaving" class="w-full md:w-auto bg-amber-500 hover:bg-amber-400 text-slate-900 font-black px-8 py-3.5 rounded-xl transition-all shadow-[0_0_20px_rgba(245,158,11,0.3)] flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer">
          <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path></svg>
          <span v-if="isSaving">در حال ذخیره در دیتابیس...</span>
          <span v-else>ذخیره تمامی تنظیمات</span>
        </button>
      </div>
    </div>

    <!-- لودینگ سیستم -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-amber-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-amber-500 animate-pulse">در حال فراخوانی پیکربندی از سرور اصلی...</p>
    </div>

    <div v-else class="grid grid-cols-1 lg:grid-cols-12 gap-8 animate-fade-in">
      
      <!-- ================= ستون راست: عمومی، مالیات و درگاه‌ها (6 ستون) ================= -->
      <div class="lg:col-span-6 space-y-6">
        
        <!-- کارت مشخصات عمومی و مالیات -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg p-6 md:p-8 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-blue-500 to-emerald-500"></div>
          <h3 class="text-white font-black text-lg mb-6 flex items-center gap-2 border-b border-slate-800 pb-4">
            <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 14l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            عمومی و مالیات بر ارزش افزوده (VAT)
          </h3>
          <div class="space-y-5">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">نام پلتفرم (Site Title)</label>
                <input v-model="settingsData.site_name" type="text" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-amber-500 transition-colors text-sm font-bold" />
              </div>
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">درصد کارمزد سیستم (%)</label>
                <input v-model="settingsData.platform_fee_percent" type="number" class="w-full bg-slate-950 border border-slate-700 text-amber-400 px-4 py-3 rounded-xl focus:outline-none focus:border-amber-500 transition-colors text-sm font-black text-left" dir="ltr" />
              </div>
            </div>

            <div class="bg-slate-950/60 p-4 rounded-2xl border border-slate-800 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-white font-bold text-sm">محاسبه مالیات بر ارزش افزوده (VAT)</h4>
                  <p class="text-[11px] text-slate-400 mt-0.5">افزودن درصد قانونی مالیات به فاکتور نهایی خریدار در صورت‌حساب</p>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="settingsData.enable_vat" class="sr-only peer">
                  <div class="w-11 h-6 bg-slate-800 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-emerald-500"></div>
                </label>
              </div>

              <div v-if="settingsData.enable_vat" class="pt-3 border-t border-slate-800 flex items-center gap-4">
                <label class="text-slate-300 text-xs font-bold shrink-0">درصد مالیات بر ارزش افزوده:</label>
                <div class="relative flex-grow">
                  <input v-model="settingsData.vat_percent" type="number" min="0" max="30" class="w-full bg-slate-900 border border-slate-700 text-emerald-400 px-4 py-2.5 rounded-xl focus:outline-none focus:border-emerald-500 text-sm font-black text-left" dir="ltr" />
                  <span class="absolute right-3 top-2.5 text-slate-500 text-xs font-bold">%</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- کارت تنظیمات درگاه‌های پرداخت -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg p-6 md:p-8 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-amber-500 to-orange-500"></div>
          <h3 class="text-white font-black text-lg mb-6 flex items-center gap-2 border-b border-slate-800 pb-4">
            <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
            تنظیمات درگاه‌های پرداخت آنلاین و تسویه
          </h3>
          
          <div class="space-y-4">
            
            <!-- درگاه زرین‌پال -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800/80 space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-lg bg-amber-500/10 text-amber-500 font-black text-xs flex items-center justify-center border border-amber-500/20">زرین</div>
                  <div>
                    <h4 class="text-white font-bold text-sm">درگاه آنلاین زرین‌پال (ZarinPal)</h4>
                    <p class="text-[11px] text-slate-400">اتصال به شتاب با مرچنت‌آیدی رسمی</p>
                  </div>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="settingsData.enable_zarinpal" class="sr-only peer">
                  <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-amber-500"></div>
                </label>
              </div>
              <div v-if="settingsData.enable_zarinpal" class="pt-2">
                <label class="block text-slate-400 text-[11px] font-bold mb-1">مرچنت‌آیدی (Merchant ID / UUID)</label>
                <input v-model="settingsData.zarinpal_merchant" type="text" placeholder="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" class="w-full bg-slate-900 border border-slate-700 text-amber-400 font-mono px-3 py-2 rounded-xl text-xs outline-none focus:border-amber-500" dir="ltr">
              </div>
            </div>

            <!-- درگاه زیبال -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800/80 space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-500 font-black text-xs flex items-center justify-center border border-blue-500/20">زیبال</div>
                  <div>
                    <h4 class="text-white font-bold text-sm">درگاه آنلاین زیبال (Zibal)</h4>
                    <p class="text-[11px] text-slate-400">درگاه پرداخت هوشمند چندسروره</p>
                  </div>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="settingsData.enable_zibal" class="sr-only peer">
                  <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-500"></div>
                </label>
              </div>
              <div v-if="settingsData.enable_zibal" class="pt-2">
                <label class="block text-slate-400 text-[11px] font-bold mb-1">مرچنت کد زیبال (Merchant Key)</label>
                <input v-model="settingsData.zibal_merchant" type="text" placeholder="zibal" class="w-full bg-slate-900 border border-slate-700 text-blue-400 font-mono px-3 py-2 rounded-xl text-xs outline-none focus:border-blue-500" dir="ltr">
              </div>
            </div>

            <!-- پرداخت از کیف پول حقوقی -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800/80 flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-purple-500/10 text-purple-400 font-black text-xs flex items-center justify-center border border-purple-500/20">کیف</div>
                <div>
                  <h4 class="text-white font-bold text-sm">پرداخت از کیف پول حقوقی (Wallet)</h4>
                  <p class="text-[11px] text-slate-400">کسر آنی از موجودی حساب کاربر در پلتفرم</p>
                </div>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="settingsData.enable_wallet" class="sr-only peer">
                <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-purple-500"></div>
              </label>
            </div>

            <!-- پرداخت در محل / پس‌کرایه -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800/80 flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 font-black text-xs flex items-center justify-center border border-emerald-500/20">پس‌کرایه</div>
                <div>
                  <h4 class="text-white font-bold text-sm">پرداخت در مقصد / پس‌کرایه (COD)</h4>
                  <p class="text-[11px] text-slate-400">امکان تسویه فاکتور و کرایه هنگام دریافت بار</p>
                </div>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="settingsData.enable_cod" class="sr-only peer">
                <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-emerald-500"></div>
              </label>
            </div>

          </div>
        </div>

      </div>

      <!-- ================= ستون چپ: روش‌های ارسال، هزینه‌ها و پلن‌ها (6 ستون) ================= -->
      <div class="lg:col-span-6 space-y-6">
        
        <!-- کارت روش‌های ارسال و تعرفه کرایه -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg p-6 md:p-8 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-orange-500 to-amber-500"></div>
          <h3 class="text-white font-black text-lg mb-6 flex items-center gap-2 border-b border-slate-800 pb-4">
            <svg class="w-5 h-5 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
            تنظیمات روش‌های ارسال و هزینه کرایه
          </h3>

          <div class="space-y-5">
            
            <!-- باربری سنگین / پس‌کرایه -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-white font-bold text-sm">باربری سنگین صنعتی (پس‌کرایه)</h4>
                  <p class="text-[11px] text-slate-400 mt-0.5">تسویه کرایه حمل در مقصد توسط خریدار به انباردار/باربری</p>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="settingsData.enable_shipping_cargo" class="sr-only peer">
                  <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-orange-500"></div>
                </label>
              </div>
            </div>

            <!-- پست پیشتاز / پیش‌کرایه -->
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-white font-bold text-sm">پست پیشتاز ویژه (پیش‌کرایه)</h4>
                  <p class="text-[11px] text-slate-400 mt-0.5">افزودن مبلغ مشخص کرایه به فاکتور آنلاین خریدار</p>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="settingsData.enable_shipping_express" class="sr-only peer">
                  <div class="w-11 h-6 bg-slate-800 rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-orange-500"></div>
                </label>
              </div>

              <div v-if="settingsData.enable_shipping_express" class="pt-3 border-t border-slate-800 flex items-center gap-4">
                <label class="text-slate-300 text-xs font-bold shrink-0">هزینه ثابت ارسال پیشتاز:</label>
                <div class="relative flex-grow">
                  <input v-model="settingsData.shipping_express_cost" type="number" step="10000" class="w-full bg-slate-900 border border-slate-700 text-orange-400 px-4 py-2.5 rounded-xl focus:outline-none focus:border-orange-500 text-sm font-black text-left" dir="ltr" />
                  <span class="absolute right-3 top-2.5 text-slate-500 text-xs font-bold">تومان</span>
                </div>
              </div>
            </div>

            <!-- سقف خرید برای ارسال رایگان -->
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">حداقل مبلغ سفارش برای ارسال رایگان (۰ = غیرفعال)</label>
              <div class="relative">
                <input v-model="settingsData.free_shipping_threshold" type="number" step="500000" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-orange-500 transition-colors text-sm font-black text-left" dir="ltr" />
                <span class="absolute right-4 top-3.5 text-slate-500 text-xs font-bold">تومان</span>
              </div>
            </div>

          </div>
        </div>

        <!-- کارت مدیریت تعرفه پلن‌های اشتراکی -->
        <div class="bg-slate-900 border border-slate-800 rounded-[2rem] shadow-lg flex flex-col relative overflow-hidden">
          <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-violet-500 to-fuchsia-500"></div>
          
          <div class="p-6 border-b border-slate-800 bg-slate-950/30 flex justify-between items-center">
            <h3 class="text-white font-black text-lg flex items-center gap-2">
              <svg class="w-5 h-5 text-violet-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
              تعرفه اشتراک‌ها (SaaS Plans)
            </h3>
            <span class="bg-violet-500/10 text-violet-400 px-3 py-1 rounded-lg text-xs font-bold border border-violet-500/20">
              {{ plans.length }} پلن
            </span>
          </div>

          <div class="p-6 space-y-4 max-h-[300px] overflow-y-auto custom-scrollbar-dark">
            <div v-for="plan in plans" :key="plan.id" class="bg-slate-950 border border-slate-700/50 p-4 rounded-2xl flex items-center justify-between">
              <div>
                <h4 class="text-white font-bold text-sm">{{ plan.name }}</h4>
                <div class="flex gap-4 mt-1 text-xs font-mono text-slate-400">
                  <span>ماهانه: {{ formatPrice(plan.monthly_price) }} تومان</span>
                  <span>سالانه: {{ formatPrice(plan.annual_price) }} تومان</span>
                </div>
              </div>
              <button @click="openEditPlan(plan)" class="bg-slate-800 hover:bg-violet-600 text-violet-300 hover:text-white border border-slate-700 hover:border-violet-500 transition-all font-bold px-3.5 py-2 rounded-xl text-xs cursor-pointer">
                ویرایش
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ================= Modal: ویرایش قیمت پلن ================= -->
    <div v-if="isPlanModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="closeEditPlan"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2rem] w-full max-w-md relative z-10 shadow-2xl overflow-hidden animate-fade-in">
        <div class="p-8">
          <h2 class="text-2xl font-black text-white mb-2">تعیین تعرفه اشتراک</h2>
          <p class="text-xs text-slate-400 mb-6 font-bold pb-4 border-b border-slate-800">
            پلن: <span class="text-white">{{ activePlanEdit.name }}</span>
          </p>
          
          <div class="space-y-4 mb-8">
            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">قیمت اشتراک یک‌ماهه (تومان)</label>
              <input v-model="activePlanEdit.monthly_price" type="number" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 text-base font-black text-left" dir="ltr" :disabled="activePlanEdit.is_free" />
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">قیمت اشتراک یک‌ساله (تومان)</label>
              <input v-model="activePlanEdit.annual_price" type="number" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-violet-500 text-base font-black text-left" dir="ltr" :disabled="activePlanEdit.is_free" />
            </div>
          </div>

          <div class="flex gap-4">
            <button @click="closeEditPlan" class="flex-1 bg-slate-800 text-white font-bold py-3.5 rounded-xl text-sm">انصراف</button>
            <button @click="submitPlanEdit" :disabled="isSavingPlan || activePlanEdit.is_free" class="flex-[2] bg-violet-600 hover:bg-violet-500 text-white font-bold py-3.5 rounded-xl text-sm transition-all shadow-lg">
              {{ isSavingPlan ? 'در حال ذخیره...' : 'ذخیره تعرفه' }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Toast Notification -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-800 border border-emerald-500/30 shadow-2xl rounded-2xl p-4 flex items-center gap-4 z-50 animate-fade-in max-w-sm">
      <div class="w-10 h-10 bg-emerald-500/10 rounded-full flex items-center justify-center shrink-0">
        <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <div>
        <h4 class="text-white font-bold text-sm">{{ toastData.title }}</h4>
        <p class="text-slate-400 text-xs mt-0.5">{{ toastData.text }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token');

const isLoading = ref(true);
const isSaving = ref(false);
const isSavingPlan = ref(false);
const isPlanModalOpen = ref(false);
const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

// داده‌های پیکربندی
const settingsData = ref({
  site_name: '',
  site_slogan: '',
  platform_fee_percent: 5,
  min_withdrawal_amount: 500000,
  enable_vat: true,
  vat_percent: 10,
  enable_zarinpal: true,
  zarinpal_merchant: '',
  enable_zibal: true,
  zibal_merchant: '',
  enable_wallet: true,
  enable_cod: true,
  enable_shipping_cargo: true,
  enable_shipping_express: true,
  shipping_express_cost: 350000,
  free_shipping_threshold: 0
});

const plans = ref([]);
const activePlanEdit = ref(null);

const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 3500);
};

const fetchAllData = async () => {
  isLoading.value = true;
  try {
    const headers = { 'Authorization': `Bearer ${token()}`, 'Content-Type': 'application/json' };

    const setRes = await fetch(`${API_BASE}/api/admin/settings`, { headers });
    if (setRes.ok) {
      const setData = await setRes.json();
      if (setData.settings) {
        const s = setData.settings;
        settingsData.value.site_name = s.site_name || '';
        settingsData.value.platform_fee_percent = parseFloat(s.platform_fee_percent || 5);
        settingsData.value.min_withdrawal_amount = parseInt(s.min_withdrawal_amount || 500000);
        settingsData.value.enable_vat = s.enable_vat === 'true' || s.enable_vat === true;
        settingsData.value.vat_percent = parseFloat(s.vat_percent || 10);
        settingsData.value.enable_zarinpal = s.enable_zarinpal !== 'false';
        settingsData.value.zarinpal_merchant = s.zarinpal_merchant || '';
        settingsData.value.enable_zibal = s.enable_zibal !== 'false';
        settingsData.value.zibal_merchant = s.zibal_merchant || '';
        settingsData.value.enable_wallet = s.enable_wallet !== 'false';
        settingsData.value.enable_cod = s.enable_cod !== 'false';
        settingsData.value.enable_shipping_cargo = s.enable_shipping_cargo !== 'false';
        settingsData.value.enable_shipping_express = s.enable_shipping_express !== 'false';
        settingsData.value.shipping_express_cost = parseInt(s.shipping_express_cost || 350000);
        settingsData.value.free_shipping_threshold = parseInt(s.free_shipping_threshold || 0);
      }
    }

    const planRes = await fetch(`${API_BASE}/api/admin/plans`, { headers });
    if (planRes.ok) {
      const planData = await planRes.json();
      if (planData.success) plans.value = planData.plans;
    }
  } catch (e) {
    console.error("Error loading settings:", e);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchAllData();
});

const saveAllSettings = async () => {
  isSaving.value = true;
  const headers = { 'Authorization': `Bearer ${token()}`, 'Content-Type': 'application/json' };

  try {
    const keysToSave = [
      { key: 'site_name', value: settingsData.value.site_name },
      { key: 'platform_fee_percent', value: String(settingsData.value.platform_fee_percent) },
      { key: 'min_withdrawal_amount', value: String(settingsData.value.min_withdrawal_amount) },
      { key: 'enable_vat', value: String(settingsData.value.enable_vat) },
      { key: 'vat_percent', value: String(settingsData.value.vat_percent) },
      { key: 'enable_zarinpal', value: String(settingsData.value.enable_zarinpal) },
      { key: 'zarinpal_merchant', value: settingsData.value.zarinpal_merchant },
      { key: 'enable_zibal', value: String(settingsData.value.enable_zibal) },
      { key: 'zibal_merchant', value: settingsData.value.zibal_merchant },
      { key: 'enable_wallet', value: String(settingsData.value.enable_wallet) },
      { key: 'enable_cod', value: String(settingsData.value.enable_cod) },
      { key: 'enable_shipping_cargo', value: String(settingsData.value.enable_shipping_cargo) },
      { key: 'enable_shipping_express', value: String(settingsData.value.enable_shipping_express) },
      { key: 'shipping_express_cost', value: String(settingsData.value.shipping_express_cost) },
      { key: 'free_shipping_threshold', value: String(settingsData.value.free_shipping_threshold) }
    ];

    for (const item of keysToSave) {
      await fetch(`${API_BASE}/api/admin/settings`, {
        method: 'PUT', headers, body: JSON.stringify(item)
      });
    }

    showToast('تنظیمات ذخیره شد', 'تنظیمات درگاه‌ها، ارسال و مالیات با موفقیت در دیتابیس بروزرسانی شد.');
  } catch (e) {
    showToast('خطا', 'مشکلی در بروزرسانی تنظیمات رخ داد.');
  } finally {
    isSaving.value = false;
  }
};

const openEditPlan = (plan) => { activePlanEdit.value = { ...plan }; isPlanModalOpen.value = true; };
const closeEditPlan = () => { isPlanModalOpen.value = false; activePlanEdit.value = null; };

const submitPlanEdit = async () => {
  isSavingPlan.value = true;
  try {
    const payload = {
      name: activePlanEdit.value.name,
      monthly_price: Number(activePlanEdit.value.monthly_price),
      annual_price: Number(activePlanEdit.value.annual_price)
    };
    const response = await fetch(`${API_BASE}/api/admin/plans/${activePlanEdit.value.id}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token()}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (response.ok) {
      const index = plans.value.findIndex(p => p.id === activePlanEdit.value.id);
      if (index !== -1) plans.value[index] = { ...activePlanEdit.value };
      closeEditPlan();
      showToast('تعرفه‌ها به‌روز شد', 'قیمت جدید با موفقیت اعمال شد.');
    }
  } catch (e) {
    console.error(e);
  } finally {
    isSavingPlan.value = false;
  }
};

const formatPrice = (price) => {
  if (!price) return '0';
  return Number(price).toLocaleString('fa-IR');
};
</script>

<style scoped>
.custom-scrollbar-dark::-webkit-scrollbar { width: 4px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>