<template>
  <div class="min-h-screen bg-slate-50 flex flex-col font-sans relative overflow-x-hidden selection:bg-blue-200 selection:text-blue-900" dir="rtl">
    
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
      isHomePage && !isScrolled ? 'bg-transparent py-6' : 'bg-white/90 backdrop-blur-2xl shadow-[0_10px_40px_rgba(0,0,0,0.04)] border-b border-slate-200/50 py-3',
      !isHomePage && !isScrolled ? 'py-4' : ''
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
              <span :class="['text-2xl md:text-3xl font-black tracking-tighter transition-colors duration-500', isHomePage && !isScrolled ? 'text-white drop-shadow-md' : 'text-slate-900']">تاجربام</span>
              <span :class="['text-[9px] md:text-[10px] font-black tracking-[0.25em] transition-colors duration-500', isHomePage && !isScrolled ? 'text-blue-300 drop-shadow-md' : 'text-blue-600']">B2B NETWORK</span>
            </div>
          </router-link>

          <!-- منوی دسکتاپ (مگامنو متصل به دیتابیس) -->
          <nav class="hidden lg:flex items-center gap-2">
            
            <div class="relative group px-3 py-2 cursor-pointer h-full flex items-center" @mouseenter="isMegaMenuOpen = true" @mouseleave="isMegaMenuOpen = false">
              <span :class="['text-sm font-black flex items-center gap-1.5 transition-all duration-300 px-4 py-2.5 rounded-xl border border-transparent', isHomePage && !isScrolled ? 'text-white hover:bg-white/10 hover:border-white/20' : 'text-slate-700 hover:bg-slate-50 hover:text-blue-600 hover:border-slate-200']">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                دسته‌بندی کالاها 
                <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
              </span>
              
              <!-- ساختار مگامنو (دریافت هوشمند دسته‌های والد از DB) -->
              <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-4" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-4">
                <div v-show="isMegaMenuOpen" class="absolute top-full right-0 pt-4 w-[920px] cursor-default">
                  <div class="bg-white/95 backdrop-blur-3xl rounded-[2.5rem] shadow-[0_40px_100px_rgba(0,0,0,0.12)] border border-slate-200/80 p-8 flex gap-8 relative overflow-hidden">
                    <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-blue-100 rounded-full mix-blend-multiply filter blur-[60px] opacity-60"></div>
                    
                    <!-- منوی عمودی دسته‌های والد اصلی -->
                    <div class="w-1/3 border-l border-slate-100 pl-6 flex flex-col gap-2 max-h-[420px] overflow-y-auto custom-scrollbar">
                      <div v-for="cat in parentCategories" :key="cat.id" @mouseenter="activeMegaCategory = cat" :class="['px-4 py-3 rounded-2xl flex items-center justify-between font-black text-sm transition-all cursor-pointer', activeMegaCategory?.id === cat.id ? 'bg-blue-50 text-blue-700 shadow-sm border border-blue-100' : 'text-slate-600 hover:bg-slate-50']">
                        <div class="flex items-center gap-3">
                          <div class="w-8 h-8 rounded-xl flex items-center justify-center shrink-0" :class="activeMegaCategory?.id === cat.id ? 'bg-blue-100 text-blue-600' : 'bg-slate-100 text-slate-400'" v-html="getCategorySvg(cat.icon)"></div>
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
                            <span v-html="getCategorySvg(activeMegaCategory.icon)" class="text-blue-600"></span> 
                            {{ activeMegaCategory.name }}
                          </h3>
                          <router-link :to="`/category/${activeMegaCategory.id}`" class="text-xs font-bold text-blue-600 hover:underline flex items-center gap-1">
                            مشاهده تمام کالاهای دسته ({{ activeMegaCategory.products_count || 0 }})
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                          </router-link>
                        </div>

                        <!-- زیرمجموعه‌های دسته والد انتخاب شده -->
                        <div v-if="activeMegaCategory.children && activeMegaCategory.children.length > 0" class="grid grid-cols-2 gap-x-8 gap-y-6 max-h-[260px] overflow-y-auto custom-scrollbar pr-2">
                          <div v-for="sub in activeMegaCategory.children" :key="sub.id" class="bg-slate-50/80 p-3.5 rounded-2xl border border-slate-100 hover:border-blue-200 hover:bg-blue-50/30 transition-all">
                            <router-link :to="`/category/${sub.id}`" class="font-black text-slate-800 text-sm mb-1.5 flex items-center justify-between hover:text-blue-600">
                              <span class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>{{ sub.name }}</span>
                              <span class="text-[10px] font-bold text-slate-400 bg-white px-2 py-0.5 rounded-full border border-slate-100">{{ sub.products_count || 0 }}</span>
                            </router-link>
                            <p class="text-[11px] text-slate-400 font-medium line-clamp-1 mt-1">{{ sub.description || 'تامین مستقیم از تولیدکنندگان' }}</p>
                          </div>
                        </div>

                        <div v-else class="py-12 text-center text-slate-400 font-bold bg-slate-50 rounded-2xl border border-dashed border-slate-200">
                          زیردسته‌ای برای این بخش ثبت نشده است. برای مشاهده کالاهای مستقیم کلیک کنید.
                        </div>
                        
                        <!-- بنر پیش‌فرض داخل مگامنو -->
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

            <!-- لینک‌های سریع -->
            <router-link to="/buyer/rfq" :class="['px-4 py-2.5 rounded-xl text-sm font-black transition-colors', isHomePage && !isScrolled ? 'text-white hover:bg-white/10' : 'text-slate-700 hover:bg-slate-50 hover:text-blue-600']">استعلام خرید (RFQ)</router-link>
            <router-link to="/marketer" :class="['px-4 py-2.5 rounded-xl text-sm font-black transition-colors flex items-center gap-1.5', isHomePage && !isScrolled ? 'text-white hover:bg-white/10' : 'text-slate-700 hover:bg-slate-50 hover:text-blue-600']">
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
                <select v-model="selectedCategoryFilter" :class="['bg-transparent border-none text-xs font-black pl-2 pr-4 py-3.5 outline-none cursor-pointer border-l transition-colors', (isHomePage && !isScrolled && !isSearchFocused) ? 'text-white border-white/20 [&>option]:text-slate-800' : 'text-slate-600 border-slate-200']">
                  <option value="all">همه دسته‌ها</option>
                  <option v-for="cat in parentCategories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                </select>
              </div>

              <input 
                type="text" 
                v-model="searchQuery" 
                @focus="isSearchFocused = true"
                @input="handleSearch"
                placeholder="جستجوی کالای عمده، تامین‌کننده، برند یا شناسه (SKU)..." 
                :class="['w-full bg-transparent border-none outline-none text-sm font-bold px-4 transition-colors', (isHomePage && !isScrolled && !isSearchFocused) ? 'text-white placeholder-white/70' : 'text-slate-800 placeholder-slate-400']"
              >
              
              <button class="bg-blue-600 hover:bg-blue-500 text-white p-2.5 rounded-xl m-1.5 transition-colors shadow-md flex-shrink-0">
                <svg v-if="!isSearching" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <svg v-else class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              </button>
            </div>
          </div>

          <!-- باکس نتایج جستجو (Dropdown) -->
          <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-2">
            <div v-if="isSearchFocused && (searchResults.length > 0 || searchQuery.length > 2)" class="absolute top-[calc(100%+8px)] left-0 right-0 bg-white rounded-[2rem] shadow-[0_20px_60px_rgba(0,0,0,0.1)] border border-slate-100 p-4 z-[100] overflow-hidden">
              <div v-if="searchResults.length > 0" class="max-h-[60vh] overflow-y-auto custom-scrollbar pr-2">
                <div class="text-[10px] font-black text-slate-400 mb-3 px-2">نتایج جستجو برای "{{ searchQuery }}"</div>
                <ul class="space-y-2">
                  <li v-for="item in searchResults" :key="item.id">
                    <router-link :to="`/product/${item.id}`" class="flex items-center gap-4 p-3 rounded-2xl hover:bg-slate-50 transition-colors group/item">
                      <div class="w-14 h-14 bg-white border border-slate-100 rounded-xl p-1 shrink-0"><img :src="item.img" class="w-full h-full object-contain mix-blend-multiply"></div>
                      <div class="flex-grow">
                        <h4 class="font-black text-slate-800 text-sm group-hover/item:text-blue-600 transition-colors line-clamp-1 mb-1">{{ item.name }}</h4>
                        <div class="flex items-center gap-2">
                          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md">تامین‌کننده: {{ item.seller }}</span>
                          <span class="text-[10px] font-black text-blue-600 bg-blue-50 border border-blue-100 px-2 py-0.5 rounded-md">شروع از: {{ formatPrice(item.price) }} ت</span>
                        </div>
                      </div>
                      <svg class="w-5 h-5 text-slate-300 group-hover/item:text-blue-500 transform group-hover/item:-translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                    </router-link>
                  </li>
                </ul>
              </div>
              <div v-else-if="!isSearching && searchQuery.length > 2" class="py-10 text-center flex flex-col items-center">
                <div class="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center text-slate-300 mb-4"><svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
                <p class="font-black text-slate-600 text-sm mb-1">نتیجه‌ای یافت نشد!</p>
                <p class="text-xs font-bold text-slate-400">لطفاً املای کلمه را بررسی کنید یا از عبارات کلی‌تر استفاده نمایید.</p>
              </div>
            </div>
          </transition>
        </div>

        <!-- ابزارها و پنل کاربری -->
        <div class="flex items-center gap-2 md:gap-4 shrink-0">
          
          <!-- دکمه سبد خرید (Live State) -->
          <router-link to="/cart" class="relative group p-2 md:p-3">
            <div :class="['absolute inset-0 rounded-xl transition-all duration-300', isHomePage && !isScrolled ? 'bg-white/10 backdrop-blur-md border border-white/20 group-hover:bg-white/20' : 'bg-slate-100 group-hover:bg-slate-200 border border-transparent']"></div>
            <svg :class="['w-6 h-6 relative z-10 transition-colors duration-300', isHomePage && !isScrolled ? 'text-white' : 'text-slate-700']" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            <span v-if="cartItemCount > 0" class="absolute -top-1 -right-1 w-5 h-5 bg-rose-500 text-white text-[10px] font-black rounded-full flex items-center justify-center shadow-lg border-2 border-white transform scale-100 group-hover:scale-110 transition-transform z-20">{{ cartItemCount }}</span>
          </router-link>

          <!-- دکمه احراز هویت / پروفایل -->
          <div class="relative ml-2" @mouseenter="isProfileMenuOpen = true" @mouseleave="isProfileMenuOpen = false">
            <template v-if="isLoggedIn">
              <button @click="goToDashboard" :class="['px-4 md:px-5 py-2.5 md:py-3 rounded-xl font-black text-sm transition-all shadow-lg flex items-center gap-2.5', isHomePage && !isScrolled ? 'bg-white/10 backdrop-blur-md text-white border border-white/20 hover:bg-white/20' : 'bg-slate-900 text-white hover:bg-slate-800 shadow-slate-900/20']">
                <div class="w-6 h-6 rounded-full bg-white/20 flex items-center justify-center text-xs border border-white/30 backdrop-blur-sm">{{ userName.charAt(0) || 'ک' }}</div>
                <span class="hidden sm:block">میزکار من</span>
              </button>
              
              <!-- منوی کشویی پروفایل -->
              <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-2">
                <div v-show="isProfileMenuOpen" class="absolute top-full left-0 pt-2 w-56">
                  <div class="bg-white rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.1)] border border-slate-100 overflow-hidden flex flex-col p-2">
                    <div class="p-3 border-b border-slate-100 mb-2">
                      <p class="font-black text-slate-800 text-sm truncate">{{ userName }}</p>
                      <p class="text-[10px] font-bold text-slate-400 mt-1 capitalize">{{ getRoleName(userRole) }} تاجربام</p>
                    </div>
                    <button @click="goToDashboard" class="flex items-center gap-2.5 px-3 py-2.5 text-sm font-bold text-slate-600 hover:bg-slate-50 hover:text-blue-600 rounded-xl transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg> ورود به داشبورد</button>
                    <button class="flex items-center gap-2.5 px-3 py-2.5 text-sm font-bold text-slate-600 hover:bg-slate-50 hover:text-blue-600 rounded-xl transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg> سفارشات من</button>
                    <div class="h-px bg-slate-100 my-1"></div>
                    <button @click="logout" class="flex items-center gap-2.5 px-3 py-2.5 text-sm font-bold text-rose-600 hover:bg-rose-50 rounded-xl transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg> خروج از حساب</button>
                  </div>
                </div>
              </transition>
            </template>

            <template v-else>
              <router-link to="/login" :class="['px-5 md:px-6 py-2.5 md:py-3 rounded-xl font-black text-sm transition-all flex items-center gap-2 border shadow-sm', isHomePage && !isScrolled ? 'bg-white/10 border-white/20 text-white hover:bg-white/20 backdrop-blur-md' : 'bg-white border-slate-200 text-slate-800 hover:border-blue-400 hover:text-blue-600 hover:shadow-md']">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path></svg>
                ورود / عضویت
              </router-link>
            </template>
          </div>
        </div>

      </div>
    </header>

    <!-- ================= 3. Main Content Router View ================= -->
    <main :class="['flex-grow flex flex-col relative w-full', !isHomePage ? 'pt-24 lg:pt-32' : '']">
      <router-view v-slot="{ Component }">
        <transition name="page-fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- ================= 4. Global Premium Footer ================= -->
    <footer class="bg-slate-950 pt-24 pb-24 md:pb-12 border-t border-slate-800 relative overflow-hidden flex-shrink-0 z-10 mt-auto">
      <div class="absolute left-0 bottom-0 w-full h-2/3 bg-gradient-to-t from-blue-900/20 to-transparent pointer-events-none"></div>
      <div class="absolute -right-40 -bottom-40 w-96 h-96 bg-indigo-600 rounded-full mix-blend-screen filter blur-[120px] opacity-20 pointer-events-none"></div>
      
      <div class="container mx-auto px-4 lg:px-8 relative z-10">
        <!-- خبرنامه -->
        <div class="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-[2.5rem] p-8 md:p-12 shadow-[0_20px_50px_rgba(37,99,235,0.3)] mb-16 flex flex-col md:flex-row items-center justify-between gap-8 relative overflow-hidden">
          <div class="relative z-10 md:w-1/2">
            <h3 class="text-2xl md:text-3xl font-black text-white mb-3 tracking-tight">از فرصت‌های تجاری جا نمانید!</h3>
            <p class="text-blue-100 font-medium text-sm leading-relaxed">با عضویت در خبرنامه B2B، هفته‌ای یک‌بار لیست کالاهای زیر فی بازار و مناقصات پرسود را در ایمیل خود دریافت کنید.</p>
          </div>
          <div class="relative z-10 w-full md:w-1/2">
            <div class="bg-white/10 backdrop-blur-xl border border-white/20 p-1.5 rounded-2xl flex items-center shadow-inner focus-within:bg-white/20 transition-colors">
              <input type="email" placeholder="آدرس ایمیل سازمانی شما..." class="w-full bg-transparent border-none text-white placeholder-blue-200 px-4 py-3 outline-none text-sm font-bold" dir="ltr">
              <button class="bg-white text-blue-600 hover:bg-slate-50 font-black px-6 py-3.5 rounded-xl transition-all shadow-md text-sm whitespace-nowrap">عضویت VIP</button>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 border-b border-slate-800 pb-16">
          <div class="lg:col-span-2">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-14 h-14 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center text-white shadow-lg shadow-blue-500/30">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
              </div>
              <div class="flex flex-col">
                <span class="text-3xl font-black text-white tracking-tighter">تاجربام</span>
                <span class="text-[10px] font-black tracking-[0.25em] text-blue-500">B2B NETWORK</span>
              </div>
            </div>
            <p class="text-slate-400 text-sm font-medium leading-loose mb-8 max-w-sm text-justify">
              تاجربام، اکوسیستم یکپارچه تجارت عمده (B2B) در ایران است. ما با حذف واسطه‌ها، ارائه سیستم پرداخت تضمینی (Escrow) و احراز هویت دقیق تامین‌کنندگان، تجربه‌ای امن را خلق می‌کنیم.
            </p>
          </div>

          <div>
            <h4 class="text-white font-black mb-6 border-b border-slate-800 pb-3 inline-block">خدمات خریداران</h4>
            <ul class="space-y-4 text-sm font-bold text-slate-400">
              <li><router-link to="/buyer/rfq" class="hover:text-blue-400 hover:pl-2 transition-all flex items-center gap-2"><span class="w-1 h-1 rounded-full bg-slate-600"></span> ثبت استعلام خرید (RFQ)</router-link></li>
              <li><router-link to="/buyer/orders" class="hover:text-blue-400 hover:pl-2 transition-all flex items-center gap-2"><span class="w-1 h-1 rounded-full bg-slate-600"></span> پیگیری سفارشات</router-link></li>
            </ul>
          </div>

          <div>
            <h4 class="text-white font-black mb-6 border-b border-slate-800 pb-3 inline-block">خدمات تامین‌کنندگان</h4>
            <ul class="space-y-4 text-sm font-bold text-slate-400">
              <li><router-link to="/login" class="hover:text-blue-400 hover:pl-2 transition-all flex items-center gap-2"><span class="w-1 h-1 rounded-full bg-slate-600"></span> ثبت‌نام فروشنده</router-link></li>
              <li><router-link to="/panel/plans" class="hover:text-blue-400 hover:pl-2 transition-all flex items-center gap-2"><span class="w-1 h-1 rounded-full bg-slate-600"></span> تعرفه‌ها و پلن‌های VIP</router-link></li>
            </ul>
          </div>

          <div>
            <h4 class="text-white font-black mb-6 border-b border-slate-800 pb-3 inline-block">امپراتوری B2B</h4>
            <div class="w-full h-20 bg-slate-900 rounded-2xl border border-slate-800 flex items-center justify-center p-2 shadow-inner">
              <span class="text-xs font-bold text-slate-400">پرداخت امن Escrow تایید شده</span>
            </div>
          </div>
        </div>

        <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs font-bold text-slate-600">
          <p>© ۱۴۰۵ تمامی حقوق برای پلتفرم B2B تاجربام محفوظ است.</p>
        </div>
      </div>
    </footer>

    <!-- ================= 5. Mobile Bottom Navigation ================= -->
    <nav class="md:hidden fixed bottom-0 left-0 w-full bg-white/90 backdrop-blur-2xl border-t border-slate-200/80 z-[100] pb-safe shadow-[0_-10px_40px_rgba(0,0,0,0.05)]">
      <div class="flex items-center justify-around px-2 h-16">
        <router-link to="/" class="flex flex-col items-center justify-center w-16 h-full text-slate-400 hover:text-blue-600 group" active-class="text-blue-600">
          <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
          <span class="text-[9px] font-black">خانه</span>
        </router-link>
        
        <router-link to="/category/all" class="flex flex-col items-center justify-center w-16 h-full text-slate-400 hover:text-blue-600 group" active-class="text-blue-600">
          <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
          <span class="text-[9px] font-black">دسته‌بندی</span>
        </router-link>

        <router-link to="/cart" class="relative flex flex-col items-center justify-center w-16 h-full text-slate-400 hover:text-blue-600 group" active-class="text-blue-600">
          <div class="relative">
            <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            <span v-if="cartItemCount > 0" class="absolute -top-1 -right-2 w-4 h-4 bg-rose-500 text-white text-[9px] font-black rounded-full flex items-center justify-center shadow-md border-2 border-white">{{ cartItemCount }}</span>
          </div>
          <span class="text-[9px] font-black">سبد خرید</span>
        </router-link>

        <a v-if="isLoggedIn" @click="goToDashboard" class="flex flex-col items-center justify-center w-16 h-full text-slate-400 hover:text-blue-600 cursor-pointer group">
          <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
          <span class="text-[9px] font-black">پروفایل</span>
        </a>
        <router-link v-else to="/login" class="flex flex-col items-center justify-center w-16 h-full text-slate-400 hover:text-blue-600 group" active-class="text-blue-600">
          <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path></svg>
          <span class="text-[9px] font-black">ورود</span>
        </router-link>
      </div>
    </nav>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'https://tajerbam.com';

const route = useRoute();
const router = useRouter();

// State
const showTopBar = ref(true);
const isScrolled = ref(false);
const isMegaMenuOpen = ref(false);
const isSearchFocused = ref(false);
const isSearching = ref(false);
const isProfileMenuOpen = ref(false);

const searchQuery = ref('');
const searchResults = ref([]);
const cartItemCount = ref(0);
const selectedCategoryFilter = ref('all');

// Categories from Backend DB
const parentCategories = ref([]);
const activeMegaCategory = ref(null);

// Auth State
const isLoggedIn = ref(false);
const userRole = ref('');
const userName = ref('');

const isHomePage = computed(() => route.path === '/');

const fetchCategoriesFromDb = async () => {
  try {
    const res = await fetch(`${API_BASE_URL}/api/categories`);
    if (res.ok) {
      const data = await res.json();
      parentCategories.value = Array.isArray(data) ? data : [];
      if (parentCategories.value.length > 0) {
        activeMegaCategory.value = parentCategories.value[0];
      }
    }
  } catch (err) {
    console.error("Failed fetching categories from DB:", err);
  }
};

const getCategorySvg = (iconName) => {
  const icons = {
    computer: `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>`,
    tool: `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37.996.608 2.296.07 2.572-1.065z"></path></svg>`,
    home: `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>`,
    heart: `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>`
  };
  return icons[iconName] || `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"></path></svg>`;
};

let searchTimeout;
const handleSearch = () => {
  if (searchQuery.value.length < 2) {
    searchResults.value = [];
    isSearching.value = false;
    return;
  }
  
  isSearching.value = true;
  clearTimeout(searchTimeout);
  
  searchTimeout = setTimeout(async () => {
    try {
      let url = `${API_BASE_URL}/api/products`;
      if (selectedCategoryFilter.value !== 'all') {
        url += `?category_id=${selectedCategoryFilter.value}`;
      }
      const res = await fetch(url);
      if (res.ok) {
        const prods = await res.json();
        const items = Array.isArray(prods) ? prods : (prods.products || []);
        const query = searchQuery.value.toLowerCase();
        searchResults.value = items.filter(p => 
          (p.title || p.name || '').toLowerCase().includes(query) || 
          (p.seller || '').toLowerCase().includes(query)
        );
      }
    } catch (e) {
      console.error("Search API Error:", e);
    } finally {
      isSearching.value = false;
    }
  }, 400);
};

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
  showTopBar.value = window.scrollY <= 150;
};

const checkAuth = () => {
  const token = localStorage.getItem('tajerbam_token');
  if (token) {
    isLoggedIn.value = true;
    userRole.value = localStorage.getItem('user_role') || 'buyer';
    userName.value = localStorage.getItem('user_name') || 'کاربر تاجربام';
  } else {
    isLoggedIn.value = false;
  }
};

const goToDashboard = () => {
  isProfileMenuOpen.value = false;
  const role = userRole.value;
  if (role === 'admin') router.push('/admin');
  else if (role === 'buyer') router.push('/buyer');
  else if (role === 'marketer') router.push('/marketer');
  else router.push('/panel');
};

const logout = () => {
  localStorage.removeItem('tajerbam_token');
  localStorage.removeItem('user_role');
  localStorage.removeItem('user_name');
  isLoggedIn.value = false;
  isProfileMenuOpen.value = false;
  router.push('/');
};

const getRoleName = (role) => {
  const map = { 'seller': 'فروشنده', 'buyer': 'خریدار', 'marketer': 'بازاریاب', 'admin': 'مدیر' };
  return map[role] || 'کاربر';
};

const syncCartCount = () => {
  try {
    const cart = JSON.parse(localStorage.getItem('tajerbam_cart') || '[]');
    cartItemCount.value = cart.length;
  } catch (e) {
    cartItemCount.value = 0;
  }
};

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '0';
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  window.addEventListener('storage', syncCartCount);
  fetchCategoriesFromDb();
  checkAuth();
  syncCartCount();
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  window.removeEventListener('storage', syncCartCount);
  clearTimeout(searchTimeout);
});

watch(() => route.path, () => {
  checkAuth();
  syncCartCount();
  isMegaMenuOpen.value = false;
  isSearchFocused.value = false;
  searchQuery.value = '';
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;700;900&display=swap');

.font-sans {
  font-family: 'Vazirmatn', sans-serif;
}

.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.page-fade-enter-from {
  opacity: 0;
  transform: translateY(10px) scale(0.99);
}
.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.99);
}

.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }

.pb-safe { padding-bottom: env(safe-area-inset-bottom); }
</style>