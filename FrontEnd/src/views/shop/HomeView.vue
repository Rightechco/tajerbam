<template>
  <div class="tajerbam-premium-home bg-slate-50 font-sans text-slate-800 overflow-x-hidden min-h-screen flex flex-col" dir="rtl">
    
    <!-- ================= 1. Top Bar (نوار اطلاعیه هوشمند) ================= -->
    <div v-show="showTopBar" class="hidden lg:flex items-center justify-between bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-slate-300 text-[11px] font-bold px-8 h-11 fixed top-0 left-0 w-full z-[60] border-b border-white/5">
      <div class="flex items-center gap-6">
        <span class="flex items-center gap-1.5 hover:text-white transition-colors cursor-pointer">
          <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          پشتیبانی ۲۴/۷ B2B: ۰۲۱-۹۱۰۰XXXX
        </span>
        <span class="flex items-center gap-1.5 hover:text-white transition-colors cursor-pointer">
          <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"></path></svg>
          زبان: فارسی / ارز: تومان (IRR)
        </span>
      </div>
      <div class="flex items-center gap-5">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          <span class="text-emerald-400 font-mono tracking-widest">سیستم پرداخت امن (Escrow) فعال است</span>
        </div>
        <div class="w-px h-4 bg-slate-700"></div>
        <router-link to="/marketer" class="hover:text-white transition-colors flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> همکاری در فروش</router-link>
        <router-link to="/admin" class="text-indigo-400 hover:text-indigo-300 transition-colors flex items-center gap-1">ورود مدیریت <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path></svg></router-link>
      </div>
    </div>

    <!-- ================= 2. Mega Navbar (هدر چسبان و شیشه‌ای) ================= -->
    <header :class="[
      'fixed left-0 w-full z-50 transition-all duration-500 ease-out',
      showTopBar ? 'lg:top-11 top-0' : 'top-0',
      isScrolled ? 'bg-white/95 backdrop-blur-2xl shadow-[0_10px_40px_rgba(0,0,0,0.06)] border-b border-slate-200/80 py-3' : 'bg-slate-900/90 backdrop-blur-xl border-b border-white/10 py-5'
    ]">
      <div class="container mx-auto px-4 lg:px-8 flex items-center justify-between gap-4 md:gap-8">
        
        <!-- لوگو و برند -->
        <div class="flex items-center gap-8 shrink-0">
          <router-link to="/" class="flex items-center gap-3 group relative">
            <div class="absolute inset-0 bg-blue-500 blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500"></div>
            <div class="w-12 h-12 md:w-14 md:h-14 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-600/30 transform group-hover:scale-105 group-hover:-rotate-3 transition-all duration-300">
              <svg class="w-6 h-6 md:w-7 md:h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            </div>
            <div class="flex flex-col">
              <span :class="['text-2xl md:text-3xl font-black tracking-tighter transition-colors duration-500', isScrolled ? 'text-slate-900' : 'text-white drop-shadow-md']">تاجربام</span>
              <span :class="['text-[9px] md:text-[10px] font-black tracking-[0.25em] transition-colors duration-500', isScrolled ? 'text-blue-600' : 'text-blue-300 drop-shadow-md']">B2B NETWORK</span>
            </div>
          </router-link>

          <!-- منوی دسکتاپ (مگامنو متصل به دیتابیس) -->
          <nav class="hidden lg:flex items-center gap-2">
            
            <div class="relative group px-3 py-2 cursor-pointer h-full flex items-center" @mouseenter="isMegaMenuOpen = true" @mouseleave="isMegaMenuOpen = false">
              <span :class="['text-sm font-black flex items-center gap-1.5 transition-all duration-300 px-4 py-2.5 rounded-xl border border-transparent', isScrolled ? 'text-slate-700 hover:bg-slate-50 hover:text-blue-600 hover:border-slate-200' : 'text-white hover:bg-white/10 hover:border-white/20']">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                دسته‌بندی کالاها 
                <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
              </span>
              
              <!-- ساختار مگامنو (دریافت داینامیک دسته‌های والد و فرزند از DB) -->
              <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-4" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
                <div v-show="isMegaMenuOpen" class="absolute top-full right-0 pt-4 w-[920px] cursor-default">
                  <div class="bg-white/95 backdrop-blur-3xl rounded-[2.5rem] shadow-[0_40px_100px_rgba(0,0,0,0.12)] border border-slate-200/80 p-8 flex gap-8 relative overflow-hidden text-right">
                    <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-100 rounded-full mix-blend-multiply filter blur-[60px] opacity-60"></div>
                    
                    <!-- منوی عمودی دسته‌های والد DB -->
                    <div class="w-1/3 border-l border-slate-100 pl-6 flex flex-col gap-2 max-h-[420px] overflow-y-auto custom-scrollbar">
                      <div v-for="cat in parentCategories" :key="cat.id" @mouseenter="activeMegaCategory = cat" :class="['px-4 py-3 rounded-2xl flex items-center justify-between font-black text-sm transition-all cursor-pointer', activeMegaCategory?.id === cat.id ? 'bg-blue-50 text-blue-700 shadow-sm border border-blue-100' : 'text-slate-600 hover:bg-slate-50']">
                        <div class="flex items-center gap-3">
                          <div class="w-8 h-8 rounded-xl flex items-center justify-center shrink-0" :class="activeMegaCategory?.id === cat.id ? 'bg-blue-100 text-blue-600' : 'bg-slate-100 text-slate-400'" v-html="getCategorySvgIcon(cat.icon)"></div>
                          <span class="truncate">{{ cat.name }}</span>
                        </div>
                        <svg class="w-4 h-4 shrink-0 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                      </div>
                    </div>

                    <!-- زیردسته‌ها (Dynamic Subcategories) -->
                    <div class="w-2/3 pr-2 relative z-10">
                      <div v-if="activeMegaCategory" class="animate-fade-in">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-4 mb-6">
                          <h3 class="font-black text-slate-800 text-lg flex items-center gap-2">
                            <span v-html="getCategorySvgIcon(activeMegaCategory.icon)" class="text-blue-600"></span> 
                            {{ activeMegaCategory.name }}
                          </h3>
                          <router-link :to="`/category/${activeMegaCategory.id}`" class="text-xs font-bold text-blue-600 hover:underline flex items-center gap-1">
                            مشاهده تمام کالاها ({{ activeMegaCategory.products_count || 0 }})
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                          </router-link>
                        </div>

                        <!-- زیرمجموعه‌های دسته انتخاب شده -->
                        <div v-if="activeMegaCategory.children && activeMegaCategory.children.length > 0" class="grid grid-cols-2 gap-x-6 gap-y-4 max-h-[260px] overflow-y-auto custom-scrollbar pr-2">
                          <div v-for="sub in activeMegaCategory.children" :key="sub.id" class="bg-slate-50/80 p-3.5 rounded-2xl border border-slate-100 hover:border-blue-200 hover:bg-blue-50/30 transition-all cursor-pointer" @click="$router.push(`/category/${sub.id}`)">
                            <div class="font-black text-slate-800 text-sm mb-1 flex items-center justify-between hover:text-blue-600">
                              <span class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>{{ sub.name }}</span>
                              <span class="text-[10px] font-bold text-slate-400 bg-white px-2 py-0.5 rounded-full border border-slate-100">{{ sub.products_count || 0 }}</span>
                            </div>
                            <p class="text-[11px] text-slate-400 font-medium line-clamp-1 mt-1">{{ sub.description || 'تامین مستقیم از تولیدکننده' }}</p>
                          </div>
                        </div>

                        <div v-else class="py-12 text-center text-slate-400 font-bold bg-slate-50 rounded-2xl border border-dashed border-slate-200">
                          زیردسته‌ای ثبت نشده است. برای مشاهده کالاهای مستقیم کلیک کنید.
                        </div>
                        
                        <!-- بنر پیش فرض داخل مگامنو -->
                        <div class="mt-6 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-2xl p-4 flex items-center justify-between text-white shadow-lg relative overflow-hidden group/banner cursor-pointer" @click="$router.push(`/category/${activeMegaCategory.id}`)">
                          <div class="relative z-10">
                            <p class="font-black text-sm mb-1">استعلام قیمت عمده {{ activeMegaCategory.name }}</p>
                            <p class="text-[10px] font-medium text-blue-200">با تضمین پایین‌ترین نرخ B2B و ارسال مستقیم از انبار تامین‌کننده</p>
                          </div>
                          <div class="w-10 h-10 bg-white/20 backdrop-blur rounded-xl flex items-center justify-center transform group-hover/banner:translate-x-1 transition-transform relative z-10">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </transition>
            </div>

            <router-link to="/buyer/rfq" :class="['px-4 py-2.5 rounded-xl text-sm font-black transition-colors', isScrolled ? 'text-slate-700 hover:bg-slate-50 hover:text-blue-600' : 'text-white hover:bg-white/10']">استعلام خرید (RFQ)</router-link>
            <router-link to="/marketer" :class="['px-4 py-2.5 rounded-xl text-sm font-black transition-colors flex items-center gap-1.5', isScrolled ? 'text-slate-700 hover:bg-slate-50 hover:text-blue-600' : 'text-white hover:bg-white/10']">
              بازاریابی <span class="bg-rose-500 text-white text-[9px] px-1.5 py-0.5 rounded-md shadow-sm animate-pulse">Hot</span>
            </router-link>
          </nav>
        </div>

        <!-- جستجوی زنده (Live Search Engine) -->
        <div class="hidden md:block flex-1 max-w-2xl mx-8 relative" ref="searchContainerRef">
          <div class="relative group">
            <div :class="['absolute -inset-1 rounded-2xl blur opacity-0 transition duration-500', isSearchFocused ? 'bg-gradient-to-r from-blue-500 to-indigo-500 opacity-20' : '']"></div>
            <div :class="['relative flex items-center w-full rounded-2xl border transition-all duration-300', isHomePage && !isScrolled ? (isSearchFocused ? 'bg-white border-white shadow-xl' : 'bg-white/10 border-white/20 backdrop-blur-md') : 'bg-slate-50 border-slate-200 focus-within:bg-white focus-within:border-blue-300 focus-within:shadow-lg']">
              
              <div class="relative flex-shrink-0">
                <select v-model="selectedCategoryFilter" @change="handleSearch" :class="['bg-transparent border-none text-xs font-black pl-2 pr-4 py-3.5 outline-none cursor-pointer border-l transition-colors', (isHomePage && !isScrolled && !isSearchFocused) ? 'text-white border-white/20 [&>option]:text-slate-800' : 'text-slate-600 border-slate-200']">
                  <option value="all">همه دسته‌ها</option>
                  <option v-for="cat in parentCategories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                </select>
              </div>

              <input 
                type="text" 
                v-model="searchQuery" 
                @focus="isSearchFocused = true"
                @input="handleSearch"
                @keydown.enter="executePrimarySearch"
                placeholder="جستجوی کالای عمده، تامین‌کننده، برند یا شناسه (SKU)..." 
                :class="['w-full bg-transparent border-none outline-none text-sm font-bold px-4 transition-colors', (isHomePage && !isScrolled && !isSearchFocused) ? 'text-white placeholder-white/70' : 'text-slate-800 placeholder-slate-400']"
              >
              
              <button @click="executePrimarySearch" class="bg-blue-600 hover:bg-blue-500 text-white p-2.5 rounded-xl m-1.5 transition-colors shadow-md flex-shrink-0">
                <svg v-if="!isSearching" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <svg v-else class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              </button>
            </div>
          </div>

          <!-- باکس نتایج جستجو (Dropdown) -->
          <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-2">
            <div v-if="isSearchFocused && (searchResults.length > 0 || searchQuery.length >= 2)" class="absolute top-[calc(100%+8px)] left-0 right-0 bg-white rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.12)] border border-slate-100 p-4 z-[100] overflow-hidden">
              <div v-if="searchResults.length > 0" class="max-h-[60vh] overflow-y-auto custom-scrollbar pr-2">
                <div class="text-[10px] font-black text-slate-400 mb-3 px-2 flex justify-between items-center">
                  <span>{{ searchResults.length }} نتیجه برای "{{ searchQuery }}"</span>
                  <span class="text-[9px] text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">جستجوی هوشمند</span>
                </div>
                <ul class="space-y-2">
                  <li v-for="item in searchResults" :key="item.id" @click="isSearchFocused = false">
                    <router-link :to="`/product/${item.id}`" class="flex items-center gap-4 p-3 rounded-2xl hover:bg-slate-50 transition-colors group/item">
                      <div class="w-14 h-14 bg-white border border-slate-100 rounded-xl p-1 shrink-0 flex items-center justify-center overflow-hidden">
                        <img :src="item.img" class="max-h-full max-w-full object-contain">
                      </div>
                      <div class="flex-grow">
                        <h4 class="font-black text-slate-800 text-sm group-hover/item:text-blue-600 transition-colors line-clamp-1 mb-1">{{ item.name }}</h4>
                        <div class="flex items-center gap-2 flex-wrap">
                          <span class="text-[10px] font-mono font-bold text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">SKU: {{ item.sku }}</span>
                          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md">تامین‌کننده: {{ item.seller }}</span>
                          <span class="text-[10px] font-black text-blue-600 bg-blue-50 border border-blue-100 px-2 py-0.5 rounded-md">شروع از: {{ formatPrice(item.price) }} ت</span>
                        </div>
                      </div>
                      <svg class="w-5 h-5 text-slate-300 group-hover/item:text-blue-500 transform group-hover/item:-translate-x-1 transition-all shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                    </router-link>
                  </li>
                </ul>
              </div>
              <div v-else-if="!isSearching && searchQuery.length >= 2" class="py-10 text-center flex flex-col items-center">
                <div class="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center text-slate-300 mb-4"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
                <p class="font-black text-slate-600 text-sm mb-1">کالایی با عبارت "{{ searchQuery }}" یافت نشد!</p>
                <p class="text-xs font-bold text-slate-400">لطفاً املای کلمه را بررسی کنید یا از کلمات عمومی‌تر استفاده نمایید.</p>
              </div>
            </div>
          </transition>
        </div>

        <!-- ابزارها و پنل کاربری -->
        <div class="flex items-center gap-2 md:gap-4 shrink-0">
          <router-link to="/cart" class="relative group p-2 md:p-3">
            <div :class="['absolute inset-0 rounded-xl transition-all duration-300', isScrolled ? 'bg-slate-100 group-hover:bg-slate-200' : 'bg-white/10 backdrop-blur-md border border-white/20 group-hover:bg-white/20']"></div>
            <svg :class="['w-6 h-6 relative z-10 transition-colors duration-300', isScrolled ? 'text-slate-700' : 'text-white']" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            <span v-if="cartItemCount > 0" class="absolute -top-1 -right-1 w-5 h-5 bg-rose-500 text-white text-[10px] font-black rounded-full flex items-center justify-center shadow-lg border-2 border-white transform scale-100 group-hover:scale-110 transition-transform z-20">{{ cartItemCount }}</span>
          </router-link>

          <div class="relative ml-2">
            <template v-if="isLoggedIn">
              <button @click="goToDashboard" :class="['px-4 md:px-5 py-2.5 md:py-3 rounded-xl font-black text-sm transition-all shadow-lg flex items-center gap-2.5', isScrolled ? 'bg-slate-900 text-white hover:bg-slate-800' : 'bg-white/10 backdrop-blur-md text-white border border-white/20 hover:bg-white/20']">
                <div class="w-6 h-6 rounded-full bg-white/20 flex items-center justify-center text-xs border border-white/30 backdrop-blur-sm">{{ userName.charAt(0) || 'ک' }}</div>
                <span class="hidden sm:block">میزکار من</span>
              </button>
            </template>
            <template v-else>
              <router-link to="/login" :class="['px-5 md:px-6 py-2.5 md:py-3 rounded-xl font-black text-sm transition-all flex items-center gap-2 border shadow-sm', isScrolled ? 'bg-white border-slate-200 text-slate-800 hover:border-blue-400 hover:text-blue-600' : 'bg-white/10 border-white/20 text-white hover:bg-white/20 backdrop-blur-md']">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path></svg>
                ورود / عضویت
              </router-link>
            </template>
          </div>
        </div>

      </div>
    </header>

    <!-- ================= 3. Hero Section (بخش قهرمان سه بعدی) ================= -->
    <section class="relative min-h-[95vh] flex items-center justify-center overflow-hidden bg-[#0f172a] pt-32 pb-20 perspective-1000">
      
      <!-- افکت‌های بک‌گراند اولترا پریمیوم -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute -top-[10%] -left-[10%] w-[50vw] h-[50vw] bg-blue-600/30 rounded-full mix-blend-color-dodge filter blur-[120px] animate-blob"></div>
        <div class="absolute top-[20%] -right-[10%] w-[40vw] h-[40vw] bg-indigo-500/20 rounded-full mix-blend-color-dodge filter blur-[100px] animate-blob animation-delay-2000"></div>
        <div class="absolute -bottom-[20%] left-[20%] w-[60vw] h-[60vw] bg-fuchsia-600/20 rounded-full mix-blend-color-dodge filter blur-[130px] animate-blob animation-delay-4000"></div>
        <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCI+CjxwYXRoIGQ9Ik0wIDBoNDB2NDBIMHoiIGZpbGw9Im5vbmUiLz4KPHBhdGggZD0iTTAgMTBoNDBNMTAgMHY0ME0wIDIwaDQwTTIwIDB2NDBNMCAzMGg0ME0zMCAwdjQwIiBzdHJva2U9InJnYmEoMjU1LDI1NSwyNTUsMC4wMykiIHN0cm9rZS13aWR0aD0iMSIvPgo8L3N2Zz4=')] opacity-50"></div>
      </div>

      <div class="container mx-auto px-4 relative z-10 text-center flex flex-col items-center">
        <div class="animate-fade-in-up" style="animation-delay: 0.1s;">
          <div class="inline-flex items-center gap-2 bg-white/5 border border-white/10 text-blue-200 px-6 py-2.5 rounded-full text-xs font-black mb-8 backdrop-blur-xl shadow-2xl hover:bg-white/10 transition-colors cursor-pointer group">
            <span class="relative flex h-2.5 w-2.5">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
            </span>
            اکوسیستم هوشمند تامین و توزیع B2B
            <svg class="w-4 h-4 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          </div>
        </div>

        <h1 class="text-5xl md:text-7xl lg:text-[5.5rem] font-black text-white tracking-tighter mb-6 leading-[1.1] animate-fade-in-up drop-shadow-2xl" style="animation-delay: 0.2s;">
          آینده تجارت عمده، <br class="hidden md:block">
          <span class="relative inline-block mt-2">
            <span class="relative z-10 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">بدون واسطه و امن.</span>
            <span class="absolute bottom-1 left-0 w-full h-4 bg-blue-600/30 -z-10 transform -skew-x-12"></span>
          </span>
        </h1>
        
        <p class="text-slate-400 font-medium text-lg md:text-xl max-w-3xl mx-auto leading-relaxed mb-12 animate-fade-in-up" style="animation-delay: 0.3s;">
          مستقیماً به <b class="text-slate-200">۵,۴۰۰+ واردکننده و تولیدکننده</b> متصل شوید. با سیستم پرداخت تضمینی (Escrow) تاجربام، تا زمان دریافت و تایید سلامت کالا، وجه شما نزد ما محفوظ می‌ماند.
        </p>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-5 w-full sm:w-auto animate-fade-in-up" style="animation-delay: 0.4s;">
          <button @click="$router.push('/category/all')" class="w-full sm:w-auto bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-black px-10 py-5 rounded-2xl shadow-[0_15px_40px_rgba(37,99,235,0.4)] transition-all hover:-translate-y-1 hover:scale-105 flex items-center justify-center gap-3 text-lg border border-blue-500/50">
            جستجو در بازار عمده
            <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
          <button @click="showVideoModal = true" class="w-full sm:w-auto bg-white/5 hover:bg-white/10 border border-white/10 backdrop-blur-xl text-white font-bold px-8 py-5 rounded-2xl transition-all hover:-translate-y-1 flex items-center justify-center gap-3 text-base group">
            <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center group-hover:bg-white/20 transition-colors">
              <svg class="w-4 h-4 ml-1 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4l12 6-12 6z"></path></svg>
            </div>
            مشاهده ویدیوی پلتفرم
          </button>
        </div>

        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png" class="absolute hidden lg:block right-10 top-1/4 w-32 filter drop-shadow-2xl animate-float" style="animation-delay: 1s;" alt="Laptop">
        <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Package.png" class="absolute hidden lg:block left-10 bottom-1/4 w-32 filter drop-shadow-2xl animate-float-reverse" style="animation-delay: 0.5s;" alt="Package">
      </div>

      <div class="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] transform rotate-180 pointer-events-none">
        <svg class="relative block w-[calc(100%+1.3px)] h-[80px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
          <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" class="fill-slate-50"></path>
        </svg>
      </div>
    </section>

    <!-- Live Market Ticker (رنگ آبی و موقعیت اصلی بعد از هیرو) -->
    <div class="bg-blue-600 text-white py-3.5 overflow-hidden relative border-y border-blue-500 shadow-inner z-20">
      <div class="flex whitespace-nowrap animate-marquee items-center text-xs font-extrabold tracking-wide">
        <div v-for="i in 3" :key="i" class="flex items-center">
          <span class="mx-8 flex items-center gap-2 text-white"><span class="w-2 h-2 bg-emerald-400 rounded-full animate-ping"></span> آخرین معامله B2B: ۵۰ عدد لپ‌تاپ ایسوس (دقایقی پیش)</span>
          <span class="mx-4 text-blue-300">|</span>
          <span class="mx-8 flex items-center gap-1.5 text-amber-300"><svg class="w-4 h-4 text-amber-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> تامین‌کننده برتر هفته: رایان تکرو</span>
          <span class="mx-4 text-blue-300">|</span>
          <span class="mx-8 flex items-center gap-1.5 text-emerald-300"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> رشد ۳.۲٪ استعلام‌های فعال تجهیزات دیجیتال</span>
          <span class="mx-4 text-blue-300">|</span>
        </div>
      </div>
    </div>

    <!-- Value Proposition Cards (انتقال به پایین‌تر بدون تداخل با زیرنویس) -->
    <div class="container mx-auto px-4 py-8 my-2 relative z-30">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="(feature, idx) in features" :key="idx" class="bg-white rounded-3xl p-6 shadow-[0_15px_40px_rgba(0,0,0,0.04)] border border-slate-100 hover:-translate-y-2 transition-transform duration-300 group">
          <div :class="`w-12 h-12 rounded-2xl mb-4 flex items-center justify-center shadow-inner ${feature.bg} ${feature.color} group-hover:scale-110 transition-transform`" v-html="feature.icon"></div>
          <h3 class="text-base font-black text-slate-800 mb-1.5">{{ feature.title }}</h3>
          <p class="text-xs font-bold text-slate-500 leading-relaxed">{{ feature.desc }}</p>
        </div>
      </div>
    </div>

    <!-- ================= 4. Premium Parent Categories (اسلایدر روشن اولترا پریمیوم بدون اسکرول‌بار) ================= -->
    <section class="py-16 bg-slate-50 border-y border-slate-200/60 relative overflow-hidden my-6">
      <!-- Background Ambient Glows -->
      <div class="absolute -left-20 top-0 w-96 h-96 bg-blue-500/5 rounded-full blur-[100px] pointer-events-none"></div>
      <div class="absolute -right-20 bottom-0 w-96 h-96 bg-indigo-500/5 rounded-full blur-[100px] pointer-events-none"></div>

      <div class="container mx-auto px-4 lg:px-8 relative z-10">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <div class="inline-flex items-center gap-2 text-blue-600 font-black text-xs uppercase tracking-wider mb-2">
              <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
              بازار تخصصی B2B
            </div>
            <h2 class="text-3xl md:text-4xl font-black text-slate-800 tracking-tight mb-2">دسته‌بندی‌های استراتژیک</h2>
            <p class="text-slate-500 font-bold text-sm">دسترسی سریع به دسته‌های اصلی دیتابیس با تامین‌کنندگان احراز شده.</p>
          </div>

          <!-- Slider Nav Controls & View All -->
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-2 bg-white p-1.5 rounded-2xl border border-slate-200 shadow-sm">
              <button @click="scrollCategorySlider('rtl')" class="w-10 h-10 rounded-xl bg-slate-100 hover:bg-blue-600 text-slate-600 hover:text-white flex items-center justify-center transition-all active:scale-95" title="قبلی">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
              </button>
              <button @click="scrollCategorySlider('ltr')" class="w-10 h-10 rounded-xl bg-slate-100 hover:bg-blue-600 text-slate-600 hover:text-white flex items-center justify-center transition-all active:scale-95" title="بعدی">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
              </button>
            </div>
            <button @click="$router.push('/category/all')" class="text-xs font-black text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 px-5 py-3 rounded-2xl transition-all shadow-lg shadow-blue-600/20 border border-blue-400/30 flex items-center gap-1.5">
              مشاهده همه
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
            </button>
          </div>
        </div>

        <div v-if="isLoading" class="flex justify-center py-12">
          <svg class="w-12 h-12 text-blue-600 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        </div>

        <div v-else-if="parentCategories.length === 0" class="text-center py-12 text-slate-400 font-bold bg-white rounded-3xl border border-slate-200">
           درحال حاضر دسته‌بندی والد در دیتابیس یافت نشد.
        </div>

        <!-- Ultra Premium Small Square Slider (محیط روشن، بدون مات بودن و بدون اسکرول‌بار ظاهری) -->
        <div v-else ref="categorySliderRef" class="flex items-center gap-5 overflow-x-auto hide-scrollbar snap-x snap-mandatory py-4 scroll-smooth">
          <router-link 
            :to="`/category/${cat.id}`" 
            v-for="cat in parentCategories" 
            :key="cat.id" 
            class="snap-start shrink-0 w-40 h-40 md:w-48 md:h-48 aspect-square rounded-[2.2rem] bg-white border border-slate-200/80 hover:border-blue-500 p-5 flex flex-col items-center justify-between shadow-md hover:shadow-[0_15px_35px_rgba(37,99,235,0.15)] hover:-translate-y-2 transition-all duration-300 group relative overflow-hidden text-center"
          >
            <!-- Top Subtle Glow Line -->
            <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-blue-500 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            
            <!-- Category Image Overlay -->
            <div class="absolute inset-0 bg-cover bg-center opacity-5 group-hover:opacity-15 group-hover:scale-125 transition-all duration-700 pointer-events-none" :style="`background-image: url(${getCategoryImageUrl(cat)})`"></div>

            <!-- Top Badge: Products Count -->
            <div class="w-full flex justify-between items-center relative z-10">
              <span class="bg-blue-50 text-blue-700 border border-blue-100 text-[9px] font-black px-2.5 py-0.5 rounded-full">
                {{ cat.products_count || 0 }} کالا
              </span>
              <div class="w-2 h-2 rounded-full bg-emerald-500 animate-ping opacity-75"></div>
            </div>

            <!-- Center Icon -->
            <div class="relative z-10 my-auto">
              <div class="w-14 h-14 md:w-16 md:h-16 rounded-2xl bg-slate-50 border border-slate-100 group-hover:border-blue-200 group-hover:bg-blue-600 text-blue-600 group-hover:text-white flex items-center justify-center shadow-sm transform group-hover:scale-110 group-hover:-rotate-3 transition-all duration-300">
                <span v-html="getCategorySvgIcon(cat.icon)"></span>
              </div>
            </div>

            <!-- Bottom Title -->
            <div class="w-full relative z-10">
              <h3 class="text-slate-800 font-black text-xs md:text-sm truncate group-hover:text-blue-600 transition-colors">
                {{ cat.name }}
              </h3>
            </div>
          </router-link>
        </div>
      </div>
    </section>

        <!-- ================= 5. Dynamic Flash Sales (Slideable Slider) ================= -->
    <section class="py-24 bg-slate-950 relative overflow-hidden">
      <div class="absolute right-0 top-0 w-1/3 h-full bg-gradient-to-l from-rose-600/20 to-transparent pointer-events-none"></div>
      
      <div class="container mx-auto px-4 relative z-10">
        <div class="flex flex-col lg:flex-row items-center gap-12">
          
          <!-- Timer Column -->
          <div class="w-full lg:w-1/4 flex flex-col items-center lg:items-start text-center lg:text-right">
            <div class="w-16 h-16 bg-rose-500/20 rounded-2xl flex items-center justify-center text-rose-500 mb-6 border border-rose-500/30">
              <svg class="w-8 h-8 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            </div>
            <h2 class="text-4xl font-black text-white mb-4">پیشنهادات <br><span class="text-rose-500">شگفت‌انگیز B2B</span></h2>
            <p class="text-slate-400 text-sm font-medium mb-8 leading-relaxed">تامین‌کنندگان منتخب، موجودی مازاد خود را با قیمت‌های زیر فی بازار و به مدت محدود عرضه می‌کنند.</p>
            
            <div class="flex gap-3" dir="ltr">
              <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-xl p-3 w-16 flex flex-col items-center">
                <span class="text-2xl font-black text-white font-mono">{{ hours }}</span>
                <span class="text-[9px] text-rose-300 font-bold uppercase">Hours</span>
              </div>
              <span class="text-2xl font-black text-slate-500 self-center">:</span>
              <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-xl p-3 w-16 flex flex-col items-center">
                <span class="text-2xl font-black text-white font-mono">{{ minutes }}</span>
                <span class="text-[9px] text-rose-300 font-bold uppercase">Mins</span>
              </div>
              <span class="text-2xl font-black text-slate-500 self-center">:</span>
              <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-xl p-3 w-16 flex flex-col items-center">
                <span class="text-2xl font-black text-white font-mono">{{ seconds }}</span>
                <span class="text-[9px] text-rose-300 font-bold uppercase">Secs</span>
              </div>
            </div>
          </div>

          <!-- Flash Products Slider (Dynamic from DB & Slideable) -->
          <div class="w-full lg:w-3/4 relative">
            <div class="flex justify-between items-center mb-4">
              <span class="text-xs font-bold text-slate-400 hidden lg:inline-block">اسکرول افقی پیشنهادها</span>
              <div class="flex items-center gap-2 mr-auto lg:mr-0">
                <button @click="scrollFlashSlider('rtl')" class="w-10 h-10 rounded-xl bg-white/10 border border-white/20 text-white flex items-center justify-center hover:bg-rose-600 transition-all active:scale-95 shadow-md" title="قبلی">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
                </button>
                <button @click="scrollFlashSlider('ltr')" class="w-10 h-10 rounded-xl bg-white/10 border border-white/20 text-white flex items-center justify-center hover:bg-rose-600 transition-all active:scale-95 shadow-md" title="بعدی">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
                </button>
              </div>
            </div>

            <div v-if="isLoading" class="flex justify-center py-10">
              <svg class="w-10 h-10 text-rose-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            </div>
            
            <div v-else-if="flashProducts.length === 0" class="flex justify-center py-10 text-slate-500 font-bold">
               در حال حاضر پیشنهاد شگفت‌انگیزی وجود ندارد.
            </div>

            <div v-else ref="flashSliderRef" class="flex items-center gap-6 overflow-x-auto hide-scrollbar snap-x snap-mandatory py-4 scroll-smooth">
              <div v-for="prod in flashProducts" :key="prod.id" class="snap-start shrink-0 w-[280px] sm:w-[320px] bg-white rounded-[2.2rem] p-5 shadow-2xl relative overflow-hidden group border border-slate-100 flex flex-col justify-between hover:-translate-y-1.5 transition-all duration-300">
                <div class="absolute top-0 right-0 w-full h-1.5 bg-rose-500 z-20"></div>
                <div class="absolute top-4 left-4 z-20 bg-rose-500 text-white font-black text-xs px-3 py-1 rounded-xl shadow-lg transform -rotate-3">
                  {{ prod.discount }}٪ تخفیف
                </div>
                
                <div class="w-full h-44 bg-slate-50 rounded-[1.5rem] mb-4 p-4 flex items-center justify-center relative overflow-hidden group-hover:bg-rose-50/50 transition-colors cursor-pointer" @click="$router.push(`/product/${prod.id}`)">
                  <img :src="prod.img || 'https://placehold.co/400x400/f8fafc/475569?text=TajerBam'" @error="$event.target.src='https://placehold.co/400x400/f8fafc/475569?text=TajerBam'" class="max-h-full max-w-full object-contain group-hover:scale-110 transition-transform duration-500">
                </div>

                <div class="mb-3 cursor-pointer" @click="$router.push(`/product/${prod.id}`)">
                  <div class="text-[10px] font-bold text-slate-400 mb-1.5 flex justify-between items-center">
                    <span class="flex items-center gap-1 text-blue-600 bg-blue-50 px-2 py-0.5 rounded">{{ prod.seller }}</span>
                    <span class="text-slate-500">حداقل سفارش: {{ prod.min }}</span>
                  </div>
                  <h3 class="font-black text-slate-800 text-sm line-clamp-2 leading-relaxed group-hover:text-rose-600 transition-colors">{{ prod.name }}</h3>
                </div>

                <div class="bg-slate-50 rounded-2xl p-3 border border-slate-100 mb-4">
                  <div class="flex justify-between items-center text-xs mb-1 opacity-60">
                    <span>قیمت بازار:</span>
                    <span class="line-through font-bold">{{ formatPrice(prod.retail) }}</span>
                  </div>
                  <div class="flex justify-between items-end">
                    <span class="text-xs font-black text-rose-600 bg-rose-50 px-2 py-0.5 rounded">حراج عمده:</span>
                    <span class="font-black text-rose-600 text-lg tracking-tight">{{ formatPrice(prod.wholesale) }} <span class="text-[10px]">تومان</span></span>
                  </div>
                </div>

                <!-- Add to Cart with Interactive + / - Stepper -->
                <div class="mt-auto pt-2 border-t border-slate-100">
                  <div v-if="getCartQty(prod.id) === 0" @click.stop="increaseCart(prod)" class="w-full bg-slate-900 hover:bg-rose-600 text-white font-black py-3 px-4 rounded-xl transition-all shadow-md flex items-center justify-center gap-2 cursor-pointer active:scale-95 text-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
                    افزودن به سبد خرید
                  </div>
                  <div v-else class="flex items-center justify-between bg-rose-50 border border-rose-200 rounded-xl p-1.5 text-rose-700 shadow-sm">
                    <button @click.stop="decreaseCart(prod)" class="w-8 h-8 rounded-lg bg-white border border-rose-200 hover:bg-rose-600 hover:text-white text-rose-600 flex items-center justify-center font-black transition-all active:scale-90 shadow-sm" title="کاهش تعداد">
                      <svg v-if="getCartQty(prod.id) === prod.min" class="w-4 h-4 text-rose-500 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                      <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M20 12H4"></path></svg>
                    </button>
                    <span class="font-black text-sm px-2 font-mono">{{ getCartQty(prod.id) }} عدد</span>
                    <button @click.stop="increaseCart(prod)" class="w-8 h-8 rounded-lg bg-rose-600 text-white hover:bg-rose-700 flex items-center justify-center font-black transition-all active:scale-90 shadow-md" title="افزایش تعداد">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
                    </button>
                  </div>
                </div>

              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ================= 6. Dynamic Trending Products (Slideable Slider) ================= -->
    <section class="py-20 bg-slate-50">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <div class="inline-flex items-center gap-2 text-blue-600 font-black text-xs uppercase tracking-wider mb-2">
              <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
              محبوب‌ترین کالاهای بازار
            </div>
            <h2 class="text-3xl md:text-4xl font-black text-slate-800 tracking-tight mb-2">پرطرفدارترین‌های بازار</h2>
            <p class="text-slate-500 font-bold text-sm">کالاهایی که بیشترین حجم معامله را در دیتابیس داشته‌اند.</p>
          </div>

          <!-- Trending Slider Controls -->
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-2 bg-white p-1.5 rounded-2xl border border-slate-200 shadow-sm">
              <button @click="scrollTrendingSlider('rtl')" class="w-10 h-10 rounded-xl bg-slate-100 hover:bg-blue-600 text-slate-600 hover:text-white flex items-center justify-center transition-all active:scale-95" title="قبلی">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
              </button>
              <button @click="scrollTrendingSlider('ltr')" class="w-10 h-10 rounded-xl bg-slate-100 hover:bg-blue-600 text-slate-600 hover:text-white flex items-center justify-center transition-all active:scale-95" title="بعدی">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
              </button>
            </div>
          </div>
        </div>

        <div v-if="isLoading" class="flex justify-center py-10">
          <svg class="w-12 h-12 text-blue-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        </div>

        <div v-else-if="trendingProducts.length === 0" class="text-center py-10 text-slate-500 font-bold">
           کالایی در دیتابیس یافت نشد.
        </div>

        <div v-else ref="trendingSliderRef" class="flex items-center gap-6 overflow-x-auto hide-scrollbar snap-x snap-mandatory py-4 scroll-smooth">
          <div v-for="prod in trendingProducts" :key="prod.id" class="snap-start shrink-0 w-[260px] sm:w-[290px] bg-white rounded-[2rem] p-4 border border-slate-200/80 shadow-[0_8px_20px_rgba(0,0,0,0.03)] hover:shadow-2xl hover:border-blue-300 hover:-translate-y-1 transition-all duration-300 flex flex-col group relative">
            <div class="w-full h-44 bg-slate-50/80 rounded-2xl mb-4 p-4 flex items-center justify-center group-hover:bg-blue-50/50 transition-colors cursor-pointer" @click="$router.push(`/product/${prod.id}`)">
              <img :src="prod.img || 'https://placehold.co/400x400/f8fafc/475569?text=TajerBam'" @error="$event.target.src='https://placehold.co/400x400/f8fafc/475569?text=TajerBam'" class="max-h-full max-w-full object-contain group-hover:scale-110 transition-transform duration-500">
            </div>
            
            <div class="flex-grow flex flex-col justify-between">
              <div class="cursor-pointer mb-3" @click="$router.push(`/product/${prod.id}`)">
                <span class="text-[10px] font-bold text-slate-400 mb-1.5 flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> {{ prod.seller }}</span>
                <h3 class="font-black text-slate-800 text-sm line-clamp-2 leading-relaxed group-hover:text-blue-600 transition-colors">{{ prod.name }}</h3>
              </div>
              
              <div class="bg-slate-50 rounded-xl p-3 border border-slate-100 mb-3">
                 <div class="flex justify-between items-center text-[11px] text-slate-500 font-bold mb-1">
                   <span>شروع قیمت عمده از:</span>
                 </div>
                 <div class="font-black text-blue-700 text-lg tracking-tight">{{ formatPrice(prod.wholesale || prod.retail) }} <span class="text-[10px]">تومان</span></div>
              </div>

              <!-- Add to Cart Stepper (+ / -) -->
              <div class="mt-auto">
                <div v-if="getCartQty(prod.id) === 0" @click.stop="increaseCart(prod)" class="w-full bg-slate-900 hover:bg-blue-600 text-white font-black py-2.5 px-3 rounded-xl transition-all shadow-md flex items-center justify-center gap-2 cursor-pointer active:scale-95 text-xs">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
                  افزودن به سبد
                </div>
                <div v-else class="flex items-center justify-between bg-blue-50 border border-blue-200 rounded-xl p-1.5 text-blue-700 shadow-sm">
                  <button @click.stop="decreaseCart(prod)" class="w-8 h-8 rounded-lg bg-white border border-blue-200 hover:bg-rose-600 hover:border-rose-600 hover:text-white text-blue-600 flex items-center justify-center font-black transition-all active:scale-90 shadow-sm" title="کاهش تعداد">
                    <svg v-if="getCartQty(prod.id) === prod.min" class="w-4 h-4 text-rose-500 hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M20 12H4"></path></svg>
                  </button>
                  <span class="font-black text-sm px-2 font-mono">{{ getCartQty(prod.id) }} عدد</span>
                  <button @click.stop="increaseCart(prod)" class="w-8 h-8 rounded-lg bg-blue-600 text-white hover:bg-blue-700 flex items-center justify-center font-black transition-all active:scale-90 shadow-md" title="افزایش تعداد">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"></path></svg>
                  </button>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ================= 7. Smart RFQ Section (فرم ۴ مرحله‌ای RFQ) ================= -->
    <section id="rfq-section" class="py-24 bg-gradient-to-br from-indigo-900 via-blue-900 to-slate-900 relative overflow-hidden">
      <div class="container mx-auto px-4 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          
          <div class="text-white">
            <div class="w-16 h-16 bg-blue-500/20 border border-blue-500/30 rounded-2xl flex items-center justify-center text-blue-400 mb-6 backdrop-blur-md">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg>
            </div>
            <h2 class="text-4xl md:text-5xl font-black mb-6 tracking-tight">سیستم مناقصه و <br><span class="text-blue-400">استعلام هوشمند (RFQ)</span></h2>
            <p class="text-blue-100/80 font-medium text-lg leading-relaxed mb-8">
              نیاز خرید سازمان یا فروشگاه خود را ثبت کنید. سیستم هوش مصنوعی ما درخواست شما را مستقیماً برای تامین‌کنندگان معتبر ارسال می‌کند.
            </p>
          </div>

          <div class="bg-white rounded-[3rem] p-8 md:p-10 shadow-[0_30px_60px_rgba(0,0,0,0.3)] relative">
            <div class="flex items-center justify-between mb-8 relative">
              <div class="absolute left-0 right-0 top-1/2 h-1 bg-slate-100 -z-10 rounded-full"></div>
              <div class="absolute right-0 top-1/2 h-1 bg-blue-600 -z-10 rounded-full transition-all duration-500" :style="`width: ${(rfqStep - 1) * 33.33}%`"></div>
              
              <div class="flex flex-col items-center gap-2" v-for="i in 4" :key="i">
                <div :class="['w-10 h-10 rounded-full flex items-center justify-center font-black transition-colors shadow-sm', rfqStep >= i ? 'bg-blue-600 text-white shadow-blue-500/40 shadow-lg' : 'bg-white border-2 border-slate-200 text-slate-400']">
                  {{ i }}
                </div>
              </div>
            </div>

            <!-- Step 1: Info & Category -->
            <transition name="slide-fade" mode="out-in">
              <div v-if="rfqStep === 1" key="step1" class="space-y-5">
                <h3 class="text-xl font-black text-slate-800 mb-6">ثبت مشخصات کالا</h3>
                <div>
                  <label class="block text-xs font-bold text-slate-500 mb-2">نام دقیق کالا</label>
                  <input type="text" v-model="rfqData.name" placeholder="مثلا: هارد اکسترنال وسترن دیجیتال 2TB" class="w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 transition-colors font-bold text-sm text-slate-800">
                </div>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-bold text-slate-500 mb-2">دسته‌بندی (ارجاع هوشمند)</label>
                    <select v-model="rfqData.category" class="w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 transition-colors font-bold text-sm text-slate-700 cursor-pointer">
                      <option v-for="cat in parentCategories" :key="cat.id" :value="cat.name">{{ cat.name }}</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-xs font-bold text-slate-500 mb-2">تعداد درخواستی</label>
                    <input type="number" v-model="rfqData.qty" placeholder="100" class="w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 transition-colors font-black text-lg text-slate-800 text-center">
                  </div>
                </div>
                <button @click="rfqStep = 2" :disabled="!rfqData.name || !rfqData.qty" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-2xl shadow-lg transition-all disabled:opacity-50 mt-4">مرحله بعدی</button>
              </div>

              <!-- Step 2: Contact -->
              <div v-else-if="rfqStep === 2" key="step2" class="space-y-5">
                <h3 class="text-xl font-black text-slate-800 mb-6">اطلاعات تماس</h3>
                <div>
                  <label class="block text-xs font-bold text-slate-500 mb-2">شماره موبایل</label>
                  <input type="tel" v-model="rfqData.phone" placeholder="09123456789" class="w-full bg-slate-50 border border-slate-200 p-4 rounded-2xl outline-none text-center font-black text-lg">
                </div>
                <div class="flex gap-3 mt-4">
                  <button @click="rfqStep = 1" class="w-1/3 bg-slate-100 text-slate-600 font-black py-4 rounded-2xl">بازگشت</button>
                  <button @click="requestOtp" :disabled="!rfqData.phone" class="w-2/3 bg-blue-600 text-white font-black py-4 rounded-2xl shadow-lg">ارسال کد تایید</button>
                </div>
              </div>

              <!-- Step 3: OTP -->
              <div v-else-if="rfqStep === 3" key="step3" class="space-y-5">
                <h3 class="text-xl font-black text-slate-800 mb-2 text-center">کد تایید پیامکی</h3>
                <input type="text" v-model="rfqData.otp" placeholder="- - - - -" maxlength="5" class="w-full bg-slate-50 border p-4 rounded-2xl text-center font-black text-3xl tracking-[1em]" dir="ltr">
                <button @click="submitRfqForm" class="w-full bg-emerald-600 text-white font-black py-4 rounded-2xl shadow-lg mt-4">تایید و ثبت نهایی</button>
              </div>

              <!-- Step 4: Complete -->
              <div v-else key="step4" class="text-center py-8">
                <h3 class="text-2xl font-black text-slate-800 mb-2">درخواست شما ثبت شد!</h3>
                <p class="text-slate-500 font-bold text-sm mb-6">پیش‌فاکتورها به زودی برای شما ارسال خواهند شد.</p>
                <button @click="rfqStep = 1" class="bg-slate-100 px-8 py-3 rounded-xl font-black">درخواست جدید</button>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>

    <!-- Top Verified Suppliers -->
    <section class="py-24 bg-white">
      <div class="container mx-auto px-4 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-black text-slate-800 tracking-tight mb-4">تامین‌کنندگان رسمی و تایید شده</h2>
          <p class="text-slate-500 font-bold max-w-2xl mx-auto">خرید مستقیم از واردکنندگان اصلی با تضمین بازگشت وجه.</p>
        </div>

        <div class="flex overflow-x-auto hide-scrollbar gap-6 pb-8">
          <div v-for="seller in topSuppliers" :key="seller.id" class="flex-shrink-0 w-[300px] bg-white rounded-[2rem] border border-slate-100 p-6 shadow-sm hover:shadow-xl transition-all">
            <h3 class="font-black text-slate-800 text-base mb-2">{{ seller.name }}</h3>
            <p class="text-xs font-bold text-slate-400 mb-4">{{ seller.category }}</p>
            <div class="flex justify-between items-center bg-slate-50 p-3 rounded-xl">
              <span class="text-xs font-bold text-slate-500">محصولات: {{ seller.productsCount }}</span>
              <span class="text-xs font-black text-amber-500">★ {{ seller.rating }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick View Modal -->
    <Teleport to="body">
      <transition name="fade">
        <div v-if="quickViewProduct" class="fixed inset-0 z-[100000] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md" dir="rtl" @click.self="quickViewProduct = null">
          <div class="bg-white w-full max-w-4xl rounded-[2.5rem] shadow-2xl relative overflow-hidden font-sans border border-slate-200 flex flex-col md:flex-row max-h-[90vh]">
            <button @click="quickViewProduct = null" class="absolute top-4 left-4 z-20 w-10 h-10 bg-slate-100 hover:bg-slate-200 text-slate-500 rounded-full flex items-center justify-center transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
            <div class="w-full md:w-1/2 bg-slate-50 p-10 flex items-center justify-center">
              <img :src="quickViewProduct.img" class="max-h-[300px] object-contain">
            </div>
            <div class="w-full md:w-1/2 p-8 md:p-10 flex flex-col overflow-y-auto text-right">
              <h2 class="text-2xl font-black text-slate-800 mb-2">{{ quickViewProduct.name }}</h2>
              <p class="text-sm font-bold text-slate-500 mb-6">تامین‌کننده: {{ quickViewProduct.seller }}</p>
              <div class="mt-auto flex gap-4">
                <button @click="addToCart(quickViewProduct); quickViewProduct = null" class="flex-1 bg-slate-900 text-white font-black py-4 rounded-xl shadow-lg">افزودن به سبد</button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>

    <!-- Footer -->
    <footer class="bg-slate-950 pt-16 pb-12 text-slate-400 text-xs font-bold text-center mt-auto border-t border-slate-800">
      <div class="container mx-auto px-4">
        <p>تمامی حقوق محفوظ است. © ۱۴۰۵ تاجربام - اکوسیستم تجارت عمده B2B</p>
      </div>
    </footer>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://tajerbam.com';

const isHomePage = computed(() => route.path === '/');

const searchContainerRef = ref(null);
const categorySliderRef = ref(null);
const flashSliderRef = ref(null);
const trendingSliderRef = ref(null);

const searchQuery = ref('');
const searchResults = ref([]);
const selectedCategoryFilter = ref('all');
const cartItemCount = ref(0);
const isSearching = ref(false);
const isSearchFocused = ref(false);

const isLoading = ref(true);
const showTopBar = ref(true);
const isScrolled = ref(false);
const isMegaMenuOpen = ref(false);

const isLoggedIn = ref(false);
const userRole = ref('buyer');
const userName = ref('کاربر تاجربام');

const quickViewProduct = ref(null);
const showVideoModal = ref(false);

// RFQ State
const rfqStep = ref(1);
const rfqData = ref({ name: '', category: '', qty: '', phone: '', otp: '' });

// Timer State
const hours = ref('00');
const minutes = ref('00');
const seconds = ref('00');

// Dynamic Containers for DB
const parentCategories = ref([]);
const activeMegaCategory = ref(null);
const flashProducts = ref([]);
const trendingProducts = ref([]);
const topSuppliers = ref([]);

const features = ref([
  { title: 'تضمین اصالت و سلامت', desc: 'تمامی کالاها با فاکتور رسمی ارسال می‌شوند.', icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>', bg: 'bg-emerald-50', color: 'text-emerald-500' },
  { title: 'سیستم پرداخت امن Escrow', desc: 'وجه پرداختی تا زمان تایید تحویل، محفوظ می‌ماند.', icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 04-8 0v4h8z"></path></svg>', bg: 'bg-blue-50', color: 'text-blue-600' },
  { title: 'قیمت‌گذاری هوشمند AI', desc: 'ارائه پایین‌ترین قیمت خرید عمده در بازار.', icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>', bg: 'bg-purple-50', color: 'text-purple-600' },
  { title: 'لجستیک کانتینری', desc: 'ارسال ایمن و بیمه‌شده بارهای سنگین به سراسر کشور.', icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>', bg: 'bg-amber-50', color: 'text-amber-500' }
]);

// Sliders Scroll
const scrollCategorySlider = (direction) => {
  if (categorySliderRef.value) {
    categorySliderRef.value.scrollBy({ left: direction === 'rtl' ? -320 : 300, behavior: 'smooth' });
  }
};

const scrollFlashSlider = (direction) => {
  if (flashSliderRef.value) {
    flashSliderRef.value.scrollBy({ left: direction === 'rtl' ? -340 : 340, behavior: 'smooth' });
  }
};

const scrollTrendingSlider = (direction) => {
  if (trendingSliderRef.value) {
    trendingSliderRef.value.scrollBy({ left: direction === 'rtl' ? -310 : 310, behavior: 'smooth' });
  }
};

// Cart Methods
const getCartQty = (prodId) => {
  try {
    const cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
    const item = cart.find(i => i.id === prodId);
    return item ? item.qty : 0;
  } catch (e) {
    return 0;
  }
};

const increaseCart = (prod) => {
  let cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  const existing = cart.find(i => i.id === prod.id);
  const minQty = prod.min || 1;
  const unitPrice = prod.wholesale || prod.retail || 0;

  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({
      id: prod.id,
      name: prod.name,
      seller: prod.seller,
      img: prod.img,
      unitPrice: unitPrice,
      qty: minQty,
      min: minQty
    });
  }

  localStorage.setItem('tajerbam_cart', JSON.stringify(cart));
  cartItemCount.value = cart.length;
  window.dispatchEvent(new Event('storage'));
};

const decreaseCart = (prod) => {
  let cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  const existingIndex = cart.findIndex(i => i.id === prod.id);
  
  if (existingIndex !== -1) {
    const minQty = prod.min || 1;
    if (cart[existingIndex].qty <= minQty) {
      cart.splice(existingIndex, 1);
    } else {
      cart[existingIndex].qty -= 1;
    }
    localStorage.setItem('tajerbam_cart', JSON.stringify(cart));
    cartItemCount.value = cart.length;
    window.dispatchEvent(new Event('storage'));
  }
};

const handleClickOutside = (e) => {
  if (searchContainerRef.value && !searchContainerRef.value.contains(e.target)) {
    isSearchFocused.value = false;
  }
};

let searchTimeout;
const handleSearch = () => {
  const query = searchQuery.value.trim().toLowerCase();
  if (query.length < 2) {
    searchResults.value = [];
    isSearching.value = false;
    return;
  }
  
  isSearching.value = true;
  clearTimeout(searchTimeout);
  
  searchTimeout = setTimeout(async () => {
    try {
      let url = `${API_BASE_URL}/api/products?search=${encodeURIComponent(query)}`;
      if (selectedCategoryFilter.value !== 'all') {
        url += `&category_id=${selectedCategoryFilter.value}`;
      }
      
      const res = await fetch(url);
      let items = [];
      if (res.ok) {
        const prods = await res.json();
        items = Array.isArray(prods) ? prods : (prods.products || []);
      }

      try {
        const customProds = JSON.parse(localStorage.getItem('tajerbam_custom_products') || '[]');
        if (customProds.length > 0) {
          customProds.forEach(cp => {
            const idx = items.findIndex(p => String(p.id) === String(cp.id));
            if (idx !== -1) {
              items[idx] = { ...items[idx], ...cp };
            } else {
              items.unshift(cp);
            }
          });
        }
      } catch (e) {}

      searchResults.value = items.filter(p => {
        const nameMatch = (p.title || p.name || '').toLowerCase().includes(query);
        const sellerStr = typeof p.seller === 'string' ? p.seller : (p.seller?.name || '');
        const sellerMatch = sellerStr.toLowerCase().includes(query);
        const skuMatch = (p.sku || '').toLowerCase().includes(query);
        const keywordsMatch = (p.keywords || '').toLowerCase().includes(query);
        const catMatch = (p.category || '').toLowerCase().includes(query);

        const matchesCatFilter = selectedCategoryFilter.value === 'all' || String(p.category_id) === String(selectedCategoryFilter.value);

        return matchesCatFilter && (nameMatch || sellerMatch || skuMatch || keywordsMatch || catMatch);
      }).map(p => ({
        id: p.id,
        name: p.title || p.name,
        sku: p.sku || `SKU-${p.id}`,
        seller: typeof p.seller === 'string' ? p.seller : (p.seller?.name || 'تامین‌کننده تایید شده'),
        img: p.image_url || p.img || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png',
        price: p.price_retail || p.retailPrice || p.price || 0
      }));

    } catch (e) {
      console.error("Search Engine Error:", e);
    } finally {
      isSearching.value = false;
    }
  }, 250);
};

const executePrimarySearch = () => {
  if (searchResults.value.length > 0) {
    isSearchFocused.value = false;
    router.push(`/product/${searchResults.value[0].id}`);
  } else if (searchQuery.value.trim()) {
    isSearchFocused.value = false;
    router.push(`/category/all?q=${encodeURIComponent(searchQuery.value.trim())}`);
  }
};

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '۰';
};

const getCategoryImageUrl = (cat) => {
  if (cat.image_url && cat.image_url.startsWith('http')) return cat.image_url;
  const map = {
    digital: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=80',
    industrial: 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&auto=format&fit=crop&q=80',
    home: 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=600&auto=format&fit=crop&q=80',
    medical: 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=600&auto=format&fit=crop&q=80'
  };
  return map[cat.slug] || 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=600&auto=format&fit=crop&q=80';
};

const getCategorySvgIcon = (iconName) => {
  const map = {
    computer: `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>`,
    tool: `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37.996.608 2.296.07 2.572-1.065z"></path></svg>`,
    home: `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 01-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>`,
    heart: `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>`
  };
  return map[iconName] || `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>`;
};

const fetchDynamicData = async () => {
  isLoading.value = true;
  try {
    const [catsRes, prodsRes] = await Promise.all([
      fetch(`${API_BASE_URL}/api/categories`).catch(() => null),
      fetch(`${API_BASE_URL}/api/products`).catch(() => null)
    ]);

    if (catsRes && catsRes.ok) {
      const catsData = await catsRes.json();
      if (Array.isArray(catsData) && catsData.length > 0) {
        parentCategories.value = catsData;
        activeMegaCategory.value = catsData[0];
        if (catsData.length > 0) rfqData.value.category = catsData[0].name;
      }
    }

    if (prodsRes && prodsRes.ok) {
      const prodsData = await prodsRes.json();
      const items = Array.isArray(prodsData) ? prodsData : (prodsData.products || []);
      
      if (items.length > 0) {
        const mappedProds = items.map(p => ({
          id: p.id,
          name: p.title || p.name,
          seller: typeof p.seller === 'string' ? p.seller : (p.seller?.name || 'تامین‌کننده تایید شده'),
          img: p.image_url || p.img || 'https://freepngimg.com/thumb/laptop/168784-laptop-asus-png-download-free.png',
          retail: p.price_retail || p.retailPrice || 10000,
          wholesale: p.wholesalePrice || p.price_tiers?.[0]?.price_per_unit || (p.price_retail * 0.9) || 9000,
          min: p.minQty || p.price_tiers?.[0]?.min_qty || 5,
          stock: p.stock || 50,
          sold: Math.floor(Math.random() * 50) + 10,
          discount: p.price_retail ? Math.round(((p.price_retail - (p.price_tiers?.[0]?.price_per_unit || p.price_retail*0.9)) / p.price_retail) * 100) : 10
        }));

        flashProducts.value = mappedProds.slice(0, 3);
        trendingProducts.value = mappedProds.slice(3, 8);

        const uniqueSellersMap = {};
        items.forEach(p => {
          const sellerName = typeof p.seller === 'string' ? p.seller : (p.seller?.name || 'تامین‌کننده تایید شده');
          if (!uniqueSellersMap[sellerName]) {
             uniqueSellersMap[sellerName] = {
                id: Object.keys(uniqueSellersMap).length + 1,
                name: sellerName,
                category: 'تامین‌کننده تایید شده',
                productsCount: 1,
                rating: 4.9
             };
          } else {
             uniqueSellersMap[sellerName].productsCount += 1;
          }
        });
        topSuppliers.value = Object.values(uniqueSellersMap);
      }
    }
  } catch (err) {
    console.error("Error connecting to backend API:", err);
  } finally {
    isLoading.value = false;
  }
};

const addToCart = (prod) => {
  let cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
  const existing = cart.find(i => i.id === prod.id);
  if (existing) existing.qty += prod.min || 1;
  else cart.push({ id: prod.id, name: prod.name, seller: prod.seller, img: prod.img, unitPrice: prod.wholesale || prod.retail, qty: prod.min || 1 });
  
  localStorage.setItem('tajerbam_cart', JSON.stringify(cart));
  cartItemCount.value = cart.length;
};

const requestOtp = () => {
  if (rfqData.value.phone) rfqStep.value = 3;
};

const submitRfqForm = () => {
  rfqStep.value = 4;
};

const goToDashboard = () => {
  router.push('/buyer');
};

const handleScroll = () => {
  isScrolled.value = window.scrollY > 40;
};

onMounted(() => {
  window.addEventListener('click', handleClickOutside);
  window.addEventListener('scroll', handleScroll);
  fetchDynamicData();
});

onUnmounted(() => {
  window.removeEventListener('click', handleClickOutside);
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;700;900&display=swap');
.tajerbam-premium-home { font-family: 'Vazirmatn', sans-serif; }
.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 8px; }
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
.animate-marquee { animation: marquee 30s linear infinite; }
@keyframes marquee { 0% { transform: translateX(0%); } 100% { transform: translateX(100%); } }
</style>