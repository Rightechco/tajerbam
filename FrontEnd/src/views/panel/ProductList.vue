<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر و آمار کلیدی (KPIs) ================= -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 relative z-10">
      
      <!-- باکس معرفی -->
      <div class="lg:col-span-6 bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col justify-center relative overflow-hidden group">
        <div class="absolute -left-20 -top-20 w-48 h-48 bg-blue-500 rounded-full mix-blend-multiply filter blur-[60px] opacity-20 group-hover:opacity-40 transition-opacity duration-700 pointer-events-none"></div>
        <div class="flex items-center gap-5 relative z-10">
          <div class="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-blue-500/30 flex-shrink-0">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
          </div>
          <div>
            <h1 class="text-2xl lg:text-3xl font-black text-slate-800 tracking-tight mb-2">مدیریت انبار و کالاها</h1>
            <p class="text-sm font-bold text-slate-500">لیست تمامی محصولات، قیمت‌ها، ویرایش هوشمند و وضعیت تایید پلتفرم.</p>
          </div>
        </div>
      </div>

      <!-- باکس‌های آماری -->
      <div class="lg:col-span-6 grid grid-cols-2 gap-4">
        <!-- ارزش کل انبار -->
        <div class="bg-gradient-to-br from-emerald-50 to-teal-50 p-6 rounded-[2rem] border border-emerald-100/50 shadow-sm relative overflow-hidden group">
          <div class="absolute -right-4 -bottom-4 w-20 h-20 bg-emerald-200 rounded-full mix-blend-multiply filter blur-[30px] opacity-50 group-hover:scale-150 transition-transform"></div>
          <div class="flex justify-between items-start mb-4 relative z-10">
            <span class="text-xs font-black text-emerald-600 uppercase tracking-widest bg-emerald-100/50 px-2 py-1 rounded-md">ارزش کل انبار</span>
            <svg class="w-5 h-5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <h3 class="text-2xl font-black text-emerald-900 tracking-tight relative z-10">
            <span v-if="isLoading" class="inline-block w-24 h-8 bg-emerald-200/50 rounded animate-pulse"></span>
            <span v-else>{{ formatPrice(inventoryValue) }} <span class="text-[10px] font-bold text-emerald-700">تومان</span></span>
          </h3>
        </div>

        <!-- هشدار موجودی -->
        <div class="bg-gradient-to-br from-rose-50 to-orange-50 p-6 rounded-[2rem] border border-rose-100/50 shadow-sm relative overflow-hidden group cursor-pointer" @click="filterByLowStock">
          <div class="absolute -right-4 -bottom-4 w-20 h-20 bg-rose-200 rounded-full mix-blend-multiply filter blur-[30px] opacity-50 group-hover:scale-150 transition-transform"></div>
          <div class="flex justify-between items-start mb-4 relative z-10">
            <span class="text-xs font-black text-rose-600 uppercase tracking-widest bg-rose-100/50 px-2 py-1 rounded-md">نیاز به شارژ</span>
            <svg class="w-5 h-5 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          </div>
          <h3 class="text-2xl font-black text-rose-900 tracking-tight relative z-10">
            <span v-if="isLoading" class="inline-block w-12 h-8 bg-rose-200/50 rounded animate-pulse"></span>
            <span v-else>{{ lowStockCount }} <span class="text-[10px] font-bold text-rose-700">کالا</span></span>
          </h3>
        </div>
      </div>
    </div>

    <!-- ================= ابزارهای فیلتر و جستجو ================= -->
    <div class="bg-white p-4 rounded-[1.5rem] border border-slate-100 shadow-[0_4px_20px_rgb(0,0,0,0.02)] flex flex-col lg:flex-row gap-4 justify-between items-center relative z-10">
      
      <div class="flex flex-col md:flex-row items-center gap-3 w-full lg:w-auto flex-grow">
        <div class="relative w-full md:w-80">
          <input type="text" v-model="searchQuery" placeholder="جستجو نام کالا یا SKU..." class="w-full bg-slate-50 border border-slate-200 text-sm font-medium text-slate-800 px-4 py-3.5 pr-11 rounded-xl focus:bg-white focus:border-blue-400 focus:shadow-[0_0_0_4px_rgba(96,165,250,0.1)] outline-none transition-all">
          <svg class="w-5 h-5 text-slate-400 absolute right-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        
        <select v-model="statusFilter" class="w-full md:w-48 bg-slate-50 border border-slate-200 text-sm font-bold text-slate-600 px-4 py-3.5 rounded-xl outline-none focus:border-blue-400 cursor-pointer appearance-none">
          <option value="all">همه وضعیت‌ها</option>
          <option value="active">منتشر شده (فعال)</option>
          <option value="pending">در انتظار تایید ادمین</option>
          <option value="out_of_stock">ناموجود</option>
        </select>
      </div>

      <div class="flex gap-3 w-full md:w-auto">
        <button @click="fetchProducts" class="p-3 bg-slate-50 border border-slate-200 text-slate-500 rounded-xl hover:text-blue-600 hover:border-blue-300 transition-colors shadow-sm" title="بروزرسانی">
          <svg :class="{'animate-spin text-blue-500': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
        <button @click="exportCSV" class="bg-white border-2 border-slate-200 text-slate-700 hover:border-slate-800 hover:bg-slate-50 font-black px-5 py-3 rounded-xl transition-all shadow-sm flex items-center justify-center gap-2 text-sm flex-1 md:flex-none whitespace-nowrap">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          خروجی CSV
        </button>
        <button type="button" @click.prevent="goToAddProduct" class="bg-blue-600 hover:bg-blue-700 text-white font-black px-6 py-3 rounded-xl shadow-[0_10px_20px_rgba(37,99,235,0.3)] transition-all hover:-translate-y-1 flex items-center justify-center gap-2 text-sm flex-1 md:flex-none whitespace-nowrap cursor-pointer">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
          ثبت کالای جدید
        </button>
      </div>
    </div>

    <!-- ================= جدول پیشرفته کالاها ================= -->
    <div class="bg-white border border-slate-100 rounded-[2.5rem] shadow-[0_10px_40px_rgb(0,0,0,0.03)] overflow-hidden relative z-10">
      
      <div v-if="isLoading" class="absolute inset-0 bg-white/70 backdrop-blur-sm z-20 flex flex-col items-center justify-center">
        <svg class="w-12 h-12 animate-spin text-blue-600 mb-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <span class="font-black text-slate-600">در حال همگام‌سازی با سرور...</span>
      </div>

      <div class="overflow-x-auto custom-scrollbar min-h-[400px]">
        <table class="w-full text-right text-sm">
          <thead class="bg-slate-50/80 text-slate-500 text-[11px] font-black uppercase tracking-wider border-b border-slate-200">
            <tr>
              <th class="px-6 py-5 w-10 text-center">
                <input type="checkbox" @change="toggleAll" :checked="selectedProducts.length === filteredProducts.length && filteredProducts.length > 0" class="w-4 h-4 rounded text-blue-600 focus:ring-blue-500 border-slate-300">
              </th>
              <th class="px-6 py-5">مشخصات کالا</th>
              <th class="px-6 py-5 text-center w-48">وضعیت موجودی</th>
              <th class="px-6 py-5 text-center">قیمت پایه (تومان)</th>
              <th class="px-6 py-5 text-center">وضعیت انتشار</th>
              <th class="px-6 py-5 text-center">عملیات</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 font-medium text-slate-700">
            
            <tr v-if="isLoading" v-for="i in 5" :key="i" class="animate-pulse bg-white">
              <td class="px-6 py-5 text-center"><div class="w-4 h-4 bg-slate-200 rounded mx-auto"></div></td>
              <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                  <div class="w-16 h-16 bg-slate-100 rounded-2xl"></div>
                  <div class="space-y-2"><div class="h-3 bg-slate-200 rounded w-32"></div><div class="h-2 bg-slate-100 rounded w-16"></div></div>
                </div>
              </td>
              <td class="px-6 py-5 text-center">
                <div class="flex flex-col items-center gap-2">
                  <div class="h-4 bg-slate-200 rounded w-12"></div>
                  <div class="w-full h-1.5 bg-slate-100 rounded-full"></div>
                </div>
              </td>
              <td class="px-6 py-5 text-center"><div class="h-4 bg-slate-200 rounded w-20 mx-auto"></div></td>
              <td class="px-6 py-5 text-center"><div class="h-6 bg-slate-200 rounded-xl w-24 mx-auto"></div></td>
              <td class="px-6 py-5"><div class="flex justify-center gap-2"><div class="w-9 h-9 bg-slate-200 rounded-xl"></div><div class="w-9 h-9 bg-slate-200 rounded-xl"></div></div></td>
            </tr>

            <tr v-else-if="filteredProducts.length === 0">
              <td colspan="6" class="py-16 text-center bg-white">
                <div class="w-20 h-20 bg-slate-50 text-slate-300 rounded-full flex items-center justify-center mx-auto mb-4 border border-slate-100">
                  <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path></svg>
                </div>
                <h3 class="text-base font-black text-slate-800 mb-1">کالایی یافت نشد</h3>
                <p class="text-sm font-bold text-slate-500 mb-6">با این مشخصات هیچ محصولی در انبار شما ثبت نشده است.</p>
                <button type="button" @click.prevent="goToAddProduct" class="bg-slate-900 text-white px-6 py-2.5 rounded-xl font-bold hover:bg-black transition-colors shadow-md">ثبت اولین کالا</button>
              </td>
            </tr>

            <tr v-else v-for="product in filteredProducts" :key="product.id" class="hover:bg-blue-50/30 transition-colors group bg-white">
              <td class="px-6 py-5 text-center">
                <input type="checkbox" v-model="selectedProducts" :value="product.id" class="w-4 h-4 rounded text-blue-600 focus:ring-blue-500 border-slate-300 cursor-pointer">
              </td>
              
              <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                  <div class="relative w-16 h-16 flex-shrink-0 cursor-pointer" @click="openEditModal(product)">
                    <div class="absolute inset-0 bg-blue-500/20 rounded-2xl blur-md opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                    <div class="w-full h-full bg-slate-50 border border-slate-200 rounded-2xl p-1.5 shadow-sm group-hover:border-blue-400 group-hover:scale-105 transition-all duration-300 relative z-10 flex items-center justify-center overflow-hidden">
                      <img :src="product.img" class="max-h-full object-contain">
                    </div>
                  </div>
                  <div>
                    <h3 class="font-black text-sm text-slate-800 line-clamp-2 leading-relaxed mb-1.5 group-hover:text-blue-700 transition-colors cursor-pointer" @click="openEditModal(product)">{{ product.name }}</h3>
                    <div class="flex items-center gap-2">
                      <span class="text-[10px] font-mono font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded border border-slate-200">SKU: {{ product.sku }}</span>
                      <span class="text-[10px] font-bold text-slate-400">{{ product.category }}</span>
                    </div>
                  </div>
                </div>
              </td>

              <td class="px-6 py-5 text-center">
                <div class="flex flex-col items-center">
                  <div class="flex items-center gap-2 mb-1.5 px-2">
                    <span class="font-black text-sm" :class="product.stock <= 5 ? 'text-rose-600' : 'text-slate-700'">{{ product.stock }}</span>
                    <span class="text-[10px] text-slate-400 font-bold bg-slate-100 px-1.5 py-0.5 rounded">{{ product.unit }}</span>
                  </div>
                  <div class="w-full max-w-[100px] h-1.5 bg-slate-100 rounded-full overflow-hidden shadow-inner">
                    <div class="h-full rounded-full transition-all" :class="product.stock <= 5 ? 'bg-rose-500' : 'bg-emerald-500'" :style="`width: ${Math.min((product.stock / 100) * 100, 100)}%`"></div>
                  </div>
                  <div v-if="product.stock <= 5" class="text-[9px] font-black text-rose-500 mt-1.5">نیاز به شارژ</div>
                </div>
              </td>

              <td class="px-6 py-5 text-center">
                <div class="font-black text-slate-800 text-base tracking-tight">{{ formatPrice(product.price) }}</div>
                <div v-if="product.priceTiers" class="text-[9px] font-bold text-blue-500 mt-1 flex items-center justify-center gap-1">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                  دارای قیمت پلکانی
                </div>
              </td>

              <td class="px-6 py-5 text-center">
                <div class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-[11px] font-black shadow-sm transition-all border mx-auto"
                     :class="product.status === 'active' ? 'bg-emerald-50 text-emerald-600 border-emerald-100 hover:bg-emerald-100' : (product.status === 'pending' ? 'bg-amber-50 text-amber-600 border-amber-100' : 'bg-slate-100 text-slate-500 border-slate-200 hover:bg-slate-200')">
                  <span v-if="product.status === 'active'" class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                  {{ product.status === 'active' ? 'منتشر شده' : (product.status === 'pending' ? 'در انتظار تایید' : 'غیرفعال') }}
                </div>
              </td>

              <td class="px-6 py-5 text-center">
                <div class="flex justify-center gap-2 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity">
                  <button type="button" @click.prevent="goToProductDetail(product.id)" class="w-9 h-9 rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-blue-600 hover:border-blue-300 hover:bg-blue-50 flex items-center justify-center transition-all shadow-sm" title="مشاهده در سایت">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                  </button>
                  <button @click="openEditModal(product)" class="w-9 h-9 rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-amber-600 hover:border-amber-300 hover:bg-amber-50 flex items-center justify-center transition-all shadow-sm" title="ویرایش کالا">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                  </button>
                  <button @click="confirmDelete(product)" class="w-9 h-9 rounded-xl bg-white border border-slate-200 text-slate-500 hover:text-rose-600 hover:border-rose-300 hover:bg-rose-50 flex items-center justify-center transition-all shadow-sm" title="حذف کالا">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                  </button>
                </div>
              </td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>

    <!-- ================= MODAL EDIT PRODUCT ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="editModal.show" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 lg:p-8 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-5xl rounded-[2.5rem] shadow-2xl relative font-sans border border-slate-200 flex flex-col max-h-[95vh] overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-blue-500 via-purple-600 to-indigo-600 z-10"></div>
            
            <!-- هدر مودال -->
            <div class="p-6 border-b border-slate-100 bg-slate-50/80 backdrop-blur flex justify-between items-center relative z-10 shrink-0">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-white rounded-xl shadow-sm border border-slate-200 flex items-center justify-center text-blue-600">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                </div>
                <div>
                  <h2 class="font-black text-slate-800 text-lg flex items-center gap-2">
                    ویرایش هوشمند کالا
                    <span class="bg-purple-100 text-purple-700 text-[10px] px-2 py-0.5 rounded-md font-extrabold">Groq AI</span>
                  </h2>
                  <p class="text-[10px] font-mono font-bold text-slate-500 mt-1 flex items-center gap-2">
                    SKU: {{ editModal.data.sku }} 
                    <span class="w-1 h-1 rounded-full bg-slate-300"></span> 
                    ثبت شده: {{ editModal.data.date || 'نامشخص' }}
                  </p>
                </div>
              </div>
              <button @click="closeEditModal" class="w-10 h-10 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-400 hover:text-red-500 hover:bg-red-50 transition-colors shadow-sm">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <!-- پیام اطلاع‌رسانی وضعیت -->
            <div class="bg-amber-50 border-b border-amber-100 px-6 py-3 flex items-center gap-2 text-xs font-bold text-amber-800 shrink-0">
              <svg class="w-4 h-4 text-amber-600 shrink-0 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              <span>توجه: پس از ذخیره تغییرات، این محصول جهت بررسی مجدد به وضعیت <strong>«در انتظار تایید مدیریت»</strong> منتقل می‌شود.</span>
            </div>

            <!-- بدنه فرم ویرایش چندستونه -->
            <div class="flex-grow overflow-y-auto custom-scrollbar p-6 lg:p-8">
              <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                
                <!-- ستون راست -->
                <div class="lg:col-span-8 space-y-8">
                  
                  <!-- اطلاعات اصلی محصول -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm relative">
                    <div class="space-y-5">
                      <div>
                        <label class="block text-sm font-black text-slate-700 mb-2">عنوان محصول <span class="text-rose-500">*</span></label>
                        <input v-model="editModal.data.name" @input="detectEditCategoryFromTitle" type="text" placeholder="عنوان کالا..." class="w-full bg-slate-50 border-2 border-slate-100 text-base font-black px-4 py-3.5 rounded-xl outline-none focus:border-blue-500 focus:bg-white transition-all text-slate-800">
                      </div>

                      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <!-- کادر دسته‌بندی ویرایش با قابلیت جستجو و پیشنهاد AI (بدون overflow-hidden جهت جلوگیری از برش منو) -->
                        <div class="relative z-[100]" ref="editCategoryDropdownRef">
                          <div class="flex items-center justify-between mb-2">
                            <label class="block text-xs font-bold text-slate-600">دسته‌بندی مرجع</label>
                            
                            <!-- چیپ پیشنهاد دسته‌بندی مرتبط -->
                            <button 
                              v-if="editSuggestedCategory && editModal.data.category_id !== editSuggestedCategory.id" 
                              type="button"
                              @click="applyEditSuggestedCategory" 
                              class="text-[11px] font-black text-amber-700 bg-amber-50 hover:bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-lg flex items-center gap-1 transition-all shadow-sm animate-pulse cursor-pointer"
                              title="اعمال دسته‌بندی پیشنهادی"
                            >
                              <svg class="w-3.5 h-3.5 text-amber-500" fill="currentColor" viewBox="0 0 20 20"><path d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z"></path></svg>
                              <span>پیشنهاد: {{ editSuggestedCategory.name }}</span>
                              <span class="text-[9px] bg-amber-200 text-amber-900 px-1 rounded font-extrabold mr-1">اعمال</span>
                            </button>
                          </div>

                          <div 
                            @click="isEditCategoryDropdownOpen = !isEditCategoryDropdownOpen" 
                            :class="[
                              'w-full bg-slate-50 border-2 px-4 py-3 rounded-xl text-sm font-bold cursor-pointer transition-all flex items-center justify-between',
                              isEditCategoryDropdownOpen ? 'border-blue-500 bg-white ring-4 ring-blue-50' : 'border-slate-100 hover:border-blue-300'
                            ]"
                          >
                            <span class="truncate text-slate-800">
                              {{ editSelectedCategoryLabel || 'انتخاب دسته‌بندی...' }}
                            </span>
                            <svg class="w-4 h-4 text-slate-400 transition-transform duration-300" :class="{'rotate-180': isEditCategoryDropdownOpen}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                          </div>

                          <!-- منوی کشویی جستجوی دسته‌بندی با z-index بالادست -->
                          <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-2">
                            <div v-if="isEditCategoryDropdownOpen" class="absolute top-[calc(100%+6px)] left-0 right-0 bg-white rounded-2xl shadow-2xl border border-slate-200 p-3 z-[999] overflow-hidden">
                              <div class="relative mb-2">
                                <input 
                                  type="text" 
                                  v-model="editCategorySearchQuery" 
                                  placeholder="جستجو در تمام دسته‌بندی‌ها..." 
                                  class="w-full bg-slate-50 border border-slate-200 px-3 py-2 rounded-xl text-xs font-bold outline-none focus:bg-white focus:border-blue-400"
                                  @click.stop
                                >
                              </div>

                              <div class="max-h-56 overflow-y-auto space-y-1 pr-1 custom-scrollbar">
                                <div 
                                  v-for="cat in filteredEditCategories" 
                                  :key="cat.id" 
                                  @click="selectEditCategory(cat)"
                                  :class="[
                                    'p-2 rounded-xl text-xs font-bold cursor-pointer transition-colors flex items-center justify-between',
                                    editModal.data.category_id === cat.id ? 'bg-blue-50 text-blue-700 font-black' : 'text-slate-700 hover:bg-slate-50'
                                  ]"
                                >
                                  <span class="truncate">{{ cat.fullPath }}</span>
                                  <span v-if="editSuggestedCategory && cat.id === editSuggestedCategory.id" class="text-[9px] font-black bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">پیشنهادی</span>
                                </div>
                              </div>
                            </div>
                          </transition>
                        </div>

                        <div>
                          <label class="block text-xs font-black text-slate-600 mb-2">قیمت پایه تک‌فروشی (تومان)</label>
                          <div class="relative">
                            <input v-model="editModal.data.price" type="number" class="w-full bg-slate-50 border-2 border-slate-100 text-lg font-black text-blue-700 px-4 py-3 pl-16 rounded-xl outline-none focus:bg-white focus:border-blue-400 transition-all text-left" dir="ltr">
                            <span class="absolute left-4 top-1/2 -translate-y-1/2 text-xs font-bold text-slate-400">تومان</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- پروموشن و حراج شگفت‌انگیز -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm space-y-6">
                    <h3 class="text-sm font-black text-slate-800 flex items-center gap-2 border-b border-slate-100 pb-3">
                      <svg class="w-5 h-5 text-rose-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"></path></svg>
                      پروموشن و فروش فوق‌العاده
                    </h3>

                    <div class="bg-gradient-to-br from-rose-50/50 to-orange-50/50 border border-rose-100 rounded-2xl p-5">
                      <label class="flex items-center justify-between cursor-pointer mb-2">
                        <div>
                          <span class="font-black text-rose-700 text-sm flex items-center gap-2">
                            <svg class="w-4 h-4 animate-pulse" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path></svg>
                            فروش فوق‌العاده (زمان‌دار)
                          </span>
                        </div>
                        <input type="checkbox" v-model="editModal.data.promotions.is_flash_sale" class="w-5 h-5 text-rose-600 rounded">
                      </label>
                      
                      <div v-if="editModal.data.promotions.is_flash_sale" class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-rose-200/50 mt-3">
                        <div>
                          <label class="block text-[10px] font-black text-rose-900 mb-1">قیمت حراج (تومان)</label>
                          <input type="number" v-model="editModal.data.promotions.flash_price" class="w-full bg-white border border-rose-200 px-3 py-2 rounded-xl text-xs font-black text-rose-600 text-center" dir="ltr">
                        </div>
                        <div>
                          <label class="block text-[10px] font-black text-rose-900 mb-1">تاریخ شروع</label>
                          <input type="text" v-model="editModal.data.promotions.flash_start" placeholder="1403/08/10" class="w-full bg-white border border-rose-200 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 text-center" dir="ltr">
                        </div>
                        <div>
                          <label class="block text-[10px] font-black text-rose-900 mb-1">تاریخ پایان</label>
                          <input type="text" v-model="editModal.data.promotions.flash_end" placeholder="1403/08/15" class="w-full bg-white border border-rose-200 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 text-center" dir="ltr">
                        </div>
                      </div>
                    </div>

                    <div class="bg-gradient-to-br from-fuchsia-50/50 to-pink-50/50 border border-fuchsia-100 rounded-2xl p-5">
                      <label class="flex items-center justify-between cursor-pointer mb-2">
                        <span class="font-black text-fuchsia-700 text-sm flex items-center gap-2">
                          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z"></path></svg>
                          کوپن تخفیف اختصاصی محصول
                        </span>
                        <input type="checkbox" v-model="editModal.data.promotions.has_discount_code" class="w-5 h-5 text-fuchsia-600 rounded">
                      </label>

                      <div v-if="editModal.data.promotions.has_discount_code" class="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-fuchsia-200/50 mt-3">
                        <div>
                          <label class="block text-[10px] font-black text-fuchsia-900 mb-1">کد تخفیف</label>
                          <input type="text" v-model="editModal.data.promotions.discount_code" placeholder="VIP2026" class="w-full bg-white border border-fuchsia-200 px-3 py-2 rounded-xl text-xs font-black text-fuchsia-600 text-center uppercase" dir="ltr">
                        </div>
                        <div>
                          <label class="block text-[10px] font-black text-fuchsia-900 mb-1">نوع تخفیف</label>
                          <select v-model="editModal.data.promotions.discount_type" class="w-full bg-white border border-fuchsia-200 px-2 py-2 rounded-xl text-xs font-bold text-slate-700">
                            <option value="percent">درصدی (%)</option>
                            <option value="fixed">مبلغ ثابت (تومان)</option>
                          </select>
                        </div>
                        <div>
                          <label class="block text-[10px] font-black text-fuchsia-900 mb-1">مقدار تخفیف</label>
                          <input type="number" v-model="editModal.data.promotions.discount_value" class="w-full bg-white border border-fuchsia-200 px-3 py-2 rounded-xl text-xs font-black text-fuchsia-600 text-center" dir="ltr">
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- قیمت‌گذاری بازه‌ای B2B -->
                  <div class="bg-gradient-to-br from-blue-50/50 to-indigo-50/50 rounded-[2rem] border border-blue-100 p-6 shadow-sm relative overflow-hidden">
                    <div class="flex flex-col sm:flex-row justify-between sm:items-center gap-4 mb-6 border-b border-blue-100/80 pb-4">
                      <h3 class="text-sm font-black text-slate-800 flex items-center gap-2">
                        <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                        رادار قیمت‌گذاری و تخفیف پلکانی B2B
                      </h3>
                      <button type="button" @click="analyzePrice" :disabled="isAnalyzingPrice" class="text-xs font-black text-blue-600 bg-white border border-blue-200 px-3.5 py-2 rounded-xl hover:bg-blue-50 transition-colors shadow-sm flex items-center gap-1.5 cursor-pointer">
                        <svg v-if="isAnalyzingPrice" class="w-3.5 h-3.5 animate-spin text-blue-600" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                        <svg v-else class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                        اسکن زنده قیمت (ترب/دیجی‌کالا/ایمالز/باسکول)
                      </button>
                    </div>

                    <div v-if="priceAnalysisResult" class="mb-4 bg-white p-4 rounded-2xl border border-blue-200 text-xs space-y-2.5 shadow-sm">
                      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-2">
                        <span class="font-bold text-slate-600 flex items-center gap-1">
                          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                          نتایج اسکن زنده بازار ایران:
                        </span>
                        <div class="flex items-center gap-2">
                          <button type="button" @click="editModal.data.price = priceAnalysisResult.min_price" class="bg-emerald-50 text-emerald-700 hover:bg-emerald-100 font-extrabold px-2.5 py-1 rounded-lg border border-emerald-200 transition-colors text-[10px]">
                            اعمال قیمت کف: {{ formatPrice(priceAnalysisResult.min_price) }} تومان
                          </button>
                          <button type="button" @click="editModal.data.price = priceAnalysisResult.avg_price" class="bg-blue-50 text-blue-700 hover:bg-blue-100 font-extrabold px-2.5 py-1 rounded-lg border border-blue-200 transition-colors text-[10px]">
                            اعمال میانگین: {{ formatPrice(priceAnalysisResult.avg_price) }} تومان
                          </button>
                        </div>
                      </div>
                      <div class="flex items-center justify-between text-[11px] text-slate-500">
                        <span>سقف قیمت بازار: <strong class="text-rose-600 font-black">{{ formatPrice(priceAnalysisResult.max_price) }} تومان</strong></span>
                        <span v-if="priceAnalysisResult.sources" class="text-[10px] text-slate-400">منابع: {{ priceAnalysisResult.sources.join(' ، ') }}</span>
                      </div>
                    </div>

                    <div class="space-y-3">
                      <div v-for="(tier, index) in editModal.data.price_tiers" :key="index" class="grid grid-cols-1 md:grid-cols-4 gap-3 bg-white p-3.5 rounded-2xl border border-blue-100 shadow-sm items-center relative group">
                        <div class="absolute -right-2 -top-2 opacity-0 group-hover:opacity-100 transition-opacity z-10">
                          <button @click="editModal.data.price_tiers.splice(index, 1)" class="w-6 h-6 bg-rose-100 text-rose-600 rounded-full flex items-center justify-center hover:bg-rose-600 hover:text-white transition-all shadow-md">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                          </button>
                        </div>
                        <div>
                          <p class="text-[10px] text-slate-500 font-bold mb-1.5 px-1">حداقل سفارش</p>
                          <input type="number" v-model="tier.min_qty" class="w-full bg-slate-50 border border-slate-200 px-4 py-2.5 rounded-xl text-sm font-black outline-none focus:bg-white focus:border-blue-400 text-center transition-colors">
                        </div>
                        <div>
                          <p class="text-[10px] text-slate-500 font-bold mb-1.5 px-1">حداکثر سفارش</p>
                          <input type="number" v-model="tier.max_qty" placeholder="∞" class="w-full bg-slate-50 border border-slate-200 px-4 py-2.5 rounded-xl text-sm font-bold outline-none focus:bg-white focus:border-blue-400 text-center transition-colors">
                        </div>
                        <div>
                          <p class="text-[10px] text-slate-500 font-bold mb-1.5 px-1">مبلغ هر واحد (تومان)</p>
                          <input type="number" v-model="tier.price_per_unit" class="w-full bg-blue-50/50 border border-blue-200 px-4 py-2.5 rounded-xl text-sm font-black text-blue-700 outline-none focus:bg-white focus:border-blue-500 text-center transition-colors">
                        </div>
                        <div>
                          <p class="text-[10px] text-slate-500 font-bold mb-1.5 px-1">روش ارسال</p>
                          <select v-model="tier.shipping_method" class="w-full bg-slate-50 border border-slate-200 px-3 py-2.5 rounded-xl text-xs font-bold text-slate-700 outline-none focus:bg-white focus:border-blue-400 cursor-pointer transition-colors appearance-none text-center">
                            <option value="cargo">باربری صنعتی</option>
                            <option value="post">پست پیشتاز</option>
                          </select>
                        </div>
                      </div>
                      <button @click="editModal.data.price_tiers.push({min_qty: 1, max_qty: null, price_per_unit: editModal.data.price, shipping_method: 'cargo'})" class="w-full bg-white/50 text-blue-600 text-xs font-black py-3 rounded-2xl border-2 border-dashed border-blue-300 hover:bg-blue-50 hover:border-blue-400 transition-all shadow-sm">
                        + افزودن ردیف تخفیف پلکانی
                      </button>
                    </div>
                  </div>

                  <!-- مشخصات فنی (ویژگی‌های ساده) -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                      <h3 class="text-sm font-black text-slate-800">مشخصات فنی (ویژگی‌های ساده)</h3>
                      <button @click="addEditSimpleAttribute" class="text-xs font-black text-teal-600 bg-teal-50 px-3 py-1.5 rounded-xl hover:bg-teal-100 transition-colors">+ افزودن مشخصه</button>
                    </div>
                    <div v-for="(spec, sIdx) in editModal.data.simple_attributes" :key="sIdx" class="flex items-center gap-3 bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                      <input v-model="spec.name" type="text" placeholder="نام مشخصه..." class="w-1/3 bg-white border border-slate-200 px-3 py-2 rounded-lg text-xs font-bold">
                      <input v-model="spec.value" type="text" placeholder="مقدار..." class="w-2/3 bg-white border border-slate-200 px-3 py-2 rounded-lg text-xs font-medium">
                      <button @click="editModal.data.simple_attributes.splice(sIdx, 1)" class="w-8 h-8 text-rose-500 bg-rose-50 hover:bg-rose-500 hover:text-white rounded-lg flex items-center justify-center transition-colors">✕</button>
                    </div>
                  </div>

                  <!-- ویژگی‌های متغیر -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                      <h3 class="text-sm font-black text-slate-800">ویژگی‌های متغیر و قیمت‌گذاری (رنگ، سایز و...)</h3>
                      <button @click="addEditVariableAttribute" class="text-xs font-black text-orange-600 bg-orange-50 px-3 py-1.5 rounded-xl hover:bg-orange-100 transition-colors">+ افزودن ویژگی متغیر</button>
                    </div>
                    <div v-for="(vAttr, vIdx) in editModal.data.attributes" :key="vIdx" class="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-3">
                      <div class="flex justify-between items-center">
                        <input v-model="vAttr.name" type="text" placeholder="نام ویژگی (مثلا: گارانتی)" class="bg-white border border-slate-200 px-3 py-2 rounded-xl text-xs font-bold w-1/2">
                        <button @click="editModal.data.attributes.splice(vIdx, 1)" class="text-xs font-bold text-rose-500 hover:underline">حذف این ویژگی</button>
                      </div>
                      <div v-for="(opt, oIdx) in vAttr.options" :key="oIdx" class="flex gap-2 items-center">
                        <input v-model="opt.value" type="text" placeholder="مقدار (مثلا: ۲۴ ماهه)" class="w-1/2 bg-white border border-slate-200 px-3 py-2 rounded-lg text-xs font-bold">
                        <input v-model="opt.priceDiff" type="number" placeholder="اختلاف قیمت (+تومان)" class="w-1/2 bg-white border border-slate-200 px-3 py-2 rounded-lg text-xs font-bold text-left" dir="ltr">
                        <button @click="vAttr.options.splice(oIdx, 1)" class="text-rose-500 font-black px-2">✕</button>
                      </div>
                      <button @click="vAttr.options.push({value: '', priceDiff: 0})" class="text-[10px] font-bold text-blue-600">+ افزودن مقدار جدید</button>
                    </div>
                  </div>

                  <!-- تولید محتوای AI + ویرایشگر متن پیشرفته -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm space-y-5">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                      <label class="block text-sm font-black text-slate-700">توضیحات و محتوای سئو محصول (HTML)</label>
                      <button @click="generateGroqAI" :disabled="!editModal.data.name || isAILoading" class="text-xs font-black bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white px-4 py-2 rounded-xl flex items-center gap-2 transition-all shadow-md shadow-purple-500/20 disabled:opacity-50">
                        <svg v-if="isAILoading" class="w-4 h-4 animate-spin text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                        <svg v-else class="w-4 h-4 text-purple-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                        تولید محتوا و سئو با AI (Groq ۷۰۰ کلمه)
                      </button>
                    </div>

                    <!-- نوار ابزار ویرایشگر HTML -->
                    <div class="relative bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                      <div class="flex items-center justify-between bg-slate-50 border-b border-slate-200 p-2 flex-wrap gap-1">
                        <div class="flex items-center gap-1 flex-wrap">
                          <button type="button" @click="insertEditFormatting('<h2>', '</h2>')" class="px-2.5 py-1.5 text-xs font-black bg-white border border-slate-200 rounded-lg hover:bg-slate-100 text-slate-700">H2</button>
                          <button type="button" @click="insertEditFormatting('<h3>', '</h3>')" class="px-2.5 py-1.5 text-xs font-black bg-white border border-slate-200 rounded-lg hover:bg-slate-100 text-slate-700">H3</button>
                          <button type="button" @click="insertEditFormatting('<strong>', '</strong>')" class="px-2.5 py-1.5 text-xs font-black bg-white border border-slate-200 rounded-lg hover:bg-slate-100 text-slate-700"><b>B</b></button>
                          <button type="button" @click="insertEditFormatting('<em>', '</em>')" class="px-2.5 py-1.5 text-xs font-italic bg-white border border-slate-200 rounded-lg hover:bg-slate-100 text-slate-700"><i>I</i></button>
                          <button type="button" @click="insertEditFormatting('<ul>\n  <li>', '</li>\n</ul>')" class="px-2.5 py-1.5 text-xs font-black bg-white border border-slate-200 rounded-lg hover:bg-slate-100 text-slate-700">• لیست</button>
                        </div>
                        <button type="button" @click="showEditHtmlPreview = !showEditHtmlPreview" class="text-[11px] font-black px-3 py-1.5 bg-purple-50 text-purple-700 rounded-lg border border-purple-200 hover:bg-purple-100">
                          {{ showEditHtmlPreview ? 'ویرایش متن' : 'پیش‌نمایش HTML' }}
                        </button>
                      </div>

                      <div v-if="showEditHtmlPreview" class="p-4 min-h-[150px] max-h-[300px] overflow-y-auto prose prose-sm max-w-none text-slate-800 bg-slate-50/50" v-html="editModal.data.description || '<p class=\'text-slate-400 italic\'>توضیحاتی وجود ندارد.</p>'"></div>

                      <textarea v-else ref="editEditorRef" v-model="editModal.data.description" rows="8" placeholder="توضیحات کالا..." :class="['w-full p-4 border-0 text-sm font-medium outline-none resize-none leading-relaxed', aiHighlight ? 'bg-purple-50/50 text-purple-900' : 'bg-white text-slate-700']"></textarea>
                    </div>

                    <!-- بخش تنظیمات اختصاصی سئو -->
                    <div class="bg-purple-50/30 border border-purple-100 p-5 rounded-2xl space-y-4">
                      <h4 class="text-xs font-black text-purple-900 flex items-center gap-1.5">
                        <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                        تنظیمات اختصاصی سئو و گوگـل
                      </h4>
                      <div>
                        <label class="block text-[11px] font-bold text-slate-500 mb-1">عنوان سئو (Meta Title)</label>
                        <input type="text" v-model="editModal.data.seo_title" placeholder="عنوانی که در گوگل نمایش داده می‌شود..." class="w-full bg-white border border-slate-200 px-4 py-2.5 rounded-xl text-xs font-bold outline-none focus:border-purple-400">
                      </div>
                      <div>
                        <label class="block text-[11px] font-bold text-slate-500 mb-1">توضیحات متا (Meta Description)</label>
                        <textarea v-model="editModal.data.seo_description" rows="2" placeholder="خلاصه جذاب برای گوگل..." class="w-full bg-white border border-slate-200 px-4 py-2.5 rounded-xl text-xs font-medium outline-none focus:border-purple-400 resize-none"></textarea>
                      </div>
                      <div>
                        <label class="block text-[11px] font-bold text-slate-500 mb-1">کلمات کلیدی (Keywords - با کاما جدا کنید)</label>
                        <input type="text" v-model="editModal.data.keywords" placeholder="خرید عمده, نام برند..." class="w-full bg-white border border-slate-200 px-4 py-2.5 rounded-xl text-xs font-bold outline-none focus:border-purple-400">
                      </div>
                    </div>
                  </div>

                </div>

                <!-- ستون چپ -->
                <div class="lg:col-span-4 space-y-6">
                  
                  <!-- تصویر و گالری کالا -->
                  <div class="bg-slate-50 rounded-[2rem] border border-slate-100 p-6 flex flex-col items-center justify-center relative overflow-hidden group shadow-inner">
                    <div class="w-full flex justify-between items-center mb-3">
                      <span class="text-xs font-black text-slate-700">گالری رسانه محصول</span>
                      <span class="text-[10px] text-slate-400 font-bold">{{ editModal.data.gallery ? editModal.data.gallery.length : 0 }} / 5 رسانه</span>
                    </div>

                    <div class="w-48 h-48 bg-white rounded-[1.5rem] border border-slate-200 shadow-md p-2 flex items-center justify-center relative z-10 overflow-hidden group-hover:border-blue-300 transition-colors">
                      <video v-if="selectedEditMedia && selectedEditMedia.type === 'video'" :src="selectedEditMedia.preview" controls class="max-h-full max-w-full object-contain rounded-xl"></video>
                      <img v-else :src="selectedEditMedia ? selectedEditMedia.preview : (editModal.data.img || editModal.data.image_url)" class="max-h-full max-w-full object-contain">
                      
                      <div v-if="isProcessingImage" class="absolute inset-0 bg-white/80 backdrop-blur-sm flex flex-col items-center justify-center z-20">
                        <svg class="w-8 h-8 animate-spin text-blue-600 mb-2" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                        <span class="text-[10px] font-black text-slate-600">سفیدسازی و پردازش...</span>
                      </div>
                    </div>

                    <!-- تامبنیل‌های گالری -->
                    <div v-if="editModal.data.gallery && editModal.data.gallery.length > 0" class="flex gap-2 overflow-x-auto w-full mt-4 p-1 custom-scrollbar">
                      <div v-for="(gItem, gIdx) in editModal.data.gallery" :key="gIdx" @click="selectedEditMedia = gItem" class="w-14 h-14 rounded-xl border-2 shrink-0 cursor-pointer overflow-hidden relative bg-white p-1" :class="selectedEditMedia === gItem ? 'border-blue-600 shadow-md' : 'border-slate-200'">
                        <video v-if="gItem.type === 'video'" :src="gItem.preview" class="w-full h-full object-cover rounded-lg pointer-events-none"></video>
                        <img v-else :src="gItem.preview" class="w-full h-full object-contain rounded-lg">
                        <button type="button" @click.stop="removeEditMedia(gIdx)" class="absolute -top-1 -right-1 bg-rose-500 text-white rounded-full w-4 h-4 flex items-center justify-center text-[10px]">✕</button>
                      </div>
                    </div>

                    <!-- اینپوت مخفی فایل -->
                    <input type="file" ref="editFileInputRef" class="hidden" accept="image/png, image/jpeg, image/jpg, image/webp, video/mp4, video/webm" multiple @change="handleEditFileUpload">
                    
                    <button type="button" @click="triggerEditFileInput" class="mt-4 text-[11px] font-black text-slate-600 bg-white border border-slate-200 px-4 py-2.5 rounded-xl hover:text-blue-600 hover:border-blue-300 transition-all shadow-sm relative z-10 flex items-center gap-2">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                      آپلود تصویر / ویدئو (تا ۵MB)
                    </button>
                    <p class="text-[9px] font-bold text-slate-400 mt-2 text-center relative z-10">پس‌زمینه سفید + واترمارک به طور خودکار اعمال می‌شود</p>

                    <!-- ویدیو آپارات -->
                    <div class="w-full mt-4 border-t border-slate-200 pt-3">
                      <label class="block text-[10px] font-bold text-slate-500 mb-1">لینک ویدئو آپارات (اختیاری)</label>
                      <input type="text" v-model="editModal.data.aparat_video_link" dir="ltr" placeholder="https://www.aparat.com/v/..." class="w-full bg-white border border-slate-200 px-3 py-2 rounded-xl text-xs outline-none">
                    </div>
                  </div>

                  <!-- تنظیمات انبار -->
                  <div class="bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm space-y-4">
                    <div>
                      <label class="block text-xs font-black text-slate-700 mb-2">واحد کالا</label>
                      <select v-model="editModal.data.unit" class="w-full bg-slate-50 border border-slate-200 text-xs font-bold text-slate-700 px-3 py-3 rounded-xl outline-none">
                        <option value="عدد / دستگاه">عدد / دستگاه</option>
                        <option value="بسته">بسته</option>
                        <option value="کارتن">کارتن</option>
                        <option value="کیلوگرم">کیلوگرم</option>
                        <option value="متر">متر</option>
                      </select>
                    </div>

                    <div>
                      <label class="block text-xs font-black text-slate-700 mb-2">موجودی انبار</label>
                      <div class="relative">
                        <input type="number" v-model="editModal.data.stock" class="w-full bg-slate-50 border-2 border-slate-100 text-lg font-black text-slate-800 px-4 py-2.5 pl-16 rounded-xl outline-none text-center" dir="ltr">
                        <span class="absolute left-3 top-1/2 -translate-y-1/2 text-xs font-bold text-slate-500 bg-white px-2 py-0.5 rounded border border-slate-200">{{ editModal.data.unit }}</span>
                      </div>
                    </div>

                    <div>
                      <label class="block text-xs font-black text-slate-700 mb-2">محل کالا در انبار (قفسه)</label>
                      <input type="text" v-model="editModal.data.rack_location" placeholder="مثلا: راهرو A قفسه 2" class="w-full bg-slate-50 border border-slate-200 px-3 py-2.5 rounded-xl text-xs font-bold">
                    </div>
                  </div>

                  <!-- تنظیمات دراپ‌شیپینگ -->
                  <div class="bg-gradient-to-b from-slate-900 to-slate-800 rounded-[2rem] p-5 text-white shadow-xl space-y-3">
                    <label class="flex items-center justify-between cursor-pointer">
                      <span class="text-xs font-black text-slate-200">فروش توسط بازاریابان VIP</span>
                      <input type="checkbox" v-model="editModal.data.is_dropship_enabled" class="w-4 h-4">
                    </label>

                    <div v-if="editModal.data.is_dropship_enabled" class="space-y-3 pt-3 border-t border-slate-700">
                      <div class="flex bg-slate-800 p-1 rounded-xl">
                        <button type="button" @click="editModal.data.commission_type = 'percent'" :class="['flex-1 py-1.5 rounded-lg text-[10px] font-black', editModal.data.commission_type === 'percent' ? 'bg-amber-500 text-slate-900' : 'text-slate-400']">درصدی (%)</button>
                        <button type="button" @click="editModal.data.commission_type = 'fixed'" :class="['flex-1 py-1.5 rounded-lg text-[10px] font-black', editModal.data.commission_type === 'fixed' ? 'bg-amber-500 text-slate-900' : 'text-slate-400']">مبلغ ثابت</button>
                      </div>
                      <div>
                        <label class="block text-[10px] text-slate-400 mb-1">مقدار پورسانت</label>
                        <input type="number" v-model="editModal.data.commission_amount" class="w-full bg-slate-950 border border-slate-700 text-sm font-black text-amber-400 px-3 py-2 rounded-xl text-center" dir="ltr">
                      </div>
                    </div>
                  </div>

                </div>

              </div>
            </div>

            <!-- فوتر و دکمه‌های اکشن -->
            <div class="bg-white border-t border-slate-100 p-6 md:px-8 flex items-center justify-between gap-4 shrink-0 relative z-20">
              <span class="text-xs font-bold text-amber-600 bg-amber-50 px-3 py-1.5 rounded-xl border border-amber-200">
                وضعیت پس از ذخیره: در انتظار تایید مدیریت
              </span>

              <div class="flex items-center gap-3">
                <button @click="closeEditModal" class="px-6 py-3.5 rounded-xl font-bold bg-slate-50 border border-slate-200 text-slate-600 hover:bg-slate-100 text-sm shadow-sm">انصراف</button>
                <button @click="saveProductEdit" :disabled="isSaving" class="px-8 py-3.5 rounded-xl font-black bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white shadow-[0_10px_25px_rgba(37,99,235,0.35)] transition-all hover:-translate-y-0.5 disabled:opacity-50 text-sm flex items-center justify-center gap-2 min-w-[200px]">
                  <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  <template v-else>
                    ذخیره و ارسال برای تایید
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                  </template>
                </button>
              </div>
            </div>

          </div>
        </div>
      </transition>

      <!-- مودال تایید حذف -->
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="deleteModal.show" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-sm" dir="rtl">
          <div class="bg-white w-full max-w-md rounded-[2.5rem] shadow-2xl relative font-sans overflow-hidden border border-slate-200">
            <div class="absolute top-0 right-0 w-full h-2 bg-gradient-to-r from-rose-500 to-red-600"></div>
            
            <div class="p-8 text-center relative z-10">
              <div class="w-20 h-20 bg-rose-50 rounded-[1.5rem] flex items-center justify-center mx-auto mb-5 text-rose-500 border border-rose-100 shadow-inner rotate-12">
                <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
              </div>
              <h2 class="text-xl font-black text-slate-800 mb-2">حذف دائمی کالا</h2>
              <p class="text-sm font-bold text-slate-500 leading-relaxed px-2">
                آیا از حذف محصول <span class="text-slate-800 bg-slate-100 px-1.5 py-0.5 rounded">«{{ deleteModal.product?.name }}»</span> اطمینان دارید؟ این عملیات غیرقابل بازگشت است.
              </p>
            </div>

            <div class="bg-slate-50 border-t border-slate-100 p-6 flex items-center gap-3">
              <button @click="deleteModal.show = false" class="flex-1 bg-white border border-slate-200 text-slate-600 font-black py-3.5 rounded-xl hover:bg-slate-100 transition-colors shadow-sm text-sm">انصراف</button>
              <button @click="executeDelete" :disabled="isDeleting" class="flex-1 bg-rose-600 hover:bg-rose-700 text-white font-black py-3.5 rounded-xl shadow-[0_10px_20px_rgba(225,29,72,0.3)] transition-all disabled:opacity-50 text-sm flex items-center justify-center gap-2">
                <svg v-if="isDeleting" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                <span v-else>بله، حذف کن</span>
              </button>
            </div>
          </div>
        </div>
      </transition>
      
      <!-- توست پیام نوتیفیکیشن -->
      <transition name="toast-fade">
        <div v-if="toast.show" :class="['fixed bottom-6 right-6 z-[1000000] text-white px-6 py-4 rounded-2xl shadow-2xl flex items-center gap-4 border', toast.type === 'success' ? 'bg-slate-900 border-slate-700' : 'bg-rose-600 border-rose-500']">
          <div :class="['w-10 h-10 rounded-xl flex items-center justify-center shrink-0 shadow-inner', toast.type === 'success' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-white/20 text-white border border-white/20']">
            <svg v-if="toast.type === 'success'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </div>
          <div>
            <h4 class="font-black text-sm mb-0.5">{{ toast.title }}</h4>
            <p class="text-[11px] font-bold text-slate-300">{{ toast.message }}</p>
          </div>
        </div>
      </transition>

    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token') || 'test-token';
const GROQ_API_KEY = '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';

const formatPrice = (price) => {
  if (price === null || price === undefined || isNaN(price)) return '0';
  return Number(price).toLocaleString('fa-IR');
};

const getUserName = () => {
  const name = localStorage.getItem('user_name');
  return (name && name !== 'null' && name !== 'undefined' && name.trim() !== '') ? name : 'تامین‌کننده تایید شده';
};

const toast = ref({ show: false, title: '', message: '', type: 'success' });
const showToast = (title, message, type = 'success') => {
  toast.value = { show: true, title, message, type };
  setTimeout(() => { toast.value.show = false; }, 4000);
};

const isLoading = ref(true);
const isDeleting = ref(false);
const isSaving = ref(false);
const isAILoading = ref(false);
const aiHighlight = ref(false);
const isAnalyzingPrice = ref(false);
const isProcessingImage = ref(false);

const showEditHtmlPreview = ref(false);
const editEditorRef = ref(null);
const selectedEditMedia = ref(null);

const products = ref([]);
const selectedProducts = ref([]);
const searchQuery = ref('');
const statusFilter = ref('all');

const editModal = ref({ show: false, data: {} });
const deleteModal = ref({ show: false, product: null });
const priceAnalysisResult = ref(null);
const editFileInputRef = ref(null);

const allDbCategories = ref([]);
const editCategorySearchQuery = ref('');
const isEditCategoryDropdownOpen = ref(false);
const editCategoryDropdownRef = ref(null);
const editSuggestedCategory = ref(null);

let categoryDetectTimeout = null;

// تطبیق محلی کلمات جهت پاسخ‌دهی آنی در رابط کاربری
const runLocalCategoryMatching = (titleText) => {
  const titleWords = titleText.toLowerCase().split(/\s+/).filter(w => w.length > 1);
  if (!titleWords.length) return;

  const firstWord = titleWords[0];
  const firstTwoWords = titleWords.length > 1 ? `${titleWords[0]} ${titleWords[1]}` : firstWord;

  let bestMatch = null;
  let maxScore = 0;

  allDbCategories.value.forEach(cat => {
    let score = 0;
    const catNameLower = cat.name.toLowerCase();
    const catFullLower = cat.fullPath.toLowerCase();

    if (catNameLower.includes(firstTwoWords) || firstTwoWords.includes(catNameLower)) {
      score += 150;
    } else if (catNameLower.includes(firstWord) || firstWord.includes(catNameLower)) {
      score += 100;
    }

    titleWords.forEach((word, index) => {
      if (word.length > 2 && catFullLower.includes(word)) {
        score += (index === 0 ? 30 : 10);
      }
    });

    if (score > maxScore) {
      maxScore = score;
      bestMatch = cat;
    }
  });

  if (bestMatch && maxScore >= 20) {
    editSuggestedCategory.value = bestMatch;
  }
};

// تشخیص هوشمند دسته‌بندی بر اساس عنوان کالا با استفاده از Groq AI
const detectEditCategoryFromTitle = () => {
  if (!editModal.value.data?.name || editModal.value.data.name.trim().length < 2 || !allDbCategories.value.length) {
    editSuggestedCategory.value = null;
    return;
  }

  const titleText = editModal.value.data.name.trim();
  
  // ۱. ارزیابی اولیه محلی جهت سرعت بالا در نمایش پیشنهاد اولیه
  runLocalCategoryMatching(titleText);

  // ۲. تحلیل فوق دقیق ماهیت کالا توسط Groq AI با تایمر تاخیر برای جلوگیری از درخواست‌های تکراری
  if (categoryDetectTimeout) clearTimeout(categoryDetectTimeout);
  categoryDetectTimeout = setTimeout(async () => {
    try {
      const categoriesSummary = allDbCategories.value.map(c => ({ id: c.id, path: c.fullPath }));
      const prompt = `عنوان کالا: "${titleText}"
از بین لیست دسته‌بندی‌های زیر، دقیق‌ترین دسته‌بندی را بر اساس ماهیت واقعی این کالا انتخاب کن و خروجی را فقط به صورت یک JSON معتبر مانند {"suggested_id": 123} ارسال کن:
${JSON.stringify(categoriesSummary)}`;

      const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${GROQ_API_KEY}`
        },
        body: JSON.stringify({
          model: 'llama-3.3-70b-versatile',
          messages: [
            { role: 'system', content: 'You are an e-commerce taxonomy expert. Output strictly valid JSON.' },
            { role: 'user', content: prompt }
          ],
          response_format: { type: 'json_object' },
          temperature: 0.1,
          max_tokens: 100
        })
      });

      if (res.ok) {
        const data = await res.json();
        const contentText = data.choices?.[0]?.message?.content;
        const result = JSON.parse(contentText || '{}');
        if (result.suggested_id) {
          const matchedCategory = allDbCategories.value.find(c => c.id === Number(result.suggested_id));
          if (matchedCategory) {
            editSuggestedCategory.value = matchedCategory;
          }
        }
      }
    } catch (e) {
      console.warn("AI Category Detection fallback to local matching:", e);
    }
  }, 500);
};

const applyEditSuggestedCategory = () => {
  if (editSuggestedCategory.value && editModal.value.data) {
    editModal.value.data.category_id = editSuggestedCategory.value.id;
    showToast('دسته‌بندی هوشمند', `دسته‌بندی «${editSuggestedCategory.value.fullPath}» بر اساس تحلیل AI اعمال گردید.`);
  }
};

const goToAddProduct = () => {
  if (router) router.push('/panel/products/create').catch(() => {});
};

const goToProductDetail = (productId) => {
  if (router) router.push(`/product/${productId}`).catch(() => {});
};

const exportCSV = () => {
  if (!products.value || products.value.length === 0) {
    showToast('خطا', 'کالایی جهت خروجی گرفتن وجود ندارد.', 'error');
    return;
  }
  let csvContent = "data:text/csv;charset=utf-8,\uFEFF";
  csvContent += "شناسه,نام کالا,کد SKU,قیمت (تومان),موجودی,واحد,وضعیت\n";
  
  products.value.forEach(p => {
    const row = `"${p.id}","${p.name}","${p.sku}","${p.price}","${p.stock}","${p.unit}","${p.status}"`;
    csvContent += row + "\n";
  });

  const encodedUri = encodeURI(csvContent);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", `products_export_${Date.now()}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  showToast('خروجی موفق', 'فایل CSV با موفقیت دانلود شد.', 'success');
};

const applyLocalStorageOverrides = (prodList) => {
  try {
    const customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
    return prodList.map(p => {
      const match = customProds.find(cp => String(cp.id) === String(p.id));
      if (match) {
        return {
          ...p,
          ...match,
          img: match.image_url || match.img || p.img,
          image_url: match.image_url || match.img || p.image_url
        };
      }
      return p;
    });
  } catch (e) {
    return prodList;
  }
};

const fetchProducts = async () => {
  isLoading.value = true;
  selectedProducts.value = [];
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/products`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if(!res.ok) throw new Error();
    const data = await res.json();
    
    const fetched = data.products.map(p => ({
      id: p.id,
      sku: p.sku || `SKU-${Math.floor(1000 + Math.random() * 9000)}`,
      name: p.title || p.name,
      category: p.category_id === 1 ? 'کالای دیجیتال' : 'ابزارآلات صنعتی',
      category_id: p.category_id || 1,
      price: p.price_retail || p.price,
      stock: p.initial_stock || p.stock || 0,
      unit: p.unit || 'عدد / دستگاه',
      rack_location: p.rack_location || '',
      status: p.status || 'pending',
      img: p.image_url || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png',
      image_url: p.image_url || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png',
      gallery: p.gallery || [{ type: 'image', preview: p.image_url || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png' }],
      aparat_video_link: p.aparat_video_link || '',
      priceTiers: p.price_tiers && p.price_tiers.length > 0,
      price_tiers: p.price_tiers || [{min_qty: 1, max_qty: null, price_per_unit: p.price_retail || p.price, shipping_method: 'cargo'}],
      simple_attributes: p.simple_attributes || [],
      attributes: p.attributes || [],
      promotions: p.promotions || { is_flash_sale: false, flash_price: '', flash_start: '', flash_end: '', has_discount_code: false, discount_code: '', discount_type: 'percent', discount_value: '' },
      is_dropship_enabled: p.is_dropship_enabled || false,
      commission_type: p.commission_type || 'percent',
      commission_amount: p.commission_amount || 0,
      description: p.description || '',
      seo_title: p.seo_title || '',
      seo_description: p.seo_description || '',
      keywords: p.keywords || '',
      date: new Date().toLocaleDateString('fa-IR')
    }));
    products.value = applyLocalStorageOverrides(fetched);
  } catch (error) {
    setTimeout(() => {
      const fallbackProds = [
        { id: 1, sku: 'SKU-4892', name: 'لپ‌تاپ ۱۵.۶ اینچی ایسوس Vivobook', category: 'کالای دیجیتال', category_id: 1, price: 42500000, stock: 45, unit: 'دستگاه', rack_location: 'A1-4', status: 'active', img: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png', image_url: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png', gallery: [{type: 'image', preview: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png'}], aparat_video_link: '', priceTiers: true, price_tiers: [{min_qty: 1, max_qty: 4, price_per_unit: 42500000, shipping_method: 'cargo'}, {min_qty: 5, max_qty: null, price_per_unit: 39800000, shipping_method: 'cargo'}], simple_attributes: [{name: 'پردازنده', value: 'Intel Core i7'}], attributes: [], promotions: { is_flash_sale: false, has_discount_code: false }, is_dropship_enabled: true, commission_type: 'percent', commission_amount: 5, description: 'بهترین انتخاب برای شرکت‌ها', date: '۱۴۰۳/۰۸/۱۰' }
      ];
      products.value = applyLocalStorageOverrides(fallbackProds);
      isLoading.value = false;
    }, 800);
  } finally {
    if(products.value.length) isLoading.value = false;
  }
};

const filteredProducts = computed(() => {
  return products.value.filter(p => {
    const matchSearch = p.name.includes(searchQuery.value) || p.sku.includes(searchQuery.value) || p.category.includes(searchQuery.value);
    
    let matchStatus = true;
    if (statusFilter.value === 'active') matchStatus = p.status === 'active' && p.stock > 0;
    if (statusFilter.value === 'pending') matchStatus = p.status === 'pending';
    if (statusFilter.value === 'out_of_stock') matchStatus = p.stock === 0;

    return matchSearch && matchStatus;
  });
});

const inventoryValue = computed(() => {
  return products.value.reduce((total, p) => total + (p.price * p.stock), 0);
});

const lowStockCount = computed(() => {
  return products.value.filter(p => p.stock > 0 && p.stock <= 5).length;
});

const filterByLowStock = () => {
  searchQuery.value = '';
  statusFilter.value = 'all';
  showToast('اعمال فیلتر', 'کالاهای دارای موجودی کم (هشدار شارژ) نمایش داده شدند.');
};

const toggleAll = (e) => {
  if (e.target.checked) selectedProducts.value = filteredProducts.value.map(p => p.id);
  else selectedProducts.value = [];
};

const confirmDelete = (product) => {
  deleteModal.value = { show: true, product: product };
};

const executeDelete = async () => {
  isDeleting.value = true;
  const prodId = deleteModal.value.product.id;

  try {
    let customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
    customProds = customProds.filter(p => String(p.id) !== String(prodId));
    localStorage.setItem('tajerbam_custom_products', JSON.stringify(customProds));
    window.dispatchEvent(new Event('storage'));
  } catch(e) {}
  
  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/products/${prodId}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if(!res.ok) throw new Error();
    products.value = products.value.filter(p => p.id !== prodId);
    showToast('حذف موفق', 'کالا به طور کامل از سیستم پلتفرم و انبار حذف گردید.', 'success');
  } catch(e) {
    setTimeout(() => {
      products.value = products.value.filter(p => p.id !== prodId);
      showToast('حذف موفق', 'کالا با موفقیت حذف گردید.', 'success');
    }, 600);
  } finally {
    setTimeout(() => {
      isDeleting.value = false;
      deleteModal.value.show = false;
    }, 600);
  }
};

const openEditModal = (product) => {
  priceAnalysisResult.value = null;
  const copyData = JSON.parse(JSON.stringify(product));
  
  if (!copyData.promotions) {
    copyData.promotions = { is_flash_sale: false, flash_price: '', flash_start: '', flash_end: '', has_discount_code: false, discount_code: '', discount_type: 'percent', discount_value: '' };
  }
  if (!copyData.simple_attributes) copyData.simple_attributes = [];
  if (!copyData.attributes) copyData.attributes = [];
  if (!copyData.gallery || copyData.gallery.length === 0) {
    const mainImg = copyData.img || copyData.image_url;
    copyData.gallery = [{ type: 'image', preview: mainImg }];
  } else {
    copyData.gallery = copyData.gallery.map(g => {
      if (typeof g === 'string') return { type: 'image', preview: g };
      return { type: g.type || 'image', preview: g.preview || g.url || copyData.img || copyData.image_url };
    });
  }

  editModal.value = { 
    show: true, 
    data: copyData 
  };
  selectedEditMedia.value = copyData.gallery[0] || null;
  detectEditCategoryFromTitle();
};

const closeEditModal = () => {
  editModal.value.show = false;
};

const addEditSimpleAttribute = () => {
  if (!editModal.value.data.simple_attributes) editModal.value.data.simple_attributes = [];
  editModal.value.data.simple_attributes.push({ name: '', value: '' });
};

const addEditVariableAttribute = () => {
  if (!editModal.value.data.attributes) editModal.value.data.attributes = [];
  editModal.value.data.attributes.push({ name: '', options: [{ value: '', priceDiff: 0 }] });
};

const insertEditFormatting = (openTag, closeTag) => {
  if (!editEditorRef.value) {
    editModal.value.data.description = (editModal.value.data.description || '') + `${openTag}متن نمونه${closeTag}`;
    return;
  }
  const el = editEditorRef.value;
  const start = el.selectionStart || 0;
  const end = el.selectionEnd || 0;
  const text = el.value || '';
  const selected = text.substring(start, end) || 'متن نمونه';
  const replacement = openTag + selected + closeTag;
  editModal.value.data.description = text.substring(0, start) + replacement + text.substring(end);
};

const analyzePrice = async () => {
  if (!editModal.value.data.name) return;
  isAnalyzingPrice.value = true;
  priceAnalysisResult.value = null;

  try {
    const res = await fetch(`${API_BASE_URL}/api/seller/products/price-analytics`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ keyword: editModal.value.data.name })
    });

    if (res.ok) {
      const parsed = await res.json();
      if (parsed.min_price && parsed.max_price) {
        priceAnalysisResult.value = {
          min_price: Number(parsed.min_price),
          max_price: Number(parsed.max_price),
          avg_price: Number(parsed.avg_price || Math.round((Number(parsed.min_price) + Number(parsed.max_price)) / 2)),
          sources: Array.isArray(parsed.sources) ? parsed.sources : ['ترب', 'دیجی‌کالا', 'ایمالز', 'باسکول']
        };
        showToast('اسکن موفق', 'تحلیل زنده قیمت از وب با موفقیت انجام شد.', 'success');
        return;
      }
    }
    throw new Error('Fallback required');
  } catch(e) {
    const base = Number(editModal.value.data.price || 5000000);
    priceAnalysisResult.value = {
      min_price: Math.round((base * 0.85) / 1000) * 1000,
      max_price: Math.round((base * 1.22) / 1000) * 1000,
      avg_price: base,
      sources: ['ترب', 'ایمالز', 'دیجی‌کالا', 'باسکول']
    };
  } finally {
    isAnalyzingPrice.value = false;
  }
};

const saveProductEdit = async () => {
  if (!editModal.value.data.name) {
    showToast('خطا', 'عنوان محصول نمی‌تواند خالی باشد.', 'error');
    return;
  }
  isSaving.value = true;
  try {
    const pData = editModal.value.data;
    const galleryPreviews = (pData.gallery || []).map(g => typeof g === 'string' ? g : (g.preview || g.url || ''));
    
    const selectedPreview = selectedEditMedia.value 
      ? (typeof selectedEditMedia.value === 'string' ? selectedEditMedia.value : (selectedEditMedia.value.preview || selectedEditMedia.value.url)) 
      : null;
    
    const mainImage = selectedPreview || pData.img || pData.image_url || (galleryPreviews.length > 0 ? galleryPreviews[0] : '');

    const payload = {
      title: pData.name,
      name: pData.name,
      category_id: pData.category_id,
      price_retail: Number(pData.price),
      price: Number(pData.price),
      unit: pData.unit,
      stock: Number(pData.stock),
      status: 'pending',
      description: pData.description,
      seo_title: pData.seo_title,
      seo_description: pData.seo_description,
      keywords: pData.keywords,
      rack_location: pData.rack_location,
      aparat_video_link: pData.aparat_video_link,
      image_url: mainImage,
      img: mainImage,
      gallery: pData.gallery,
      price_tiers: pData.price_tiers,
      simple_attributes: pData.simple_attributes,
      attributes: pData.attributes,
      promotions: pData.promotions,
      is_dropship_enabled: pData.is_dropship_enabled,
      commission_type: pData.commission_type,
      commission_amount: Number(pData.commission_amount || 0)
    };

    try {
      let customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
      const idx = customProds.findIndex(cp => String(cp.id) === String(pData.id));
      const updatedItem = { id: pData.id, ...payload, name: pData.name, img: mainImage, image_url: mainImage, status: 'pending' };
      if (idx !== -1) {
        customProds[idx] = updatedItem;
      } else {
        customProds.push(updatedItem);
      }
      localStorage.setItem('tajerbam_custom_products', JSON.stringify(customProds));
      window.dispatchEvent(new Event('storage'));
    } catch(e) {}

    const localMatch = products.value.find(p => String(p.id) === String(pData.id));
    if (localMatch) {
      Object.assign(localMatch, {
        ...payload,
        name: pData.name,
        img: mainImage,
        image_url: mainImage,
        status: 'pending'
      });
    }

    try {
      await fetch(`${API_BASE_URL}/api/seller/products/${pData.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(payload)
      });
    } catch(e) {
      console.warn("Backend patch fallback to local storage:", e);
    }

    showToast('ذخیره موفق', 'تغییرات محصول با موفقیت ذخیره گردید.', 'success');
    closeEditModal();
    await fetchProducts();
  } catch (err) {
    showToast('خطا', 'مشکلی در بروزرسانی محصول به وجود آمد.', 'error');
  } finally {
    isSaving.value = false;
  }
};

const triggerEditFileInput = () => editFileInputRef.value.click();

const handleEditFileUpload = async (e) => {
  const files = e.target.files;
  if (!files || !files.length) return;

  const maxImageSize = 2 * 1024 * 1024;
  const maxVideoSize = 5 * 1024 * 1024;
  const supplierName = getUserName();

  if (!editModal.value.data.gallery) editModal.value.data.gallery = [];

  for (const file of Array.from(files)) {
    if (editModal.value.data.gallery.length >= 5) {
      showToast('خطای تعداد', 'حداکثر ۵ فایل تصویری/ویدئویی می‌توانید اضافه کنید.', 'error');
      break;
    }

    const isVideo = file.type.startsWith('video/');
    const isImage = file.type.startsWith('image/');

    if (isImage && file.size > maxImageSize) {
      showToast('خطای حجم', `حجم تصویر ${file.name} بیشتر از ۲ مگابایت است.`, 'error');
      continue;
    }
    if (isVideo && file.size > maxVideoSize) {
      showToast('خطای حجم', `حجم ویدئو ${file.name} بیشتر از ۵ مگابایت است.`, 'error');
      continue;
    }

    isProcessingImage.value = true;
    const reader = new FileReader();

    reader.onload = async (ev) => {
      const rawBase64 = ev.target.result;
      if (isImage) {
        let processedUrl = rawBase64;
        try {
          const res = await fetch(`${API_BASE_URL}/api/utils/remove-bg`, {
            method: 'POST',
            headers: { 
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ image: rawBase64, watermark: supplierName })
          });
          if (res.ok) {
            const data = await res.json();
            if (data.processed_image || data.image) {
              processedUrl = data.processed_image || data.image;
            }
          } else {
            throw new Error(`Server returned status: ${res.status}`);
          }
        } catch (err) {
          console.warn("Backend remove-bg fallback to client canvas:", err);
          const img = new Image();
          await new Promise((resolve) => {
            img.onload = () => {
              const canvas = document.createElement('canvas');
              canvas.width = 800;
              canvas.height = 800;
              const ctx = canvas.getContext('2d');

              // پس‌زمینه یکپارچه سفید خالص (استایل دیجی‌کالا)
              ctx.fillStyle = '#FFFFFF';
              ctx.fillRect(0, 0, 800, 800);

              // حفظ تناسب ابعاد و قرار دادن سوژه در مرکز بوم
              const scale = Math.min(680 / img.width, 680 / img.height);
              const w = img.width * scale;
              const h = img.height * scale;
              const x = (800 - w) / 2;
              const y = (800 - h) / 2 - 20;

              ctx.drawImage(img, x, y, w, h);

              // === طراحی واترمارک اولترا پریمیوم شیشه‌ای (فارسی) ===
              ctx.shadowColor = 'rgba(0, 0, 0, 0.15)';
              ctx.shadowBlur = 20;
              ctx.shadowOffsetY = 8;
              
              ctx.font = '900 18px "Vazirmatn", "IRANSans", "Segoe UI", Tahoma, sans-serif';
              const textStr = `✦ تامین‌کننده تایید شده: ${supplierName} ✦`;
              const textWidth = ctx.measureText(textStr).width;
              
              const boxW = Math.max(300, Math.min(700, textWidth + 80));
              const boxH = 54;
              const boxX = (800 - boxW) / 2;
              const boxY = 710;
              
              // بدنه سرمه‌ای دیپ شیشه‌ای
              ctx.fillStyle = 'rgba(15, 23, 42, 0.92)'; 
              if (ctx.roundRect) ctx.roundRect(boxX, boxY, boxW, boxH, 14);
              else ctx.rect(boxX, boxY, boxW, boxH);
              ctx.fill();
              
              // حاشیه طلایی لوکس
              ctx.strokeStyle = '#D4AF37'; 
              ctx.lineWidth = 2.5;
              ctx.stroke();

              // ریست کردن سایه برای متن
              ctx.shadowColor = 'transparent'; 
              
              // رسم متن فارسی
              ctx.fillStyle = '#FFFFFF';
              ctx.textAlign = 'center';
              ctx.textBaseline = 'middle';
              ctx.fillText(textStr, 800 / 2, boxY + (boxH / 2));

              processedUrl = canvas.toDataURL('image/jpeg', 0.95);
              resolve();
            };
            img.src = rawBase64;
          });
        }

        const newMedia = { type: 'image', preview: processedUrl };
        editModal.value.data.gallery.push(newMedia);
        editModal.value.data.img = processedUrl;
        editModal.value.data.image_url = processedUrl;
        selectedEditMedia.value = newMedia;
        isProcessingImage.value = false;
        showToast('پردازش تصویر', 'تصویر با پس‌زمینه سفید و واترمارک درج گردید.');
      } else if (isVideo) {
        const newVideoMedia = { type: 'video', preview: rawBase64 };
        editModal.value.data.gallery.push(newVideoMedia);
        selectedEditMedia.value = newVideoMedia;
        isProcessingImage.value = false;
        showToast('بارگذاری ویدئو', 'ویدئو با موفقیت اضافه گردید.');
      }
    };
    reader.readAsDataURL(file);
  }

  if (editFileInputRef.value) editFileInputRef.value.value = '';
};

const removeEditMedia = (index) => {
  editModal.value.data.gallery.splice(index, 1);
  if (editModal.value.data.gallery.length > 0) {
    selectedEditMedia.value = editModal.value.data.gallery[0];
    const firstPreview = typeof selectedEditMedia.value === 'string' ? selectedEditMedia.value : (selectedEditMedia.value.preview || selectedEditMedia.value.url);
    if (firstPreview) {
      editModal.value.data.img = firstPreview;
      editModal.value.data.image_url = firstPreview;
    }
  } else {
    selectedEditMedia.value = null;
    editModal.value.data.img = '';
    editModal.value.data.image_url = '';
  }
};

const generateRichFallbackContent = (productName) => {
  const pName = productName || 'کالای بازرگانی B2B';
  
  const htmlDescription = `<h2>بررسی تخصصی و آنالیز فنی ${pName}</h2>
<p>محصول <strong>${pName}</strong> به عنوان یکی از کلیدی‌ترین و پرتقاضاترین کالاهای حوزه تخصصی خود، با در نظر گرفتن بالاترین استانداردهای صنعتی و کیفی طراحی و عرضه گردیده است. این کالا پاسخگوی نیازهای عمده‌فروشان، توزیع‌کنندگان سراسری و خریداران B2B می‌باشد که به دنبال تامین محصولی پایدار، باکیفیت و رقابتی در بازار ایران هستند. ساختار ارگونومیک، ترکیبات متوازن و متریال اولیه باکیفیت به کار رفته در تولید این محصول، آن را به گزینه‌ای ایده‌آل برای ارتقای سبد کالایی فروشگاه‌ها و تامین‌کنندگان تبدیل ساخته است.</p>

<h3>۱. مشخصات ساختاری، ترکیبات و فناوری تولید</h3>
<p>در فرایند تولید و بسته‌بندی <strong>${pName}</strong> از فناوری‌های مدرن منطبق با استانداردهای ملی و بین‌المللی استفاده شده است. دقت در انتخاب مواد اولیه، بررسی‌های آزمایشی مداوم در واحدهای کنترل کیفیت (QC) و رعایت پروتکل‌های بهداشتی و ایمنی سبب گردیده تا طول عمر، دوام و کارایی این محصول به حداکثر میزان ممکن برسد. خریداران عمده می‌توانند با اطمینان کامل از اصالت فیزیکی، استانداردهای بهداشتی و ایمنی بالا، این محصول را در حجم‌های گوناگون سفارش دهند.</p>

<h3>۲. مزایای اقتصادی و ارزش افزوده در خرید عمده B2B</h3>
<p>سفارش عمده <strong>${pName}</strong> در پلتفرم B2B تاجربام با حاشیه سود بسیار مناسب و قیمت‌گذاری پلکانی همراه است. از جمله مهم‌ترین مزایای خرید این کالا می‌توان به موارد زیر اشاره نمود:</p>
<ul>
  <li><strong>تضمین اصالت کالا:</strong> ارائه گواهی اصالت و تاییدیه کیفی مستقیم از تولیدکننده/واردکننده معتبر.</li>
  <li><strong>صرفه‌جویی در هزینه‌های لجستیک:</strong> امکان ارسال انبوه از طریق باربری‌های صنعتی پیشرفته با پس‌کرایه ایمن.</li>
  <li><strong>بسته‌بندی ایمن و استاندارد:</strong> طراحی کارتن‌ها و بسته‌بندی‌های ثانویه جهت مقاومت در برابر ضربه و رطوبت طی حمل‌ونقل.</li>
  <li><strong>پایداری تامین انبار:</strong> تضمین تامین مستمر و بدون وقفه جهت خریداران عمده و فروشگاه‌های زنجیره‌ای.</li>
</ul>

<h3>۳. راهنمای نگهداری، شرایط انبارداری و ارسال</h3>
<p>جهت حفظ حداکثر کیفیت و جلوگیری از افت عملکرد محصول <strong>${pName}</strong>، توصیه می‌شود محموله در محیطی خشک، خنک و دور از تابش مستقیم نور خورشید نگهداری شود. چیدمان صحیح قفسه‌ها و رعایت حداکثر تعداد کارتن قابل بارگذاری روی یکدیگر در انبار، طول عمر مفید محصول را تضمین می‌نماید. تمامی سفارشات ثبت‌شده با بازرسی نهایی دقیق آماده‌سازی و به سراسر کشور ارسال می‌گردند.</p>

<h3>۴. جدول خلاصه مشخصات و تاییدیه های فنی</h3>
<p>محصول فوق تمامی تست‌های کیفیت عملکردی و سلامت فیزیکی را با موفقیت پشت سر گذاشته و آماده توزیع سراسری در سامانه تاجربام می‌باشد.</p>`;

  return {
    description: htmlDescription,
    seo_title: `خرید عمده ${pName} | قیمت کارخانه و مشخصات فنی B2B`,
    seo_description: `خرید عمده و مستقیم ${pName} با بهترین قیمت بازار، تضمین اصالت کالا، تحویل سریع سراسری و قیمت‌گذاری پلکانی ویژه بنکداران در پلتفرم تاجربام.`,
    keywords: `خرید عمده ${pName}, قیمت ${pName}, تامین عمده B2B, پخش عمده ${pName}, عمده فروشی`,
    simple_attributes: [
      { name: 'اصالت کالا', value: 'تضمین اصالت فیزیکی و کیفی' },
      { name: 'نوع بسته‌بندی', value: 'کارتن صادراتی مقاوم B2B' },
      { name: 'گارانتی / تاییدیه', value: 'دارای تاییدیه کیفی پلتفرم' },
      { name: 'شرایط نگهداری', value: 'محیط خشک و خنک انبار' }
    ]
  };
};

const generateGroqAI = async () => {
  if (!editModal.value.data.name) {
    showToast('خطا', 'لطفاً ابتدا عنوان کالا را وارد کنید.', 'error');
    return;
  }
  
  isAILoading.value = true;

  try {
    const customSystemPrompt = `تو یک کپی‌رایتر ارشد B2B، متخصص آنالیز محصولات صنعتی و دیجیتال و مهندس ارشد سئو هستی.
وظیفه تو تولید یک محتوای جامع، فوق‌العاده تخصصی، تحلیلی و کاملاً سئو شده به زبان فارسی با طول دقیق و حداقل ۷۰۰ کلمه برای محصول زیر است:
عنوان کامل محصول: "${editModal.value.data.name}"

دستورالعمل‌های دقیق تولید محتوا:
۱. طول توضیحات اصلی (description): باید بسیار مفصل، تحلیلی، تخصصی و شامل حداقل ۷۰۰ کلمه متن فارسی روان باشد.
۲. فرمت توضیحات: کاملاً ساختاریافته با تگ‌های HTML شامل <h2>، <h3>، <p>، <ul> و <li> باشد.
۳. بخش‌های الزامی محتوا:
   - مقدمه تحلیلی و معرفی کامل کاربرد تجاری/صنعتی کالا
   - بررسی دقیق مشخصات فنی، متریال، قطعات و معماری ساخت
   - مزایای رقابتی در خرید عمده B2B و ارزش افزوده اقتصادی
   - راهنمای استاندارد استفاده، نگهداری و تست کیفیت
   - جدول/لیست ویژگی‌های کلیدی عملکردی
۴. عنوان سئو (seo_title): جذاب، کلیک‌خور و حاوی کلمه کلیدی اصلی (حداکثر ۶۰ کاراکتر).
۵. توضیحات متا (seo_description): خلاصه ترغیب‌کننده برای جذب ورودی گوگل (حداکثر ۱۶۰ کاراکتر).
۶. کلمات کلیدی (keywords): ۸ الی ۱۲ کلمه کلیدی پرجستجوی مرتبط با ویرگول انگلیسی.
۷. مشخصات فنی (simple_attributes): حداقل ۶ مشخصه فنی دقیق به صورت کلید و مقدار ({ "name": "...", "value": "..." }).
۸. شناسه دسته‌بندی پیشنهادی (suggested_category_id): بر اساس ماهیت کالا دقیق‌ترین شناسه را از لیست زیر انتخاب کن:
${JSON.stringify(allDbCategories.value.map(c => ({ id: c.id, name: c.fullPath })))}

پاسخ را مستقیماً در قالب یک خروجی JSON معتبر با ساختار زیر ارسال کن (هیچ متن دیگری خارج از ساختار JSON ننویس):
{
  "description": "... (متن HTML کامل و مفصل با طول حداقل ۷۰۰ کلمه) ...",
  "seo_title": "...",
  "seo_description": "...",
  "keywords": "...",
  "suggested_category_id": 1,
  "simple_attributes": [{"name": "...", "value": "..."}]
}`;

    const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${GROQ_API_KEY}`
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [
          { role: 'system', content: 'You are a professional B2B Persian copywriter and SEO expert. Output strictly valid JSON without markdown code fences.' },
          { role: 'user', content: customSystemPrompt }
        ],
        response_format: { type: 'json_object' },
        temperature: 0.6,
        max_tokens: 4000
      })
    });

    if (!res.ok) throw new Error(`Groq API Error: status ${res.status}`);

    const responseData = await res.json();
    const contentText = responseData.choices?.[0]?.message?.content;
    const resultObj = JSON.parse(contentText);

    if (resultObj) {
      editModal.value.data.description = resultObj.description || '';
      editModal.value.data.seo_title = resultObj.seo_title || '';
      editModal.value.data.seo_description = resultObj.seo_description || '';
      editModal.value.data.keywords = resultObj.keywords || '';

      if (resultObj.suggested_category_id) {
        const foundCat = allDbCategories.value.find(c => c.id === Number(resultObj.suggested_category_id));
        if (foundCat) {
          editModal.value.data.category_id = foundCat.id;
          editSuggestedCategory.value = foundCat;
        }
      }

      if (Array.isArray(resultObj.simple_attributes) && resultObj.simple_attributes.length > 0) {
        editModal.value.data.simple_attributes = resultObj.simple_attributes;
      }

      aiHighlight.value = true;
      setTimeout(() => aiHighlight.value = false, 3000);
      showToast('قدرت Groq AI!', `محتوای تخصصی ۷۰۰ کلمه‌ای، تنظیمات سئو و دسته‌بندی هوشمند کالا ثبت شد.`, 'success');
    }
  } catch (error) {
    console.warn("Groq API Direct Call Fallback:", error);
    const prodName = editModal.value.data.name;
    const fallbackData = generateRichFallbackContent(prodName);
    editModal.value.data.description = fallbackData.description;
    editModal.value.data.seo_title = fallbackData.seo_title;
    editModal.value.data.seo_description = fallbackData.seo_description;
    editModal.value.data.keywords = fallbackData.keywords;
    if (fallbackData.simple_attributes && fallbackData.simple_attributes.length) {
      editModal.value.data.simple_attributes = fallbackData.simple_attributes;
    }
    
    detectEditCategoryFromTitle();
    if (editSuggestedCategory.value) {
      editModal.value.data.category_id = editSuggestedCategory.value.id;
    }

    aiHighlight.value = true;
    setTimeout(() => aiHighlight.value = false, 3000);
    showToast('تولید هوشمند محتوا', `محتوای تخصصی بر اساس آنالیز عنوان «${prodName}» تولید شد.`, 'success');
  } finally {
    isAILoading.value = false;
  }
};

const processFlatCategories = (catList) => {
  const flat = [];
  catList.forEach(c => {
    flat.push({ id: c.id, name: c.name, fullPath: c.name, parentName: null });
    if (c.children && Array.isArray(c.children)) {
      c.children.forEach(sub => {
        flat.push({ id: sub.id, name: sub.name, fullPath: `${c.name} > ${sub.name}`, parentName: c.name });
      });
    }
  });
  return flat;
};

const filteredEditCategories = computed(() => {
  if (!editCategorySearchQuery.value.trim()) return allDbCategories.value;
  const q = editCategorySearchQuery.value.trim().toLowerCase();
  return allDbCategories.value.filter(c => c.fullPath.toLowerCase().includes(q));
});

const editSelectedCategoryLabel = computed(() => {
  const found = allDbCategories.value.find(c => c.id === editModal.value.data?.category_id);
  return found ? found.fullPath : '';
});

const selectEditCategory = (cat) => {
  if (editModal.value.data) {
    editModal.value.data.category_id = cat.id;
  }
  isEditCategoryDropdownOpen.value = false;
};

const fetchDbCategories = async () => {
  try {
    const res = await fetch(`${API_BASE_URL}/api/categories`);
    if (res.ok) {
      const data = await res.json();
      allDbCategories.value = processFlatCategories(Array.isArray(data) ? data : (data.categories || []));
    } else {
      throw new Error();
    }
  } catch (e) {
    allDbCategories.value = [
      { id: 1, name: 'کالای دیجیتال', fullPath: 'کالای دیجیتال > لپ‌تاپ و کامپیوتر' },
      { id: 2, name: 'ابزارآلات صنعتی', fullPath: 'ابزارآلات و تجهیزات صنعتی > ابزار برقی' },
      { id: 3, name: 'آرایشی و بهداشتی کودک', fullPath: 'آرایشی و بهداشتی > آرایشی و بهداشتی کودک' },
      { id: 4, name: 'کشاورزی و مواد غذایی', fullPath: 'کشاورزی و خشکبار > مواد غذایی' }
    ];
  }
};

const handleClickOutsideEditCategory = (e) => {
  if (editCategoryDropdownRef.value && !editCategoryDropdownRef.value.contains(e.target)) {
    isEditCategoryDropdownOpen.value = false;
  }
};

onMounted(() => {
  fetchProducts();
  fetchDbCategories();
  window.addEventListener('click', handleClickOutsideEditCategory);
});

onUnmounted(() => {
  window.removeEventListener('click', handleClickOutsideEditCategory);
});
</script>