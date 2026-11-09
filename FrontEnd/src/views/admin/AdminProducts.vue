<template>
  <div class="space-y-8 max-w-[1440px] mx-auto pb-24 font-sans text-slate-300 relative select-none" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارهای فیلتر و جستجو ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.6)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10 backdrop-blur-xl">
      <!-- افکت‌های نوری پس‌زمینه (Ambient Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-cyan-500 rounded-full mix-blend-screen filter blur-[100px] opacity-15 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-600 rounded-full mix-blend-screen filter blur-[80px] opacity-15 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-5">
        <div class="w-16 h-16 md:w-20 md:h-20 bg-slate-800/90 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-cyan-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-8 h-8 md:w-10 md:h-10 text-cyan-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
          </svg>
        </div>
        <div>
          <div class="flex items-center gap-3">
            <h1 class="text-2xl md:text-3xl font-black text-white tracking-tight">مدیریت جامع کاتالوگ و محصولات</h1>
            <span class="bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-[11px] font-extrabold px-2.5 py-0.5 rounded-full">نسخه سازمانی v8.5</span>
          </div>
          <p class="text-xs md:text-sm font-semibold text-slate-400 mt-1.5 leading-relaxed">
            بازبینی و ممیزی مشخصات فنی، گالری رسانه، تولید محتوای سئو با GapGPT، تایید یا ویرایش آنی محصولات
          </p>
        </div>
      </div>

      <div class="relative z-10 flex flex-wrap sm:flex-nowrap items-center gap-3 w-full md:w-auto">
        <!-- کادر جستجو -->
        <div class="relative w-full sm:w-80">
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="جستجوی عنوان، فروشنده یا SKU..." 
            class="w-full bg-slate-950/80 border border-slate-700/80 text-white px-4 py-3.5 pr-11 rounded-2xl focus:outline-none focus:border-cyan-500 focus:ring-2 focus:ring-cyan-500/20 transition-all text-xs md:text-sm font-medium placeholder-slate-500"
          >
          <svg class="w-5 h-5 text-slate-500 absolute right-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <button v-if="searchQuery" @click="searchQuery = ''" class="absolute left-3 top-3.5 text-slate-400 hover:text-white">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>
        
        <!-- دکمه رفرش -->
        <button 
          @click="fetchProducts" 
          :disabled="isLoading" 
          class="bg-slate-800/90 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold p-3.5 rounded-2xl transition-all shadow-md flex items-center justify-center shrink-0 disabled:opacity-50 hover:border-cyan-500/40 cursor-pointer" 
          title="بروزرسانی داده‌ها"
        >
          <svg :class="{'animate-spin text-cyan-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- ================= فیلتر وضعیت‌ها و آمار تعاملی ================= -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div 
        @click="statusFilter = 'all'" 
        class="cursor-pointer bg-slate-900/90 rounded-3xl border p-5 transition-all relative overflow-hidden group shadow-lg"
        :class="statusFilter === 'all' ? 'border-cyan-500 bg-cyan-950/30 ring-2 ring-cyan-500/20' : 'border-slate-800 hover:border-slate-700 hover:bg-slate-850'"
      >
        <div class="flex justify-between items-center mb-3">
          <span class="text-slate-400 text-xs font-bold">کل محصولات کاتالوگ</span>
          <span class="w-3 h-3 rounded-full bg-cyan-400 shadow-[0_0_10px_rgba(34,211,238,0.6)]"></span>
        </div>
        <div class="text-2xl md:text-3xl font-black text-white">
          {{ stats.total }} <span class="text-xs text-slate-500 font-normal">کالا</span>
        </div>
      </div>

      <div 
        @click="statusFilter = 'pending'" 
        class="cursor-pointer bg-slate-900/90 rounded-3xl border p-5 transition-all relative overflow-hidden group shadow-lg"
        :class="statusFilter === 'pending' ? 'border-amber-500 bg-amber-950/30 ring-2 ring-amber-500/20' : 'border-slate-800 hover:border-slate-700 hover:bg-slate-850'"
      >
        <div class="flex justify-between items-center mb-3">
          <span class="text-amber-400 text-xs font-bold">در انتظار بررسی</span>
          <span class="w-3 h-3 rounded-full bg-amber-400 shadow-[0_0_10px_rgba(251,191,36,0.8)] animate-pulse"></span>
        </div>
        <div class="text-2xl md:text-3xl font-black text-amber-400">
          {{ stats.pending }} <span class="text-xs text-amber-500/50 font-normal">کالا</span>
        </div>
      </div>

      <div 
        @click="statusFilter = 'active'" 
        class="cursor-pointer bg-slate-900/90 rounded-3xl border p-5 transition-all relative overflow-hidden group shadow-lg"
        :class="statusFilter === 'active' ? 'border-emerald-500 bg-emerald-950/30 ring-2 ring-emerald-500/20' : 'border-slate-800 hover:border-slate-700 hover:bg-slate-850'"
      >
        <div class="flex justify-between items-center mb-3">
          <span class="text-emerald-400 text-xs font-bold">تایید شده و فعال</span>
          <span class="w-3 h-3 rounded-full bg-emerald-400 shadow-[0_0_10px_rgba(52,211,153,0.6)]"></span>
        </div>
        <div class="text-2xl md:text-3xl font-black text-emerald-400">
          {{ stats.active }} <span class="text-xs text-emerald-500/50 font-normal">کالا</span>
        </div>
      </div>

      <div 
        @click="statusFilter = 'suspended'" 
        class="cursor-pointer bg-slate-900/90 rounded-3xl border p-5 transition-all relative overflow-hidden group shadow-lg"
        :class="statusFilter === 'suspended' ? 'border-rose-500 bg-rose-950/30 ring-2 ring-rose-500/20' : 'border-slate-800 hover:border-slate-700 hover:bg-slate-850'"
      >
        <div class="flex justify-between items-center mb-3">
          <span class="text-rose-400 text-xs font-bold">مسدود یا ناموجود</span>
          <span class="w-3 h-3 rounded-full bg-rose-500 shadow-[0_0_10px_rgba(244,63,94,0.6)]"></span>
        </div>
        <div class="text-2xl md:text-3xl font-black text-rose-400">
          {{ stats.suspended + stats.outOfStock }} <span class="text-xs text-rose-500/50 font-normal">کالا</span>
        </div>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-28 z-20 relative bg-slate-900/60 rounded-[2.5rem] border border-slate-800">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-cyan-400 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-cyan-400 animate-pulse">در حال دریافت و همگام‌سازی کاتالوگ محصولات با سرور...</p>
    </div>

    <!-- ================= جدول محصولات ================= -->
    <div v-else class="bg-slate-900/95 rounded-[2.5rem] border border-slate-800 shadow-2xl overflow-hidden relative animate-fade-in backdrop-blur-md">
      <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-cyan-500 via-blue-500 to-indigo-500"></div>
      
      <div class="overflow-x-auto custom-scrollbar-dark p-3">
        <table class="w-full text-right border-collapse whitespace-nowrap">
          <thead>
            <tr class="bg-slate-950/70 text-slate-400 text-xs font-bold border-b border-slate-800/80">
              <th class="p-5 font-semibold rounded-tr-2xl">تصویر و مشخصات کالا</th>
              <th class="p-5 font-semibold">کد کالا (SKU)</th>
              <th class="p-5 font-semibold">تامین‌کننده</th>
              <th class="p-5 font-semibold">قیمت پایه (تومان)</th>
              <th class="p-5 font-semibold text-center">وضعیت انتشار</th>
              <th class="p-5 font-semibold text-left rounded-tl-2xl">عملیات ممیزی و ویرایش</th>
            </tr>
          </thead>
          <tbody class="text-sm divide-y divide-slate-800/40">
            <tr v-if="filteredProducts.length === 0">
              <td colspan="6" class="py-20 text-center text-slate-500 font-bold">
                <div class="flex flex-col items-center justify-center gap-3">
                  <svg class="w-12 h-12 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                  <span>هیچ کالایی با فیلترهای انتخابی یافت نشد.</span>
                </div>
              </td>
            </tr>
            
            <tr v-for="product in filteredProducts" :key="product.id" class="hover:bg-slate-800/40 transition-colors group">
              <!-- ستون تصویر و نام -->
              <td class="p-5">
                <div class="flex items-center gap-4">
                  <div 
                    @click="openViewModal(product)" 
                    class="w-14 h-14 rounded-2xl bg-white p-1.5 border border-slate-700 shrink-0 shadow-sm overflow-hidden flex items-center justify-center cursor-pointer hover:border-cyan-400 transition-all"
                    title="مشاهده بزرگنمایی و مشخصات فنی"
                  >
                    <img 
                      :src="product.img || product.image_url || 'https://placehold.co/100x100/1e293b/475569?text=No+Img'" 
                      class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-300" 
                      @error="handleImageError" 
                      alt="Product"
                    >
                  </div>
                  <div>
                    <h4 
                      @click="openViewModal(product)" 
                      class="font-bold text-white text-sm max-w-[280px] truncate cursor-pointer hover:text-cyan-400 transition-colors" 
                      :title="product.name || product.title"
                    >
                      {{ product.name || product.title }}
                    </h4>
                    <div class="flex items-center gap-2 mt-1.5">
                      <span class="text-[10px] text-cyan-400 bg-cyan-950/60 px-2 py-0.5 rounded-md border border-cyan-900 font-mono">ID: #{{ product.id }}</span>
                      <span v-if="product.category_name || product.category" class="text-[10px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded-md">{{ product.category_name || product.category }}</span>
                    </div>
                  </div>
                </div>
              </td>

              <!-- ستون SKU -->
              <td class="p-5 font-mono text-xs text-slate-400 font-semibold">{{ product.sku || '---' }}</td>

              <!-- ستون تامین‌کننده -->
              <td class="p-5 font-bold text-white">
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                  <span class="truncate max-w-[160px]">{{ product.seller || 'تامین‌کننده سیستم' }}</span>
                </div>
              </td>

              <!-- ستون قیمت -->
              <td class="p-5 font-black text-emerald-400 text-base font-mono">
                {{ formatPrice(product.price || product.price_retail) }} <span class="text-xs font-normal text-slate-500">تومان</span>
              </td>
              
              <!-- تغییر سریع وضعیت در جدول -->
              <td class="p-5 text-center">
                <div class="inline-block relative">
                  <select 
                    :value="product.status || 'pending'" 
                    @change="quickChangeStatus(product, $event.target.value)"
                    :class="getStatusSelectClass(product.status)"
                    class="appearance-none text-xs font-bold py-2 px-3 pr-7 pl-6 rounded-xl border focus:outline-none cursor-pointer shadow-sm transition-all text-center focus:ring-2 focus:ring-cyan-500/20"
                  >
                    <option value="active">🟢 تایید شده و فعال</option>
                    <option value="pending">🟡 در انتظار بررسی</option>
                    <option value="suspended">🔴 مسدود شده</option>
                    <option value="out_of_stock">⚪ ناموجود موقت</option>
                  </select>
                </div>
              </td>

              <!-- دکمه‌های عملیات -->
              <td class="p-5 text-left">
                <div class="flex items-center justify-end gap-2">
                  <!-- تایید فوری در صورت در انتظار بودن -->
                  <button 
                    v-if="product.status === 'pending'" 
                    @click="approveProduct(product.id)" 
                    class="bg-emerald-500/15 hover:bg-emerald-500 text-emerald-400 hover:text-white border border-emerald-500/30 transition-all font-bold px-3 py-2 rounded-xl text-xs flex items-center gap-1.5 shadow-sm active:scale-95 cursor-pointer" 
                    title="تایید فوری و انتشار در سایت"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                    تایید
                  </button>

                  <!-- دکمه مشاهده جزئیات کامل -->
                  <button 
                    @click="openViewModal(product)" 
                    class="bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition-all font-bold p-2.5 rounded-xl text-xs flex items-center justify-center shadow-sm hover:border-cyan-500/40 active:scale-95 cursor-pointer" 
                    title="مشاهده و بازرسی کامل مشخصات"
                  >
                    <svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                    </svg>
                  </button>

                  <!-- دکمه ویرایش جامع -->
                  <button 
                    @click="openFullEditModal(product)" 
                    class="bg-blue-600/15 hover:bg-blue-600 text-blue-400 hover:text-white border border-blue-600/30 transition-all font-bold px-3 py-2 rounded-xl text-xs flex items-center gap-1.5 shadow-sm active:scale-95 cursor-pointer" 
                    title="ویرایش جامع کالا"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
                    </svg>
                    ویرایش
                  </button>

                  <!-- دکمه حذف -->
                  <button 
                    @click="promptDeleteProduct(product)" 
                    class="bg-rose-500/10 hover:bg-rose-500 text-rose-400 hover:text-white border border-rose-500/20 transition-all font-bold p-2.5 rounded-xl text-xs flex items-center justify-center shadow-sm active:scale-95 cursor-pointer" 
                    title="حذف کالا"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= مودال ۱: مشاهده کامل جزئیات کالا (Inspect Modal) ================= -->
    <div v-if="viewModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/85 backdrop-blur-md transition-opacity" @click="viewModal.show = false"></div>
      
      <div class="bg-slate-900 border border-slate-700/80 rounded-[2.5rem] w-full max-w-3xl max-h-[90vh] flex flex-col relative z-10 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.9)] overflow-hidden animate-fade-in">
        <!-- هدر مودال -->
        <div class="p-6 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
          <div class="flex items-center gap-3">
            <span class="w-3 h-3 rounded-full bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.8)] animate-pulse"></span>
            <div>
              <h3 class="text-lg md:text-xl font-black text-white">مشاهده مشخصات کامل کالا</h3>
              <p class="text-[11px] text-slate-400 font-mono mt-0.5">شناسه محصول: #{{ viewModal.data?.id }}</p>
            </div>
          </div>
          <button @click="viewModal.show = false" class="text-slate-400 hover:text-white p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 transition-colors cursor-pointer">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>

        <!-- محتوای مودال -->
        <div class="p-6 md:p-8 overflow-y-auto space-y-6 custom-scrollbar-dark flex-1" v-if="viewModal.data">
          <!-- بخش تصویر و اطلاعات پایه -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-white p-3 rounded-2xl border border-slate-700 flex items-center justify-center max-h-56 shadow-inner">
              <img :src="viewModal.data.img || viewModal.data.image_url" class="max-h-52 object-contain" alt="Product Image">
            </div>
            <div class="md:col-span-2 space-y-3">
              <h2 class="text-base md:text-lg font-black text-white leading-relaxed">{{ viewModal.data.title || viewModal.data.name }}</h2>
              
              <div class="grid grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                  <span class="text-slate-400 block mb-1">کد کالا (SKU):</span>
                  <span class="text-white font-mono font-bold">{{ viewModal.data.sku || '---' }}</span>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                  <span class="text-slate-400 block mb-1">قیمت پایه (تومان):</span>
                  <span class="text-emerald-400 font-bold font-mono">{{ formatPrice(viewModal.data.price_retail || viewModal.data.price) }}</span>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                  <span class="text-slate-400 block mb-1">تامین‌کننده / فروشنده:</span>
                  <span class="text-cyan-400 font-bold">{{ viewModal.data.seller || 'سیستم' }}</span>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                  <span class="text-slate-400 block mb-1">دسته‌بندی:</span>
                  <span class="text-white font-bold">{{ viewModal.data.category || viewModal.data.category_name || 'عمومی' }}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- پلکان‌های قیمت عمده -->
          <div v-if="viewModal.data.price_tiers && viewModal.data.price_tiers.length" class="space-y-2">
            <h4 class="text-xs font-black text-slate-300 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
              پلکان‌های قیمت عمده‌فروشی:
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <div v-for="(tier, idx) in viewModal.data.price_tiers" :key="idx" class="bg-slate-950 border border-slate-800 p-3 rounded-xl flex justify-between items-center text-xs">
                <span class="text-slate-400">از {{ tier.min_qty }} تا {{ tier.max_qty || '∞' }} عدد:</span>
                <span class="text-emerald-400 font-bold font-mono">{{ formatPrice(tier.price_per_unit) }} تومان</span>
              </div>
            </div>
          </div>

          <!-- مشخصات فنی کالا -->
          <div v-if="viewModal.data.simple_attributes && viewModal.data.simple_attributes.length" class="space-y-2">
            <h4 class="text-xs font-black text-slate-300 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-teal-400"></span>
              ویژگی‌ها و مشخصات فنی (ساده):
            </h4>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
              <div v-for="(attr, idx) in viewModal.data.simple_attributes" :key="idx" class="bg-slate-950 border border-slate-800 p-2.5 rounded-xl text-xs">
                <span class="text-slate-400 block">{{ attr.name }}:</span>
                <span class="text-white font-bold mt-0.5 block">{{ attr.value }}</span>
              </div>
            </div>
          </div>

          <!-- توضیحات کالا -->
          <div class="space-y-2">
            <h4 class="text-xs font-black text-slate-300 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-amber-400"></span>
              توضیحات و معرفی محصول:
            </h4>
            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 text-xs leading-loose text-slate-300 max-h-44 overflow-y-auto custom-scrollbar-dark" v-html="viewModal.data.description || 'توضیحاتی برای این محصول ثبت نشده است.'"></div>
          </div>
        </div>

        <!-- فوتر مودال -->
        <div class="p-5 border-t border-slate-800 bg-slate-950/60 flex justify-end gap-3">
          <button @click="viewModal.show = false" class="bg-slate-800 hover:bg-slate-700 text-white px-5 py-2.5 rounded-xl font-bold text-xs transition-colors cursor-pointer">بستن</button>
          <button @click="switchToEditModal" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 shadow-lg shadow-blue-600/30 transition-all cursor-pointer">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
            ویرایش کامل این کالا
          </button>
        </div>
      </div>
    </div>

    <!-- ================= مودال ۲: ویرایش جامع کالا (Full Edit - 100% منطبق با افزودن کالا) ================= -->
    <div v-if="editModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4">
      <div class="absolute inset-0 bg-slate-950/90 backdrop-blur-md" @click="closeFullEdit"></div>
      
      <div class="bg-slate-900 border border-slate-700 rounded-[2.5rem] w-full max-w-5xl max-h-[94vh] flex flex-col relative z-10 shadow-2xl overflow-hidden animate-fade-in text-slate-300">
        <!-- هدر فرم ویرایش -->
        <div class="p-5 sm:p-6 border-b border-slate-800 flex items-center justify-between bg-slate-950/80 shrink-0">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-cyan-500/10 border border-cyan-500/30 rounded-xl flex items-center justify-center text-cyan-400">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
            </div>
            <div>
              <h2 class="text-base sm:text-lg font-black text-white">ویرایش جامع و ممیزی کالا</h2>
              <p class="text-[11px] text-slate-400 font-mono mt-0.5">شناسه: #{{ editModal.productId }} | SKU: {{ editModal.form.sku || '---' }}</p>
            </div>
          </div>
          <button @click="closeFullEdit" class="text-slate-400 hover:text-white p-2 rounded-xl bg-slate-800 hover:bg-slate-700 transition-colors cursor-pointer">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>

        <!-- فیلدهای فرم جامع -->
        <div class="p-5 sm:p-8 overflow-y-auto space-y-8 custom-scrollbar-dark flex-1">
          
          <!-- بخش ۱: اطلاعات اصلی و دسته‌بندی -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-5">
            <h3 class="text-xs font-black text-cyan-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-cyan-400"></span> اطلاعات پایه کالا
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div class="md:col-span-2">
                <label class="block text-slate-400 text-xs font-bold mb-2">عنوان کامل کالا:</label>
                <input v-model="editModal.form.title" type="text" class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 font-bold text-sm" />
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">دسته‌بندی مرجع:</label>
                <select v-model="editModal.form.category_id" class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-xs font-bold cursor-pointer">
                  <option v-for="cat in flatCategories" :key="cat.id" :value="cat.id">{{ cat.fullPath }}</option>
                </select>
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">قیمت پایه تک‌فروشی (تومان):</label>
                <input v-model.number="editModal.form.price_retail" type="number" class="w-full bg-slate-900 border border-slate-700 text-emerald-400 font-black px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-left font-mono" dir="ltr" />
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">موجودی انبار:</label>
                <input v-model.number="editModal.form.stock" type="number" class="w-full bg-slate-900 border border-slate-700 text-white font-bold px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-left font-mono" dir="ltr" />
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">واحد کالا:</label>
                <select v-model="editModal.form.unit" class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-xs font-bold cursor-pointer">
                  <option value="عدد / دستگاه">عدد / دستگاه</option>
                  <option value="دست / ثوب">دست / ثوب</option>
                  <option value="بسته">بسته</option>
                  <option value="کارتن">کارتن</option>
                  <option value="کیلوگرم">کیلوگرم</option>
                  <option value="متر">متر</option>
                  <option value="جین">جین</option>
                  <option value="جفت">جفت</option>
                </select>
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">وضعیت انتشار:</label>
                <select v-model="editModal.form.status" class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-xs font-bold cursor-pointer">
                  <option value="active">🟢 تایید شده و فعال (انتشار در سایت)</option>
                  <option value="pending">🟡 در انتظار بررسی ادمین</option>
                  <option value="suspended">🔴 مسدود شده</option>
                  <option value="out_of_stock">⚪ ناموجود موقت</option>
                </select>
              </div>

              <div class="md:col-span-2">
                <label class="block text-slate-400 text-xs font-bold mb-2">محل کالا در انبار (قفسه):</label>
                <input v-model="editModal.form.rack_location" type="text" placeholder="مثال: راهرو B قفسه 4" class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-xs" />
              </div>
            </div>
          </div>

          <!-- بخش ۲: تصاویر و رسانه (با قابلیت آپلود و حذف گالری) -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-4">
            <div class="flex justify-between items-center">
              <h3 class="text-xs font-black text-cyan-400 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-cyan-400"></span> تصویر و رسانه کالا
              </h3>
              <span class="text-[11px] text-slate-400 font-bold">{{ editModal.form.gallery?.length || 0 }} / 5 رسانه در گالری</span>
            </div>
            
            <!-- کادر آپلود مستقیم رسانه -->
            <div @click="triggerEditUpload" class="bg-slate-900/80 border-2 border-dashed border-slate-700 hover:border-cyan-400 rounded-2xl p-4 flex flex-col items-center justify-center cursor-pointer transition-all text-center group">
              <input type="file" ref="editFileInputRef" class="hidden" accept="image/png, image/jpeg, image/jpg, image/webp, video/mp4" multiple @change="handleEditFileUpload">
              <div class="w-10 h-10 bg-slate-800 group-hover:bg-cyan-950 text-cyan-400 rounded-xl flex items-center justify-center mb-1.5 transition-colors border border-slate-700">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path></svg>
              </div>
              <p class="text-xs font-bold text-slate-300 group-hover:text-cyan-400 transition-colors">بارگذاری تصویر یا ویدئو جدید</p>
              <p class="text-[10px] text-slate-500">حذف خودکار پس‌زمینه + بوم سفید و واترمارک اختصاصی</p>
            </div>

            <!-- پیش‌نمایش گالری با قابلیت حذف تک‌تک آیتم‌ها -->
            <div v-if="editModal.form.gallery && editModal.form.gallery.length > 0" class="grid grid-cols-3 sm:grid-cols-5 gap-3 pt-2">
              <div v-for="(media, mIdx) in editModal.form.gallery" :key="mIdx" class="relative rounded-xl overflow-hidden border border-slate-700 aspect-square bg-slate-900 group">
                <img :src="media.preview || media" class="w-full h-full object-contain p-1 bg-white" alt="Gallery item">
                <button type="button" @click.stop="removeGalleryItem(mIdx)" class="absolute top-1 left-1 bg-rose-600/90 hover:bg-rose-500 text-white p-1 rounded-md shadow-md transition-all cursor-pointer" title="حذف این تصویر">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <div v-if="mIdx === 0" class="absolute bottom-1 right-1 bg-cyan-600/90 text-white text-[9px] font-bold px-1.5 py-0.5 rounded">اصلی</div>
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">آدرس تصویر اصلی:</label>
              <div class="flex gap-3 items-center">
                <input v-model="editModal.form.image_url" type="text" class="flex-1 bg-slate-900 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-cyan-500 text-xs font-mono" dir="ltr" />
                <div class="w-14 h-14 bg-white rounded-xl p-1 border border-slate-700 shrink-0 overflow-hidden flex items-center justify-center shadow-inner">
                  <img :src="editModal.form.image_url || 'https://placehold.co/100x100/1e293b/475569?text=Img'" class="w-full h-full object-contain" alt="Preview">
                </div>
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">لینک ویدئو از آپارات (اختیاری):</label>
              <input v-model="editModal.form.aparat_video_link" type="text" placeholder="https://www.aparat.com/v/..." class="w-full bg-slate-900 border border-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-mono" dir="ltr" />
            </div>
          </div>

          <!-- بخش ۳: پروموشن و فروش شگفت‌انگیز -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-black text-rose-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-rose-500"></span> پروموشن و فروش فوق‌العاده
            </h3>

            <!-- حراج شگفت‌انگیز -->
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 space-y-3">
              <label class="flex items-center justify-between cursor-pointer">
                <span class="text-xs font-bold text-rose-300">فعالسازی فروش فوق‌العاده زمان‌دار</span>
                <input type="checkbox" v-model="editModal.form.promotions.is_flash_sale" class="w-4 h-4 rounded text-rose-500">
              </label>
              
              <div v-if="editModal.form.promotions.is_flash_sale" class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">قیمت حراج (تومان):</span>
                  <input v-model="editModal.form.promotions.flash_price" type="text" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-rose-400 font-black text-center" dir="ltr" />
                </div>
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">تاریخ شروع:</span>
                  <input v-model="editModal.form.promotions.flash_start" type="text" placeholder="1403/08/10" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-white text-center" dir="ltr" />
                </div>
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">تاریخ پایان:</span>
                  <input v-model="editModal.form.promotions.flash_end" type="text" placeholder="1403/08/15" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-white text-center" dir="ltr" />
                </div>
              </div>
            </div>

            <!-- کوپن تخفیف -->
            <div class="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 space-y-3">
              <label class="flex items-center justify-between cursor-pointer">
                <span class="text-xs font-bold text-fuchsia-300">کوپن تخفیف اختصاصی کالا</span>
                <input type="checkbox" v-model="editModal.form.promotions.has_discount_code" class="w-4 h-4 rounded text-fuchsia-500">
              </label>

              <div v-if="editModal.form.promotions.has_discount_code" class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">کد تخفیف:</span>
                  <input v-model="editModal.form.promotions.discount_code" type="text" placeholder="VIP2026" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-fuchsia-400 font-bold uppercase text-center" dir="ltr" />
                </div>
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">نوع تخفیف:</span>
                  <select v-model="editModal.form.promotions.discount_type" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-white">
                    <option value="percent">درصدی (%)</option>
                    <option value="fixed">مبلغ ثابت (تومان)</option>
                  </select>
                </div>
                <div>
                  <span class="text-[10px] text-slate-400 block mb-1">مقدار تخفیف:</span>
                  <input v-model="editModal.form.promotions.discount_value" type="text" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs text-fuchsia-400 font-bold text-center" dir="ltr" />
                </div>
              </div>
            </div>
          </div>

          <!-- بخش ۴: پلکان‌های قیمت عمده B2B -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-4">
            <div class="flex justify-between items-center">
              <h3 class="text-xs font-black text-emerald-400 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span> پلکان‌های قیمت عمده‌فروشی
              </h3>
              <button @click="addPriceTier" type="button" class="text-cyan-400 hover:text-cyan-300 text-xs font-bold flex items-center gap-1 cursor-pointer">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                افزودن پله جدید
              </button>
            </div>

            <div v-for="(tier, idx) in editModal.form.price_tiers" :key="idx" class="grid grid-cols-1 md:grid-cols-4 gap-3 bg-slate-900 p-3.5 rounded-2xl border border-slate-800 items-center">
              <div>
                <span class="text-[10px] text-slate-500 block mb-1">حداقل تعداد:</span>
                <input v-model.number="tier.min_qty" type="number" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs font-mono text-white text-center" />
              </div>
              <div>
                <span class="text-[10px] text-slate-500 block mb-1">حداکثر تعداد (خالی = ∞):</span>
                <input v-model.number="tier.max_qty" type="number" placeholder="∞" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs font-mono text-white text-center" />
              </div>
              <div>
                <span class="text-[10px] text-slate-500 block mb-1">قیمت واحد (تومان):</span>
                <input v-model.number="tier.price_per_unit" type="number" class="w-full bg-slate-950 border border-slate-700 px-3 py-2 rounded-lg text-xs font-mono text-emerald-400 font-bold text-center" />
              </div>
              <div class="flex items-center gap-2">
                <select v-model="tier.shipping_method" class="w-full bg-slate-950 border border-slate-700 px-2 py-2 rounded-lg text-xs text-slate-300">
                  <option value="cargo">باربری صنعتی</option>
                  <option value="post">پست پیشتاز</option>
                </select>
                <button @click="removePriceTier(idx)" type="button" class="text-rose-400 hover:text-rose-300 p-2 rounded-lg bg-slate-950 hover:bg-rose-950/40 cursor-pointer">✕</button>
              </div>
            </div>
          </div>

          <!-- بخش ۵: مشخصات فنی ساده -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-4">
            <div class="flex justify-between items-center">
              <h3 class="text-xs font-black text-teal-400 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-teal-400"></span> مشخصات فنی (ویژگی‌های ساده)
              </h3>
              <button @click="addSimpleAttribute" type="button" class="text-teal-400 hover:text-teal-300 text-xs font-bold cursor-pointer">+ افزودن مشخصه</button>
            </div>

            <div v-for="(attr, idx) in editModal.form.simple_attributes" :key="idx" class="flex gap-3 items-center bg-slate-900 p-2.5 rounded-xl border border-slate-800">
              <input v-model="attr.name" type="text" placeholder="نام مشخصه (مثلا: پردازنده / جنس)" class="w-1/3 bg-slate-950 border border-slate-700 text-white px-3 py-2 rounded-lg text-xs" />
              <input v-model="attr.value" type="text" placeholder="مقدار (مثلا: Core i7 / نخ پنبه)" class="w-2/3 bg-slate-950 border border-slate-700 text-white px-3 py-2 rounded-lg text-xs" />
              <button @click="editModal.form.simple_attributes.splice(idx, 1)" type="button" class="text-rose-400 p-2 rounded-lg hover:bg-slate-800 cursor-pointer">✕</button>
            </div>
          </div>

          <!-- بخش ۶: توضیحات و سئو به همراه هوش مصنوعی GapGPT -->
          <div class="bg-slate-950/60 p-6 rounded-3xl border border-slate-800 space-y-4">
            <div class="flex justify-between items-center">
              <h3 class="text-xs font-black text-purple-400 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-purple-400"></span> توضیحات تخصصی و سئو
              </h3>
              <button @click="generateAIForEdit" :disabled="isAILoading || !editModal.form.title" type="button" class="text-xs font-black bg-purple-600 hover:bg-purple-500 text-white px-3.5 py-1.5 rounded-xl flex items-center gap-1.5 shadow-md shadow-purple-600/30 disabled:opacity-50 cursor-pointer">
                <svg v-if="isAILoading" class="w-3.5 h-3.5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>✨ تولید مجدد محتوا با GapGPT</span>
              </button>
            </div>

            <!-- نوار ابزار فرمت‌بندی HTML -->
            <div class="flex items-center gap-1 bg-slate-900 p-2 rounded-xl border border-slate-800 flex-wrap">
              <button type="button" @click="insertFormatting('<h2>', '</h2>')" class="px-2.5 py-1 text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">H2</button>
              <button type="button" @click="insertFormatting('<h3>', '</h3>')" class="px-2.5 py-1 text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">H3</button>
              <button type="button" @click="insertFormatting('<strong>', '</strong>')" class="px-2.5 py-1 text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">B</button>
              <button type="button" @click="insertFormatting('<em>', '</em>')" class="px-2.5 py-1 text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">I</button>
              <button type="button" @click="insertFormatting('<ul>\n  <li>', '</li>\n</ul>')" class="px-2.5 py-1 text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">• لیست</button>
              <button type="button" @click="showHtmlPreview = !showHtmlPreview" class="mr-auto text-[11px] text-cyan-400 hover:underline">
                {{ showHtmlPreview ? 'حالت ویرایش متن' : 'پیش‌نمایش HTML' }}
              </button>
            </div>

            <div v-if="showHtmlPreview" class="bg-slate-900 border border-slate-700 text-white p-4 rounded-xl text-xs leading-relaxed max-h-56 overflow-y-auto" v-html="editModal.form.description || '<p class=\'text-slate-500\'>توضیحاتی وجود ندارد.</p>'"></div>
            <textarea v-else ref="editorRef" v-model="editModal.form.description" rows="6" class="w-full bg-slate-900 border border-slate-700 text-white p-4 rounded-xl focus:outline-none focus:border-cyan-500 text-xs leading-relaxed custom-scrollbar-dark"></textarea>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-1">عنوان سئو (Meta Title):</label>
                <input v-model="editModal.form.seo_title" type="text" class="w-full bg-slate-900 border border-slate-700 text-white px-3 py-2 rounded-lg text-xs" />
              </div>
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-1">کلمات کلیدی (Keywords):</label>
                <input v-model="editModal.form.keywords" type="text" class="w-full bg-slate-900 border border-slate-700 text-white px-3 py-2 rounded-lg text-xs" />
              </div>
              <div class="md:col-span-2">
                <label class="block text-slate-400 text-xs font-bold mb-1">توضیحات متا (Meta Description):</label>
                <textarea v-model="editModal.form.seo_description" rows="2" class="w-full bg-slate-900 border border-slate-700 text-white px-3 py-2 rounded-lg text-xs"></textarea>
              </div>
            </div>
          </div>

        </div>

        <!-- فوتر مودال ویرایش -->
        <div class="p-5 sm:p-6 border-t border-slate-800 bg-slate-950/80 flex justify-end gap-3 shrink-0">
          <button @click="closeFullEdit" class="bg-slate-800 hover:bg-slate-700 text-white px-6 py-3 rounded-xl font-bold text-xs transition-colors cursor-pointer">انصراف</button>
          <button @click="saveFullEdit" :disabled="isSaving" class="bg-cyan-600 hover:bg-cyan-500 text-white px-8 py-3 rounded-xl font-black text-xs flex items-center gap-2 shadow-lg shadow-cyan-600/30 disabled:opacity-50 transition-all cursor-pointer">
            <svg v-if="isSaving" class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            <span v-else>ذخیره تغییرات در دیتابیس</span>
          </button>
        </div>
      </div>
    </div>

    <!-- ================= مودال تأیید حذف سفارشی ================= -->
    <div v-if="confirmModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/85 backdrop-blur-sm" @click="confirmModal.show = false"></div>
      <div class="bg-slate-900 border border-rose-500/30 rounded-3xl w-full max-w-md p-6 relative z-10 shadow-2xl animate-fade-in text-center">
        <div class="w-16 h-16 bg-rose-500/10 text-rose-500 border border-rose-500/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
        </div>
        <h3 class="text-lg font-black text-white mb-2">{{ confirmModal.title }}</h3>
        <p class="text-xs text-slate-400 mb-6 leading-relaxed">{{ confirmModal.message }}</p>
        <div class="flex gap-3">
          <button @click="confirmModal.show = false" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3 rounded-xl text-xs transition-colors cursor-pointer">انصراف</button>
          <button @click="executeConfirmAction" class="flex-1 bg-rose-600 hover:bg-rose-500 text-white font-black py-3 rounded-xl text-xs transition-all shadow-lg shadow-rose-600/30 cursor-pointer">تایید و حذف کالا</button>
        </div>
      </div>
    </div>

    <!-- ================= پیام شناور (Toast Notification) ================= -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-900 border border-cyan-500/40 shadow-[0_10px_35px_rgba(0,0,0,0.6)] rounded-2xl p-4 flex items-center gap-3.5 z-50 animate-fade-in max-w-sm backdrop-blur-xl">
      <div class="w-10 h-10 bg-cyan-500/10 text-cyan-400 rounded-xl flex items-center justify-center shrink-0 border border-cyan-500/20">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      </div>
      <div>
        <h4 class="text-white font-bold text-sm">{{ toastData.title }}</h4>
        <p class="text-slate-400 text-xs mt-0.5">{{ toastData.text }}</p>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token') || 'test-token';

const isLoading = ref(true);
const isSaving = ref(false);
const isAILoading = ref(false);
const showHtmlPreview = ref(false);
const editorRef = ref(null);
const editFileInputRef = ref(null);

const searchQuery = ref('');
const statusFilter = ref('all');

const products = ref([]);
const flatCategories = ref([]);

const stats = ref({
  total: 0,
  active: 0,
  pending: 0,
  suspended: 0,
  outOfStock: 0
});

// مودال مشاهده کامل مشخصات
const viewModal = ref({
  show: false,
  data: null
});

// مودال ویرایش جامع کالا (پوشش کامل تمام فیلدها)
const editModal = ref({
  show: false,
  productId: null,
  form: {
    title: '',
    sku: '',
    category_id: 1,
    price_retail: 0,
    status: 'pending',
    stock: 100,
    unit: 'عدد / دستگاه',
    rack_location: '',
    image_url: '',
    gallery: [],
    aparat_video_link: '',
    description: '',
    seo_title: '',
    seo_description: '',
    keywords: '',
    price_tiers: [],
    simple_attributes: [],
    attributes: [],
    promotions: {
      is_flash_sale: false,
      flash_price: '',
      flash_start: '',
      flash_end: '',
      has_discount_code: false,
      discount_code: '',
      discount_type: 'percent',
      discount_value: ''
    },
    is_dropship_enabled: false,
    commission_type: 'percent',
    commission_amount: 0
  }
});

// مودال تأییدیه اختصاصی
const confirmModal = ref({
  show: false,
  title: '',
  message: '',
  targetId: null
});

// سیستم نوتیفیکیشن
const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 4000);
};

const handleImageError = (e) => {
  e.target.src = 'https://placehold.co/100x100/1e293b/475569?text=No+Img';
};

// دریافت دسته‌بندی‌های دیتابیس
const fetchCategories = async () => {
  try {
    const res = await fetch(`${API_BASE}/api/categories`);
    if (res.ok) {
      const data = await res.json();
      const rawCats = Array.isArray(data) ? data : (data.categories || []);
      const flat = [];
      rawCats.forEach(c => {
        flat.push({ id: c.id, name: c.name, fullPath: c.name });
        if (c.children && Array.isArray(c.children)) {
          c.children.forEach(sub => {
            flat.push({ id: sub.id, name: sub.name, fullPath: `${c.name} > ${sub.name}` });
          });
        }
      });
      flatCategories.value = flat;
    }
  } catch (e) {
    flatCategories.value = [
      { id: 1, name: 'کشاورزی', fullPath: 'کشاورزی' },
      { id: 2, name: 'پوشاک و مد', fullPath: 'پوشاک، مد و پارچه' },
      { id: 3, name: 'کالای دیجیتال', fullPath: 'کالای دیجیتال و لوازم خانگی' }
    ];
  }
};

// ================= دریافت لیست محصولات =================
const fetchProducts = async () => {
  isLoading.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/products`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      const data = await response.json();
      let prodList = [];
      if (data.success && Array.isArray(data.products)) {
        prodList = data.products;
      } else if (Array.isArray(data)) {
        prodList = data;
      }

      // ادغام داده‌های لوکال استوریج در صورت وجود جهت سینک آنی
      try {
        const customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
        customProds.forEach(cp => {
          const idx = prodList.findIndex(p => String(p.id) === String(cp.id));
          if (idx !== -1) {
            prodList[idx] = { ...prodList[idx], ...cp };
          } else {
            prodList.unshift({
              id: cp.id,
              name: cp.title || cp.name,
              title: cp.title || cp.name,
              sku: cp.sku || `SKU-${cp.id}`,
              price: cp.price_retail || cp.price,
              price_retail: cp.price_retail || cp.price,
              seller: 'تامین‌کننده تایید شده',
              status: cp.status || 'pending',
              stock: cp.initial_stock || cp.stock || 100,
              unit: cp.unit || 'عدد / دستگاه',
              img: cp.image_url,
              image_url: cp.image_url,
              gallery: cp.gallery || [],
              category_name: 'پوشاک و محصولات B2B',
              price_tiers: cp.price_tiers || [],
              simple_attributes: cp.simple_attributes || [],
              attributes: cp.attributes || [],
              promotions: cp.promotions || {},
              description: cp.description || ''
            });
          }
        });
      } catch (err) {}

      products.value = prodList;
      calculateStats();
    } else if (response.status === 401) {
      showToast("نیاز به ورود", "لطفاً مجدداً وارد حساب کاربری مدیریت شوید.");
    }
  } catch (error) {
    console.error("خطا در دریافت لیست محصولات:", error);
    showToast("خطای شبکه", "امکان برقراری ارتباط با سرور پایگاه داده وجود ندارد.");
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchCategories();
  fetchProducts();
});

const calculateStats = () => {
  stats.value.total = products.value.length;
  stats.value.active = products.value.filter(p => p.status === 'active').length;
  stats.value.pending = products.value.filter(p => p.status === 'pending').length;
  stats.value.suspended = products.value.filter(p => p.status === 'suspended').length;
  stats.value.outOfStock = products.value.filter(p => p.status === 'out_of_stock' || (p.stock !== undefined && p.stock <= 0)).length;
};

// فیلتر و جستجوی چندگانه
const filteredProducts = computed(() => {
  let list = products.value;

  if (statusFilter.value !== 'all') {
    if (statusFilter.value === 'suspended') {
      list = list.filter(p => p.status === 'suspended' || p.status === 'out_of_stock');
    } else {
      list = list.filter(p => p.status === statusFilter.value);
    }
  }

  if (!searchQuery.value.trim()) return list;

  const q = searchQuery.value.toLowerCase().trim();
  return list.filter(p => 
    (p.name && p.name.toLowerCase().includes(q)) || 
    (p.title && p.title.toLowerCase().includes(q)) ||
    (p.sku && p.sku.toLowerCase().includes(q)) ||
    (p.seller && p.seller.toLowerCase().includes(q)) ||
    (p.id && p.id.toString().includes(q))
  );
});

// ================= باز کردن مودال مشاهده کامل کالا =================
const openViewModal = (product) => {
  viewModal.value.data = { ...product };
  viewModal.value.show = true;
};

const switchToEditModal = () => {
  const current = viewModal.value.data;
  viewModal.value.show = false;
  if (current) {
    openFullEditModal(current);
  }
};

// ================= تغییر سریع وضعیت =================
const quickChangeStatus = async (product, newStatus) => {
  const prevStatus = product.status;
  product.status = newStatus;

  try {
    const res = await fetch(`${API_BASE}/api/admin/products/${product.id}/status`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ status: newStatus })
    });

    if (res.ok) {
      calculateStats();
      showToast('وضعیت بروزرسانی شد', `وضعیت کالا به «${getStatusName(newStatus)}» تغییر یافت.`);
    } else {
      throw new Error();
    }
  } catch (e) {
    product.status = prevStatus;
    calculateStats();
    showToast('خطا در ذخیره', 'تغییر وضعیت کالا روی سرور ثبت نگردید.');
  }
};

// ================= تایید فوری انتشار کالا =================
const approveProduct = async (id) => {
  try {
    const response = await fetch(`${API_BASE}/api/admin/products/${id}/approve`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    const result = await response.json();
    if (response.ok && result.success) {
      const p = products.value.find(item => item.id === id);
      if (p) p.status = 'active';
      calculateStats();
      showToast('کالا تایید شد', 'این محصول هم‌اکنون در فروشگاه برای خریداران منتشر شد.');
    } else {
      throw new Error(result.detail || 'خطا در تایید کالا');
    }
  } catch (error) {
    showToast('خطا', error.message || 'عملیات تایید با خطا مواجه شد.');
  }
};

// ================= مودال ویرایش جامع کالا =================
const openFullEditModal = (product) => {
  editModal.value.productId = product.id;
  
  const promos = product.promotions || {};
  let galleryArr = product.gallery || [];
  if (typeof galleryArr === 'string') {
    try { galleryArr = JSON.parse(galleryArr); } catch(e) { galleryArr = []; }
  }
  if (galleryArr.length === 0 && (product.img || product.image_url)) {
    galleryArr = [{ type: 'image', preview: product.img || product.image_url }];
  }

  editModal.value.form = {
    title: product.name || product.title || '',
    sku: product.sku || '',
    category_id: product.category_id || 1,
    price_retail: product.price || product.price_retail || 0,
    status: product.status || 'pending',
    stock: product.stock !== undefined ? product.stock : 100,
    unit: product.unit || 'عدد / دستگاه',
    rack_location: product.rack_location || '',
    image_url: product.img || product.image_url || '',
    gallery: galleryArr.map(g => typeof g === 'string' ? { type: 'image', preview: g } : g),
    aparat_video_link: product.aparat_video_link || '',
    description: product.description || '',
    seo_title: product.seo_title || '',
    seo_description: product.seo_description || '',
    keywords: product.keywords || '',
    price_tiers: product.price_tiers ? JSON.parse(JSON.stringify(product.price_tiers)) : [],
    simple_attributes: product.simple_attributes ? JSON.parse(JSON.stringify(product.simple_attributes)) : [],
    attributes: product.attributes ? JSON.parse(JSON.stringify(product.attributes)) : [],
    promotions: {
      is_flash_sale: promos.is_flash_sale || false,
      flash_price: promos.flash_price || '',
      flash_start: promos.flash_start || '',
      flash_end: promos.flash_end || '',
      has_discount_code: promos.has_discount_code || false,
      discount_code: promos.discount_code || '',
      discount_type: promos.discount_type || 'percent',
      discount_value: promos.discount_value || ''
    },
    is_dropship_enabled: product.is_dropship_enabled || false,
    commission_type: product.commission_type || 'percent',
    commission_amount: product.commission_amount || 0
  };
  editModal.value.show = true;
};

const closeFullEdit = () => {
  editModal.value.show = false;
  editModal.value.productId = null;
};

const triggerEditUpload = () => {
  if (editFileInputRef.value) editFileInputRef.value.click();
};

const handleEditFileUpload = async (e) => {
  const files = e.target.files;
  if (!files || !files.length) return;

  for (const file of Array.from(files)) {
    if ((editModal.value.form.gallery?.length || 0) >= 5) {
      showToast('محدودیت تعداد', 'حداکثر ۵ تصویر/ویدئو مجاز است.');
      break;
    }

    const isVideo = file.type.startsWith('video/');
    const isImage = file.type.startsWith('image/');
    const reader = new FileReader();

    reader.onload = async (ev) => {
      const rawBase64 = ev.target.result;
      if (isImage) {
        let processedUrl = rawBase64;
        try {
          const res = await fetch(`${API_BASE}/api/utils/remove-bg`, {
            method: 'POST',
            headers: { 
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token()}`
            },
            body: JSON.stringify({ image: rawBase64, watermark: 'مدیریت تاجربام' })
          });
          if (res.ok) {
            const data = await res.json();
            if (data.processed_image || data.image) {
              processedUrl = data.processed_image || data.image;
            }
          }
        } catch(err) {}

        editModal.value.form.gallery.push({ type: 'image', preview: processedUrl });
        if (!editModal.value.form.image_url) {
          editModal.value.form.image_url = processedUrl;
        }
        showToast('تصویر اضافه شد', 'تصویر با پس‌زمینه سفید و واترمارک درج گردید.');
      } else if (isVideo) {
        editModal.value.form.gallery.push({ type: 'video', preview: rawBase64 });
        showToast('ویدئو اضافه شد', 'فایل ویدئویی با موفقیت در گالری ثبت شد.');
      }
    };
    reader.readAsDataURL(file);
  }
  if (editFileInputRef.value) editFileInputRef.value.value = '';
};

const removeGalleryItem = (index) => {
  editModal.value.form.gallery.splice(index, 1);
  if (editModal.value.form.gallery.length > 0) {
    const first = editModal.value.form.gallery[0];
    editModal.value.form.image_url = first.preview || first;
  } else {
    editModal.value.form.image_url = '';
  }
};

const addPriceTier = () => {
  editModal.value.form.price_tiers.push({
    min_qty: 10,
    max_qty: null,
    price_per_unit: Math.round(Number(editModal.value.form.price_retail || 0) * 0.9),
    shipping_method: 'cargo'
  });
};

const removePriceTier = (idx) => {
  editModal.value.form.price_tiers.splice(idx, 1);
};

const addSimpleAttribute = () => {
  editModal.value.form.simple_attributes.push({ name: '', value: '' });
};

const insertFormatting = (openTag, closeTag) => {
  if (!editorRef.value) {
    editModal.value.form.description = (editModal.value.form.description || '') + `${openTag}متن نمونه${closeTag}`;
    return;
  }
  const el = editorRef.value;
  const start = el.selectionStart || 0;
  const end = el.selectionEnd || 0;
  const text = el.value || '';
  const selected = text.substring(start, end) || 'متن نمونه';
  const replacement = openTag + selected + closeTag;
  editModal.value.form.description = text.substring(0, start) + replacement + text.substring(end);
};

const generateAIForEdit = async () => {
  if (!editModal.value.form.title) return;
  isAILoading.value = true;
  try {
    const res = await fetch(`${API_BASE}/api/ai/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: editModal.value.form.title })
    });
    if (res.ok) {
      const data = await res.json();
      if (data.description) editModal.value.form.description = data.description;
      if (data.seo_title) editModal.value.form.seo_title = data.seo_title;
      if (data.seo_description) editModal.value.form.seo_description = data.seo_description;
      if (data.keywords) editModal.value.form.keywords = data.keywords;
      if (data.simple_attributes && Array.isArray(data.simple_attributes)) {
        editModal.value.form.simple_attributes = data.simple_attributes;
      }
      showToast('GapGPT AI', 'محتوای تخصصی سئو و مشخصات فنی با مدل GPT-4o بازنویسی گردید.');
    }
  } catch (e) {
    showToast('خطا در هوش مصنوعی', 'امکان ارتباط با سرویس AI وجود نداشت.');
  } finally {
    isAILoading.value = false;
  }
};

const saveFullEdit = async () => {
  isSaving.value = true;
  const pId = editModal.value.productId;

  try {
    const f = editModal.value.form;
    const payload = {
      title: f.title,
      name: f.title,
      category_id: f.category_id,
      price: Number(f.price_retail),
      price_retail: Number(f.price_retail),
      status: f.status,
      stock: Number(f.stock),
      unit: f.unit,
      rack_location: f.rack_location,
      image_url: f.image_url,
      gallery: f.gallery.map(g => g.preview || g),
      aparat_video_link: f.aparat_video_link,
      description: f.description,
      seo_title: f.seo_title,
      seo_description: f.seo_description,
      keywords: f.keywords,
      price_tiers: f.price_tiers,
      simple_attributes: f.simple_attributes,
      attributes: f.attributes,
      promotions: f.promotions,
      is_dropship_enabled: f.is_dropship_enabled,
      commission_type: f.commission_type,
      commission_amount: f.commission_amount
    };

    const res = await fetch(`${API_BASE}/api/admin/products/${pId}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      const idx = products.value.findIndex(p => p.id === pId);
      if (idx !== -1) {
        products.value[idx] = { ...products.value[idx], ...payload, img: f.image_url };
      }
      calculateStats();
      showToast('ویرایش موفق', 'تغییرات کالا با موفقیت در پایگاه داده ذخیره شد.');
      closeFullEdit();
    } else {
      throw new Error("خطا در ثبت تغییرات در دیتابیس");
    }
  } catch (error) {
    showToast('خطا', error.message || 'ذخیره‌سازی اطلاعات با خطا مواجه شد.');
  } finally {
    isSaving.value = false;
  }
};

// ================= حذف محصول =================
const promptDeleteProduct = (product) => {
  confirmModal.value = {
    show: true,
    title: 'حذف کامل کالا',
    message: `آیا از حذف محصول «${product.name || product.title}» از پایگاه داده اطمینان دارید؟ این عملیات غیرقابل بازگشت است.`,
    targetId: product.id
  };
};

const executeConfirmAction = async () => {
  const id = confirmModal.value.targetId;
  confirmModal.value.show = false;
  if (!id) return;

  try {
    const response = await fetch(`${API_BASE}/api/admin/products/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    const result = await response.json();
    if (response.ok && result.success) {
      products.value = products.value.filter(p => p.id !== id);
      calculateStats();
      showToast('حذف موفق', 'کالا با موفقیت از سیستم حذف گردید.');
    } else {
      throw new Error(result.detail || 'خطا در حذف کالا');
    }
  } catch (error) {
    showToast('خطا', error.message || 'حذف کالا با خطا مواجه شد.');
  }
};

// ================= توابع کمکی =================
const formatPrice = (price) => {
  return price !== undefined && price !== null ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

const getStatusName = (status) => {
  const map = {
    active: 'فعال و تایید شده',
    pending: 'در انتظار تایید',
    suspended: 'مسدود شده',
    out_of_stock: 'ناموجود'
  };
  return map[status] || status;
};

const getStatusSelectClass = (status) => {
  const map = {
    active: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30 hover:border-emerald-500',
    pending: 'bg-amber-500/10 text-amber-400 border-amber-500/30 hover:border-amber-500',
    suspended: 'bg-rose-500/10 text-rose-400 border-rose-500/30 hover:border-rose-500',
    out_of_stock: 'bg-slate-800 text-slate-400 border-slate-700 hover:border-slate-600'
  };
  return map[status] || 'bg-slate-800 text-slate-400 border-slate-700';
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.custom-scrollbar-dark::-webkit-scrollbar { width: 5px; height: 6px; }
.custom-scrollbar-dark::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
.custom-scrollbar-dark::-webkit-scrollbar-thumb:hover { background: #475569; }

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>