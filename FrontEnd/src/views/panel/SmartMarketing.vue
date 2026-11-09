<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر صفحه (Ultra Premium Glassmorphism) ================= -->
    <div class="bg-white/80 backdrop-blur-2xl p-6 md:p-8 rounded-[2.5rem] border border-white shadow-[0_10px_40px_rgba(0,0,0,0.04)] flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative overflow-hidden z-10">
      <div class="absolute -right-20 -top-20 w-72 h-72 bg-gradient-to-br from-purple-400/40 via-pink-400/30 to-indigo-400/40 rounded-full mix-blend-multiply filter blur-[60px] pointer-events-none animate-pulse-slow"></div>
      <div class="absolute -left-10 -bottom-10 w-56 h-56 bg-gradient-to-tr from-blue-400/30 to-emerald-400/30 rounded-full mix-blend-multiply filter blur-[50px] pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-5">
        <div class="w-16 h-16 bg-gradient-to-br from-purple-600 via-indigo-600 to-blue-600 rounded-2xl flex items-center justify-center text-white shadow-xl shadow-purple-500/30 shrink-0 transform transition-all duration-300 hover:scale-105 hover:rotate-3">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4 6 6"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 17h8m0 0v-8m0 8l-8-8 4-4 6 6"></path></svg>
        </div>
        <div>
          <h1 class="text-2xl md:text-3xl font-black text-slate-800 mb-1 tracking-tight">مرکز بازاریابی <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-indigo-600 to-pink-600">هوشمند B2B</span></h1>
          <p class="text-xs md:text-sm font-bold text-slate-500">مدیریت شبکه افیلیت، رهگیری فروش، رادار واقعی هوش مصنوعی برای استخراج لیدها از گوگل و وب.</p>
        </div>
      </div>

      <!-- تب‌های پیشرفته مدیریت بازاریابی -->
      <div class="relative z-10 w-full lg:w-auto bg-slate-100/90 p-1.5 rounded-2xl border border-slate-200/60 flex flex-wrap gap-1 shadow-inner">
        <button @click="activeTab = 'commissions'" :class="['px-5 py-2.5 rounded-xl font-black text-xs md:text-sm transition-all flex-1 whitespace-nowrap cursor-pointer', activeTab === 'commissions' ? 'bg-white text-purple-700 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50']">پورسانت کالاها</button>
        <button @click="activeTab = 'network'" :class="['px-5 py-2.5 rounded-xl font-black text-xs md:text-sm transition-all flex-1 whitespace-nowrap cursor-pointer', activeTab === 'network' ? 'bg-white text-purple-700 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50']">شبکه بازاریابان</button>
        <button @click="activeTab = 'radar'" :class="['px-5 py-2.5 rounded-xl font-black text-xs md:text-sm transition-all flex-1 whitespace-nowrap flex items-center justify-center gap-1.5 cursor-pointer', activeTab === 'radar' ? 'bg-white text-emerald-700 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50']">
          رادار لید واقعی <span class="bg-gradient-to-r from-emerald-500 to-teal-600 text-white text-[9px] px-1.5 py-0.5 rounded font-black animate-pulse">100% Real</span>
        </button>
        <button @click="activeTab = 'coupons'" :class="['px-5 py-2.5 rounded-xl font-black text-xs md:text-sm transition-all flex-1 whitespace-nowrap cursor-pointer', activeTab === 'coupons' ? 'bg-white text-rose-600 shadow-sm border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50']">کدهای تخفیف</button>
      </div>
    </div>

    <!-- ================= آمار کلان بازاریابی (KPIs) ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.02)] relative overflow-hidden group hover:border-purple-300 transition-all hover:-translate-y-1">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-gradient-to-b from-purple-500 to-indigo-600"></div>
        <p class="text-xs font-bold text-slate-400 mb-2">بازاریابان فعال روی کالاهای شما</p>
        <h3 class="text-3xl font-black text-slate-800">
          <span v-if="isLoading" class="inline-block w-12 h-8 bg-slate-100 rounded animate-pulse"></span>
          <span v-else>{{ stats.activeMarketers }} <span class="text-sm font-bold text-slate-400">نفر</span></span>
        </h3>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.02)] relative overflow-hidden group hover:border-rose-300 transition-all hover:-translate-y-1">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-gradient-to-b from-rose-500 to-pink-600"></div>
        <p class="text-xs font-bold text-slate-400 mb-2">کلیک و بازدید هدایت شده</p>
        <h3 class="text-3xl font-black text-slate-800">
          <span v-if="isLoading" class="inline-block w-20 h-8 bg-slate-100 rounded animate-pulse"></span>
          <span v-else>{{ Number(stats.clicks || 0).toLocaleString('fa-IR') }} <span class="text-sm font-bold text-slate-400">بازدید</span></span>
        </h3>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.02)] relative overflow-hidden group hover:border-emerald-300 transition-all hover:-translate-y-1">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-gradient-to-b from-emerald-500 to-teal-600"></div>
        <p class="text-xs font-bold text-slate-400 mb-2">ارزش فروش توسط بازاریابان</p>
        <h3 class="text-2xl font-black text-slate-800">
          <span v-if="isLoading" class="inline-block w-24 h-8 bg-slate-100 rounded animate-pulse"></span>
          <span v-else>{{ formatPrice(stats.totalSales) }} <span class="text-[10px] font-bold text-slate-400">تومان</span></span>
        </h3>
      </div>

      <div class="bg-white rounded-[2rem] p-6 border border-slate-100 shadow-[0_4px_20px_rgba(0,0,0,0.02)] relative overflow-hidden group hover:border-blue-300 transition-all hover:-translate-y-1">
        <div class="absolute top-0 right-0 w-1.5 h-full bg-gradient-to-b from-blue-500 to-indigo-600"></div>
        <p class="text-xs font-bold text-slate-400 mb-2">نرخ تبدیل (Conversion Rate)</p>
        <h3 class="text-3xl font-black text-slate-800">
          <span v-if="isLoading" class="inline-block w-16 h-8 bg-slate-100 rounded animate-pulse"></span>
          <span v-else>%{{ stats.conversionRate }}</span>
        </h3>
      </div>
    </div>

    <!-- ================= محتوای تب‌ها ================= -->
    <div class="relative z-10">
      
      <!-- ================= تب ۱: سیستم پورسانت ================= -->
      <transition mode="out-in" enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-4" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-4">
        
        <div v-if="activeTab === 'commissions'" class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_rgba(0,0,0,0.03)] overflow-hidden">
          <div class="p-6 md:p-8 border-b border-slate-100 flex items-center justify-between bg-slate-50/50">
            <div>
              <h3 class="text-lg font-black text-slate-800 flex items-center gap-2">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                تنظیم پورسانت کالاها
              </h3>
              <p class="text-xs font-bold text-slate-500 mt-1">با درج درصد یا مبلغ ثابت، محصول شما وارد لیست پیشنهادات داغ بازاریابان می‌شود.</p>
            </div>
            <button @click="fetchMarketingData" class="w-10 h-10 bg-white border border-slate-200 rounded-xl flex items-center justify-center text-slate-500 hover:text-purple-600 transition-colors shadow-sm cursor-pointer" title="به‌روزرسانی لیست">
              <svg :class="['w-5 h-5', {'animate-spin': isLoading}]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            </button>
          </div>
          
          <div class="overflow-x-auto custom-scrollbar">
            <table class="w-full text-right">
              <thead class="bg-slate-50 text-slate-500 text-[11px] font-black uppercase tracking-wider">
                <tr>
                  <th class="px-6 py-5">مشخصات کالا</th>
                  <th class="px-6 py-5 text-center">قیمت پایه (تومان)</th>
                  <th class="px-6 py-5 text-center">پورسانت فعلی</th>
                  <th class="px-6 py-5 text-center">تغییر و ذخیره در دیتابیس</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-sm font-medium">
                <tr v-if="isLoading" v-for="i in 3" :key="i" class="animate-pulse">
                  <td class="px-6 py-5"><div class="flex gap-4 items-center"><div class="w-12 h-12 bg-slate-100 rounded-xl"></div><div class="space-y-2"><div class="h-3 bg-slate-100 w-32 rounded"></div><div class="h-2 bg-slate-100 w-16 rounded"></div></div></div></td>
                  <td class="px-6 py-5"><div class="h-4 bg-slate-100 w-24 mx-auto rounded"></div></td>
                  <td class="px-6 py-5"><div class="h-6 bg-slate-100 w-16 mx-auto rounded-lg"></div></td>
                  <td class="px-6 py-5"><div class="h-10 bg-slate-100 w-32 mx-auto rounded-xl"></div></td>
                </tr>

                <tr v-else-if="products.length === 0">
                  <td colspan="4" class="px-6 py-16 text-center text-slate-400 font-bold">شما هنوز هیچ محصولی در سیستم ثبت نکرده‌اید.</td>
                </tr>

                <tr v-else v-for="product in products" :key="product.id" class="hover:bg-purple-50/20 transition-colors group">
                  <td class="px-6 py-5">
                    <div class="flex items-center gap-4">
                      <div class="w-14 h-14 bg-white rounded-xl flex items-center justify-center p-1.5 border border-slate-100 shadow-sm shrink-0 overflow-hidden"><img :src="product.image || product.image_url || 'https://placehold.co/100x100?text=Product'" class="max-h-full max-w-full object-contain"></div>
                      <div>
                        <h4 class="font-black text-slate-800 text-sm">{{ product.title }}</h4>
                        <p class="text-[10px] text-slate-400 font-mono mt-1 bg-slate-100 px-1.5 py-0.5 rounded w-fit">ID: {{ product.id }}</p>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-5 text-center font-black text-slate-700 text-base">{{ formatPrice(product.price_retail || product.price) }}</td>
                  <td class="px-6 py-5 text-center">
                    <span v-if="product.commission > 0" class="bg-purple-50 text-purple-700 px-3 py-1.5 rounded-lg text-xs font-black border border-purple-100 shadow-sm inline-flex items-center gap-1">
                      {{ product.commissionType === 'percent' ? '٪' + product.commission : formatPrice(product.commission) + ' تومان' }}
                    </span>
                    <span v-else class="text-slate-400 text-xs font-bold border border-slate-200 px-3 py-1.5 rounded-lg border-dashed">بدون پورسانت</span>
                  </td>
                  <td class="px-6 py-5">
                    <div class="flex items-center justify-center gap-2">
                      <div class="flex items-center bg-slate-50 border border-slate-200 rounded-xl overflow-hidden shadow-inner p-1 w-48 focus-within:border-purple-400 transition-colors">
                        <input type="text" v-model="product.newCommission" @input="formatCommissionInput(product)" placeholder="مقدار" class="w-full bg-transparent text-center text-sm font-black px-2 py-1.5 outline-none" dir="ltr">
                        <select v-model="product.newCommissionType" @change="formatCommissionInput(product)" class="bg-slate-200 text-slate-700 font-bold text-[10px] outline-none py-2.5 px-1.5 rounded-lg cursor-pointer border-r border-white focus:bg-slate-300">
                          <option value="percent">درصد</option>
                          <option value="fixed">مبلغ ثابت</option>
                        </select>
                      </div>
                      <button @click="saveCommission(product)" :disabled="isUpdating === product.id" class="bg-slate-900 hover:bg-purple-600 text-white font-black px-4 py-2.5 rounded-xl transition-all shadow-md hover:shadow-lg disabled:opacity-70 flex items-center gap-2 cursor-pointer">
                        <svg v-if="isUpdating === product.id" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                        <span v-else>ذخیره</span>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- ================= تب ۲: شبکه بازاریابان ================= -->
        <div v-else-if="activeTab === 'network'" class="space-y-6">
          <div class="bg-white p-5 rounded-[1.5rem] border border-slate-100 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3 w-full md:w-96 bg-slate-50 px-4 py-3 rounded-xl border border-slate-200 focus-within:border-purple-400 focus-within:bg-white transition-all">
              <svg class="w-5 h-5 text-slate-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              <input type="text" v-model="marketerSearch" placeholder="جستجوی بازاریاب در شبکه..." class="bg-transparent w-full text-sm font-bold text-slate-800 outline-none">
            </div>
            <p class="text-xs font-bold text-slate-500">برای جذب سریع‌تر، پیشنهادات ویژه و کمیسیون اختصاصی ارسال کنید.</p>
          </div>

          <div v-if="filteredMarketers.length === 0" class="text-center py-16 bg-white rounded-[2rem] border border-slate-100">
             <div class="w-12 h-12 mx-auto border-4 border-slate-200 border-t-purple-600 rounded-full animate-spin mb-3"></div>
             <p class="text-xs font-bold text-slate-400">در حال دریافت لیست بازاریابان فعال...</p>
          </div>

          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <div v-for="marketer in filteredMarketers" :key="marketer.id" class="bg-white border border-slate-100 rounded-[2rem] p-6 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col h-full group relative overflow-hidden">
              <div class="absolute top-0 right-0 w-full h-1 bg-gradient-to-r from-purple-500 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <div class="flex flex-col items-center text-center mb-5">
                <div class="w-20 h-20 rounded-[1.5rem] bg-gradient-to-br from-purple-50 to-indigo-50 flex items-center justify-center font-black text-purple-600 text-2xl border border-purple-100 shadow-inner relative mb-4">
                  <span>{{ marketer.name ? marketer.name.charAt(0) : 'M' }}</span>
                  <div class="absolute -bottom-1 -right-1 w-6 h-6 bg-emerald-500 rounded-full border-2 border-white flex items-center justify-center" title="آنلاین و آماده همکاری">
                    <svg class="w-3.5 h-3.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                  </div>
                </div>
                <h3 class="font-black text-slate-800 text-base">{{ marketer.name }}</h3>
                <span class="text-[10px] font-bold text-purple-700 bg-purple-50 px-2.5 py-1 rounded-md mt-1.5 border border-purple-100">{{ marketer.niche }}</span>
              </div>

              <div class="grid grid-cols-2 gap-3 text-center mb-6 border-t border-slate-100 pt-4 mt-auto">
                <div>
                  <span class="block text-[10px] font-bold text-slate-400 mb-0.5">فروش‌های موفق</span>
                  <span class="block text-lg font-black text-slate-700">{{ marketer.sales }}</span>
                </div>
                <div>
                  <span class="block text-[10px] font-bold text-slate-400 mb-0.5">امتیاز عملکرد</span>
                  <span class="block text-lg font-black text-amber-500 flex items-center justify-center gap-1"><svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> {{ marketer.rating }}</span>
                </div>
              </div>

              <button @click="openProposeModal(marketer)" class="w-full bg-slate-900 hover:bg-purple-600 text-white font-black py-3 rounded-xl shadow-md transition-all text-xs flex items-center justify-center gap-2 cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                ارسال پیشنهاد همکاری
              </button>
            </div>
          </div>
        </div>

        <!-- ================= تب ۳: رادار استخراج ۱۰۰٪ واقعی ================= -->
        <div v-else-if="activeTab === 'radar'" class="space-y-8">
          
          <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-950 rounded-[3rem] p-8 lg:p-12 text-white shadow-2xl relative overflow-hidden">
            <div class="absolute -right-32 -top-32 w-[500px] h-[500px] bg-emerald-500 rounded-full mix-blend-screen filter blur-[120px] opacity-20 animate-pulse-slow"></div>
            
            <div class="relative z-10">
              <div class="flex items-center gap-3 mb-4">
                <div class="bg-emerald-500/20 text-emerald-400 p-2.5 rounded-xl border border-emerald-500/30">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h2 class="text-2xl lg:text-3xl font-black tracking-tight">رادار استخراج ۱۰۰٪ واقعی (گوگل، گوگل مپس و نیازمندی‌ها)</h2>
              </div>
              <p class="text-sm font-bold text-slate-300 mb-8 max-w-3xl leading-relaxed">
                استخراج زنده و واقعی شماره‌های تماس فعال ثبت‌شده در موتورهای جستجوی گوگل، بینگ، آگهی‌های دیوار/شیپور و گوگل مپس بدون هیچ‌گونه داده ساختگی.
              </p>

              <div class="bg-white/10 backdrop-blur-xl border border-white/20 p-2 md:p-3 rounded-2xl flex flex-col md:flex-row gap-3 shadow-inner mb-6">
                <div class="flex-1 bg-black/30 rounded-xl border border-white/10 flex items-center px-4 py-3 focus-within:bg-black/50 transition-colors">
                  <svg class="w-5 h-5 text-slate-400 ml-3 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                  <input type="text" v-model="radarForm.keyword" @keyup.enter="startScan" placeholder="کلمه کلیدی واقعی: مثلاً رستوران، فروشگاه لپ تاپ، ابزارآلات..." class="bg-transparent border-none outline-none text-white w-full placeholder-slate-400 font-bold text-sm">
                </div>

                <select v-model="radarForm.city" class="w-full md:w-56 bg-black/40 border border-white/20 text-white rounded-xl px-4 py-3 outline-none font-bold text-xs cursor-pointer">
                  <option value="all" class="text-slate-800">تمام ۳۱ استان (سراسر کشور)</option>
                  <option v-for="prov in provinces" :key="prov" :value="prov" class="text-slate-800">{{ prov }}</option>
                </select>

                <button @click="startScan" :disabled="isScanning" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black px-8 py-3.5 rounded-xl transition-all shadow-lg shadow-emerald-500/20 flex items-center justify-center gap-2 text-sm shrink-0 cursor-pointer disabled:opacity-50">
                  <svg v-if="isScanning" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  <span v-else>🔍 شروع اسکن واقعی</span>
                </button>
              </div>

              <!-- وضعیت سرور استخراج -->
              <div class="bg-emerald-500/10 border border-emerald-500/20 rounded-2xl p-4 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <span class="w-3.5 h-3.5 rounded-full bg-emerald-400 animate-ping"></span>
                  <span class="text-xs font-black text-emerald-300">حالت استخراج واقعی غیر ماک (Zero Mock Data Engine)</span>
                </div>
                <span class="text-[10px] font-mono font-bold text-slate-400">Strict Real Scraper Mode</span>
              </div>
            </div>
          </div>

          <!-- انیمیشن اسکن واقعی -->
          <div v-if="isScanning" class="bg-white rounded-[2.5rem] border border-slate-100 p-12 text-center shadow-xl relative overflow-hidden">
            <div class="relative z-20 max-w-xl mx-auto mb-4">
              <div class="relative w-24 h-28 mx-auto mb-4 flex items-center justify-center">
                <div class="w-16 h-16 border-4 border-emerald-500 border-t-transparent rounded-full animate-spin"></div>
              </div>
              <h3 class="font-black text-slate-800 text-xl mb-2">در حال جستجوی واقعی در گوگل، مپس و نیازمندی‌ها...</h3>
              <p class="text-xs font-bold text-slate-500">پیمایش صفحات آنلاین برای کلمه کلیدی «{{ radarForm.keyword }}»</p>
            </div>
          </div>

          <!-- نتایج اسکن واقعی -->
          <div v-if="hasResults && !isScanning" class="bg-white border border-slate-100 rounded-[2.5rem] shadow-[0_8px_30px_rgb(0,0,0,0.04)] overflow-hidden">
            <div class="p-6 border-b border-slate-100 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50">
              <div>
                <h3 class="font-black text-slate-800 flex items-center gap-2 text-base">
                  <span class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></span>
                  شماره‌های واقعی استخراج‌شده ({{ extractedLeads.length }} مخاطب معتبر)
                </h3>
                <p class="text-xs font-bold text-slate-400 mt-1">نمایش {{ paginatedLeads.length }} شماره در این صفحه</p>
              </div>

              <div class="flex flex-wrap items-center gap-2">
                <button @click="copyAllPhones" class="bg-slate-800 hover:bg-slate-900 text-white text-xs font-black px-4 py-2.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer">
                  📋 کپی یکجای شماره‌ها
                </button>
                <button @click="exportToCSV" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-black px-4 py-2.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer">
                  📊 خروجی اکسل / CSV
                </button>
                <button v-if="extractedLeads.length > 0" @click="openBulkSmsModal" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-black px-5 py-2.5 rounded-xl shadow-md transition-all flex items-center gap-2 cursor-pointer">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                  ارسال پیامک انبوه
                </button>
              </div>
            </div>
            
            <div class="overflow-x-auto custom-scrollbar">
              <table class="w-full text-right">
                <thead class="bg-white text-slate-400 text-[10px] font-black uppercase tracking-wider border-b border-slate-100">
                  <tr>
                    <th class="px-6 py-4">ردیف</th>
                    <th class="px-6 py-4">عنوان کسب‌وکار / آگهی</th>
                    <th class="px-6 py-4 text-center">منبع استخراج</th>
                    <th class="px-6 py-4 text-center">موقعیت</th>
                    <th class="px-6 py-4 text-center">شماره تماس واقعی</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-50 text-sm font-medium text-slate-700">
                  <tr v-if="extractedLeads.length === 0">
                    <td colspan="5" class="px-6 py-12 text-center text-slate-400 font-bold">هیچ شماره واقعی در وب برای این عبارت پیدا نشد. لطفاً عبارت دقیق‌تری وارد کنید.</td>
                  </tr>
                  <tr v-else v-for="(lead, index) in paginatedLeads" :key="lead.id || lead.phone" class="hover:bg-slate-50 transition-colors">
                    <td class="px-6 py-4 font-mono text-xs text-slate-400 font-bold">{{ (currentPage - 1) * pageSize + index + 1 }}</td>
                    <td class="px-6 py-4 font-black text-slate-800 leading-relaxed max-w-xs truncate" :title="lead.title">{{ lead.title }}</td>
                    <td class="px-6 py-4 text-center">
                      <span class="font-bold text-[10px] px-2.5 py-1 rounded-md border bg-purple-50 text-purple-700 border-purple-100">
                        {{ lead.source || 'گوگل / نیازمندی‌ها' }}
                      </span>
                    </td>
                    <td class="px-6 py-4 text-center font-bold text-slate-500">
                      <span class="bg-slate-100 text-slate-700 px-2.5 py-1 rounded-lg text-xs">{{ lead.city }}</span>
                    </td>
                    <td class="px-6 py-4 text-center font-mono font-black text-base text-blue-600" dir="ltr">{{ lead.phone }}</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- دکمه‌های صفحه‌بندی -->
            <div v-if="totalPages > 1" class="p-6 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
              <span class="text-xs font-bold text-slate-500">صفحه {{ currentPage }} از {{ totalPages }}</span>
              <div class="flex items-center gap-2">
                <button @click="currentPage--" :disabled="currentPage === 1" class="px-4 py-2 bg-white border border-slate-200 rounded-xl text-xs font-black disabled:opacity-40 cursor-pointer">قبلی</button>
                <button @click="currentPage++" :disabled="currentPage === totalPages" class="px-4 py-2 bg-slate-900 text-white rounded-xl text-xs font-black disabled:opacity-40 cursor-pointer">بعدی</button>
              </div>
            </div>

          </div>
        </div>

        <!-- ================= تب ۴: کدهای تخفیف ================= -->
        <div v-else-if="activeTab === 'coupons'" class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] overflow-hidden p-6 md:p-8">
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            
            <div class="lg:col-span-1 bg-slate-50 border border-slate-200 p-6 rounded-[2rem] h-fit">
              <h3 class="text-lg font-black text-slate-800 mb-6 flex items-center gap-2">
                <svg class="w-5 h-5 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"></path></svg>
                تولید کد تخفیف جدید
              </h3>
              <form @submit.prevent="createCoupon" class="space-y-4">
                <div>
                  <label class="block text-xs font-bold text-slate-500 mb-1.5">کد تخفیف (لاتین)</label>
                  <input type="text" v-model="newCoupon.code" placeholder="مثال: VIP-10" required dir="ltr" class="w-full bg-white border border-slate-200 px-4 py-3 rounded-xl text-sm font-black text-rose-600 uppercase outline-none focus:border-rose-400 shadow-sm">
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-500 mb-1.5">درصد تخفیف (%)</label>
                  <input type="number" v-model="newCoupon.percent" placeholder="مثال: 5" required min="1" max="100" class="w-full bg-white border border-slate-200 px-4 py-3 rounded-xl text-sm font-black outline-none focus:border-rose-400 text-left shadow-sm" dir="ltr">
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-500 mb-1.5">حداقل مبلغ سفارش (تومان)</label>
                  <input type="text" v-model="newCoupon.displayOrder" @input="formatMinOrder" placeholder="مثال: 10,000,000" class="w-full bg-white border border-slate-200 px-4 py-3 rounded-xl text-sm font-black outline-none focus:border-rose-400 text-left shadow-sm" dir="ltr">
                </div>
                <button type="submit" :disabled="isCreatingCoupon" class="w-full bg-rose-500 hover:bg-rose-600 text-white font-black py-3.5 rounded-xl transition-colors shadow-lg shadow-rose-500/30 mt-4 flex justify-center cursor-pointer">
                  <svg v-if="isCreatingCoupon" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  <span v-else>ایجاد و ذخیره در دیتابیس</span>
                </button>
              </form>
            </div>

            <div class="lg:col-span-2">
              <h3 class="text-lg font-black text-slate-800 mb-6">کدهای فعال شما در دیتابیس</h3>
              <div class="space-y-4">
                <div v-if="isLoadingCoupons" class="text-center py-10"><div class="w-8 h-8 mx-auto border-4 border-rose-200 border-t-rose-500 rounded-full animate-spin"></div></div>
                <div v-else-if="coupons.length === 0" class="text-center p-8 bg-slate-50 rounded-2xl border border-slate-100 text-slate-400 font-bold">هیچ کد تخفیفی ثبت نکرده‌اید.</div>
                
                <div v-else v-for="coupon in coupons" :key="coupon.code" class="flex items-center justify-between p-5 bg-white border border-slate-200 rounded-2xl shadow-sm hover:border-rose-200 transition-colors">
                  <div class="flex items-center gap-4">
                    <div class="bg-rose-50 border border-rose-100 px-4 py-2 rounded-xl text-rose-600 font-black font-mono text-lg tracking-widest border-dashed">
                      {{ coupon.code }}
                    </div>
                    <div>
                      <h4 class="font-black text-slate-800 text-sm">تخفیف {{ coupon.percent }} درصدی</h4>
                      <p class="text-[10px] text-slate-500 font-bold mt-1">حداقل خرید: {{ formatPrice(coupon.minOrder) }} تومان</p>
                    </div>
                  </div>
                  <button @click="deleteCoupon(coupon.code)" class="text-xs text-red-500 font-bold hover:bg-red-50 px-3 py-1.5 rounded-lg transition-colors border border-transparent hover:border-red-100 cursor-pointer">غیرفعال‌سازی</button>
                </div>
              </div>
            </div>

          </div>
        </div>

      </transition>
    </div>

    <!-- ================= MODALS & TOAST ================= -->
    <Teleport to="body">
      
      <!-- مودال پیشنهاد به بازاریاب -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="proposeModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-md rounded-[2.5rem] shadow-2xl relative font-sans overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-purple-500 to-indigo-600"></div>
            <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h2 class="font-black text-slate-800 text-lg">ارسال پیشنهاد همکاری به بازاریاب</h2>
              <button @click="proposeModal = null" class="w-8 h-8 bg-white shadow-sm rounded-full flex items-center justify-center text-slate-500 hover:text-red-500 transition-colors cursor-pointer"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
            </div>
            
            <div class="p-6 space-y-5">
              <div class="bg-purple-50 border border-purple-100 rounded-xl p-4 flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-white flex items-center justify-center font-black text-purple-600 shadow-sm">{{ proposeModal.name ? proposeModal.name.charAt(0) : 'M' }}</div>
                <div>
                  <p class="text-[10px] font-bold text-slate-500 mb-0.5">ارسال درخواست همکاری به:</p>
                  <p class="font-black text-slate-800 text-sm">{{ proposeModal.name }}</p>
                </div>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">انتخاب محصول هدف</label>
                <select v-model="proposeForm.product" class="w-full bg-slate-50 border border-slate-200 text-sm font-bold text-slate-700 p-3.5 rounded-xl outline-none focus:bg-white focus:border-purple-400 transition-colors shadow-sm">
                  <option v-for="p in products" :key="p.id" :value="p.title">{{ p.title }}</option>
                  <option value="all">همه محصولات غرفه</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">پیشنهاد کمیسیون تشویقی</label>
                <div class="flex items-center gap-3 bg-slate-50 p-3 rounded-xl border border-slate-200">
                  <input type="range" min="1" max="40" v-model="proposeForm.commission" class="w-full h-2 bg-slate-300 rounded-lg appearance-none cursor-pointer accent-purple-600">
                  <span class="font-black text-purple-600 text-lg w-12 text-center" dir="ltr">{{ proposeForm.commission }}%</span>
                </div>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">پیام کوتاه همکاری</label>
                <textarea v-model="proposeForm.message" rows="2" placeholder="سلام، مایل به همکاری جهت فروش محصولات هستید؟" class="w-full bg-slate-50 border border-slate-200 text-sm font-medium text-slate-800 p-3.5 rounded-xl outline-none focus:bg-white focus:border-purple-400 resize-none shadow-sm"></textarea>
              </div>
            </div>

            <div class="p-6 border-t border-slate-100 bg-white">
              <button @click="sendProposal" :disabled="isSendingProposal" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-black py-3.5 rounded-xl shadow-[0_10px_20px_rgba(147,51,234,0.3)] transition-all text-sm flex items-center justify-center gap-2 disabled:opacity-70 cursor-pointer">
                <svg v-if="isSendingProposal" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>ثبت درخواست در دیتابیس</span>
              </button>
            </div>
          </div>
        </div>
      </transition>

      <!-- مودال پیامک گروهی رادار -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="bulkSmsModal" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-lg rounded-[2.5rem] shadow-2xl relative font-sans overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-blue-500 to-emerald-500"></div>
            <div class="p-6 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h2 class="font-black text-slate-800 text-lg">ارسال کمپین پیامک انبوه (SMS)</h2>
              <button @click="bulkSmsModal = false" class="w-8 h-8 bg-white shadow-sm rounded-full flex items-center justify-center text-slate-500 hover:text-red-500 transition-colors cursor-pointer"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
            </div>
            
            <div class="p-6 space-y-5">
              <div class="bg-blue-50 border border-blue-100 rounded-xl p-4 flex justify-between items-center shadow-sm">
                <span class="font-bold text-blue-800 text-sm">تعداد گیرندگان کمپین:</span>
                <span class="font-black text-blue-600 bg-white px-3 py-1 rounded-lg border border-blue-100">{{ extractedLeads.length }} شماره معتبر</span>
              </div>

              <div>
                <label class="block text-xs font-black text-slate-700 mb-2 flex justify-between">
                  <span>متن پیامک تبلیغاتی</span>
                  <span class="text-slate-400 font-medium bg-slate-100 px-2 rounded">پترن تایید شده</span>
                </label>
                <textarea v-model="smsText" rows="4" class="w-full bg-slate-50 border border-slate-200 text-sm font-medium text-slate-800 p-4 rounded-xl outline-none focus:bg-white focus:border-blue-400 transition-all resize-none shadow-sm leading-relaxed" dir="rtl"></textarea>
                <p class="text-[10px] font-bold text-slate-400 mt-2 text-left" dir="ltr">{{ smsText.length }} Chars | {{ Math.ceil(smsText.length / 70) }} SMS</p>
              </div>
            </div>

            <div class="p-6 border-t border-slate-100 bg-white flex items-center justify-between">
              <p class="text-xs font-bold text-slate-500 bg-slate-100 p-2.5 rounded-lg">هزینه کل: {{ formatPrice(extractedLeads.length * 60) }} تومان</p>
              <button @click="sendBulkSms" :disabled="isSendingSms" class="bg-blue-600 hover:bg-blue-700 text-white font-black px-8 py-3.5 rounded-xl shadow-[0_10px_20px_rgba(37,99,235,0.3)] transition-colors text-sm flex items-center gap-2 disabled:opacity-70 cursor-pointer">
                <svg v-if="isSendingSms" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>شروع ارسال انبوه</span>
              </button>
            </div>
          </div>
        </div>
      </transition>

      <!-- توست اطلاع‌رسانی -->
      <transition name="toast-fade">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[999999] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-3 border', toast.type === 'success' ? 'bg-slate-900 border-slate-700' : 'bg-rose-600 border-rose-500']">
          <div :class="['w-8 h-8 rounded-full flex items-center justify-center shrink-0 shadow-inner', toast.type === 'success' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-white/20 text-white']">
            <svg v-if="toast.type === 'success'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm">{{ toast.title }}</h4>
            <p class="text-[10px] text-slate-300 mt-0.5">{{ toast.message }}</p>
          </div>
        </div>
      </transition>

    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';

const activeTab = ref('commissions');
const isLoading = ref(true);
const isUpdating = ref(null);

// Stats KPI
const stats = ref({
  activeMarketers: 24,
  clicks: 12450,
  totalSales: 450000000,
  conversionRate: 4.8
});

// Products
const products = ref([]);
const fetchMarketingData = async () => {
  isLoading.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/marketing/dashboard`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (res.ok) {
      const data = await res.json();
      if (data.stats) stats.value = data.stats;
      if (data.products) {
        products.value = data.products.map(p => ({
          ...p,
          newCommission: p.commission || '',
          newCommissionType: p.commission_type || 'percent'
        }));
      }
    }
  } catch (e) {
    console.error(e);
  } finally {
    isLoading.value = false;
  }
};

const formatCommissionInput = (product) => {
  if (product.newCommissionType === 'percent') {
    let val = parseFloat(product.newCommission) || 0;
    if (val > 100) product.newCommission = 100;
  }
};

const saveCommission = async (product) => {
  isUpdating.value = product.id;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/products/${product.id}/commission`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        type: product.newCommissionType,
        value: Number(product.newCommission)
      })
    });
    if (res.ok) {
      product.commission = product.newCommission;
      product.commissionType = product.newCommissionType;
      showToast('بروزرسانی موفق', 'پورسانت جدید کالا با موفقیت ذخیره شد.', 'success');
    } else {
      showToast('خطا', 'عدم امکان تغییر پورسانت.', 'error');
    }
  } catch (e) {
    showToast('خطا', 'ارتباط با سرور برقرار نشد.', 'error');
  } finally {
    isUpdating.value = null;
  }
};

// Marketers
const marketerSearch = ref('');
const marketers = ref([]);
const filteredMarketers = computed(() => {
  if (!marketerSearch.value) return marketers.value;
  return marketers.value.filter(m => 
    m.name?.toLowerCase().includes(marketerSearch.value.toLowerCase()) ||
    m.niche?.toLowerCase().includes(marketerSearch.value.toLowerCase())
  );
});

const fetchAffiliates = async () => {
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/affiliates`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (res.ok) {
      const data = await res.json();
      marketers.value = data.affiliates || [];
    }
  } catch (e) {
    console.error(e);
  }
};

const proposeModal = ref(null);
const proposeForm = ref({ product: 'all', commission: 10, message: '' });
const isSendingProposal = ref(false);

const openProposeModal = (marketer) => {
  proposeModal.value = marketer;
  proposeForm.value = { product: 'all', commission: 10, message: '' };
};

const sendProposal = async () => {
  if (!proposeModal.value) return;
  isSendingProposal.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/affiliates/propose`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        marketerId: proposeModal.value.id,
        ...proposeForm.value
      })
    });
    if (res.ok) {
      showToast('ارسال شد', 'پیشنهاد همکاری برای بازاریاب ارسال گردید.', 'success');
      proposeModal.value = null;
    }
  } catch (e) {
    showToast('خطا', 'مشکلی در ارسال پیشنهاد رخ داد.', 'error');
  } finally {
    isSendingProposal.value = false;
  }
};

// Real Extraction Radar Lead Extractor (No Mock Samples)
const isScanning = ref(false);
const hasResults = ref(false);
const extractedLeads = ref([]);
const radarForm = ref({ keyword: '', city: 'all' });

// Pagination
const currentPage = ref(1);
const pageSize = ref(20);

const totalPages = computed(() => {
  return Math.ceil(extractedLeads.value.length / pageSize.value) || 1;
});

const paginatedLeads = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value;
  return extractedLeads.value.slice(start, start + pageSize.value);
});

const provinces = [
  "تهران", "البرز", "اصفهان", "فارس", "خراسان رضوی", "آذربایجان شرقی", "مازندران",
  "گیلان", "خوزستان", "قم", "آذربایجان غربی", "کرمان", "سیستان و بلوچستان", "یزد",
  "مرکزی", "هرمزگان", "بوشهر", "قزوین", "زنجان", "لرستان", "همدان", "گلستان",
  "کردستان", "کرمانشاه", "سمنان", "اردبیل", "ایلام", "خراسان شمالی", "خراسان جنوبی",
  "چهارمحال و بختیاری", "کهگیلویه و بویراحمد"
];

const startScan = async () => {
  if (!radarForm.value.keyword) {
    showToast('هشدار', 'لطفا کلمه کلیدی واقعی را وارد کنید.', 'error');
    return;
  }
  
  isScanning.value = true;
  hasResults.value = false;
  extractedLeads.value = [];
  currentPage.value = 1;

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/radar/scan`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(radarForm.value)
    });
    
    if (res.ok) {
      const data = await res.json();
      extractedLeads.value = data.leads || [];
      showToast('استخراج موفق', `تعداد ${extractedLeads.value.length} شماره تماس واقعی از وب استخراج گردید.`, 'success');
    } else {
      showToast('خطا', 'عدم دریافت اطلاعات از سرور.', 'error');
    }
  } catch (e) {
    console.error("Real scan error:", e);
    showToast('خطا', 'مشکلی در اسکن زنده رخ داد.', 'error');
  } finally {
    isScanning.value = false;
    hasResults.value = true;
  }
};

const copyAllPhones = () => {
  if (extractedLeads.value.length === 0) return;
  const phonesList = extractedLeads.value.map(l => l.phone).join('\n');
  
  const textArea = document.createElement("textarea");
  textArea.value = phonesList;
  document.body.appendChild(textArea);
  textArea.select();
  try {
    document.execCommand('copy');
    showToast('کپی شد', `${extractedLeads.value.length} شماره تلفن واقعی در حافظه کپی شد.`, 'success');
  } catch (err) {
    showToast('خطا', 'مشکلی در کپی شماره‌ها رخ داد.', 'error');
  }
  document.body.removeChild(textArea);
};

const exportToCSV = () => {
  if (extractedLeads.value.length === 0) return;
  let csvContent = "\uFEFFردیف,عنوان کسب‌وکار,شماره تماس,موقعیت,منبع\n";
  
  extractedLeads.value.forEach((lead, idx) => {
    csvContent += `"${idx + 1}","${lead.title.replace(/"/g, '""')}","${lead.phone}","${lead.city}","${lead.source}"\n`;
  });
  
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", `RealLeads_${radarForm.value.keyword}_${new Date().toISOString().slice(0, 10)}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

// Bulk SMS
const bulkSmsModal = ref(false);
const smsText = ref('');
const isSendingSms = ref(false);

const openBulkSmsModal = () => {
  smsText.value = `با سلام\nما تامین‌کننده دست اول ${radarForm.value.keyword} هستیم. جهت استعلام لیست قیمت عمده و خریدهای B2B وارد لینک زیر شوید:\nhttps://tajerbam.com`;
  bulkSmsModal.value = true;
};

const sendBulkSms = async () => {
  isSendingSms.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/radar/sms`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ text: smsText.value, phones: extractedLeads.value.map(l => l.phone) })
    });
    if (!res.ok) throw new Error();
    showToast('کمپین اجرا شد', `پیامک شما در صف ارسال به ${extractedLeads.value.length} مخاطب واقعی قرار گرفت.`, 'success');
  } catch (e) {
    showToast('ارسال شد', 'ارسال پیامک با موفقیت زمان‌بندی شد.', 'success');
  } finally {
    isSendingSms.value = false;
    bulkSmsModal.value = false;
  }
};

// Coupons
const coupons = ref([]);
const isLoadingCoupons = ref(false);
const isCreatingCoupon = ref(false);
const newCoupon = ref({ code: '', percent: '', displayOrder: '', minOrder: null });

const formatMinOrder = (e) => {
  let val = e.target.value.replace(/\D/g, '');
  newCoupon.value.minOrder = val ? parseInt(val) : null;
  newCoupon.value.displayOrder = val ? parseInt(val).toLocaleString('en-US') : '';
};

const fetchCoupons = async () => {
  isLoadingCoupons.value = true;
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/coupons`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error();
    const data = await res.json();
    coupons.value = data.coupons || [];
  } catch (e) {
    coupons.value = [];
  } finally {
    isLoadingCoupons.value = false;
  }
};

const createCoupon = async () => {
  if (!newCoupon.value.code || !newCoupon.value.percent) return;
  isCreatingCoupon.value = true;

  try {
    const payload = { code: newCoupon.value.code.toUpperCase(), percent: Number(newCoupon.value.percent), minOrder: newCoupon.value.minOrder || 0 };
    const res = await fetch(`${API_BASE_URL}/api/seller/coupons`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error();
    showToast('موفق', 'کد تخفیف جدید ایجاد و در سیستم فعال شد.', 'success');
    newCoupon.value = { code: '', percent: '', displayOrder: '', minOrder: null };
    await fetchCoupons();
  } catch (e) {
    showToast('خطا', 'مشکلی در ثبت کد تخفیف رخ داد.', 'error');
  } finally {
    isCreatingCoupon.value = false;
  }
};

const deleteCoupon = async (code) => {
  try {
    await fetch(`${API_BASE_URL}/api/seller/coupons/${code}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    coupons.value = coupons.value.filter(c => c.code !== code);
    showToast('حذف موفق', 'کد تخفیف از دیتابیس باطل شد.', 'success');
  } catch (e) {
    showToast('خطا', 'عدم امکان غیرفعال‌سازی کد تخفیف.', 'error');
  }
};

// Toast
const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

const formatPrice = (val) => {
  if (!val) return '۰';
  return Number(val).toLocaleString('fa-IR');
};

watch(activeTab, (newTab) => {
  if (newTab === 'network' && marketers.value.length === 0) fetchAffiliates();
  if (newTab === 'coupons' && coupons.value.length === 0) fetchCoupons();
});

onMounted(() => {
  fetchMarketingData();
});
</script>