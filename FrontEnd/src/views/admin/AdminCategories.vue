<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-300 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و ابزارها ================= -->
    <div class="bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 md:p-10 rounded-[2.5rem] border border-slate-700/50 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.5)] relative overflow-hidden flex flex-col md:flex-row items-start md:items-center justify-between gap-6 z-10">
      <!-- افکت‌های نوری (Glow) -->
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-emerald-500 rounded-full mix-blend-screen filter blur-[100px] opacity-10 pointer-events-none animate-pulse"></div>
      <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-teal-600 rounded-full mix-blend-screen filter blur-[80px] opacity-10 pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-20 h-20 bg-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center shadow-inner relative shrink-0">
          <div class="absolute inset-0 bg-emerald-500/20 rounded-2xl animate-pulse"></div>
          <svg class="w-10 h-10 text-emerald-400 relative z-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-white tracking-tight mb-2">مدیریت دسته‌بندی محصولات</h1>
          <p class="text-sm font-bold text-slate-400">سازماندهی دسته‌بندی‌ها، زیردسته‌ها، تصاویر بنری و تولید محتوای سئو شده با AI</p>
        </div>
      </div>

      <div class="relative z-10 flex flex-wrap gap-3 w-full md:w-auto">
        <button @click="openModal()" class="flex-grow md:flex-grow-0 bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-6 py-3.5 rounded-xl transition-all shadow-[0_0_15px_rgba(16,185,129,0.4)] flex items-center justify-center gap-2 text-sm">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
          افزودن دسته‌بندی جدید
        </button>
        <button @click="fetchCategories" :disabled="isLoading" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 font-bold p-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center tooltip disabled:opacity-50" title="بروزرسانی">
          <svg :class="{'animate-spin text-emerald-400': isLoading}" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
        </button>
      </div>
    </div>

    <!-- ================= وضعیت لودینگ ================= -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 z-20 relative">
      <div class="relative w-16 h-16 mb-4">
        <div class="absolute inset-0 border-4 border-slate-700 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-emerald-500 rounded-full border-t-transparent animate-spin"></div>
      </div>
      <p class="text-sm font-bold text-emerald-500 animate-pulse">در حال دریافت ساختار دسته‌بندی‌ها از پایگاه داده...</p>
    </div>

    <div v-else class="space-y-8 animate-fade-in">
      
      <!-- ================= کارت‌های آماری کلیدی ================= -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-emerald-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">کل دسته‌بندی‌ها</span>
            <div class="w-10 h-10 bg-emerald-500/10 text-emerald-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.total }} <span class="text-sm text-slate-500 font-sans font-bold">دسته</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-blue-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-blue-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">دسته‌های اصلی (والد)</span>
            <div class="w-10 h-10 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.parents }} <span class="text-sm text-slate-500 font-sans font-bold">اصلی</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-violet-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-violet-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">زیردسته‌ها (Sub-categories)</span>
            <div class="w-10 h-10 bg-violet-500/10 text-violet-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V94-4m-2 0h-4m-2 0H7a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.children }} <span class="text-sm text-slate-500 font-sans font-bold">زیرمجموعه</span></div>
        </div>

        <div class="bg-slate-900 rounded-3xl border border-slate-800 p-6 relative overflow-hidden group hover:border-amber-500/50 transition-all shadow-lg">
          <div class="absolute top-0 left-0 w-32 h-32 bg-amber-500 rounded-br-full mix-blend-overlay opacity-10 group-hover:opacity-20 transition-opacity"></div>
          <div class="relative z-10 flex justify-between items-start mb-4">
            <span class="text-slate-400 text-xs font-bold uppercase tracking-wider">فعال در وب‌سایت</span>
            <div class="w-10 h-10 bg-amber-500/10 text-amber-400 rounded-xl flex items-center justify-center"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
          </div>
          <div class="relative z-10 text-3xl font-black text-white mb-1">{{ stats.active }} <span class="text-sm text-slate-500 font-sans font-bold">فعال</span></div>
        </div>
      </div>

      <!-- ================= جستجو و فیلتر ================= -->
      <div class="bg-slate-900 rounded-[2.5rem] border border-slate-800 shadow-lg p-6 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="relative w-full md:w-96">
          <input v-model="searchQuery" @input="currentPage = 1" type="text" placeholder="جستجوی نام دسته‌بندی یا اسلاگ..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 pr-11 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-medium">
          <svg class="w-5 h-5 text-slate-500 absolute right-4 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>

        <div class="flex items-center gap-3 w-full md:w-auto justify-end">
          <select v-model="parentFilter" @change="currentPage = 1" class="bg-slate-950 border border-slate-700 text-slate-300 font-bold px-4 py-3.5 rounded-xl outline-none focus:border-emerald-500 text-sm cursor-pointer">
            <option value="all">همه گروه‌ها</option>
            <option value="parents_only">فقط دسته‌های اصلی (والد)</option>
            <option value="subs_only">فقط زیردسته‌ها</option>
          </select>
        </div>
      </div>

      <!-- ================= جدول دسته‌بندی‌ها ================= -->
      <div class="bg-slate-900 rounded-[2rem] border border-slate-800 shadow-lg overflow-hidden relative">
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-emerald-500 to-teal-500"></div>
        
        <div class="overflow-x-auto custom-scrollbar-dark p-2">
          <table class="w-full text-right border-collapse whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/50 text-slate-400 text-xs font-bold border-b border-slate-800">
                <th class="p-5 font-normal rounded-tr-xl">تصویر و عنوان دسته</th>
                <th class="p-5 font-normal">نام لاتین (Slug)</th>
                <th class="p-5 font-normal">دسته والد</th>
                <th class="p-5 font-normal text-center">کالاهای مرتبط</th>
                <th class="p-5 font-normal text-center">وضعیت سئو</th>
                <th class="p-5 font-normal text-center">وضعیت</th>
                <th class="p-5 font-normal text-left rounded-tl-xl">عملیات</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr v-if="paginatedCategories.length === 0">
                <td colspan="7" class="py-12 text-center text-slate-500 font-bold">هیچ دسته‌بندی یافت نشد.</td>
              </tr>
              <tr v-for="cat in paginatedCategories" :key="cat.id" class="border-b border-slate-800/50 hover:bg-slate-800/30 transition-colors group">
                <td class="p-5">
                  <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-xl bg-slate-800 p-1 border border-slate-700 shrink-0 shadow-sm overflow-hidden relative">
                      <img :src="cat.image_url" class="w-full h-full object-cover rounded-lg" @error="handleImageError" alt="Category">
                    </div>
                    <div>
                      <h4 class="font-bold text-white text-sm flex items-center gap-2">
                        <span v-if="cat.level === 1" class="text-xs text-emerald-400 font-mono">└─</span>
                        <span v-else-if="cat.level >= 2" class="text-xs text-teal-400 font-mono">└───</span>
                        <span v-else-if="cat.parent_id" class="text-xs text-emerald-400 font-mono">└─</span>
                        {{ cat.name }}
                      </h4>
                      <p class="text-[11px] text-slate-500 mt-0.5 line-clamp-1 max-w-xs">{{ cat.description || 'بدون توضیحات کوتاه' }}</p>
                    </div>
                  </div>
                </td>
                <td class="p-5 font-mono text-xs text-slate-400 bg-slate-950/20 rounded">{{ cat.slug }}</td>
                <td class="p-5">
                  <span v-if="cat.parent_name" class="bg-blue-500/10 text-blue-400 border border-blue-500/20 px-3 py-1 rounded-lg text-xs font-bold">
                    {{ cat.parent_name }}
                  </span>
                  <span v-else class="text-slate-500 text-xs font-bold">شاخه اصلی (Root)</span>
                </td>
                <td class="p-5 text-center font-black text-white">
                  <span class="bg-slate-800 border border-slate-700 px-3 py-1 rounded-lg text-xs text-slate-300 font-mono">{{ cat.products_count || 0 }} کالا</span>
                </td>
                <td class="p-5 text-center">
                  <span v-if="cat.seo_title && cat.content" class="text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-1 rounded text-[10px] font-bold">کامل با AI</span>
                  <span v-else-if="cat.seo_title" class="text-amber-400 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1 rounded text-[10px] font-bold">سئو پایه</span>
                  <span v-else class="text-slate-500 bg-slate-800 px-2.5 py-1 rounded text-[10px] font-bold">نیازمند سئو</span>
                </td>
                <td class="p-5 text-center">
                  <span :class="cat.is_active ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : 'bg-slate-800 text-slate-500 border-slate-700'" class="px-3 py-1.5 rounded-lg text-[11px] font-bold border inline-block">
                    {{ cat.is_active ? 'فعال' : 'غیرفعال' }}
                  </span>
                </td>
                <td class="p-5 text-left">
                  <div class="flex items-center justify-end gap-2">
                    <button @click="openModal(cat)" class="bg-emerald-600/10 hover:bg-emerald-600 text-emerald-400 hover:text-white border border-emerald-600/30 transition-all font-bold px-3 py-2 rounded-xl text-xs flex items-center justify-center gap-1 shadow-sm">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                      ویرایش و سئو
                    </button>
                    <button @click="confirmDelete(cat)" class="bg-rose-500/10 hover:bg-rose-500 text-rose-500 hover:text-white border border-rose-500/20 transition-all font-bold p-2 rounded-xl text-xs flex items-center justify-center shadow-sm" title="حذف">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- ================= کنترل‌های صفحه‌بندی (Pagination) ================= -->
        <div v-if="totalPages > 1" class="p-4 border-t border-slate-800 bg-slate-950/40 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-bold">
          <div class="text-slate-400">
            نمایش {{ ((currentPage - 1) * itemsPerPage) + 1 }} تا {{ Math.min(currentPage * itemsPerPage, filteredCategories.length) }} از مجموع {{ filteredCategories.length }} دسته‌بندی
          </div>
          <div class="flex items-center gap-2">
            <button @click="currentPage--" :disabled="currentPage === 1" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg disabled:opacity-40 transition-colors">قبلی</button>
            <span class="px-3 py-2 bg-slate-900 border border-slate-700 text-emerald-400 rounded-lg">صفحه {{ currentPage }} از {{ totalPages }}</span>
            <button @click="currentPage++" :disabled="currentPage === totalPages" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg disabled:opacity-40 transition-colors">بعدی</button>
          </div>
        </div>
      </div>

    </div>

    <!-- ================= MODAL: ایجاد و ویرایش جامع دسته‌بندی و سئو ================= -->
    <div v-if="modal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="closeModal"></div>
      <div class="bg-slate-900 border border-slate-700 rounded-[2.5rem] w-full max-w-4xl relative z-10 shadow-2xl overflow-hidden animate-fade-in flex flex-col max-h-[90vh]">
        
        <!-- نوار رنگی هدر -->
        <div class="h-2 bg-gradient-to-r from-emerald-500 via-teal-500 to-blue-500"></div>
        
        <!-- عنوان مودال و تب‌ها -->
        <div class="p-6 md:p-8 border-b border-slate-800 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-slate-950/40">
          <div>
            <h2 class="text-2xl font-black text-white mb-1">
              {{ isEditing ? 'ویرایش و سئوسازی دسته‌بندی' : 'افزودن دسته‌بندی جدید' }}
            </h2>
            <p class="text-xs text-slate-400 font-bold">تنظیمات مشخصات ظاهر، ساختار درختی و تولید محتوای سئو شده</p>
          </div>

          <div class="bg-slate-900 border border-slate-700 p-1 rounded-xl flex gap-1">
            <button @click="activeTab = 'general'" :class="activeTab === 'general' ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'" class="px-4 py-2 rounded-lg text-xs font-bold transition-all">مشخصات اصلی</button>
            <button @click="activeTab = 'seo'" :class="activeTab === 'seo' ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'" class="px-4 py-2 rounded-lg text-xs font-bold transition-all">محتوا و سئو (SEO)</button>
          </div>
        </div>

        <!-- فرم متغیر بر اساس تب -->
        <div class="p-6 md:p-8 overflow-y-auto custom-scrollbar-dark flex-grow space-y-6">
          
          <!-- TAB 1: اطلاعات اصلی -->
          <div v-if="activeTab === 'general'" class="space-y-6 animate-fade-in">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">عنوان دسته‌بندی (فارسی) *</label>
                <input v-model="form.name" type="text" placeholder="مثال: تجهیزات شبکه و سرور" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-bold" />
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">نام انگلیسی / آدرس یکتا (Slug)</label>
                <input v-model="form.slug" type="text" placeholder="مثال: network-equipment" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-mono text-left" dir="ltr" />
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">دسته‌بندی والد (اختیاری)</label>
                <select v-model="form.parent_id" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3.5 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-bold cursor-pointer">
                  <option :value="null">-- دسته‌بندی اصلی (بدون والد) --</option>
                  <option v-for="c in parentOptions" :key="c.id" :value="c.id">
                    {{ c.name }}
                  </option>
                </select>
              </div>

              <div>
                <label class="block text-slate-400 text-xs font-bold mb-2">اولویت نمایش (ترتیب)</label>
                <input v-model.number="form.display_order" type="number" class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-mono text-left" dir="ltr" />
              </div>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">آدرس تصویر بنری / کاور (URL)</label>
              <input v-model="form.image_url" type="text" placeholder="https://..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-mono text-left" dir="ltr" />
            </div>

            <div v-if="form.image_url" class="w-full h-36 bg-slate-950 rounded-2xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
              <img :src="form.image_url" class="max-w-full max-h-full object-contain rounded-xl" @error="handleImageError" alt="پیش‌نمایش">
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">توضیحات کوتاه خلاصه دسته‌بندی</label>
              <textarea v-model="form.description" rows="3" placeholder="توضیحات کوتاه جهت نمایش در کارت دسته‌بندی..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm resize-none"></textarea>
            </div>

            <div class="flex items-center gap-3 bg-slate-950 p-4 rounded-xl border border-slate-800">
              <input type="checkbox" id="cat_active" v-model="form.is_active" class="w-5 h-5 rounded text-emerald-600 focus:ring-emerald-500 bg-slate-800 border-slate-700 cursor-pointer">
              <label for="cat_active" class="text-sm font-bold text-slate-300 cursor-pointer">نمایش و فعال بودن این دسته‌بندی در وب‌سایت</label>
            </div>
          </div>

          <!-- TAB 2: محتوا و سئو + تولید خودکار AI -->
          <div v-if="activeTab === 'seo'" class="space-y-6 animate-fade-in">
            
            <div class="bg-gradient-to-r from-emerald-950/40 via-slate-950 to-slate-950 p-5 rounded-2xl border border-emerald-500/30 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-emerald-500/10 rounded-xl flex items-center justify-center border border-emerald-500/20 shrink-0">
                  <svg class="w-6 h-6 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <div>
                  <h4 class="text-white font-bold text-sm">کپی‌رایتر هوش مصنوعی سئو (AI Generator)</h4>
                  <p class="text-xs text-slate-400">تولید خودکار عنوان سئو، توضیحات متا و مقاله کامل HTML برای این دسته</p>
                </div>
              </div>

              <button @click="generateAIContent" :disabled="isGeneratingAI || !form.name" class="bg-gradient-to-r from-emerald-600 to-teal-600 hover:brightness-110 text-white font-bold px-5 py-2.5 rounded-xl transition-all shadow-md text-xs flex items-center gap-2 disabled:opacity-50 shrink-0">
                <svg v-if="isGeneratingAI" class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                <span>{{ isGeneratingAI ? 'در حال نگارش AI...' : 'تولید محتوای هوشمند' }}</span>
              </button>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">عنوان سئو (SEO Title)</label>
              <input v-model="form.seo_title" type="text" placeholder="عنوان بهینه‌شده برای موتورهای جستجو..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm font-bold" />
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">توضیحات متا سئو (Meta Description)</label>
              <textarea v-model="form.seo_description" rows="2" placeholder="توضیحات متا خلاصه برای نمایش در گوگل..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm resize-none"></textarea>
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">کلمات کلیدی سئو (Keywords)</label>
              <input v-model="form.keywords" type="text" placeholder="خرید عمده, قیمت کارخانه, تامین کننده..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-sm" />
            </div>

            <div>
              <label class="block text-slate-400 text-xs font-bold mb-2">محتوا و راهنمای کامل دسته‌بندی (HTML Rich Content)</label>
              <textarea v-model="form.content" rows="8" placeholder="متن کامل راهنمای خرید و معرفی دسته‌بندی همراه با تگ‌های HTML..." class="w-full bg-slate-950 border border-slate-700 text-white px-4 py-3 rounded-xl focus:outline-none focus:border-emerald-500 transition-colors text-xs font-mono resize-y custom-scrollbar-dark"></textarea>
            </div>

          </div>

        </div>

        <!-- دکمه‌های عملیات مودال -->
        <div class="p-6 md:p-8 border-t border-slate-800 bg-slate-950/40 flex gap-4">
          <button @click="closeModal" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 rounded-xl transition-colors text-sm">انصراف</button>
          <button @click="saveCategory" :disabled="isSaving" class="flex-[2] bg-emerald-600 hover:bg-emerald-500 text-white font-black py-3.5 rounded-xl transition-all shadow-[0_0_20px_rgba(16,185,129,0.3)] disabled:opacity-50 flex justify-center items-center gap-2 text-sm">
            <svg v-if="isSaving" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
            <span v-else>ذخیره دسته‌بندی</span>
          </button>
        </div>

      </div>
    </div>

    <!-- ================= MODAL: تایید حذف دسته‌بندی ================= -->
    <div v-if="deleteModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-slate-950/80 backdrop-blur-sm" @click="deleteModal.show = false"></div>
      <div class="bg-slate-900 border border-rose-500/30 rounded-[2rem] w-full max-w-md relative z-10 shadow-2xl p-6 text-center animate-fade-in">
        <div class="w-16 h-16 bg-rose-500/10 text-rose-500 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-rose-500/20">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
        </div>
        <h3 class="text-xl font-black text-white mb-2">تایید حذف دسته‌بندی</h3>
        <p class="text-xs text-slate-400 font-bold mb-6">آیا از حذف دسته‌بندی "{{ deleteModal.item?.name }}" اطمینان دارید؟ محصولات مرتبط به وضعیت بدون دسته منتقل می‌شوند.</p>
        <div class="flex gap-3">
          <button @click="deleteModal.show = false" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-3 rounded-xl text-xs">انصراف</button>
          <button @click="executeDelete" :disabled="isDeleting" class="flex-1 bg-rose-600 hover:bg-rose-500 text-white font-bold py-3 rounded-xl text-xs flex justify-center items-center gap-1 shadow-lg shadow-rose-600/20">
            <span>حذف قطعی</span>
          </button>
        </div>
      </div>
    </div>

    <!-- ================= Toast Notification ================= -->
    <div v-if="toastShow" class="fixed bottom-6 right-6 bg-slate-800 border border-emerald-500/30 shadow-[0_10px_30px_rgba(0,0,0,0.5)] rounded-2xl p-4 flex items-center gap-4 z-50 animate-fade-in max-w-sm">
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
import { ref, computed, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = () => localStorage.getItem('tajerbam_token') || localStorage.getItem('access_token') || 'test-token';

const isLoading = ref(true);
const isSaving = ref(false);
const isDeleting = ref(false);
const isGeneratingAI = ref(false);

const searchQuery = ref('');
const parentFilter = ref('all');
const activeTab = ref('general');

const currentPage = ref(1);
const itemsPerPage = ref(15);

const categories = ref([]);

const stats = ref({
  total: 0,
  parents: 0,
  children: 0,
  active: 0
});

const modal = ref({
  show: false,
  data: null
});

const deleteModal = ref({
  show: false,
  item: null
});

const isEditing = computed(() => !!modal.value.data);

const form = ref({
  name: '',
  slug: '',
  icon: 'folder',
  image_url: '',
  description: '',
  content: '',
  seo_title: '',
  seo_description: '',
  keywords: '',
  parent_id: null,
  is_active: true,
  display_order: 0
});

const toastShow = ref(false);
const toastData = ref({ title: '', text: '' });

const showToast = (title, text) => {
  toastData.value = { title, text };
  toastShow.value = true;
  setTimeout(() => { toastShow.value = false; }, 4000);
};

const handleImageError = (e) => {
  e.target.src = 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=600&auto=format&fit=crop&q=80';
};

const calculateStats = () => {
  const total = categories.value.length;
  const parents = categories.value.filter(c => !c.parent_id).length;
  const children = categories.value.filter(c => !!c.parent_id).length;
  const active = categories.value.filter(c => c.is_active).length;

  stats.value = { total, parents, children, active };
};

const flattenTree = (nodes, parentName = null, level = 0) => {
  let list = [];
  if (!Array.isArray(nodes)) return list;
  for (const node of nodes) {
    list.push({
      id: node.id || node.slug,
      name: node.name || node.title,
      slug: node.slug,
      icon: node.icon || 'folder',
      image_url: node.image_url || node.image || '',
      description: node.description || '',
      content: node.content || '',
      seo_title: node.seo_title || '',
      seo_description: node.seo_description || '',
      keywords: node.keywords || '',
      parent_id: node.parent_id || null,
      parent_name: parentName || node.parent_name || null,
      level: level,
      is_active: node.is_active !== undefined ? node.is_active : true,
      display_order: node.display_order || 0,
      products_count: node.products_count || 0
    });
    if (node.children && node.children.length > 0) {
      list = list.concat(flattenTree(node.children, node.name || node.title, level + 1));
    }
  }
  return list;
};

const fetchCategories = async () => {
  isLoading.value = true;
  let loaded = false;

  try {
    // روش اول: دریافت از اندپوینت اختصاصی مدیریت
    const response = await fetch(`${API_BASE}/api/admin/categories`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.ok) {
      const data = await response.json();
      if (data.success && data.categories && data.categories.length > 0) {
        categories.value = data.categories;
        calculateStats();
        loaded = true;
      }
    }

    // روش دوم: اگر اندپوینت ادمین خالی بود، دریافت از اندپوینت عمومی درخت کامل
    if (!loaded) {
      const pubRes = await fetch(`${API_BASE}/api/categories`);
      if (pubRes.ok) {
        const pubData = await pubRes.json();
        if (Array.isArray(pubData) && pubData.length > 0) {
          categories.value = flattenTree(pubData);
          calculateStats();
          loaded = true;
        }
      }
    }

    if (!loaded) {
      useFallbackCategories();
    }
  } catch (error) {
    console.error("خطا در دریافت لیست دسته‌بندی‌ها:", error);
    try {
      const pubRes = await fetch(`${API_BASE}/api/categories`);
      if (pubRes.ok) {
        const pubData = await pubRes.json();
        if (Array.isArray(pubData) && pubData.length > 0) {
          categories.value = flattenTree(pubData);
          calculateStats();
          loaded = true;
        }
      }
    } catch (e) {}
    if (!loaded) useFallbackCategories();
  } finally {
    isLoading.value = false;
  }
};

const filteredCategories = computed(() => {
  let result = categories.value;
  
  if (parentFilter.value === 'parents_only') {
    result = result.filter(c => !c.parent_id);
  } else if (parentFilter.value === 'subs_only') {
    result = result.filter(c => !!c.parent_id);
  }

  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase();
    result = result.filter(c => 
      (c.name && c.name.toLowerCase().includes(q)) || 
      (c.slug && c.slug.toLowerCase().includes(q))
    );
  }
  return result;
});

const totalPages = computed(() => {
  return Math.ceil(filteredCategories.value.length / itemsPerPage.value) || 1;
});

const paginatedCategories = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  return filteredCategories.value.slice(start, start + itemsPerPage.value);
});

const parentOptions = computed(() => {
  return categories.value.filter(c => !c.parent_id && (!modal.value.data || c.id !== modal.value.data.id));
});

const useFallbackCategories = () => {
  categories.value = [
    {
      id: 1,
      name: 'کالای دیجیتال و آی‌تی',
      slug: 'digital',
      icon: 'computer',
      image_url: 'https://images.unsplash.com/photo-1526738549149-8e07eca6c147?w=600&auto=format&fit=crop&q=80',
      description: 'انواع لپ‌تاپ، موبایل، قطعات کامپیوتر و گجت‌های هوشمند',
      content: '<h2>راهنمای خرید عمده کالای دیجیتال</h2><p>خرید بی‌واسطه از واردکنندگان اصلی.</p>',
      seo_title: 'خرید عمده کالای دیجیتال و قطعات کامپیوتر',
      seo_description: 'مرکز تامین عمده تجهیزات دیجیتال و آی‌تی با تضمین اصالت و بهترین قیمت',
      keywords: 'دیجیتال, لپ تاپ عمده, موبایل عمده',
      parent_id: null,
      parent_name: null,
      is_active: true,
      display_order: 1,
      products_count: 14
    },
    {
      id: 2,
      name: 'لپ‌تاپ و تجهیزات جانبی',
      slug: 'laptops-accessories',
      icon: 'laptop',
      image_url: 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=80',
      description: 'لپ‌تاپ‌های گیمینگ، اداری و تجاری به همراه لوازم جانبی',
      content: '',
      seo_title: 'فروش عمده لپ تاپ ایسوس و لنوو',
      seo_description: 'تامین کننده مستقیم لپ تاپ و لوازم جانبی',
      keywords: 'لپ تاپ, لوازم جانبی, ایسوس',
      parent_id: 1,
      parent_name: 'کالای دیجیتال و آی‌تی',
      is_active: true,
      display_order: 2,
      products_count: 8
    },
    {
      id: 3,
      name: 'ابزارآلات و تجهیزات صنعتی',
      slug: 'industrial',
      icon: 'tool',
      image_url: 'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=600&auto=format&fit=crop&q=80',
      description: 'ابزارآلات برقی، شارژی، دستگیره و تجهیزات ایمنی کارگاهی',
      content: '',
      seo_title: 'خرید عمده ابزارآلات صنعتی و کارگاهی',
      seo_description: 'مرکز پخش ابزار برقی و صنعتی با قیمت کارخانه',
      keywords: 'ابزار صنعتی, ابزار برقی, تجهیزات ایمنی',
      parent_id: null,
      parent_name: null,
      is_active: true,
      display_order: 3,
      products_count: 6
    }
  ];
  calculateStats();
};

onMounted(() => {
  fetchCategories();
});

const openModal = (category = null) => {
  activeTab.value = 'general';
  if (category) {
    modal.value.data = category;
    form.value = {
      name: category.name || '',
      slug: category.slug || '',
      icon: category.icon || 'folder',
      image_url: category.image_url || '',
      description: category.description || '',
      content: category.content || '',
      seo_title: category.seo_title || '',
      seo_description: category.seo_description || '',
      keywords: category.keywords || '',
      parent_id: category.parent_id || null,
      is_active: category.is_active !== undefined ? category.is_active : true,
      display_order: category.display_order || 0
    };
  } else {
    modal.value.data = null;
    form.value = {
      name: '',
      slug: '',
      icon: 'folder',
      image_url: '',
      description: '',
      content: '',
      seo_title: '',
      seo_description: '',
      keywords: '',
      parent_id: null,
      is_active: true,
      display_order: categories.value.length + 1
    };
  }
  modal.value.show = true;
};

const closeModal = () => {
  modal.value.show = false;
  modal.value.data = null;
};

const generateAIContent = async () => {
  if (!form.value.name) return;
  
  isGeneratingAI.value = true;
  try {
    const response = await fetch(`${API_BASE}/ai/generate-category-seo?title=${encodeURIComponent(form.value.name)}`);
    if (response.ok) {
      const aiData = await response.json();
      if (aiData.seo_title) form.value.seo_title = aiData.seo_title;
      if (aiData.seo_description) form.value.seo_description = aiData.seo_description;
      if (aiData.description) form.value.description = aiData.description;
      if (aiData.content) form.value.content = aiData.content;
      if (aiData.keywords) form.value.keywords = aiData.keywords;
      
      showToast('محتوای AI تولید شد', 'توضیحات سئو و محتوای HTML با موفقیت ایجاد گردید.');
    }
  } catch (e) {
    console.error("AI Error:", e);
  } finally {
    isGeneratingAI.value = false;
  }
};

const saveCategory = async () => {
  if (!form.value.name) {
    showToast('خطا', 'وارد کردن عنوان دسته‌بندی الزامی است.');
    return;
  }

  isSaving.value = true;
  try {
    const url = isEditing.value 
      ? `${API_BASE}/api/admin/categories/${modal.value.data.id}`
      : `${API_BASE}/api/admin/categories`;
      
    const method = isEditing.value ? 'PUT' : 'POST';

    const response = await fetch(url, {
      method,
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(form.value)
    });

    const result = await response.json();

    if (response.ok && result.success) {
      showToast('ذخیره موفق', result.message);
      closeModal();
      await fetchCategories();
    } else {
      throw new Error(result.detail || 'خطا در ذخیره دسته‌بندی');
    }
  } catch (error) {
    console.error("Save Error:", error);
    showToast('خطا', error.message);
  } finally {
    isSaving.value = false;
  }
};

const confirmDelete = (cat) => {
  deleteModal.value.item = cat;
  deleteModal.value.show = true;
};

const executeDelete = async () => {
  if (!deleteModal.value.item) return;
  
  isDeleting.value = true;
  try {
    const response = await fetch(`${API_BASE}/api/admin/categories/${deleteModal.value.item.id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token()}`,
        'Content-Type': 'application/json'
      }
    });

    const result = await response.json();

    if (response.ok && result.success) {
      showToast('حذف شد', result.message);
      deleteModal.value.show = false;
      await fetchCategories();
    }
  } catch (error) {
    console.error("Delete Error:", error);
  } finally {
    isDeleting.value = false;
  }
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
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