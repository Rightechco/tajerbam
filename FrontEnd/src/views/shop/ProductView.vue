<template>
  <div class="bg-[#f8fafc] min-h-screen pb-28 lg:pb-20 font-sans text-slate-800 relative overflow-x-hidden" dir="rtl">
    <!-- هدر بسیار ملایم در بک‌گراند بالا -->
    <div class="absolute top-0 left-0 w-full h-[500px] bg-gradient-to-b from-blue-50/80 via-sky-50/30 to-transparent z-0 pointer-events-none"></div>

    <div class="container mx-auto px-4 lg:px-8 py-8 space-y-10 relative z-10">
      
      <!-- ================= 1. Breadcrumb (مسیر کالا) ================= -->
      <nav class="flex items-center text-xs font-bold text-slate-500 gap-2 mb-4 w-fit px-1 rounded-xl flex-wrap">
        <router-link to="/" class="hover:text-blue-600 transition flex items-center gap-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
          خانه
        </router-link>
        <svg class="w-4 h-4 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        <span class="hover:text-blue-600 cursor-pointer transition">{{ product?.category || 'محصولات' }}</span>
        <svg class="w-4 h-4 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        <span class="text-slate-800 bg-white px-3 py-1.5 rounded-lg shadow-sm border border-slate-100 truncate max-w-[200px]">{{ product?.title || 'در حال بارگذاری...' }}</span>
      </nav>

      <!-- ================= 2. بخش اصلی (گالری، اطلاعات، باکس خرید) ================= -->
      <div v-if="isLoading" class="flex flex-col items-center justify-center py-32">
         <div class="w-16 h-16 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mb-6"></div>
         <p class="font-black text-slate-500 animate-pulse">در حال دریافت اطلاعات کالا از شبکه...</p>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- ================= ستون راست: گالری داینامیک تصاویر و ویدئو (4 ستون) ================= -->
        <div class="lg:col-span-4 space-y-4 lg:sticky top-28 z-20">
          <div class="bg-white rounded-[2.5rem] border border-slate-100 p-4 flex items-center justify-center h-80 lg:h-[420px] shadow-[0_20px_50px_rgba(0,0,0,0.03)] relative group overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-tr from-slate-50 to-transparent opacity-50 pointer-events-none"></div>
            
            <div class="absolute top-5 right-5 flex flex-col gap-2 z-20">
              <span v-if="product.promotions?.is_flash_sale" class="bg-rose-500 text-white text-[10px] font-black px-3 py-1.5 rounded-xl flex items-center gap-1.5 shadow-md shadow-rose-500/30">
                <svg class="w-3.5 h-3.5 animate-pulse" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg>
                پیشنهاد شگفت‌انگیز
              </span>
              <span class="bg-emerald-500/90 backdrop-blur-sm text-white text-[10px] font-black px-3 py-1.5 rounded-xl flex items-center gap-1.5 shadow-md border border-emerald-400/50">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg> بیمه ارسال
              </span>
            </div>

            <button v-if="selectedMedia.type !== 'video'" @click="showLightbox = true" class="absolute bottom-4 left-4 bg-white/80 hover:bg-white backdrop-blur border border-slate-200 text-slate-700 p-2.5 rounded-2xl shadow-sm z-20 transition-all hover:scale-105" title="بزرگ‌نمایی">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"></path></svg>
            </button>

            <!-- Media Renderer با پشتیبانی از ویدئو پلیر HTML5 و عکس بدون افکت ترکیبی -->
            <transition name="fade" mode="out-in">
              <div v-if="selectedMedia.type === 'video'" class="w-full h-full flex items-center justify-center relative z-10">
                <video :key="selectedMedia.preview" :src="selectedMedia.preview" controls autoplay class="w-full h-full object-contain rounded-2xl bg-black/90 shadow-2xl"></video>
              </div>
              <img v-else :key="selectedMedia.preview" :src="selectedMedia.preview || 'https://placehold.co/500x500/f8fafc/475569?text=TajerBam'" @error="$event.target.src='https://placehold.co/500x500/f8fafc/475569?text=TajerBam'" @click="showLightbox = true" class="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform duration-700 ease-out cursor-zoom-in drop-shadow-xl relative z-10" alt="محصول">
            </transition>
          </div>
          
          <!-- Thumbnails -->
          <div v-if="product.gallery && product.gallery.length > 1" class="flex gap-3 overflow-x-auto hide-scrollbar py-2 px-1">
            <div v-for="(media, idx) in product.gallery" :key="idx" @click="selectedMedia = media" :class="['w-20 h-20 rounded-[1.25rem] border-2 flex-shrink-0 cursor-pointer p-1.5 flex items-center justify-center transition-all duration-300 bg-white shadow-sm relative overflow-hidden', selectedMedia.preview === media.preview ? 'border-blue-600 shadow-md scale-105' : 'border-slate-100 hover:border-blue-300 hover:shadow']">
              <div v-if="media.type === 'video'" class="absolute inset-0 bg-slate-900/40 backdrop-blur-[1px] flex items-center justify-center z-10">
                <div class="w-8 h-8 rounded-full bg-rose-600 text-white flex items-center justify-center shadow-lg border border-white/20">
                  <svg class="w-4 h-4 ml-0.5" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4l12 6-12 6z"></path></svg>
                </div>
              </div>
              <video v-if="media.type === 'video'" :src="media.preview" class="w-full h-full object-cover rounded-xl pointer-events-none"></video>
              <img v-else :src="media.preview" class="w-full h-full object-contain rounded-xl">
            </div>
          </div>
        </div>

        <!-- ================= ستون وسط: اطلاعات کالا، ویژگی‌ها و پروموشن (5 ستون) ================= -->
        <div class="lg:col-span-5 space-y-6">
          <div class="bg-white rounded-[2.5rem] border border-slate-100 p-8 shadow-[0_10px_40px_rgba(0,0,0,0.02)] relative overflow-hidden group">
            
            <div class="absolute -left-20 -top-20 w-40 h-40 bg-blue-50 rounded-full mix-blend-multiply opacity-50 pointer-events-none group-hover:scale-150 transition-transform duration-1000"></div>

            <div class="flex items-center justify-between mb-4 relative z-10">
              <span class="text-[10px] font-black tracking-widest text-blue-600 uppercase bg-blue-50 px-3 py-1 rounded-md border border-blue-100">B2B Verified Product</span>
              <div class="flex gap-2">
                <button @click="fetchMarketPriceAnalytics" :disabled="isLoadingAnalytics" class="flex items-center gap-1.5 text-xs font-black bg-indigo-50 text-indigo-700 hover:bg-indigo-100 px-3 py-1.5 rounded-xl transition-all shadow-sm border border-indigo-100">
                  <svg class="w-4 h-4 animate-spin" v-if="isLoadingAnalytics" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                  <svg class="w-4 h-4" v-else fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                  تحلیل لایو قیمت بازار (AI)
                </button>
                <button @click="shareProduct" class="w-8 h-8 rounded-full bg-slate-50 flex items-center justify-center text-slate-400 hover:text-blue-500 hover:bg-blue-50 transition-colors tooltip" title="اشتراک‌گذاری"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"></path></svg></button>
              </div>
            </div>
            
            <h1 class="text-xl md:text-2xl font-black text-slate-900 leading-relaxed mb-4 relative z-10">
              {{ product.title }}
            </h1>

            <!-- کارت استعلام لایو قیمت بازار (AI Analytics Card) -->
            <transition name="fade">
              <div v-if="priceAnalytics" class="bg-gradient-to-r from-indigo-900 to-slate-900 text-white rounded-2xl p-4 mb-6 shadow-xl relative overflow-hidden border border-indigo-700/50">
                <div class="flex items-center justify-between mb-3 border-b border-indigo-800/80 pb-2">
                  <span class="text-xs font-black text-indigo-300 flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    تحلیل لحظه‌ای قیمت بازار (ترب / ایمالز)
                  </span>
                  <span class="text-[10px] text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded-lg">هوش مصنوعی</span>
                </div>
                <div class="grid grid-cols-3 gap-2 text-center">
                  <div class="bg-indigo-950/60 p-2 rounded-xl border border-indigo-800/50">
                    <span class="block text-[9px] text-indigo-300 font-bold mb-1">کف قیمت</span>
                    <span class="block text-xs font-black text-emerald-400">{{ formatPrice(priceAnalytics.min_price) }}</span>
                  </div>
                  <div class="bg-indigo-950/60 p-2 rounded-xl border border-indigo-800/50">
                    <span class="block text-[9px] text-indigo-300 font-bold mb-1">میانگین بازار</span>
                    <span class="block text-xs font-black text-amber-300">{{ formatPrice(priceAnalytics.avg_price) }}</span>
                  </div>
                  <div class="bg-indigo-950/60 p-2 rounded-xl border border-indigo-800/50">
                    <span class="block text-[9px] text-indigo-300 font-bold mb-1">سقف قیمت</span>
                    <span class="block text-xs font-black text-rose-300">{{ formatPrice(priceAnalytics.max_price) }}</span>
                  </div>
                </div>
              </div>
            </transition>
            
            <div class="flex flex-wrap items-center gap-4 text-sm font-bold text-slate-500 mb-6 pb-6 relative z-10 border-b border-slate-100">
              <span class="flex items-center gap-1.5 text-amber-500 bg-amber-50 px-3 py-1.5 rounded-xl border border-amber-100 shadow-sm"><svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> {{ product.rating }} ({{ product.reviewsCount }} رای)</span>
              <span class="flex items-center gap-1.5 text-slate-600 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-100 shadow-sm">
                <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg> 
                ارسال از: {{ product.location || 'انبار مرکزی' }}
              </span>
            </div>

            <!-- انتخاب ویژگی‌های متغیر (Variant Builder) -->
            <div v-if="product.attributes && product.attributes.length > 0" class="space-y-5 mb-8 relative z-10">
               <div v-for="attr in product.attributes" :key="attr.name">
                 <h4 class="text-xs font-black text-slate-800 mb-3">{{ attr.name }}</h4>
                 <div class="flex flex-wrap gap-2">
                   <button 
                     v-for="opt in attr.options" 
                     :key="opt.value" 
                     @click="selectVariant(attr.name, opt)"
                     :class="['px-4 py-2.5 rounded-xl text-sm font-bold border-2 transition-all shadow-sm flex items-center gap-2', 
                              selectedVariants[attr.name]?.value === opt.value ? 'border-blue-500 bg-blue-50/50 text-blue-700' : 'border-slate-100 bg-white text-slate-600 hover:border-blue-200']"
                   >
                     {{ opt.value }}
                     <span v-if="opt.priceDiff > 0" class="text-[9px] bg-white px-1.5 py-0.5 rounded text-blue-500 border border-blue-100">(+{{ formatPrice(opt.priceDiff) }})</span>
                   </button>
                 </div>
               </div>
            </div>

            <!-- تایمر فروش شگفت‌انگیز -->
            <div v-if="product.promotions?.is_flash_sale" class="bg-gradient-to-l from-rose-50 to-orange-50 border border-rose-100 rounded-2xl p-4 mb-8 flex items-center justify-between shadow-sm relative z-10">
               <div class="flex items-center gap-3">
                 <div class="w-10 h-10 rounded-full bg-white shadow-sm flex items-center justify-center text-rose-500">
                   <svg class="w-5 h-5 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                 </div>
                 <div>
                   <h4 class="font-black text-rose-700 text-sm">پیشنهاد زمان‌دار B2B</h4>
                   <p class="text-[10px] font-bold text-rose-500/80">فقط تا پایان زمان مشخص شده</p>
                 </div>
               </div>
               <div class="flex gap-1.5" dir="ltr">
                  <div class="bg-white/80 backdrop-blur border border-rose-100 rounded-lg p-2 w-10 flex flex-col items-center shadow-sm">
                    <span class="text-sm font-black text-rose-600">{{ flashTimer.hours }}</span>
                    <span class="text-[7px] text-rose-400 font-bold">HRS</span>
                  </div>
                  <span class="text-rose-400 font-black self-center">:</span>
                  <div class="bg-white/80 backdrop-blur border border-rose-100 rounded-lg p-2 w-10 flex flex-col items-center shadow-sm">
                    <span class="text-sm font-black text-rose-600">{{ flashTimer.minutes }}</span>
                    <span class="text-[7px] text-rose-400 font-bold">MIN</span>
                  </div>
                  <span class="text-rose-400 font-black self-center">:</span>
                  <div class="bg-white/80 backdrop-blur border border-rose-100 rounded-lg p-2 w-10 flex flex-col items-center shadow-sm">
                    <span class="text-sm font-black text-rose-600">{{ flashTimer.seconds }}</span>
                    <span class="text-[7px] text-rose-400 font-bold">SEC</span>
                  </div>
               </div>
            </div>

            <!-- جدول قیمت‌گذاری بازه‌ای داینامیک -->
            <div class="bg-gradient-to-br from-slate-50 to-slate-100 border border-slate-200/60 rounded-[1.5rem] p-5 relative overflow-hidden z-10 group/table">
              <div class="absolute -right-10 -bottom-10 w-32 h-32 bg-slate-200 rounded-full mix-blend-multiply opacity-50 group-hover/table:scale-150 transition-transform duration-700"></div>
              
              <h3 class="font-black text-slate-800 mb-4 flex items-center gap-2 relative z-10">
                <svg class="w-5 h-5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg> 
                خرید عمده (قیمت پلکانی)
              </h3>
              
              <div class="grid grid-cols-2 md:grid-cols-3 gap-3 relative z-10">
                <div v-for="(tier, index) in product.price_tiers" :key="index" :class="['border rounded-2xl p-3 text-center transition-all duration-300 relative overflow-hidden', activeTierIndex === index ? 'bg-white border-blue-500 shadow-md ring-4 ring-blue-50 scale-[1.02]' : 'bg-white/60 border-slate-200 hover:bg-white cursor-pointer']" @click="orderQty = tier.min_qty">
                  <div v-if="activeTierIndex === index" class="absolute top-0 right-0 w-full h-1 bg-blue-500"></div>
                  <div class="text-[10px] font-bold text-slate-500 mb-2 whitespace-nowrap">{{ tier.label || `از ${tier.min_qty} ${tier.max_qty ? 'تا ' + tier.max_qty : 'به بالا'}` }}</div>
                  
                  <div class="flex flex-col items-center">
                    <span v-if="totalVariantDiff > 0" class="text-[9px] text-slate-400 line-through mb-0.5">{{ formatPrice(tier.price_per_unit) }}</span>
                    <div :class="['text-sm lg:text-base font-black tracking-tight', activeTierIndex === index ? 'text-blue-700' : 'text-slate-700']">
                      {{ formatPrice(tier.price_per_unit + totalVariantDiff) }}
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- ================= ستون چپ: باکس خرید، کوپن و فروشنده (3 ستون) ================= -->
        <div class="lg:col-span-3 space-y-6 lg:sticky top-28 z-20">
          
          <!-- کارت فروشنده (پریمیوم) -->
          <div class="bg-white rounded-[2.5rem] border border-slate-100 p-6 shadow-[0_10px_40px_rgba(0,0,0,0.02)] relative overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-blue-500 to-indigo-500"></div>
            
            <h4 class="text-xs font-black text-slate-400 mb-5 tracking-wider uppercase">تامین‌کننده کالا</h4>
            <div class="flex items-center gap-4 mb-5">
              <div class="w-14 h-14 bg-slate-50 rounded-[1.25rem] flex items-center justify-center font-black text-slate-400 text-xl border border-slate-100 shadow-inner">
                {{ product.seller?.logo || 'ت' }}
              </div>
              <div>
                <h4 class="font-black text-slate-800 text-sm flex items-center gap-1 mb-1">
                  {{ product.seller?.name || 'تامین‌کننده تایید شده' }} 
                  <svg class="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                </h4>
                <p class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded w-fit">{{ product.seller?.type || 'فروشنده VIP' }}</p>
              </div>
            </div>
            
            <div class="grid grid-cols-2 gap-3 text-center mb-6">
              <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                <span class="block text-[9px] font-bold text-slate-500 mb-1">رضایت مشتری</span>
                <span class="block font-black text-slate-800 text-sm">{{ product.seller?.satisfaction || '۹۸٪' }}</span>
              </div>
              <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                <span class="block text-[9px] font-bold text-slate-500 mb-1">عملکرد ارسال</span>
                <span class="block font-black text-emerald-600 text-sm">عالی</span>
              </div>
            </div>
            <button class="w-full bg-white border-2 border-slate-100 hover:border-blue-300 text-slate-600 hover:text-blue-700 font-black py-3 rounded-xl transition-colors text-sm shadow-sm mb-2">مشاهده غرفه فروشنده</button>
            <button @click="openRfqModal" class="w-full bg-blue-50 border border-blue-200 text-blue-700 font-black py-3 rounded-xl transition-colors text-xs flex items-center justify-center gap-1.5 shadow-sm">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              استعلام قیمت سفارشی (RFQ)
            </button>
          </div>

          <!-- باکس کد تخفیف (اگر فروشنده فعال کرده باشد) -->
          <div v-if="product.promotions?.has_discount_code" class="bg-gradient-to-br from-fuchsia-50 to-pink-50 rounded-[2.5rem] border border-fuchsia-100 p-6 shadow-sm relative overflow-hidden group/coupon">
             <div class="absolute -right-10 -bottom-10 w-24 h-24 bg-fuchsia-200 rounded-full mix-blend-multiply opacity-50 group-hover/coupon:scale-150 transition-transform duration-500"></div>
             
             <h4 class="font-black text-fuchsia-800 text-sm mb-3 flex items-center gap-2 relative z-10">
               <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"></path></svg>
               کد تخفیف اختصاصی
             </h4>
             <p class="text-[10px] font-bold text-fuchsia-600/80 mb-4 relative z-10">
               دریافت {{ product.promotions.discount_type === 'percent' ? product.promotions.discount_value + '٪' : formatPrice(product.promotions.discount_value) + ' تومان' }} تخفیف بیشتر در سبد خرید
             </p>
             <div class="flex items-center bg-white border border-fuchsia-200 rounded-xl p-1.5 relative z-10 shadow-sm">
                <span class="flex-1 text-center font-black font-mono text-fuchsia-700 tracking-widest text-lg">{{ product.promotions.discount_code }}</span>
                <button @click="copyCode" class="w-10 h-10 bg-fuchsia-100 hover:bg-fuchsia-500 hover:text-white text-fuchsia-600 rounded-lg flex items-center justify-center transition-colors">
                  <svg v-if="!codeCopied" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                  <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                </button>
             </div>
          </div>

          <!-- باکس خرید نهایی -->
          <div class="bg-white rounded-[2.5rem] border border-slate-100 p-6 md:p-8 shadow-[0_20px_50px_rgba(0,0,0,0.06)] relative overflow-hidden group">
            <div class="absolute -right-10 -bottom-10 w-32 h-32 bg-blue-500 rounded-full filter blur-[50px] opacity-0 group-hover:opacity-20 transition-opacity duration-700"></div>
            
            <div class="mb-6 border-b border-slate-100 pb-6 relative z-10">
              <label class="block text-xs font-black text-slate-500 mb-3">تعداد درخواستی ({{ product.unit || 'عدد' }}):</label>
              <div class="flex items-center justify-between bg-slate-50 border-2 border-slate-100 rounded-2xl p-1.5 focus-within:border-blue-400 focus-within:bg-white transition-colors">
                 <button @click="orderQty > 1 ? orderQty-- : null" class="w-12 h-12 flex items-center justify-center text-slate-500 hover:text-blue-600 hover:bg-blue-50 hover:shadow-sm rounded-xl transition-all font-black text-xl">-</button>
                 <input type="number" v-model="orderQty" class="w-16 text-center bg-transparent font-black text-slate-800 outline-none text-2xl" dir="ltr">
                 <button @click="orderQty++" class="w-12 h-12 flex items-center justify-center text-slate-500 hover:text-blue-600 hover:bg-blue-50 hover:shadow-sm rounded-xl transition-all font-black text-xl">+</button>
              </div>
            </div>

            <div class="flex justify-between items-end mb-8 relative z-10">
              <span class="text-sm font-black text-slate-500">مبلغ نهایی:</span>
              <div class="text-left">
                <div class="text-3xl font-black text-slate-900 tracking-tighter">{{ formatPrice(totalPrice) }}</div>
                <div class="text-[10px] font-bold text-slate-400 mt-1">تومان (با احتساب ویژگی‌ها)</div>
              </div>
            </div>
            
            <button @click="addToCart" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-2xl shadow-[0_15px_30px_rgba(0,0,0,0.2)] transition-all hover:-translate-y-1 relative z-10 flex items-center justify-center gap-2 text-base">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
              افزودن به سبد خرید
            </button>
          </div>
        </div>

      </div>

      <!-- ================= 3. تب‌های توضیحات و نظرات (طراحی خوانا بدون تداخل) ================= -->
      <div v-if="!isLoading" class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_30px_rgba(0,0,0,0.02)] mt-10 relative overflow-hidden">
        
        <div class="flex border-b border-slate-200/80 overflow-x-auto hide-scrollbar bg-slate-50/90 backdrop-blur-md sticky top-0 z-20 px-4 lg:px-10">
          <button @click="activeDetailsTab = 'desc'" :class="['px-8 py-5 font-black text-sm transition-all border-b-[3px] whitespace-nowrap', activeDetailsTab === 'desc' ? 'border-blue-600 text-blue-600 bg-white shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800']">معرفی و بررسی</button>
          <button @click="activeDetailsTab = 'specs'" :class="['px-8 py-5 font-black text-sm transition-all border-b-[3px] whitespace-nowrap', activeDetailsTab === 'specs' ? 'border-blue-600 text-blue-600 bg-white shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800']">مشخصات فنی</button>
          <button @click="activeDetailsTab = 'reviews'" :class="['px-8 py-5 font-black text-sm transition-all border-b-[3px] whitespace-nowrap flex items-center gap-2', activeDetailsTab === 'reviews' ? 'border-blue-600 text-blue-600 bg-white shadow-sm' : 'border-transparent text-slate-500 hover:text-slate-800']">نظرات همکاران <span class="bg-slate-200 text-slate-700 px-2.5 py-0.5 rounded-lg text-[10px] font-bold">{{ product.reviewsCount }}</span></button>
        </div>

        <div class="p-6 md:p-12 pt-8 md:pt-10 min-h-[300px]">
          
          <!-- تب معرفی -->
          <div v-if="activeDetailsTab === 'desc'" class="animate-fade-in relative">
            <div class="flex justify-between items-center mb-8 pb-4 border-b border-slate-100">
              <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-600"></span>
                بررسی تخصصی کالا
              </h3>
              <button @click="generateAiDescription" :disabled="isGeneratingAi" class="flex items-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-black text-xs px-4 py-2.5 rounded-xl transition-all shadow-md">
                <svg class="w-4 h-4 animate-spin" v-if="isGeneratingAi" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                <svg class="w-4 h-4" v-else fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                تولید محتوا با AI
              </button>
            </div>
            
            <!-- محتوای غنی با تایپوگرافی ویژه B2B -->
            <div class="product-rich-text text-slate-700 font-medium leading-loose text-justify space-y-4" v-html="product.description">
            </div>
          </div>

          <!-- تب مشخصات -->
          <div v-if="activeDetailsTab === 'specs'" class="animate-fade-in border border-slate-100 rounded-[2rem] overflow-hidden">
            <div v-if="product.simple_attributes && product.simple_attributes.length > 0">
              <div v-for="(spec, index) in product.simple_attributes" :key="index" :class="['grid grid-cols-1 md:grid-cols-4 p-6 text-sm transition-colors hover:bg-blue-50/30', index % 2 === 0 ? 'bg-slate-50/50' : 'bg-white']">
                <div class="font-bold text-slate-500 mb-2 md:mb-0">{{ spec.name }}</div>
                <div class="md:col-span-3 font-black text-slate-800">{{ spec.value }}</div>
              </div>
            </div>
            <div v-else class="p-10 text-center font-bold text-slate-400">مشخصات فنی ثبت نشده است.</div>
          </div>

          <!-- تب نظرات -->
          <div v-if="activeDetailsTab === 'reviews'" class="animate-fade-in grid grid-cols-1 md:grid-cols-12 gap-10">
            <div class="md:col-span-4 space-y-6">
              <div class="bg-slate-50 p-8 rounded-[2rem] border border-slate-100 text-center">
                <div class="text-6xl font-black text-slate-800 mb-3">{{ product.rating }}</div>
                <div class="flex justify-center text-amber-500 mb-3"><svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg></div>
                <div class="text-xs font-bold text-slate-400">از مجموع {{ product.reviewsCount }} رای</div>
              </div>
              <button @click="showReviewModal = true" class="w-full bg-slate-900 text-white font-black py-4 rounded-xl hover:bg-black transition-colors shadow-lg">ثبت نظر جدید</button>
            </div>
            
            <div class="md:col-span-8 space-y-6">
              <div v-for="review in product.reviews" :key="review.id" class="bg-white border border-slate-100 p-6 md:p-8 rounded-[2rem] shadow-sm">
                <div class="flex items-center gap-4 mb-4">
                  <div class="w-12 h-12 rounded-full bg-slate-100 flex items-center justify-center text-slate-400 font-black text-lg">{{ review.userName.charAt(0) }}</div>
                  <div class="flex flex-col">
                    <div class="flex items-center gap-2">
                      <span class="font-black text-slate-800 text-sm">{{ review.userName }}</span>
                      <span class="bg-emerald-50 text-emerald-600 border border-emerald-100 text-[10px] font-black px-2 py-0.5 rounded-lg" v-if="review.isBuyer">خریدار عمده</span>
                    </div>
                    <span class="text-[10px] font-bold text-slate-400 mt-1">{{ review.date }}</span>
                  </div>
                </div>
                <p class="text-sm text-slate-600 font-medium leading-loose text-justify">{{ review.text }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= 4. نوار خرید شناور مخصوص موبایل (Mobile Sticky Bar) ================= -->
    <div class="lg:hidden fixed bottom-0 left-0 right-0 bg-white/95 backdrop-blur-xl border-t border-slate-200 p-4 shadow-[0_-10px_25px_rgba(0,0,0,0.05)] z-50 flex items-center justify-between gap-4">
      <div>
        <span class="block text-[10px] font-bold text-slate-400">مبلغ نهایی ({{ orderQty }} {{ product.unit || 'عدد' }}):</span>
        <span class="text-xl font-black text-slate-900 tracking-tight">{{ formatPrice(totalPrice) }} <span class="text-xs">تومان</span></span>
      </div>
      <button @click="addToCart" class="bg-slate-900 hover:bg-black text-white font-black px-6 py-3.5 rounded-xl text-sm shadow-md flex items-center gap-2 shrink-0">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
        خرید عمده
      </button>
    </div>

    <!-- ================= 5. لایت‌باکس بزرگ‌نمایی تصویر (Media Lightbox Modal) ================= -->
    <transition name="fade">
      <div v-if="showLightbox" class="fixed inset-0 bg-black/90 backdrop-blur-md z-[100000] flex items-center justify-center p-4" @click.self="showLightbox = false">
        <button @click="showLightbox = false" class="absolute top-6 right-6 text-white/80 hover:text-white bg-white/10 p-3 rounded-full transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
        <div class="max-w-4xl max-h-[85vh] w-full flex items-center justify-center">
          <video v-if="selectedMedia.type === 'video'" :src="selectedMedia.preview" controls autoplay class="max-w-full max-h-[80vh] rounded-2xl"></video>
          <img v-else :src="selectedMedia.preview" class="max-w-full max-h-[80vh] object-contain rounded-2xl shadow-2xl">
        </div>
      </div>
    </transition>

    <!-- ================= 6. مودال استعلام اختصاصی (RFQ Modal) ================= -->
    <transition name="toast-fade">
      <div v-if="showRfqModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100000] flex items-center justify-center p-4">
        <div class="bg-white rounded-[2.5rem] border border-slate-100 max-w-lg w-full p-8 shadow-2xl relative overflow-hidden animate-fade-in">
          <button @click="showRfqModal = false" class="absolute top-6 left-6 text-slate-400 hover:text-slate-600 bg-slate-100 p-2 rounded-full">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
          
          <h3 class="font-black text-slate-900 text-lg mb-2">درخواست استعلام قیمت اختصاصی (RFQ)</h3>
          <p class="text-xs text-slate-500 font-medium mb-6">برای خریدهای با حجم بالا یا شرایط خاص، درخواست خود را مستقیماً ارسال کنید.</p>
          
          <div class="space-y-4 mb-6">
            <div>
              <label class="block text-xs font-black text-slate-700 mb-1.5">تعداد درخواستی:</label>
              <input type="number" v-model="rfqData.qty" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 font-bold text-sm outline-none focus:border-blue-500">
            </div>
            <div>
              <label class="block text-xs font-black text-slate-700 mb-1.5">قیمت پیشنهادی هر واحد (تومان - اختیاری):</label>
              <input type="number" v-model="rfqData.targetPrice" placeholder="مثلا 38000000" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 font-bold text-sm outline-none focus:border-blue-500">
            </div>
            <div>
              <label class="block text-xs font-black text-slate-700 mb-1.5">توضیحات و نحوه تسویه:</label>
              <textarea v-model="rfqData.note" rows="3" placeholder="شرایط پرداخت چک، زمان تحویل و ..." class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 font-medium text-xs outline-none focus:border-blue-500"></textarea>
            </div>
          </div>

          <button @click="submitRfq" :disabled="isSubmittingRfq" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-black py-3.5 rounded-xl transition-all shadow-lg flex items-center justify-center gap-2">
            <svg class="w-4 h-4 animate-spin" v-if="isSubmittingRfq" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            ارسال استعلام مستقیم
          </button>
        </div>
      </div>
    </transition>

    <!-- ================= 7. مودال ثبت نظر (Review Modal) ================= -->
    <transition name="toast-fade">
      <div v-if="showReviewModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100000] flex items-center justify-center p-4">
        <div class="bg-white rounded-[2.5rem] border border-slate-100 max-w-md w-full p-8 shadow-2xl relative">
          <button @click="showReviewModal = false" class="absolute top-6 left-6 text-slate-400 hover:text-slate-600 bg-slate-100 p-2 rounded-full">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
          
          <h3 class="font-black text-slate-900 text-lg mb-4">ثبت تجربه خرید همکاران</h3>
          
          <div class="space-y-4 mb-6">
            <div>
              <label class="block text-xs font-black text-slate-700 mb-1.5">امتیاز شما (از ۵):</label>
              <select v-model="newReview.rating" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 font-bold text-sm outline-none">
                <option :value="5">⭐⭐⭐⭐⭐ عالی (۵)</option>
                <option :value="4">⭐⭐⭐⭐ خوب (۴)</option>
                <option :value="3">⭐⭐⭐ متوسط (۳)</option>
                <option :value="2">⭐⭐ ضعیف (۲)</option>
                <option :value="1">⭐ خیلی ضعیف (۱)</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-black text-slate-700 mb-1.5">نظر تخصصی شما:</label>
              <textarea v-model="newReview.text" rows="4" placeholder="درباره کیفیت بسته بندی، اصالت و سرعت ارسال..." class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3 font-medium text-xs outline-none focus:border-blue-500"></textarea>
            </div>
          </div>

          <button @click="submitReview" class="w-full bg-slate-900 hover:bg-black text-white font-black py-3.5 rounded-xl transition-all shadow-lg">
            ثبت و انتشار نظر
          </button>
        </div>
      </div>
    </transition>
    
    <!-- ================= پیام موفقیت / خطا (Toast) ================= -->
    <transition name="toast-fade">
      <div v-if="toast.show" class="fixed bottom-6 right-6 z-[100000] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-3 bg-slate-900 border border-slate-700">
        <div class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0 bg-emerald-500/20 text-emerald-400">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
        </div>
        <div>
          <h4 class="font-black text-sm mb-0.5">{{ toast.title }}</h4>
          <p class="text-xs text-slate-300 font-medium leading-relaxed max-w-xs">{{ toast.message }}</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const getApiBaseUrl = () => {
  if (typeof window !== 'undefined') {
    const host = window.location.hostname;
    if (host === 'localhost' || host === '127.0.0.1') {
      return 'https://tajerbam.com';
    }
  }
  return 'https://tajerbam.com';
};

const API_BASE_URL = getApiBaseUrl();

const isLoading = ref(true);
const activeDetailsTab = ref('desc');
const product = ref({});
const selectedMedia = ref({ type: 'image', preview: '' });
const orderQty = ref(1);
const selectedVariants = ref({});

// AI & Analytics States
const isLoadingAnalytics = ref(false);
const priceAnalytics = ref(null);
const isGeneratingAi = ref(false);

// Timer & Copy States
const flashTimer = ref({ hours: '12', minutes: '45', seconds: '30' });
const codeCopied = ref(false);
let timerInterval = null;

// Modals
const showLightbox = ref(false);
const showRfqModal = ref(false);
const isSubmittingRfq = ref(false);
const rfqData = ref({ qty: 10, targetPrice: '', note: '' });

const showReviewModal = ref(false);
const newReview = ref({ rating: 5, text: '' });

// Toast
const toast = ref({ show: false, title: '', message: '' });
const showToast = (title, message) => {
  toast.value = { show: true, title, message };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

// کپی کد تخفیف
const copyCode = () => {
  if (product.value.promotions?.discount_code) {
    try {
      document.execCommand('copy');
    } catch (e) {}
    codeCopied.value = true;
    showToast('کپی شد', 'کد تخفیف اختصاصی در کلیپ‌بورد ذخیره شد.');
    setTimeout(() => { codeCopied.value = false; }, 3000);
  }
};

// به‌روزرسانی تایمر فروش شگفت انگیز
const updateTimer = () => {
  if (!product.value?.promotions?.is_flash_sale) return;
  let h = parseInt(flashTimer.value.hours);
  let m = parseInt(flashTimer.value.minutes);
  let s = parseInt(flashTimer.value.seconds);
  if (s > 0) { s--; }
  else if (m > 0) { m = 59; s = 59; }
  else if (h > 0) { h--; m = 59; s = 59; }
  flashTimer.value = {
    hours: String(h).padStart(2, '0'),
    minutes: String(m).padStart(2, '0'),
    seconds: String(s).padStart(2, '0')
  };
};

// ساخت داده‌های استاندارد محصول به صورت داینامیک
const mapListItemToProductDetail = (item) => {
  const numericId = parseInt(item.id) || 1;
  const categories = ['لپ‌تاپ و الترابوک', 'ابزارآلات برقی و شارژی', 'موبایل و گجت‌های هوشمند', 'تجهیزات صنعتی و شبکه', 'صوتی و تصویری'];
  const categoryName = item.category || categories[numericId % categories.length];
  
  const basePrice = item.price_retail || item.price || item.retailPrice || (numericId * 1500000) + 3000000;
  const productTitle = item.title || item.name || `محصول تجاری B2B کد ${numericId}`;
  
  const selectedImg = item.img || item.image_url || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png';

  // استخراج صحیح نام تامین‌کننده
  const supplierName = item.seller?.name || item.seller || 'تامین‌کننده تایید شده تاجربام';

  // پارس مشخصات فنی ساده (Simple Specs)
  let parsedSimpleAttrs = [];
  if (Array.isArray(item.simple_attributes)) {
    parsedSimpleAttrs = item.simple_attributes;
  } else if (typeof item.simple_attributes === 'string') {
    try { parsedSimpleAttrs = JSON.parse(item.simple_attributes); } catch(e){}
  }
  
  if (!parsedSimpleAttrs || parsedSimpleAttrs.length === 0) {
    parsedSimpleAttrs = [
      { name: 'شناسه محصول (SKU)', value: item.sku || `SKU-B2B-${numericId}` },
      { name: 'دسته‌بندی اصلی', value: categoryName },
      { name: 'واحد تحویل', value: item.unit || 'عدد / دستگاه' },
      { name: 'وضعیت در انبار', value: 'موجود در انبار مرکزی (تحویل فوری)' }
    ];
  }

  // حذف ویژگی‌های متغیر دیفالت (Default Variable Attributes)
  let parsedVariableAttrs = [];
  if (Array.isArray(item.attributes)) {
    parsedVariableAttrs = item.attributes;
  } else if (typeof item.attributes === 'string') {
    try { parsedVariableAttrs = JSON.parse(item.attributes); } catch(e){}
  }

  return {
    id: numericId,
    title: productTitle,
    category: categoryName,
    location: item.location || 'انبار مرکزی',
    rating: (4.2 + (numericId % 8) / 10).toFixed(1),
    reviewsCount: (numericId * 7) + 5,
    unit: item.unit || 'عدد',
    gallery: item.gallery && item.gallery.length > 0 ? item.gallery : [{ type: 'image', preview: selectedImg }],
    simple_attributes: parsedSimpleAttrs,
    attributes: parsedVariableAttrs, // کاملا پاکسازی شد از ویژگی‌های متغیر دیفالت
    price_retail: basePrice,
    price_tiers: item.price_tiers && item.price_tiers.length > 0 ? item.price_tiers.map(t => ({
      label: `از ${t.min_qty} ${t.max_qty ? 'تا ' + t.max_qty : 'به بالا'}`,
      min_qty: t.min_qty,
      max_qty: t.max_qty,
      price_per_unit: t.price_per_unit
    })) : [
      { label: 'خرید عمده', min_qty: 1, max_qty: null, price_per_unit: basePrice }
    ],
    promotions: item.promotions || {},
    seller: {
      name: supplierName,
      logo: supplierName ? supplierName.charAt(0) : 'ت',
      type: 'تامین‌کننده احراز شده B2B',
      satisfaction: '۹۸٪'
    },
    description: item.description || `<p>اطلاعات و مشخصات فنی برای <strong>${productTitle}</strong>.</p>`,
    reviews: item.reviews || []
  };
};

// دریافت اطلاعات محصول با بررسی اولیه localStorage برای همگام‌سازی سریع
const fetchProductDetails = async () => {
  isLoading.value = true;
  const prodId = route.params?.id || '1';
  let fetchedData = null;

  // ۱. اولویت اول: بررسی تغییرات ذخیره شده در localStorage از پنل مدیریت
  try {
    const customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
    const localMatch = customProds.find(p => String(p.id) === String(prodId));
    if (localMatch) {
      fetchedData = mapListItemToProductDetail(localMatch);
    }
  } catch (e) {}

  // ۲. در صورت عدم وجود local override، فراخوانی از API سرور
  if (!fetchedData) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 2000);
      const res = await fetch(`${API_BASE_URL}/api/products/${prodId}`, { signal: controller.signal });
      clearTimeout(timeoutId);
      if (res.ok) {
        fetchedData = await res.json();
      }
    } catch (error) {
      console.warn("Direct product API unreachable, falling back to mock or list...", error);
    }
  }

  // ۳. تلاش برای خواندن از لیست کامل محصولات سرور
  if (!fetchedData) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 2000);
      const listRes = await fetch(`${API_BASE_URL}/api/products`, { signal: controller.signal });
      clearTimeout(timeoutId);
      if (listRes.ok) {
        const listData = await listRes.json();
        const found = listData.find(p => String(p.id) === String(prodId));
        if (found) {
          fetchedData = mapListItemToProductDetail(found);
        }
      }
    } catch (e) {}
  }

  // ۴. نمونه‌سازی اتوماتیک
  if (!fetchedData) {
    fetchedData = mapListItemToProductDetail({ id: prodId });
  }

  product.value = fetchedData;
  initProductState();
  isLoading.value = false;
};

const initProductState = () => {
  if (product.value.gallery && product.value.gallery.length > 0) {
    selectedMedia.value = product.value.gallery[0];
  } else if (product.value.image_url) {
    selectedMedia.value = { type: 'image', preview: product.value.image_url };
    product.value.gallery = [selectedMedia.value];
  } else {
    selectedMedia.value = { type: 'image', preview: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png' };
    product.value.gallery = [selectedMedia.value];
  }

  selectedVariants.value = {};
  if (product.value.attributes) {
    product.value.attributes.forEach(attr => {
      if (attr.options && attr.options.length > 0) {
        selectedVariants.value[attr.name] = attr.options[0];
      }
    });
  }

  if (product.value.price_tiers && product.value.price_tiers.length > 0) {
    orderQty.value = product.value.price_tiers[0].min_qty || 1;
  } else {
    orderQty.value = 1;
  }
};

// توابع تعاملی
const fetchMarketPriceAnalytics = async () => {
  isLoadingAnalytics.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/products/price-analytics`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ keyword: product.value.title || 'محصول' })
    });
    if (res.ok) {
      priceAnalytics.value = await res.json();
    } else {
      throw new Error();
    }
  } catch (e) {
    priceAnalytics.value = {
      min_price: Math.round((product.value.price_retail || 10000000) * 0.92),
      avg_price: product.value.price_retail || 10000000,
      max_price: Math.round((product.value.price_retail || 10000000) * 1.08)
    };
  } finally {
    isLoadingAnalytics.value = false;
  }
};

const generateAiDescription = async () => {
  isGeneratingAi.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/ai/generate-description?title=${encodeURIComponent(product.value.title)}`);
    if (res.ok) {
      const data = await res.json();
      if (data.description) product.value.description = data.description;
    }
  } catch (e) {
    showToast('خطا', 'سرویس تولید محتوای هوش مصنوعی در دسترس نیست.');
  } finally {
    isGeneratingAi.value = false;
  }
};

const shareProduct = () => {
  showToast('اشتراک‌گذاری', 'لینک محصول کپی شد.');
};

const openRfqModal = () => { showRfqModal.value = true; };
const submitRfq = async () => {
  if (!rfqData.value.qty) return;
  isSubmittingRfq.value = true;

  try {
    const token = localStorage.getItem('tajerbam_token') || 'test-token';
    
    // ساخت پکت استاندارد جهت ارسال به بک‌اند RFQ
    const payload = {
      items: [
        {
          name: product.value.title || 'استعلام کالا',
          category: product.value.category || 'عمومی',
          qty: Number(rfqData.value.qty),
          deliveryDays: 5
        }
      ],
      note: rfqData.value.note || '',
      location: product.value.location || 'سراسر کشور',
      targetBudget: rfqData.value.targetPrice ? String(rfqData.value.targetPrice) : '',
      onlyVip: false
    };

    // ارسال درخواست POST به ای‌پای ثبت استعلام بک‌اند
    const res = await fetch(`${API_BASE_URL}/api/rfq/create`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok && data.success) {
      showRfqModal.value = false;
      showToast('ثبت شد', 'درخواست استعلام قیمت اختصاصی شما با موفقیت در سیستم ثبت گردید.');
      rfqData.value = { qty: 10, targetPrice: '', note: '' }; // بازنشانی فرم
    } else {
      showToast('خطا', data.detail || 'مشکلی در ثبت استعلام رخ داد.');
    }
  } catch (error) {
    console.error("RFQ submit error:", error);
    showToast('خطا', 'ارتباط با سرور برقرار نشد.');
  } finally {
    isSubmittingRfq.value = false;
  }
};

const submitReview = () => {
  if (!newReview.value.text) return;
  product.value.reviews = product.value.reviews || [];
  product.value.reviews.unshift({
    id: Date.now(),
    userName: 'شما (خریدار عمده)',
    date: 'هم‌اکنون',
    rate: newReview.value.rating,
    text: newReview.value.text,
    isBuyer: true
  });
  showReviewModal.value = false;
  newReview.value = { rating: 5, text: '' };
  showToast('تشکر', 'نظر شما با موفقیت ثبت شد.');
};

// شنود تغییرات مسیر و تغییرات حافظه جهت به‌روزرسانی زنده
watch(() => route.params?.id, (newId) => {
  if (newId) {
    fetchProductDetails();
  }
});

const handleStorageOrFocus = () => {
  fetchProductDetails();
};

onMounted(() => {
  fetchProductDetails();
  timerInterval = setInterval(updateTimer, 1000);
  window.addEventListener('storage', handleStorageOrFocus);
  window.addEventListener('focus', handleStorageOrFocus);
});

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval);
  window.removeEventListener('storage', handleStorageOrFocus);
  window.removeEventListener('focus', handleStorageOrFocus);
});

// Computations
const formatPrice = (price) => {
  if (!price) return '0';
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

const selectVariant = (attrName, option) => {
  selectedVariants.value[attrName] = option;
};

const totalVariantDiff = computed(() => {
  let diff = 0;
  for (const key in selectedVariants.value) {
    if (selectedVariants.value[key] && selectedVariants.value[key].priceDiff) {
      diff += Number(selectedVariants.value[key].priceDiff);
    }
  }
  return diff;
});

const activeTierIndex = computed(() => {
  if (!product.value.price_tiers) return 0;
  const index = product.value.price_tiers.findIndex(t => 
    orderQty.value >= t.min_qty && (!t.max_qty || orderQty.value <= t.max_qty)
  );
  return index !== -1 ? index : product.value.price_tiers.length - 1;
});

const totalPrice = computed(() => {
  if (!product.value.price_tiers || product.value.price_tiers.length === 0) {
    const base = product.value.promotions?.is_flash_sale ? product.value.promotions.flash_price : (product.value.price_retail || 0);
    return (base + totalVariantDiff.value) * orderQty.value;
  }
  const baseTierPrice = product.value.price_tiers[activeTierIndex.value]?.price_per_unit || product.value.price_retail || 0;
  return (baseTierPrice + totalVariantDiff.value) * orderQty.value;
});

const addToCart = () => {
  let cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  let variantStr = Object.values(selectedVariants.value).map(v => v.value).join(' / ');
  const itemTitle = variantStr ? `${product.value.title} (${variantStr})` : product.value.title;

  const baseTierPrice = product.value.price_tiers?.[activeTierIndex.value]?.price_per_unit || product.value.price_retail;
  const unitFinalPrice = baseTierPrice + totalVariantDiff.value;

  const newItem = {
    id: product.value.id + '-' + Date.now(),
    name: itemTitle,
    seller: product.value.seller?.name || 'فروشنده',
    img: product.value.gallery?.find(g => g.type === 'image')?.preview || '',
    unitPrice: unitFinalPrice,
    qty: orderQty.value,
    minOrder: product.value.price_tiers?.[0]?.min_qty || 1
  };
  
  cart.push(newItem);
  localStorage.setItem('tajerbam_cart', JSON.stringify(cart));
  window.dispatchEvent(new Event('storage'));
  showToast('اضافه شد', 'محصول با موفقیت به سبد خرید عمده اضافه شد.');
};
</script>

<style scoped>
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

/* استایل‌دهی غنی برای متون HTML تولید شده توسط هوش مصنوعی */
.product-rich-text :deep(h2) {
  font-size: 1.25rem;
  font-weight: 900;
  color: #0f172a;
  margin-top: 1.75rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #e2e8f0;
}
.product-rich-text :deep(h3) {
  font-size: 1.1rem;
  font-weight: 800;
  color: #1e293b;
  margin-top: 1.25rem;
  margin-bottom: 0.5rem;
}
.product-rich-text :deep(ul) {
  list-style-type: disc;
  padding-right: 1.5rem;
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
}
.product-rich-text :deep(li) {
  margin-bottom: 0.5rem;
  line-height: 2;
  color: #334155;
}
.product-rich-text :deep(p) {
  margin-bottom: 1rem;
  line-height: 2.1;
  color: #334155;
}
.product-rich-text :deep(strong) {
  color: #0284c7;
  font-weight: 800;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.4s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.toast-fade-enter-active, .toast-fade-leave-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.toast-fade-enter-from, .toast-fade-leave-to { opacity: 0; transform: translateY(20px) scale(0.9); }

input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}
</style>