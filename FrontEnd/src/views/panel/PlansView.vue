<template>
  <div class="max-w-[1200px] mx-auto pb-20 font-sans text-slate-800 relative overflow-hidden" dir="rtl">
    
    <!-- افکت‌های پس‌زمینه و نورپردازی شیشه‌ای -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-gradient-to-b from-amber-200/40 via-blue-50/20 to-transparent rounded-full filter blur-[100px] pointer-events-none z-0"></div>

    <!-- ================= هدر و معرفی ================= -->
    <div class="text-center mt-12 mb-16 relative z-10">
      <div class="inline-flex items-center gap-2 bg-white/70 backdrop-blur-md text-amber-600 px-5 py-2.5 rounded-full text-xs font-black mb-6 shadow-sm border border-amber-200/60">
        <svg class="w-4 h-4 animate-pulse" fill="currentColor" viewBox="0 0 20 20">
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
        </svg>
        ارتقای ویژه حساب تامین‌کنندگان و فروشندگان
      </div>
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-slate-800 tracking-tight mb-6 leading-tight">
        فروش عمده خود را به <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-500 to-orange-500">سطح بعدی</span> ببرید!
      </h1>
      <p class="text-slate-500 font-bold text-sm md:text-base max-w-2xl mx-auto leading-relaxed">
        با ارتقاء حساب خود به سطح طلایی، اطلاعات خریداران را به صورت نامحدود مشاهده کنید، کمیسیون پلتفرم را به صفر برسانید و در رتبه‌بندی‌های سایت بالاتر قرار بگیرید.
      </p>

      <!-- سوییچ ماهانه / سالانه -->
      <div class="mt-12 flex items-center justify-center gap-4">
        <span :class="['text-sm font-black transition-colors', !isYearly ? 'text-slate-800' : 'text-slate-400']">پرداخت ماهانه</span>
        <div class="relative bg-slate-200 w-16 h-8 rounded-full cursor-pointer shadow-inner p-1 transition-colors" :class="isYearly ? 'bg-amber-500' : ''" @click="isYearly = !isYearly">
          <div class="absolute top-1 w-6 h-6 bg-white rounded-full shadow-md transition-all duration-300 flex items-center justify-center" :class="isYearly ? 'left-1' : 'left-9'">
             <svg v-if="isYearly" class="w-3.5 h-3.5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
             </svg>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span :class="['text-sm font-black transition-colors', isYearly ? 'text-slate-800' : 'text-slate-400']">خرید سالانه</span>
          <span class="bg-emerald-100 text-emerald-700 text-[10px] font-black px-2 py-0.5 rounded-md border border-emerald-200">۲۰٪ تخفیف ویژه</span>
        </div>
      </div>
    </div>

    <!-- ================= وضعیت بارگذاری ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 relative z-10">
      <div class="w-12 h-12 border-4 border-amber-400 border-t-transparent rounded-full animate-spin mb-4"></div>
      <p class="text-xs font-bold text-slate-400">در حال استعلام پویای پلن‌ها و موجودی حساب از سرور...</p>
    </div>

    <!-- ================= کارت‌های قیمت‌گذاری (پویا از بک‌اند) ================= -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12 max-w-4xl mx-auto px-4 relative z-10">
      
      <!-- پلن پایه (رایگان) -->
      <div class="bg-white rounded-[3rem] p-8 lg:p-10 border border-slate-200 shadow-sm flex flex-col mt-4 md:mt-8 relative overflow-hidden transition-all hover:shadow-[0_10px_30px_rgba(0,0,0,0.03)]">
        <div class="mb-8 border-b border-slate-100 pb-8">
          <h3 class="text-xl font-black text-slate-800 mb-2">{{ freePlan.name || 'فروشنده پایه' }}</h3>
          <p class="text-xs font-bold text-slate-500">شروع سریع برای تامین‌کنندگان خرد</p>
          <div class="mt-6 text-4xl font-black text-slate-800">
            رایگان <span class="text-sm font-bold text-slate-400">/ همیشه</span>
          </div>
        </div>
        
        <ul class="space-y-5 mb-10 flex-grow text-sm font-bold text-slate-600">
          <li class="flex items-start gap-3">
            <svg class="w-5 h-5 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            ثبت کالا تا سقف ۵۰ عدد
          </li>
          <li class="flex items-start gap-3">
            <svg class="w-5 h-5 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            دریافت پوش نوتیفیکیشن درخواست‌ها
          </li>
          <li class="flex items-start gap-3 opacity-50">
            <svg class="w-5 h-5 text-slate-300 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            <span class="line-through">مشاهده شماره تماس خریداران B2B</span>
          </li>
          <li class="flex items-start gap-3 opacity-50">
            <svg class="w-5 h-5 text-slate-300 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            پرداخت کارمزد فروش به پلتفرم
          </li>
          <li class="flex items-start gap-3 opacity-50">
            <svg class="w-5 h-5 text-slate-300 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            <span class="line-through">تولید محتوا و سئو با هوش مصنوعی</span>
          </li>
        </ul>
        
        <button class="w-full py-4 rounded-2xl font-black text-slate-600 bg-slate-100 border border-slate-200 cursor-default">
          {{ userProfile.is_vip ? 'طرح اولیه شما' : 'طرح فعلی شما' }}
        </button>
      </div>

      <!-- پلن طلایی (VIP) -->
      <div class="bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 rounded-[3rem] p-1 border-2 border-amber-400/50 shadow-[0_20px_50px_rgba(245,158,11,0.2)] relative transform md:-translate-y-4 transition-transform hover:-translate-y-6">
        
        <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-amber-400 to-orange-500 text-slate-950 text-[10px] font-black px-4 py-1.5 rounded-full shadow-lg whitespace-nowrap z-20 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd"></path>
          </svg>
          پیشنهاد ویژه فروشندگان برتر
        </div>

        <div class="bg-gradient-to-b from-slate-900 to-slate-800 rounded-[2.8rem] p-8 lg:p-10 h-full flex flex-col relative overflow-hidden">
          <div class="absolute -right-20 -top-20 w-64 h-64 bg-amber-500 rounded-full mix-blend-screen filter blur-[90px] opacity-20 pointer-events-none"></div>
          
          <div class="mb-8 border-b border-slate-700 pb-8 relative z-10">
            <h3 class="text-xl font-black text-white mb-2 flex items-center gap-2">
              <svg class="w-6 h-6 text-amber-400" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
              </svg>
              {{ vipPlan.name || 'فروشنده طلایی (VIP)' }}
            </h3>
            <p class="text-xs font-bold text-slate-400">ابزارهای حرفه‌ای برای عمده‌فروشان و بنکداران</p>
            <div class="mt-6 text-4xl font-black text-white flex items-center gap-2">
              <span>{{ formatPrice(currentPrice) }}</span>
              <span class="text-sm font-bold text-slate-400">تومان / {{ isYearly ? 'سالانه' : 'ماهانه' }}</span>
            </div>
            <p v-if="isYearly" class="text-[10px] font-bold text-emerald-400 mt-2 bg-emerald-500/10 px-2 py-1 rounded w-fit border border-emerald-500/20">شامل ۲۰٪ تخفیف ویژه پرداخت سالانه!</p>
          </div>
          
          <ul class="space-y-5 mb-10 flex-grow text-sm font-bold text-slate-300 relative z-10">
            <li class="flex items-start gap-3 text-white">
              <svg class="w-5 h-5 text-amber-400 shrink-0 drop-shadow-[0_0_8px_rgba(251,191,36,0.5)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              <b>حذف کامل کمیسیون</b> فروش در تاجربام
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              مشاهده اطلاعات تماس تمامی خریداران
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              ارسال نامحدود پیش‌فاکتور (Quote)
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              تولید محتوا و سئوی خودکار با هوش مصنوعی
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
              بج طلایی و اولویت نمایش در خروجی گوگل
            </li>
          </ul>
          
          <button v-if="userProfile.is_vip" class="relative z-10 w-full py-4 rounded-2xl font-black text-emerald-950 bg-emerald-400 shadow-lg cursor-default flex items-center justify-center gap-2">
            <svg class="w-5 h-5 text-emerald-950" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            حساب VIP شما فعال است
          </button>
          
          <button v-else @click="openPaymentModal" class="relative z-10 w-full py-4 rounded-2xl font-black text-slate-900 bg-gradient-to-r from-amber-400 to-orange-500 hover:from-amber-300 hover:to-orange-400 shadow-[0_10px_25px_rgba(245,158,11,0.4)] transition-all hover:-translate-y-1 flex items-center justify-center gap-2 cursor-pointer">
            <span>خرید و فعال‌سازی آنی</span>
          </button>
        </div>
      </div>

    </div>

    <!-- ================= بخش سوالات متداول (FAQ) ================= -->
    <div class="mt-32 max-w-3xl mx-auto px-4 relative z-10">
      <div class="text-center mb-10">
        <h2 class="text-2xl md:text-3xl font-black text-slate-800 mb-2">سوالات متداول</h2>
        <p class="text-sm font-bold text-slate-500">پاسخ به پرتکرارترین پرسش‌های تامین‌کنندگان و فروشندگان.</p>
      </div>

      <div class="space-y-4">
        <div v-for="(faq, index) in faqs" :key="index" class="bg-white border border-slate-200 rounded-2xl overflow-hidden transition-all shadow-sm">
          <button @click="activeFaq = activeFaq === index ? null : index" class="w-full flex items-center justify-between p-6 text-right focus:outline-none hover:bg-slate-50 transition-colors">
            <h4 class="font-black text-slate-800 text-sm md:text-base flex items-center gap-3">
              <div class="w-8 h-8 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center shrink-0">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              {{ faq.question }}
            </h4>
            <svg :class="['w-5 h-5 text-slate-400 transition-transform duration-300', activeFaq === index ? 'rotate-180 text-amber-600' : '']" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>
          
          <transition @enter="enter" @leave="leave">
            <div v-if="activeFaq === index" class="overflow-hidden bg-slate-50 border-t border-slate-100">
              <p class="p-6 text-sm font-medium text-slate-600 leading-relaxed text-justify" v-html="faq.answer"></p>
            </div>
          </transition>
        </div>
      </div>
    </div>

    <!-- ================= MODAL انتخاب روش پرداخت (کیف پول / زرین‌پال / زیبال) ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="paymentModalOpen" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-lg rounded-[2.5rem] shadow-2xl relative font-sans overflow-hidden border border-slate-100">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-amber-400 via-orange-500 to-amber-600"></div>
            
            <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-slate-50/80">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center">
                  <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z"></path>
                    <path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <div>
                  <h3 class="font-black text-slate-800 text-base">انتخاب روش پرداخت</h3>
                  <p class="text-xs font-bold text-slate-400 mt-0.5">پلن {{ vipPlan.name || 'فروشنده طلایی VIP' }} ({{ isYearly ? 'سالانه' : 'ماهانه' }})</p>
                </div>
              </div>
              <button @click="paymentModalOpen = false" class="w-8 h-8 bg-white shadow-sm rounded-full flex items-center justify-center text-slate-500 hover:text-red-500 transition-colors cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="p-6 space-y-5">
              
              <!-- پیش‌فاکتور قیمت -->
              <div class="bg-amber-50/60 border border-amber-200/60 rounded-2xl p-4 flex justify-between items-center">
                <span class="text-xs font-bold text-slate-600">مبلغ قابل پرداخت:</span>
                <span class="text-xl font-black text-amber-600">{{ formatPrice(currentPrice) }} <span class="text-xs font-bold text-slate-500">تومان</span></span>
              </div>

              <!-- گزینه‌های پرداخت -->
              <div class="space-y-3">
                <label class="block text-xs font-black text-slate-700">لطفاً درگاه یا کیف پول خود را انتخاب کنید:</label>
                
                <!-- گزینه ۱: کیف پول -->
                <div @click="selectedGateway = 'wallet'" :class="['p-4 rounded-2xl border-2 transition-all cursor-pointer flex items-center justify-between', selectedGateway === 'wallet' ? 'border-amber-500 bg-amber-50/30 shadow-sm' : 'border-slate-100 hover:border-slate-200 bg-white']">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center font-black">👛</div>
                    <div>
                      <h4 class="font-black text-slate-800 text-sm">کیف پول حقوقی تاجربام</h4>
                      <p class="text-xs font-bold text-slate-400 mt-0.5">موجودی فعلی: <span class="text-slate-700 font-mono font-black">{{ formatPrice(userProfile.wallet_balance || 0) }}</span> تومان</p>
                    </div>
                  </div>
                  <div v-if="userProfile.wallet_balance < currentPrice" class="text-[10px] font-black text-rose-500 bg-rose-50 px-2 py-1 rounded-md border border-rose-100">موجودی ناکافی</div>
                  <div v-else class="w-5 h-5 rounded-full border-2 border-amber-500 flex items-center justify-center">
                    <div v-if="selectedGateway === 'wallet'" class="w-2.5 h-2.5 bg-amber-500 rounded-full"></div>
                  </div>
                </div>

                <!-- گزینه ۲: درگاه زرین‌پال -->
                <div @click="selectedGateway = 'zarinpal'" :class="['p-4 rounded-2xl border-2 transition-all cursor-pointer flex items-center justify-between', selectedGateway === 'zarinpal' ? 'border-amber-500 bg-amber-50/30 shadow-sm' : 'border-slate-100 hover:border-slate-200 bg-white']">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-black text-xs">زرین</div>
                    <div>
                      <h4 class="font-black text-slate-800 text-sm">درگاه پرداخت شتابی زرین‌پال (ZarinPal)</h4>
                      <p class="text-xs font-bold text-slate-400 mt-0.5">اتصال مستقیم به کلیه کارت‌های بانکی کشور</p>
                    </div>
                  </div>
                  <div class="w-5 h-5 rounded-full border-2 border-amber-500 flex items-center justify-center">
                    <div v-if="selectedGateway === 'zarinpal'" class="w-2.5 h-2.5 bg-amber-500 rounded-full"></div>
                  </div>
                </div>

                <!-- گزینه ۳: درگاه زیبال -->
                <div @click="selectedGateway = 'zibal'" :class="['p-4 rounded-2xl border-2 transition-all cursor-pointer flex items-center justify-between', selectedGateway === 'zibal' ? 'border-amber-500 bg-amber-50/30 shadow-sm' : 'border-slate-100 hover:border-slate-200 bg-white']">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-blue-100 text-blue-600 flex items-center justify-center font-black text-xs">زیبال</div>
                    <div>
                      <h4 class="font-black text-slate-800 text-sm">درگاه هوشمند زیبال (Zibal)</h4>
                      <p class="text-xs font-bold text-slate-400 mt-0.5">پرداخت سریع با بالاترین نرخ تراکنش موفق</p>
                    </div>
                  </div>
                  <div class="w-5 h-5 rounded-full border-2 border-amber-500 flex items-center justify-center">
                    <div v-if="selectedGateway === 'zibal'" class="w-2.5 h-2.5 bg-amber-500 rounded-full"></div>
                  </div>
                </div>

              </div>

            </div>

            <!-- دکمه تایید نهایی -->
            <div class="p-6 border-t border-slate-100 bg-slate-50 flex items-center justify-between">
              <button @click="paymentModalOpen = false" class="text-xs font-bold text-slate-400 hover:text-slate-600">انصراف</button>
              <button @click="confirmPayment" :disabled="isProcessing" class="bg-gradient-to-r from-amber-400 to-orange-500 hover:from-amber-300 hover:to-orange-400 text-slate-900 font-black px-8 py-3.5 rounded-xl shadow-lg shadow-amber-500/20 transition-all text-sm flex items-center gap-2 cursor-pointer disabled:opacity-50">
                <svg v-if="isProcessing" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>انتقال به درگاه و پرداخت</span>
              </button>
            </div>

          </div>
        </div>
      </transition>
    </Teleport>

    <!-- توست اطلاع‌رسانی -->
    <Teleport to="body">
      <transition name="toast-fade">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[100000] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-3 border', toast.type === 'error' ? 'bg-rose-600 border-rose-500' : 'bg-slate-900 border-slate-700']">
          <div :class="['w-10 h-10 rounded-xl flex items-center justify-center shrink-0', toast.type === 'error' ? 'bg-white/20' : 'bg-emerald-500/20 text-emerald-400']">
            <svg v-if="toast.type !== 'error'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm mb-0.5">{{ toast.title }}</h4>
            <p class="text-xs text-slate-300 font-medium max-w-xs leading-relaxed">{{ toast.message }}</p>
          </div>
        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';

const isYearly = ref(true);
const isLoading = ref(true);
const isProcessing = ref(false);
const activeFaq = ref(0);

// Modal and Payment State
const paymentModalOpen = ref(false);
const selectedGateway = ref('zarinpal'); // 'wallet', 'zarinpal', 'zibal'

const freePlan = ref({ name: 'فروشنده پایه', monthly_price: 0, annual_price: 0 });
const vipPlan = ref({ id: 2, name: 'فروشنده طلایی (VIP)', monthly_price: 99000, annual_price: 890000 });
const userProfile = ref({ wallet_balance: 0, is_vip: false });

const currentPrice = computed(() => {
  return isYearly.value ? (vipPlan.value.annual_price || 890000) : (vipPlan.value.monthly_price || 99000);
});

const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 5000);
};

const formatPrice = (val) => {
  if (val === undefined || val === null) return '۰';
  return Number(val).toLocaleString('fa-IR');
};

// Fetch Plans and Profile
const fetchInitialData = async () => {
  isLoading.value = true;
  try {
    // 1. Fetch Plans
    const resPlans = await fetch(`${API_BASE_URL}/api/plans`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (resPlans.ok) {
      const dataPlans = await resPlans.json();
      const planList = dataPlans.plans || dataPlans;
      if (Array.isArray(planList)) {
        const foundVip = planList.find(p => p.type === 'seller' && !p.is_free) || planList[1];
        if (foundVip) vipPlan.value = foundVip;
        const foundFree = planList.find(p => p.is_free) || planList[0];
        if (foundFree) freePlan.value = foundFree;
      }
    }

    // 2. Fetch User Profile & Balance
    const resUser = await fetch(`${API_BASE_URL}/api/user/me`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (resUser.ok) {
      const userData = await resUser.json();
      userProfile.value = userData;
    }
  } catch (e) {
    console.error("Error loading plans data:", e);
  } finally {
    isLoading.value = false;
  }
};

const openPaymentModal = () => {
  paymentModalOpen.value = true;
};

const confirmPayment = async () => {
  if (selectedGateway.value === 'wallet' && userProfile.value.wallet_balance < currentPrice.value) {
    showToast('موجودی ناکافی', 'موجودی کیف پول شما کافی نیست. لطفاً کیف پول را شارژ کرده یا از درگاه آنلاین استفاده کنید.', 'error');
    return;
  }

  isProcessing.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/plans/checkout`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        plan_id: vipPlan.value.id || 2,
        billing_cycle: isYearly.value ? 'annual' : 'monthly',
        gateway: selectedGateway.value
      })
    });

    const data = await response.json();

    if (response.ok && data.success) {
      paymentModalOpen.value = false;
      
      if (data.redirect_url) {
        showToast('در حال انتقال', 'در حال انتقال به درگاه پرداخت بانکی...', 'success');
        setTimeout(() => {
          window.location.href = data.redirect_url;
        }, 1200);
      } else {
        userProfile.value.is_vip = true;
        if (data.new_balance !== undefined) userProfile.value.wallet_balance = data.new_balance;
        showToast('پرداخت موفق!', 'تبریک! حساب شما به سطح طلایی ارتقا یافت. تمام امکانات فعال شد.', 'success');
      }
    } else {
      showToast('خطا در پرداخت', data.detail || data.message || 'مشکلی در فرایند پرداخت رخ داد.', 'error');
    }
  } catch (e) {
    showToast('خطا', 'ارتباط با سرور برقرار نشد.', 'error');
  } finally {
    isProcessing.value = false;
  }
};

const faqs = ref([
  {
    question: 'منظور از "حذف کمیسیون" در پلن طلایی چیست؟',
    answer: 'در حالت پایه (رایگان)، برای مشاهده اطلاعات خریدار و تایید نهایی سفارش، شما باید بین ۵ تا ۱۰ درصد کارمزد به پلتفرم پرداخت کنید. اما با خرید پلن طلایی، این هزینه به طور کامل <b>صفر می‌شود</b> و تمام سود فروش متعلق به خود شماست.'
  },
  {
    question: 'تولید محتوا با هوش مصنوعی (AI) چگونه کار می‌کند؟',
    answer: 'ما یک کپی‌رایتر هوش مصنوعی اختصاصی را به پنل شما متصل کرده‌ایم. کافیست نام محصول را وارد کنید؛ ربات ما به صورت خودکار توضیحات تجاری، تگ‌های سئو (SEO) و عنوان‌های جذاب را برای شما می‌نویسد تا کالای شما در گوگل رتبه بهتری بگیرد.'
  },
  {
    question: 'آیا پرداخت از طریق کیف پول حقوقی شامل تخفیف می‌شود؟',
    answer: 'بله، با شارژ قبلی کیف پول می‌توانید بلافاصله و بدون کارمزد بانکی حساب خود را ارتقا دهید.'
  },
  {
    question: 'منظور از دسترسی نامحدود به مناقصات چیست؟',
    answer: 'در بخش بازار مناقصات (RFQ)، خریداران عمده نیازهای خود را ثبت می‌کنند. فروشندگان عادی نمی‌توانند شماره تماس آن‌ها را ببینند، اما شما به عنوان <b>فروشنده طلایی</b> به تمام اطلاعات آن‌ها دسترسی دارید و می‌توانید مستقیماً برایشان پیش‌فاکتور صادر کنید.'
  }
]);

const enter = (el) => {
  el.style.height = 'auto';
  const height = getComputedStyle(el).height;
  el.style.height = 0;
  getComputedStyle(el);
  setTimeout(() => { el.style.height = height; });
};

const leave = (el) => {
  el.style.height = getComputedStyle(el).height;
  getComputedStyle(el);
  setTimeout(() => { el.style.height = 0; });
};

onMounted(() => {
  fetchInitialData();
});
</script>

<style scoped>
.overflow-hidden {
  transition: height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.toast-fade-enter-active, .toast-fade-leave-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.toast-fade-enter-from, .toast-fade-leave-to { opacity: 0; transform: translateY(20px) scale(0.9); }
</style>