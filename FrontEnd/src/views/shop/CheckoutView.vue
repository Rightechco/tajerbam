<template>
  <div class="bg-slate-50 min-h-screen pb-12 pt-8 relative font-sans text-slate-800" dir="rtl">
    
    <!-- هدر بک‌گراند ملایم -->
    <div class="absolute top-0 left-0 w-full h-[400px] bg-gradient-to-b from-sky-100/40 to-transparent z-0 pointer-events-none"></div>

    <div class="container mx-auto px-4 lg:px-8 relative z-10">
      
      <!-- نوار مراحل خرید (Stepper) -->
      <div class="max-w-3xl mx-auto mb-10 hidden md:block">
        <div class="flex items-center justify-between relative">
          <div class="absolute left-0 right-0 top-1/2 -translate-y-1/2 h-1 bg-slate-200 rounded-full z-0"></div>
          <div class="absolute right-0 top-1/2 -translate-y-1/2 h-1 bg-blue-600 rounded-full z-0 w-1/2 transition-all duration-500"></div>
          
          <div class="relative z-10 flex flex-col items-center gap-2 cursor-pointer" @click="$router.push('/cart')">
            <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-black shadow-md shadow-blue-500/30 hover:scale-110 transition-transform">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <span class="text-xs font-bold text-blue-700">سبد خرید</span>
          </div>
          
          <div class="relative z-10 flex flex-col items-center gap-2">
            <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-black shadow-md shadow-blue-500/30 ring-4 ring-blue-100">۲</div>
            <span class="text-xs font-black text-slate-800">تکمیل اطلاعات</span>
          </div>
          
          <div class="relative z-10 flex flex-col items-center gap-2">
            <div class="w-10 h-10 rounded-full bg-slate-100 border-2 border-slate-300 text-slate-400 flex items-center justify-center font-black">۳</div>
            <span class="text-xs font-bold text-slate-400">پرداخت امن</span>
          </div>
        </div>
      </div>

      <h1 class="text-3xl font-black text-slate-800 mb-8 flex items-center gap-3">
        <div class="w-2 h-8 bg-blue-500 rounded-full"></div>
        صورت‌حساب و انتخاب درگاه پرداخت
      </h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- ================= ستون راست: فرم‌ها و نقشه (8 ستون) ================= -->
        <div class="lg:col-span-8 space-y-6">
          
          <!-- بخش نقشه و آدرس -->
          <div class="bg-white rounded-[2rem] border border-slate-200/60 p-6 shadow-[0_4px_20px_rgba(0,0,0,0.02)] relative overflow-hidden">
            <h2 class="text-lg font-black text-slate-800 mb-6 flex items-center gap-2 relative z-10">
              <span class="w-8 h-8 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
              </span>
              موقعیت و آدرس تحویل (B2B)
            </h2>

            <!-- نقشه تعاملی -->
            <div class="relative w-full h-72 bg-slate-100 rounded-2xl mb-8 overflow-hidden border-2 transition-colors z-10" :class="{'border-blue-400 ring-4 ring-blue-50': isMapLoading || form.address, 'border-slate-200': !isMapLoading && !form.address}">
              <div id="osm-map" class="w-full h-full z-0"></div>

              <div v-if="isMapLoading" class="absolute inset-0 bg-white/80 backdrop-blur-sm flex flex-col items-center justify-center z-20 transition-all">
                <div class="w-8 h-8 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mb-3"></div>
                <span class="font-bold text-slate-700 text-sm">در حال دریافت موقعیت دقیق و آدرس...</span>
              </div>

              <div class="absolute bottom-4 left-1/2 -translate-x-1/2 w-max z-20">
                <button @click="getUserLocation" type="button" class="bg-slate-900 hover:bg-black text-white px-6 py-3 rounded-xl font-bold text-sm shadow-[0_10px_25px_rgba(0,0,0,0.2)] transition-all hover:-translate-y-1 flex items-center gap-2 cursor-pointer">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"></path></svg>
                  مکان‌یابی من و تکمیل خودکار آدرس
                </button>
              </div>
            </div>

            <!-- پیام موفقیت -->
            <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0">
              <div v-if="addressSuccess" class="bg-emerald-50 border border-emerald-200 text-emerald-700 px-4 py-3 rounded-xl text-sm font-bold mb-6 flex items-center gap-2 shadow-sm relative z-10">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                موقعیت شما از روی نقشه استخراج و در فرم زیر جای‌گذاری شد.
              </div>
            </transition>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 relative z-10">
              <div>
                <label class="block text-xs font-bold text-slate-500 mb-2">نام تحویل‌گیرنده / شرکت <span class="text-red-500">*</span></label>
                <input v-model="form.name" type="text" placeholder="نام خود یا شرکت را وارد کنید" class="w-full bg-slate-50 border border-slate-200 text-sm font-medium text-slate-800 px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-500 mb-2">شماره همراه (جهت ثبت حساب خریدار و رهگیری) <span class="text-red-500">*</span></label>
                <input v-model="form.phone" type="tel" dir="ltr" placeholder="0912..." class="w-full bg-slate-50 border border-slate-200 text-sm font-black text-slate-800 text-right px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-500 mb-2">استان <span class="text-red-500">*</span></label>
                <input v-model="form.province" type="text" placeholder="مثال: تهران" class="w-full bg-slate-50 border border-slate-200 text-sm font-bold text-slate-800 px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-500 mb-2">شهر <span class="text-red-500">*</span></label>
                <input v-model="form.city" type="text" placeholder="مثال: تهران" class="w-full bg-slate-50 border border-slate-200 text-sm font-bold text-slate-800 px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all">
              </div>
              <div class="md:col-span-2">
                <label class="block text-xs font-bold text-slate-500 mb-2">آدرس دقیق انبار یا فروشگاه <span class="text-red-500">*</span></label>
                <textarea v-model="form.address" rows="3" placeholder="آدرس دقیق شامل خیابان، کوچه، پلاک..." class="w-full bg-slate-50 border border-slate-200 text-sm font-bold text-slate-800 px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all resize-none"></textarea>
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-500 mb-2">کد پستی (۱۰ رقمی)</label>
                <input v-model="form.postalCode" type="text" dir="ltr" class="w-full bg-slate-50 border border-slate-200 text-sm font-black text-slate-800 text-right px-4 py-3 rounded-xl focus:bg-white focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 outline-none transition-all">
              </div>
            </div>
          </div>

          <!-- روش ارسال و کرایه -->
          <div class="bg-white rounded-[2rem] border border-slate-200/60 p-6 shadow-[0_4px_20px_rgba(0,0,0,0.02)]">
            <h2 class="text-lg font-black text-slate-800 mb-6 flex items-center gap-2">
              <span class="w-8 h-8 rounded-xl bg-orange-50 text-orange-500 flex items-center justify-center">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
              </span>
              انتخاب روش ارسال و کرایه
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- روش 1: باربری پس‌کرایه -->
              <label v-if="config.enable_shipping_cargo" class="relative border-2 rounded-2xl p-4 cursor-pointer transition-all hover:bg-slate-50" :class="selectedShipping === 'cargo' ? 'border-blue-500 bg-blue-50/30 ring-2 ring-blue-500/20' : 'border-slate-100'">
                <input type="radio" v-model="selectedShipping" value="cargo" class="sr-only">
                <div class="flex items-start gap-4">
                  <div class="w-10 h-10 bg-white rounded-xl shadow-sm border border-slate-200 flex items-center justify-center text-slate-600">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"></path></svg>
                  </div>
                  <div class="flex-grow">
                    <div class="flex justify-between items-center mb-1">
                      <span class="font-black text-slate-800 text-sm">باربری سنگین (پس‌کرایه)</span>
                      <svg v-if="selectedShipping === 'cargo'" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                    </div>
                    <p class="text-xs text-slate-500 font-medium leading-relaxed">ارسال با باربری، کرایه حمل در مقصد توسط خریدار تسویه می‌شود.</p>
                  </div>
                </div>
              </label>

              <!-- روش 2: پست پیشتاز -->
              <label v-if="config.enable_shipping_express" class="relative border-2 rounded-2xl p-4 cursor-pointer transition-all hover:bg-slate-50" :class="selectedShipping === 'express' ? 'border-blue-500 bg-blue-50/30 ring-2 ring-blue-500/20' : 'border-slate-100'">
                <input type="radio" v-model="selectedShipping" value="express" class="sr-only">
                <div class="flex items-start gap-4">
                  <div class="w-10 h-10 bg-white rounded-xl shadow-sm border border-slate-200 flex items-center justify-center text-slate-600">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"></path></svg>
                  </div>
                  <div class="flex-grow">
                    <div class="flex justify-between items-center mb-1">
                      <span class="font-black text-slate-800 text-sm">پست پیشتاز (پیش‌کرایه)</span>
                      <svg v-if="selectedShipping === 'express'" class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                    </div>
                    <p class="text-xs text-slate-500 font-medium leading-relaxed">
                      تحویل سریع ۲ تا ۳ روز کاری. (+{{ formatPrice(shippingCost) }} تومان)
                    </p>
                  </div>
                </div>
              </label>
            </div>
          </div>

        </div>

        <!-- ================= ستون چپ: خلاصه فاکتور و انتخاب درگاه پرداخت (4 ستون) ================= -->
        <div class="lg:col-span-4 space-y-6 lg:sticky top-28 z-20">
          
          <div class="bg-white rounded-[2rem] border border-slate-200/60 p-6 md:p-8 shadow-[0_15px_40px_rgba(0,0,0,0.04)] relative overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-blue-600 to-indigo-500"></div>
            
            <h3 class="font-black text-slate-800 text-lg mb-6 flex items-center justify-between">
              فاکتور نهایی
              <span class="bg-blue-50 text-blue-600 px-2.5 py-1 rounded-lg text-xs font-bold">{{ cartItems.length }} ردیف</span>
            </h3>
            
            <!-- لیست خلاصه کالاها -->
            <div class="max-h-40 overflow-y-auto custom-scrollbar pr-2 mb-6 border-b border-slate-100 pb-4 space-y-3">
              <div v-for="item in cartItems" :key="item.id" class="flex justify-between items-center text-xs">
                 <div class="flex items-center gap-2 overflow-hidden w-2/3">
                   <div class="w-8 h-8 rounded-lg bg-slate-50 border border-slate-100 flex items-center justify-center shrink-0">
                     <img :src="item.img || item.image_url" class="max-h-full object-contain mix-blend-multiply">
                   </div>
                   <span class="font-bold text-slate-600 truncate">{{ item.name || item.title }}</span>
                 </div>
                 <span class="font-black text-slate-800 text-left shrink-0 whitespace-nowrap">{{ item.qty }}x</span>
              </div>
              <div v-if="cartItems.length === 0" class="text-center text-slate-400 font-bold text-sm py-4">سبد خرید شما خالی است</div>
            </div>

            <!-- خلاصه محاسبات داینامیک فاکتور -->
            <div class="space-y-4 text-sm font-medium text-slate-500 mb-6 border-b border-slate-100 pb-6">
              <div class="flex justify-between items-center">
                <span>مبلغ کل اقلام:</span>
                <span class="font-bold text-slate-800">{{ formatPrice(subTotal) }} تومان</span>
              </div>
              
              <div v-if="config.enable_vat" class="flex justify-between items-center text-slate-700">
                <span>مالیات بر ارزش افزوده ({{ config.vat_percent }}%):</span>
                <span class="font-bold text-slate-800">{{ formatPrice(taxAmount) }} تومان</span>
              </div>

              <div class="flex justify-between items-center">
                <span>هزینه ارسال:</span>
                <span class="font-bold text-slate-800">
                  <template v-if="selectedShipping === 'cargo'">پس‌کرایه (پرداخت در مقصد)</template>
                  <template v-else-if="shippingCost === 0"><span class="text-emerald-600 font-black">رایگان</span></template>
                  <template v-else>{{ formatPrice(shippingCost) }} تومان</template>
                </span>
              </div>
            </div>

            <div class="flex justify-between items-end mb-6">
              <span class="text-sm font-black text-slate-800">مبلغ قابل پرداخت:</span>
              <div class="text-left">
                <span class="text-3xl font-black text-blue-700 tracking-tight block">{{ formatPrice(finalTotal) }}</span>
                <span class="text-xs font-bold text-slate-500 mt-1 block">تومان</span>
              </div>
            </div>

            <!-- انتخاب درگاه‌های پرداخت داینامیک -->
            <div class="space-y-3 mb-8">
              <label class="block text-xs font-black text-slate-700 mb-2">روش پرداخت را انتخاب کنید:</label>

              <!-- درگاه ۱: زرین‌پال -->
              <label v-if="config.enable_zarinpal" @click="paymentMethod = 'zarinpal'" class="flex items-center justify-between p-3.5 border border-slate-200 rounded-xl cursor-pointer hover:bg-slate-50 transition-all" :class="{'ring-2 ring-amber-500 bg-amber-50/40 border-transparent': paymentMethod === 'zarinpal'}">
                <div class="flex items-center gap-3">
                  <input type="radio" v-model="paymentMethod" value="zarinpal" class="w-4 h-4 text-amber-600 focus:ring-amber-500 border-slate-300">
                  <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 font-black text-[10px] flex items-center justify-center">زرین</div>
                    <span class="text-sm font-bold text-slate-800">درگاه آنلاین زرین‌پال</span>
                  </div>
                </div>
                <span class="text-[10px] bg-amber-100 text-amber-800 font-black px-2 py-0.5 rounded">شتابی</span>
              </label>

              <!-- درگاه ۲: زیبال -->
              <label v-if="config.enable_zibal" @click="paymentMethod = 'zibal'" class="flex items-center justify-between p-3.5 border border-slate-200 rounded-xl cursor-pointer hover:bg-slate-50 transition-all" :class="{'ring-2 ring-blue-500 bg-blue-50/40 border-transparent': paymentMethod === 'zibal'}">
                <div class="flex items-center gap-3">
                  <input type="radio" v-model="paymentMethod" value="zibal" class="w-4 h-4 text-blue-600 focus:ring-blue-500 border-slate-300">
                  <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 font-black text-[10px] flex items-center justify-center">زیبال</div>
                    <span class="text-sm font-bold text-slate-800">درگاه آنلاین زیبال</span>
                  </div>
                </div>
                <span class="text-[10px] bg-blue-100 text-blue-800 font-black px-2 py-0.5 rounded">هوشمند</span>
              </label>

              <!-- درگاه ۳: کیف پول -->
              <label v-if="config.enable_wallet" @click="paymentMethod = 'wallet'" class="flex items-center justify-between p-3.5 border border-slate-200 rounded-xl cursor-pointer hover:bg-slate-50 transition-all" :class="{'ring-2 ring-purple-500 bg-purple-50/40 border-transparent': paymentMethod === 'wallet'}">
                <div class="flex items-center gap-3">
                  <input type="radio" v-model="paymentMethod" value="wallet" class="w-4 h-4 text-purple-600 focus:ring-purple-500 border-slate-300">
                  <div class="flex flex-col">
                    <span class="text-sm font-bold text-slate-800">پرداخت از کیف پول حقوقی</span>
                    <span class="text-[10px] text-slate-500 font-bold mt-0.5">موجودی: {{ formatPrice(userWalletBalance) }} تومان</span>
                  </div>
                </div>
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
              </label>

              <!-- درگاه ۴: پس‌کرایه / پرداخت در مقصد -->
              <label v-if="config.enable_cod" @click="paymentMethod = 'cod'" class="flex items-center justify-between p-3.5 border border-slate-200 rounded-xl cursor-pointer hover:bg-slate-50 transition-all" :class="{'ring-2 ring-emerald-500 bg-emerald-50/40 border-transparent': paymentMethod === 'cod'}">
                <div class="flex items-center gap-3">
                  <input type="radio" v-model="paymentMethod" value="cod" class="w-4 h-4 text-emerald-600 focus:ring-emerald-500 border-slate-300">
                  <div class="flex flex-col">
                    <span class="text-sm font-bold text-slate-800">پرداخت در مقصد / پس‌کرایه</span>
                    <span class="text-[10px] text-slate-500 font-bold mt-0.5">تسویه هنگام تحویل بار</span>
                  </div>
                </div>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-black px-2 py-0.5 rounded">پس‌کرایه</span>
              </label>
            </div>

            <!-- دکمه نهایی ثبت و پرداخت -->
            <button @click="submitOrder" :disabled="isSubmitting || cartItems.length === 0" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(0,0,0,0.15)] transition-all hover:-translate-y-0.5 disabled:opacity-50 disabled:transform-none flex items-center justify-center gap-2 cursor-pointer">
              <svg v-if="isSubmitting" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              {{ isSubmitting ? 'در حال ثبت و انتقال...' : getSubmitButtonText() }}
            </button>

            <p class="text-[10px] font-bold text-slate-400 text-center mt-4 flex items-center justify-center gap-1">
              <svg class="w-3.5 h-3.5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              پرداخت شما تحت حمایت حساب امانی (Escrow) تاجربام است.
            </p>
          </div>
        </div>

      </div>
    </div>

    <!-- مودال موفقیت ثبت سفارش -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 scale-95 translate-y-4" enter-to-class="opacity-100 scale-100 translate-y-0" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 translate-y-4">
        <div v-if="orderSuccess" class="fixed inset-0 z-[999999] flex items-center justify-center p-4 sm:p-6 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          <div class="bg-white w-full max-w-md rounded-[3rem] shadow-2xl relative overflow-hidden font-sans border border-white/20 p-8 text-center">
             <div class="w-24 h-24 bg-emerald-100 text-emerald-500 rounded-full flex items-center justify-center mx-auto mb-6 relative">
                <div class="absolute inset-0 bg-emerald-400 rounded-full animate-ping opacity-20"></div>
                <svg class="w-12 h-12 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
             </div>
             <h2 class="text-2xl font-black text-slate-800 mb-2">سفارش شما با موفقیت ثبت شد</h2>
             <p class="text-sm font-bold text-slate-500 mb-6 leading-relaxed">
               کد پیگیری سفارش: <span class="bg-slate-100 px-2.5 py-1 rounded font-mono font-black text-slate-800 tracking-widest text-base">{{ successOrderRef }}</span>
               <br>پیامک تایید سفارش و کد پیگیری به شماره همراه شما ارسال گردید.
             </p>
             <button @click="$router.push('/buyer/orders')" class="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-black py-4 rounded-xl shadow-lg transition-colors cursor-pointer">مشاهده سفارشات من</button>
          </div>
        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const API_BASE_URL = 'https://tajerbam.com';
const router = useRouter();

const form = ref({ 
  name: localStorage.getItem('user_name') || '', 
  phone: localStorage.getItem('user_phone') || '', 
  province: '', 
  city: '', 
  address: '', 
  postalCode: '' 
});

const config = ref({
  enable_vat: true,
  vat_percent: 10,
  enable_zarinpal: true,
  enable_zibal: true,
  enable_wallet: true,
  enable_cod: true,
  enable_shipping_cargo: true,
  enable_shipping_express: true,
  shipping_express_cost: 350000,
  free_shipping_threshold: 0
});

const cartItems = ref([]);
const isMapLoading = ref(false);
const addressSuccess = ref(false);
const selectedShipping = ref('cargo');
const paymentMethod = ref('zarinpal');
const isSubmitting = ref(false);
const orderSuccess = ref(false);
const successOrderRef = ref('');
const userWalletBalance = ref(0);

let mapInstance = null;
let mapMarker = null;

// دریافت داینامیک تنظیمات مالی، مالیات و درگاه‌ها از بک‌اند
const loadCheckoutConfigAndCart = async () => {
  const savedCart = localStorage.getItem('tajerbam_cart');
  if (savedCart) {
    try { cartItems.value = JSON.parse(savedCart); } catch (e) { console.error(e); }
  }

  try {
    const resConfig = await fetch(`${API_BASE_URL}/api/checkout/settings`);
    if (resConfig.ok) {
      const dataConfig = await resConfig.json();
      if (dataConfig.settings) {
        config.value = {
          ...config.value,
          ...dataConfig.settings
        };
        if (!config.value.enable_zarinpal && paymentMethod.value === 'zarinpal') {
          paymentMethod.value = config.value.enable_zibal ? 'zibal' : (config.value.enable_wallet ? 'wallet' : 'cod');
        }
      }
    }
  } catch (e) {
    console.error("Config fetch error:", e);
  }

  const token = localStorage.getItem('tajerbam_token');
  if (token) {
    try {
      const resWallet = await fetch(`${API_BASE_URL}/api/buyer/wallet`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (resWallet.ok) {
        const dataWallet = await resWallet.json();
        if (dataWallet.balance !== undefined) userWalletBalance.value = dataWallet.balance;
      }
    } catch (e) {
      console.error("Wallet fetch error:", e);
    }
  }
};

const subTotal = computed(() => {
  return cartItems.value.reduce((sum, item) => sum + (item.qty * (item.price || item.unitPrice || 0)), 0);
});

const taxAmount = computed(() => {
  if (!config.value.enable_vat) return 0;
  return Math.round((subTotal.value * (config.value.vat_percent || 0)) / 100);
});

const shippingCost = computed(() => {
  if (selectedShipping.value !== 'express') return 0;
  if (config.value.free_shipping_threshold > 0 && subTotal.value >= config.value.free_shipping_threshold) {
    return 0;
  }
  return config.value.shipping_express_cost || 350000;
});

const finalTotal = computed(() => {
  return subTotal.value + taxAmount.value + shippingCost.value;
});

const formatPrice = (price) => {
  if (!price) return '۰';
  return Number(price).toLocaleString('fa-IR');
};

const getSubmitButtonText = () => {
  if (paymentMethod.value === 'zarinpal') return 'انتقال به درگاه زرین‌پال';
  if (paymentMethod.value === 'zibal') return 'انتقال به درگاه زیبال';
  if (paymentMethod.value === 'wallet') return 'پرداخت از کیف پول و ثبت سفارش';
  return 'ثبت سفارش به‌صورت پس‌کرایه';
};

onMounted(() => {
  loadCheckoutConfigAndCart();
  
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
  document.head.appendChild(link);

  const script = document.createElement('script');
  script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
  script.onload = initMap;
  document.head.appendChild(script);
});

const initMap = () => {
  const defaultLat = 35.6892;
  const defaultLng = 51.3890;
  if (!document.getElementById('osm-map')) return;

  mapInstance = L.map('osm-map').setView([defaultLat, defaultLng], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(mapInstance);
  mapMarker = L.marker([defaultLat, defaultLng], { draggable: true }).addTo(mapInstance);
  mapMarker.on('dragend', function () {
    const position = mapMarker.getLatLng();
    reverseGeocode(position.lat, position.lng);
  });
};

const getUserLocation = () => {
  isMapLoading.value = true;
  addressSuccess.value = false;

  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        if (mapInstance && mapMarker) {
          mapInstance.setView([lat, lng], 16);
          mapMarker.setLatLng([lat, lng]);
        }
        reverseGeocode(lat, lng);
      },
      () => {
        isMapLoading.value = false;
        alert("مرورگر نتوانست موقعیت شما را پیدا کند. لطفاً آدرس را به صورت دستی وارد کنید.");
      },
      { timeout: 10000, enableHighAccuracy: true }
    );
  } else {
    isMapLoading.value = false;
    alert("مرورگر شما از قابلیت مکان‌یابی پشتیبانی نمی‌کند.");
  }
};

const reverseGeocode = async (lat, lng) => {
  isMapLoading.value = true;
  try {
    const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&accept-language=fa`);
    const data = await res.json();
    if (data && data.address) {
      form.value.province = data.address.state || data.address.province || '';
      form.value.city = data.address.city || data.address.town || data.address.county || '';
      const addressParts = [];
      if (data.address.suburb) addressParts.push(data.address.suburb);
      if (data.address.neighbourhood) addressParts.push(data.address.neighbourhood);
      if (data.address.road) addressParts.push(data.address.road);
      form.value.address = addressParts.join('، ') || data.display_name;
      form.value.postalCode = data.address.postcode || '';
      addressSuccess.value = true;
      setTimeout(() => { addressSuccess.value = false; }, 4000);
    }
  } catch (e) {
    console.error(e);
  } finally {
    isMapLoading.value = false;
  }
};

const submitOrder = async () => {
  if (!form.value.name || !form.value.phone || !form.value.address) {
    alert("لطفاً تمامی فیلدهای ستاره‌دار (نام، شماره همراه و آدرس) را وارد کنید.");
    return;
  }
  if (cartItems.value.length === 0) {
    alert("سبد خرید شما خالی است.");
    return;
  }

  if (paymentMethod.value === 'wallet' && userWalletBalance.value < finalTotal.value) {
    alert("موجودی کیف پول کافی نیست. لطفاً حساب را شارژ کرده یا از درگاه آنلاین استفاده کنید.");
    return;
  }

  isSubmitting.value = true;

  try {
    const payload = {
      customer_name: form.value.name,
      customer_phone: form.value.phone,
      customer_address: `${form.value.province} - ${form.value.city} - ${form.value.address}`,
      province: form.value.province,
      city: form.value.city,
      postal_code: form.value.postalCode,
      payment_method: paymentMethod.value,
      shipping_method: selectedShipping.value,
      items: cartItems.value,
      total_amount: finalTotal.value,
      tax_amount: taxAmount.value,
      shipping_cost: shippingCost.value
    };

    const headers = { 'Content-Type': 'application/json' };
    const currentToken = localStorage.getItem('tajerbam_token');
    if (currentToken && currentToken !== 'null' && currentToken !== 'undefined') {
      headers['Authorization'] = `Bearer ${currentToken}`;
    }

    const res = await fetch(`${API_BASE_URL}/api/buyer/cart/checkout`, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok && data.success) {
      // ثبت خودکار توکن خریدار جهت ورود به سیستم
      if (data.access_token) {
        localStorage.setItem('tajerbam_token', data.access_token);
        localStorage.setItem('user_role', data.user_role || 'buyer');
        if (data.full_name) localStorage.setItem('user_name', data.full_name);
        if (form.value.phone) localStorage.setItem('user_phone', form.value.phone);
      }

      if (data.redirect_url) {
        window.location.href = data.redirect_url;
      } else {
        successOrderRef.value = data.order_ref || `ORD-${Math.floor(Math.random() * 90000) + 10000}`;
        orderSuccess.value = true;
        localStorage.removeItem('tajerbam_cart');
        window.dispatchEvent(new Event('storage'));
      }
    } else {
      alert(data.detail || data.message || "خطا در ثبت سفارش.");
    }
  } catch (e) {
    alert("خطا در ارتباط با سرور پرداخت.");
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
#osm-map { z-index: 1; }
</style>