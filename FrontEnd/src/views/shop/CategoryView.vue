<template>
  <div class="bg-slate-50/50 min-h-screen pb-24 font-sans text-slate-800" dir="rtl">
    
    <!-- ================= 1. هدر گرافیکی و هوشمند دسته‌بندی ================= -->
    <div class="relative w-full h-72 md:h-88 bg-gradient-to-r from-slate-950 via-blue-950 to-indigo-950 overflow-hidden flex items-center">
      <!-- پترن‌های متحرک پس‌زمینه -->
      <div class="absolute inset-0 opacity-15" style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 32px 32px;"></div>
      <div class="absolute -top-32 -right-32 w-[30rem] h-[30rem] bg-blue-600/30 rounded-full mix-blend-screen filter blur-[100px] animate-pulse"></div>
      <div class="absolute -bottom-32 -left-32 w-[30rem] h-[30rem] bg-indigo-600/20 rounded-full mix-blend-screen filter blur-[120px]"></div>
      
      <div class="container mx-auto px-4 lg:px-8 relative z-10 text-white">
        <!-- Breadcrumb -->
        <nav class="flex items-center text-xs font-black text-blue-200 gap-2 mb-6 bg-white/10 backdrop-blur-xl w-fit px-4 py-2 rounded-2xl border border-white/15 shadow-xl">
          <button @click="navigateTo('/')" class="hover:text-white transition-colors flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 01-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
            تاجربام
          </button>
          <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
          <span class="text-white">{{ currentCategory?.name || 'کالای عمومی B2B' }}</span>
        </nav>
        
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
          <div>
            <div class="inline-flex items-center gap-2 bg-blue-500/20 text-blue-300 border border-blue-400/30 px-3 py-1 rounded-full text-xs font-black mb-3 backdrop-blur-md">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
              بازار عمده و مستقیم تولیدکنندگان
            </div>
            <h1 class="text-3xl md:text-5xl font-black tracking-tight mb-3 text-white drop-shadow-lg">
              {{ currentCategory?.name || 'خرید عمده و بی‌واسطه' }}
            </h1>
            <p class="text-blue-100/90 font-medium max-w-2xl leading-relaxed text-sm md:text-base">
              {{ currentCategory?.description || 'تامین مستقیم از واردکنندگان و تولیدکنندگان اصلی با تضمین بهترین قیمت بازه‌ای، فاکتور رسمی و بیمه کامل معاملات.' }}
            </p>
          </div>
          
          <div class="bg-white/10 backdrop-blur-xl border border-white/15 p-4 rounded-3xl flex items-center gap-6 shrink-0 shadow-2xl">
            <div class="text-center">
              <span class="block text-2xl font-black text-emerald-400">{{ filteredAndSortedProducts.length }}</span>
              <span class="text-[11px] font-bold text-blue-200">کالای فعال</span>
            </div>
            <div class="w-px h-8 bg-white/20"></div>
            <div class="text-center">
              <span class="block text-2xl font-black text-amber-400">{{ subCategories.length }}</span>
              <span class="text-[11px] font-bold text-blue-200">زیردسته</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- افکت موج پایین هدر -->
      <div class="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] transform rotate-180 pointer-events-none">
        <svg class="relative block w-[calc(100%+1.3px)] h-[35px] md:h-[55px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="fill-slate-50/50"></path>
        </svg>
      </div>
    </div>

    <!-- ================= 2. نوار زیردسته‌های سریع (Pill Carousel) ================= -->
    <div class="container mx-auto px-4 lg:px-8 -mt-6 relative z-20 mb-8" v-if="subCategories.length > 0">
      <div class="bg-white/90 backdrop-blur-2xl rounded-3xl p-3 border border-slate-200/80 shadow-[0_10px_30px_rgba(0,0,0,0.04)] flex items-center gap-3 overflow-x-auto hide-scrollbar">
        <span class="text-xs font-black text-slate-500 whitespace-nowrap px-3 flex items-center gap-1.5 shrink-0">
          <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          زیردسته‌های سریع:
        </span>
        
        <button 
          @click="filters.categories = []" 
          :class="['px-4 py-2 rounded-2xl text-xs font-black whitespace-nowrap transition-all border shrink-0', filters.categories.length === 0 ? 'bg-blue-600 text-white border-blue-600 shadow-md shadow-blue-500/30' : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100']"
        >
          همه زیردسته‌ها
        </button>

        <button 
          v-for="sub in subCategories" 
          :key="sub.id" 
          @click="toggleSubcategoryFilter(sub.id)"
          :class="['px-4 py-2 rounded-2xl text-xs font-black whitespace-nowrap transition-all border shrink-0 flex items-center gap-2', filters.categories.includes(sub.id) ? 'bg-blue-600 text-white border-blue-600 shadow-md shadow-blue-500/30' : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100']"
        >
          <span>{{ sub.name }}</span>
          <span :class="['text-[10px] px-1.5 py-0.5 rounded-full font-bold', filters.categories.includes(sub.id) ? 'bg-white/20 text-white' : 'bg-slate-200/80 text-slate-500']">{{ sub.count }}</span>
        </button>
      </div>
    </div>

    <div class="container mx-auto px-4 lg:px-8 relative z-10">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- ================= 3. سایدبار فیلترها (3 ستون) ================= -->
        <aside class="lg:col-span-3 bg-white rounded-[2.5rem] border border-slate-200/80 p-6 shadow-[0_10px_35px_rgba(0,0,0,0.03)] lg:sticky top-28 space-y-7 z-20">
          
          <div class="flex items-center justify-between border-b border-slate-100 pb-4">
            <h2 class="font-black text-slate-800 text-base flex items-center gap-2">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path></svg>
              فیلترهای پیشرفته
            </h2>
            <button @click="clearFilters" class="text-[11px] font-black text-rose-600 bg-rose-50 px-2.5 py-1 rounded-xl hover:bg-rose-100 transition-colors">حذف همه</button>
          </div>

          <!-- جستجو در نتایج دسته -->
          <div>
            <label class="block text-xs font-black text-slate-600 mb-2">جستجو در این دسته‌بندی</label>
            <div class="relative">
              <input type="text" v-model="filters.search" placeholder="نام کالا، تامین‌کننده، مدل..." class="w-full bg-slate-50 border border-slate-200 text-sm font-bold text-slate-800 px-4 py-3 pr-10 rounded-2xl focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 outline-none transition-all">
              <svg class="w-5 h-5 text-slate-400 absolute right-3 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
          </div>

          <!-- زیردسته‌ها (تیک‌باکسی) -->
          <div v-if="subCategories.length > 0">
            <h3 class="font-black text-slate-800 mb-3 text-xs flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-blue-600"></span> انتخاب زیردسته
            </h3>
            <div class="space-y-2.5 max-h-56 overflow-y-auto custom-scrollbar pr-1">
              <label v-for="cat in subCategories" :key="cat.id" class="flex items-center justify-between cursor-pointer p-2 rounded-xl hover:bg-slate-50 transition-colors group">
                <div class="flex items-center gap-3">
                  <input type="checkbox" :value="cat.id" v-model="filters.categories" class="w-4 h-4 rounded-md text-blue-600 border-slate-300 focus:ring-blue-500 bg-slate-50 cursor-pointer"> 
                  <span class="text-xs font-bold text-slate-700 group-hover:text-blue-600 transition-colors">{{ cat.name }}</span>
                </div> 
                <span class="text-[10px] font-black text-slate-400 bg-slate-100 px-2 py-0.5 rounded-lg">{{ cat.count }}</span>
              </label>
            </div>
          </div>

          <!-- محدوده قیمت (تومان) -->
          <div>
            <h3 class="font-black text-slate-800 mb-3 text-xs flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-500"></span> محدوده قیمت عمده (تومان)
            </h3>
            <div class="flex items-center gap-2">
              <input type="text" :value="filters.minPriceDisplay" @input="e => formatPriceInput(e, 'minPrice')" placeholder="از" class="w-1/2 bg-slate-50 border border-slate-200 text-xs font-black text-slate-800 text-center py-3 rounded-2xl outline-none focus:border-blue-500 focus:bg-white transition-all" dir="ltr">
              <span class="text-slate-400 font-bold">-</span>
              <input type="text" :value="filters.maxPriceDisplay" @input="e => formatPriceInput(e, 'maxPrice')" placeholder="تا" class="w-1/2 bg-slate-50 border border-slate-200 text-xs font-black text-slate-800 text-center py-3 rounded-2xl outline-none focus:border-blue-500 focus:bg-white transition-all" dir="ltr">
            </div>
          </div>

          <!-- سوییچ‌های وضعیت -->
          <div class="space-y-3.5 border-t border-slate-100 pt-5">
            <label class="flex items-center justify-between cursor-pointer group bg-slate-50/80 p-3.5 rounded-2xl border border-slate-200/60 transition-colors hover:bg-slate-100/80">
              <span class="font-black text-slate-700 text-xs group-hover:text-blue-600 transition-colors">فقط کالاهای موجود</span>
              <div class="relative">
                <input type="checkbox" v-model="filters.inStock" class="sr-only peer">
                <div class="w-10 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:right-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-blue-600"></div>
              </div>
            </label>
            
            <label class="flex items-center justify-between cursor-pointer group bg-emerald-50/40 p-3.5 rounded-2xl border border-emerald-100 transition-colors hover:bg-emerald-50/80">
              <span class="font-black text-slate-700 text-xs group-hover:text-emerald-700 transition-colors flex items-center gap-1.5">
                <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                دارای بیمه معاملات
              </span>
              <div class="relative">
                <input type="checkbox" v-model="filters.insured" class="sr-only peer">
                <div class="w-10 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:right-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-600"></div>
              </div>
            </label>
          </div>
        </aside>

        <!-- ================= 4. بخش اصلی (گرید محصولات و مرتب‌سازی) ================= -->
        <div class="lg:col-span-9 space-y-6">
          
          <!-- نوار مرتب‌سازی (Sort Bar) -->
          <div class="bg-white rounded-[2rem] border border-slate-200/80 p-4 px-6 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4 sticky top-28 z-30 backdrop-blur-xl bg-white/90">
            <div class="flex items-center gap-3 overflow-x-auto hide-scrollbar w-full sm:w-auto pb-2 sm:pb-0">
              <span class="text-xs font-black text-slate-800 flex items-center gap-1 whitespace-nowrap">
                <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4h13M3 8h9m-9 4h6m4 0l4-4m0 0l4 4m-4-4v12"></path></svg> 
                مرتب‌سازی بر اساس:
              </span>
              <div class="flex gap-2">
                <button @click="sortBy = 'popular'" :class="['text-xs font-black px-4 py-2 rounded-xl border transition-all whitespace-nowrap', sortBy === 'popular' ? 'bg-blue-50 text-blue-700 border-blue-200 shadow-sm' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50']">محبوب‌ترین</button>
                <button @click="sortBy = 'newest'" :class="['text-xs font-black px-4 py-2 rounded-xl border transition-all whitespace-nowrap', sortBy === 'newest' ? 'bg-blue-50 text-blue-700 border-blue-200 shadow-sm' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50']">جدیدترین</button>
                <button @click="sortBy = 'price_asc'" :class="['text-xs font-black px-4 py-2 rounded-xl border transition-all whitespace-nowrap', sortBy === 'price_asc' ? 'bg-blue-50 text-blue-700 border-blue-200 shadow-sm' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50']">ارزان‌ترین</button>
                <button @click="sortBy = 'price_desc'" :class="['text-xs font-black px-4 py-2 rounded-xl border transition-all whitespace-nowrap', sortBy === 'price_desc' ? 'bg-blue-50 text-blue-700 border-blue-200 shadow-sm' : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50']">گران‌ترین</button>
              </div>
            </div>
            <span class="text-xs font-black text-slate-500 bg-slate-100 px-3 py-1.5 rounded-xl whitespace-nowrap shrink-0">{{ filteredAndSortedProducts.length }} کالا موجود است</span>
          </div>

          <!-- Skeleton Loading -->
          <div v-if="isLoading" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6">
            <div v-for="i in 6" :key="i" class="bg-white rounded-[2.5rem] p-5 border border-slate-100 shadow-sm flex flex-col h-96 animate-pulse">
              <div class="w-full h-48 bg-slate-200 rounded-[2rem] mb-4"></div>
              <div class="h-4 bg-slate-200 rounded-lg w-3/4 mb-2"></div>
              <div class="h-4 bg-slate-200 rounded-lg w-1/2 mb-auto"></div>
              <div class="h-12 bg-slate-200 rounded-2xl mt-4"></div>
            </div>
          </div>

          <!-- گرید محصولات (Ultra Premium Product Cards) -->
          <transition-group v-else-if="filteredAndSortedProducts.length > 0" name="list" tag="div" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6">
            <div 
              v-for="product in filteredAndSortedProducts" 
              :key="product.id" 
              class="group bg-white rounded-[2.5rem] p-5 border border-slate-200/80 shadow-[0_8px_25px_rgba(0,0,0,0.03)] hover:shadow-[0_20px_50px_rgba(37,99,235,0.12)] hover:border-blue-300 transition-all duration-500 relative flex flex-col h-full cursor-pointer overflow-hidden"
              @click="navigateToProduct(product.id)"
            >
              
              <!-- نشانگرهای وضعیت بالا -->
              <div class="absolute top-5 right-5 z-10 flex flex-col gap-1.5">
                <div class="bg-emerald-500 text-white text-[10px] font-black px-2.5 py-1 rounded-xl flex items-center gap-1 shadow-md shadow-emerald-500/20" v-if="product.insured">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg> 
                  بیمه تاجربام
                </div>
                <div class="bg-rose-500 text-white text-[10px] font-black px-2.5 py-1 rounded-xl flex items-center gap-1 shadow-md shadow-rose-500/20" v-if="!product.inStock">
                  ناموجود
                </div>
              </div>

              <!-- تصویر کالا -->
              <div :class="['w-full h-52 rounded-[2rem] mb-5 overflow-hidden flex items-center justify-center p-6 relative transition-colors border', product.inStock ? 'bg-slate-50 group-hover:bg-blue-50/40 border-slate-100' : 'bg-slate-100 grayscale border-slate-200']">
                <img :src="product.img" class="max-h-full object-contain mix-blend-multiply group-hover:scale-110 transition-transform duration-700" :alt="product.name">
              </div>
              
              <!-- اطلاعات کالا -->
              <div class="flex-grow flex flex-col justify-between">
                <div class="mb-4">
                  <div class="text-[11px] font-bold text-slate-400 mb-2 flex items-center justify-between">
                    <span class="flex items-center gap-1 bg-slate-100 px-2.5 py-0.5 rounded-lg text-slate-600 font-black"><svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg> {{ product.seller }}</span>
                    <span class="flex items-center gap-0.5 text-amber-500 font-black"><svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> {{ product.rating }}</span>
                  </div>
                  <h3 :class="['font-black text-sm line-clamp-2 leading-relaxed transition-colors', product.inStock ? 'text-slate-800 group-hover:text-blue-600' : 'text-slate-400']">{{ product.name }}</h3>
                </div>
                
                <!-- باکس قیمت‌های B2B -->
                <div :class="['rounded-2xl p-3.5 border transition-colors mb-4', product.inStock ? 'bg-gradient-to-br from-slate-50 to-slate-100/80 border-slate-200/80 group-hover:border-blue-200 group-hover:from-blue-50/30' : 'bg-slate-50 border-slate-200']">
                  <div class="flex justify-between items-center text-xs mb-1.5">
                    <span class="text-slate-400 font-bold">قیمت بازار:</span>
                    <span class="font-bold text-slate-400 line-through decoration-slate-300">{{ formatPrice(product.retailPrice) }}</span>
                  </div>
                  <div class="flex justify-between items-center text-xs border-t border-slate-200/80 pt-2">
                    <span :class="['font-black border px-2 py-0.5 rounded-lg text-[10px]', product.inStock ? 'bg-white text-blue-700 border-blue-100 shadow-sm' : 'bg-slate-100 text-slate-400 border-slate-200']">عمده (+{{ product.minQty }})</span>
                    <span :class="['font-black text-lg tracking-tight', product.inStock ? 'text-blue-700' : 'text-slate-400']">{{ formatPrice(product.wholesalePrice) }} <span class="text-[10px] font-bold">ت</span></span>
                  </div>
                </div>

                <!-- کنترلر تعداد (+ / -) یا دکمه افزودن مستقیم -->
                <div class="mt-auto" @click.stop>
                  <div v-if="getCartQty(product.id) > 0" class="flex items-center justify-between bg-blue-600 text-white rounded-2xl p-1.5 shadow-lg shadow-blue-600/30">
                    <button @click.stop="incrementCart(product)" class="w-9 h-9 rounded-xl bg-white/20 hover:bg-white/30 text-white font-black flex items-center justify-center transition-colors text-lg">+</button>
                    <div class="flex flex-col items-center">
                      <span class="text-xs font-black">{{ getCartQty(product.id) }} عدد</span>
                      <span class="text-[9px] font-bold text-blue-200">در سبد شما</span>
                    </div>
                    <button @click.stop="decrementCart(product)" class="w-9 h-9 rounded-xl bg-white/20 hover:bg-white/30 text-white font-black flex items-center justify-center transition-colors text-lg">-</button>
                  </div>

                  <button 
                    v-else 
                    @click.stop="incrementCart(product)" 
                    :disabled="!product.inStock"
                    :class="['w-full py-3 px-4 rounded-2xl font-black text-xs transition-all flex items-center justify-center gap-2 shadow-sm', product.inStock ? 'bg-slate-900 hover:bg-blue-600 text-white shadow-slate-900/10 hover:shadow-blue-500/30' : 'bg-slate-100 text-slate-400 cursor-not-allowed']"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                    {{ product.inStock ? 'افزودن به سبد خرید' : 'کالا ناموجود است' }}
                  </button>
                </div>

              </div>
            </div>
          </transition-group>

          <!-- حالت خالی (نتایج یافت نشد) -->
          <div v-else class="bg-white rounded-[2.5rem] border border-slate-200/80 border-dashed p-16 flex flex-col items-center justify-center text-center">
            <div class="w-20 h-20 bg-slate-50 text-slate-300 rounded-full flex items-center justify-center mb-6">
              <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </div>
            <h3 class="text-xl font-black text-slate-800 mb-2">کالایی با این مشخصات یافت نشد</h3>
            <p class="text-slate-500 font-bold text-sm">لطفاً فیلترهای جستجو را تغییر دهید یا محدودیت قیمت را بردارید.</p>
            <button @click="clearFilters" class="mt-6 bg-slate-900 hover:bg-blue-600 text-white px-8 py-3.5 rounded-2xl font-black text-xs transition-colors shadow-lg">پاک کردن همه فیلترها</button>
          </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute ? useRoute() : { params: { id: 'all' } };
const router = useRouter ? useRouter() : null;

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://tajerbam.com';

const isLoading = ref(true);
const cart = ref([]);

// State for Filters
const filters = ref({
  search: '',
  categories: [],
  minPrice: null,
  maxPrice: null,
  minPriceDisplay: '',
  maxPriceDisplay: '',
  inStock: false,
  insured: false
});

const sortBy = ref('popular'); // popular, newest, price_asc, price_desc

const currentCategory = ref(null);
const subCategories = ref([]);
const products = ref([]);

// Sync Cart State
const syncCart = () => {
  try {
    cart.value = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  } catch (e) {
    cart.value = [];
  }
};

const getCartQty = (productId) => {
  const item = cart.value.find(i => i.id === productId);
  return item ? item.qty : 0;
};

const incrementCart = (product) => {
  let cartItems = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  const idx = cartItems.findIndex(item => item.id === product.id);
  const minQty = product.minQty || 1;
  const wholesalePrice = product.wholesalePrice || product.retailPrice || 0;

  if (idx > -1) {
    cartItems[idx].qty += 1;
  } else {
    cartItems.push({
      id: product.id,
      name: product.name,
      seller: product.seller,
      img: product.img,
      unitPrice: wholesalePrice,
      qty: minQty,
      minOrder: minQty
    });
  }
  localStorage.setItem('tajerbam_cart', JSON.stringify(cartItems));
  cart.value = cartItems;
  window.dispatchEvent(new Event('storage'));
};

const decrementCart = (product) => {
  let cartItems = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  const idx = cartItems.findIndex(item => item.id === product.id);
  if (idx > -1) {
    const minQty = product.minQty || 1;
    if (cartItems[idx].qty > minQty) {
      cartItems[idx].qty -= 1;
    } else {
      cartItems.splice(idx, 1);
    }
    localStorage.setItem('tajerbam_cart', JSON.stringify(cartItems));
    cart.value = cartItems;
    window.dispatchEvent(new Event('storage'));
  }
};

const navigateTo = (path) => {
  if (router) router.push(path);
  else window.location.href = path;
};

const navigateToProduct = (productId) => {
  navigateTo(`/product/${productId}`);
};

const fetchData = async () => {
  isLoading.value = true;
  syncCart();
  
  const activeCatId = route.params?.id || 'all';

  try {
    // 1. Fetch Categories
    const catRes = await fetch(`${API_BASE_URL}/api/categories`).catch(() => null);
    if (catRes && catRes.ok) {
      const catData = await catRes.json();
      if (Array.isArray(catData)) {
        if (activeCatId !== 'all') {
          currentCategory.value = catData.find(c => c.id == activeCatId || c.slug == activeCatId) || catData[0];
        } else {
          currentCategory.value = { name: 'همه کالاهای عمده B2B', description: 'دایرکتوری کامل محصولات عمده و تامین‌کنندگان تایید شده تاجربام' };
        }
        
        // Extract subcategories
        if (currentCategory.value && currentCategory.value.children) {
          subCategories.value = currentCategory.value.children.map(c => ({
            id: c.id,
            name: c.name,
            count: c.products_count || 0
          }));
        } else {
          subCategories.value = catData.filter(c => c.parent_id).map(c => ({ id: c.id, name: c.name, count: c.products_count || 0 }));
        }
      }
    }

    // 2. Fetch Products
    const prodUrl = (activeCatId !== 'all' && !isNaN(activeCatId)) 
      ? `${API_BASE_URL}/api/products?category_id=${activeCatId}`
      : `${API_BASE_URL}/api/products`;
      
    const res = await fetch(prodUrl).catch(() => null);
    if (res && res.ok) {
      const data = await res.json();
      const items = Array.isArray(data) ? data : (data.products || []);
      
      if (items.length > 0) {
        products.value = items.map(p => ({
          id: p.id,
          name: p.title || p.name,
          seller: p.seller || 'تامین‌کننده تایید شده',
          rating: p.rating || '۴.۸',
          img: p.image_url || p.img || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png',
          retailPrice: p.price_retail || p.price || 10000,
          wholesalePrice: p.wholesalePrice || p.price_tiers?.[0]?.price_per_unit || (p.price_retail * 0.9) || 9000,
          minQty: p.minQty || p.price_tiers?.[0]?.min_qty || 5,
          insured: p.insured !== undefined ? p.insured : true,
          inStock: p.inStock !== undefined ? p.inStock : (p.stock > 0),
          categoryId: p.category_id || 1,
          createdAt: p.created_at ? new Date(p.created_at).getTime() : Date.now()
        }));
      } else {
        throw new Error("No products found from API");
      }
    } else {
      throw new Error("Product API Request failed");
    }
  } catch (error) {
    // Fallback Ultra Premium Mock Data for offline testing
    setTimeout(() => {
      products.value = [
        { id: 1, name: 'لپ‌تاپ ۱۵.۶ اینچی ایسوس مدل Vivobook 15 پردازنده i7', seller: 'رایان تکرو', rating: '۴.۸', img: 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png', retailPrice: 42500000, wholesalePrice: 39800000, minQty: 5, insured: true, inStock: true, categoryId: 1, createdAt: Date.now() - 1000 },
        { id: 2, name: 'گوشی موبایل سامسونگ Galaxy S23 Ultra', seller: 'دیجیتال شاپ', rating: '۴.۹', img: 'https://freepngimg.com/thumb/smartphone/133618-smart-phone-apple-free-photo.png', retailPrice: 52000000, wholesalePrice: 48500000, minQty: 10, insured: true, inStock: true, categoryId: 2, createdAt: Date.now() - 5000 },
        { id: 3, name: 'ساعت هوشمند اپل واچ سری 9 اورجینال', seller: 'واردات مستقیم', rating: '۴.۶', img: 'https://freepngimg.com/thumb/smart_watch/133618-watch-smart-apple-free-photo.png', retailPrice: 22000000, wholesalePrice: 19500000, minQty: 5, insured: true, inStock: true, categoryId: 3, createdAt: Date.now() - 10000 },
        { id: 4, name: 'موس بی‌سیم تسکو مدل TM-101 (پک ۵۰ عددی)', seller: 'عمده‌فروشی تبریز', rating: '۴.۲', img: 'https://freepngimg.com/thumb/mouse/10-mouse-png-image.png', retailPrice: 280000, wholesalePrice: 210000, minQty: 50, insured: false, inStock: true, categoryId: 3, createdAt: Date.now() - 2000 },
        { id: 5, name: 'مانیتور ۲۷ اینچ خمیده سامسونگ FHD', seller: 'رایان تکرو', rating: '۴.۷', img: 'https://freepngimg.com/thumb/monitor/6-2-monitor-png-picture.png', retailPrice: 12500000, wholesalePrice: 10800000, minQty: 3, insured: true, inStock: false, categoryId: 4, createdAt: Date.now() - 8000 },
        { id: 6, name: 'مینی فرز رونیکس صنعتی ۳۱۳۰', seller: 'صنعت پیشرو', rating: '۴.۵', img: 'https://freepngimg.com/thumb/tools/3-2-tools-png-clipart.png', retailPrice: 2400000, wholesalePrice: 1980000, minQty: 10, insured: true, inStock: true, categoryId: 5, createdAt: Date.now() - 3000 }
      ];
      if (!currentCategory.value) {
        currentCategory.value = { name: 'کالای دیجیتال و ابزارآلات', description: 'تامین بدون واسطه انواع محصولات صنعتی و الکترونیکی' };
      }
      subCategories.value = [
        { id: 1, name: 'لپ‌تاپ و الترابوک', count: 24 },
        { id: 2, name: 'موبایل و تبلت', count: 48 },
        { id: 3, name: 'لوازم جانبی', count: 120 },
        { id: 4, name: 'مانیتور و قطعات', count: 18 }
      ];
      isLoading.value = false;
    }, 600);
  } finally {
    isLoading.value = false;
  }
};

const toggleSubcategoryFilter = (subId) => {
  const index = filters.value.categories.indexOf(subId);
  if (index > -1) {
    filters.value.categories.splice(index, 1);
  } else {
    filters.value.categories.push(subId);
  }
};

const formatPrice = (price) => {
  if (!price) return '۰';
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};

const formatPriceInput = (e, field) => {
  let val = e.target.value.replace(/\D/g, '');
  filters.value[field] = val ? parseInt(val) : null;
  filters.value[field + 'Display'] = val ? parseInt(val).toLocaleString('en-US') : '';
};

const clearFilters = () => {
  filters.value = {
    search: '',
    categories: [],
    minPrice: null,
    maxPrice: null,
    minPriceDisplay: '',
    maxPriceDisplay: '',
    inStock: false,
    insured: false
  };
};

const filteredAndSortedProducts = computed(() => {
  let result = products.value;

  // 1. Search Filter
  if (filters.value.search) {
    const q = filters.value.search.toLowerCase();
    result = result.filter(p => p.name.toLowerCase().includes(q) || p.seller.toLowerCase().includes(q));
  }

  // 2. Subcategory Filter
  if (filters.value.categories.length > 0) {
    result = result.filter(p => filters.value.categories.includes(p.categoryId));
  }

  // 3. Price Filter
  if (filters.value.minPrice) {
    result = result.filter(p => p.wholesalePrice >= filters.value.minPrice);
  }
  if (filters.value.maxPrice) {
    result = result.filter(p => p.wholesalePrice <= filters.value.maxPrice);
  }

  // 4. Stock & Insurance Toggles
  if (filters.value.inStock) {
    result = result.filter(p => p.inStock);
  }
  if (filters.value.insured) {
    result = result.filter(p => p.insured);
  }

  // 5. Sorting
  return result.slice().sort((a, b) => {
    if (sortBy.value === 'price_asc') return a.wholesalePrice - b.wholesalePrice;
    if (sortBy.value === 'price_desc') return b.wholesalePrice - a.wholesalePrice;
    if (sortBy.value === 'newest') return b.createdAt - a.createdAt;
    // popular (default)
    return parseFloat(b.rating) - parseFloat(a.rating);
  });
});

onMounted(() => {
  fetchData();
  window.addEventListener('storage', syncCart);
});

onUnmounted(() => {
  window.removeEventListener('storage', syncCart);
});
</script>

<style scoped>
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }

/* Transition Group Animations for Grid */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: scale(0.92) translateY(20px);
}
.list-leave-active {
  position: absolute;
}
</style>