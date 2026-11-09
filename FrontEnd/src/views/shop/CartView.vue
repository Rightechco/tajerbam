<template>
  <div class="bg-slate-50/50 min-h-screen pb-24 pt-8 relative font-sans text-slate-800" dir="rtl">
    
    <!-- بک‌گراند ملایم -->
    <div class="absolute top-0 left-0 w-full h-96 bg-gradient-to-b from-blue-50/80 to-transparent z-0 pointer-events-none"></div>

    <div class="container mx-auto px-4 lg:px-8 relative z-10 max-w-7xl">
      
      <!-- ================= نوار مراحل خرید (Stepper) ================= -->
      <div class="max-w-3xl mx-auto mb-12 hidden md:block">
        <div class="flex items-center justify-between relative">
          <!-- خط اتصال -->
          <div class="absolute left-0 right-0 top-1/2 -translate-y-1/2 h-1 bg-slate-200 rounded-full z-0"></div>
          <div class="absolute right-0 top-1/2 -translate-y-1/2 h-1 bg-blue-600 rounded-full z-0 w-0 transition-all duration-500"></div>
          
          <!-- مرحله 1 -->
          <div class="relative z-10 flex flex-col items-center gap-2">
            <div class="w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center font-black shadow-lg shadow-blue-600/30 ring-4 ring-blue-50">۱</div>
            <span class="text-sm font-black text-slate-800">سبد خرید</span>
          </div>
          
          <!-- مرحله 2 -->
          <div class="relative z-10 flex flex-col items-center gap-2">
            <div class="w-12 h-12 rounded-full bg-slate-100 border-2 border-slate-300 text-slate-400 flex items-center justify-center font-black">۲</div>
            <span class="text-sm font-bold text-slate-400">اطلاعات ارسال</span>
          </div>
          
          <!-- مرحله 3 -->
          <div class="relative z-10 flex flex-col items-center gap-2">
            <div class="w-12 h-12 rounded-full bg-slate-100 border-2 border-slate-300 text-slate-400 flex items-center justify-center font-black">۳</div>
            <span class="text-sm font-bold text-slate-400">پرداخت امن</span>
          </div>
        </div>
      </div>

      <!-- ================= عنوان صفحه ================= -->
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
        <h1 class="text-3xl font-black tracking-tight text-slate-800 flex items-center gap-3">
          <span class="w-2 h-8 bg-blue-600 rounded-full"></span>
          سبد خرید عمده
        </h1>
        <div class="bg-white px-4 py-2 rounded-xl shadow-sm border border-slate-100 text-sm font-bold text-slate-500 flex items-center gap-2">
          {{ cartItems.length }} ردیف کالا
        </div>
      </div>

      <!-- ================= بدنه اصلی (دو ستونه) ================= -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- ستون راست: لیست محصولات (8 ستون) -->
        <div class="lg:col-span-8 space-y-6">
          
          <template v-if="cartItems.length > 0">
            <!-- گروه‌بندی فروشندگان با طراحی شیک -->
            <div v-for="(group, sellerName) in groupedCart" :key="sellerName" class="bg-white rounded-[2rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] overflow-hidden transition-all hover:shadow-[0_8px_40px_rgb(0,0,0,0.06)]">
              
              <!-- هدر فروشنده -->
              <div class="bg-slate-50/50 border-b border-slate-100 p-5 px-6 flex items-center gap-4">
                <div class="w-10 h-10 rounded-2xl bg-white border border-slate-200 flex items-center justify-center text-slate-400 font-black shadow-sm">
                  <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                </div>
                <div>
                  <h4 class="font-black text-slate-800 text-sm md:text-base">تامین‌کننده: {{ sellerName }}</h4>
                  <p class="text-xs text-slate-500 mt-1 font-medium flex items-center gap-1">
                    <svg class="w-3.5 h-3.5 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                    ارسال مستقیم از انبار و مشمول بیمه
                  </p>
                </div>
              </div>

              <!-- لیست کالاهای فروشنده -->
              <div class="p-6 md:p-8 space-y-8">
                <div v-for="(item, index) in group" :key="item.id" class="flex flex-col md:flex-row gap-6 relative group">
                  
                  <!-- خط جداکننده (به جز آیتم آخر) -->
                  <div v-if="index !== group.length - 1" class="absolute -bottom-4 left-0 right-0 h-px bg-slate-100"></div>

                  <!-- دکمه حذف کالا -->
                  <button @click="removeItem(item.id)" title="حذف از سبد" class="absolute top-0 left-0 text-slate-300 hover:text-red-500 hover:bg-red-50 p-2 rounded-xl transition-all z-10">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                  </button>

                  <!-- عکس کالا -->
                  <div class="w-24 h-24 md:w-32 md:h-32 bg-slate-50 rounded-2xl p-2 border border-slate-100 flex-shrink-0 flex items-center justify-center">
                    <img :src="item.img" class="max-h-full max-w-full object-contain mix-blend-multiply drop-shadow-sm" :alt="item.name">
                  </div>
                  
                  <!-- اطلاعات کالا -->
                  <div class="flex-grow flex flex-col justify-between pt-1 w-full pl-6 md:pl-8">
                    <div>
                      <h3 class="font-black text-slate-800 text-sm md:text-base leading-relaxed mb-3 pr-8 md:pr-0 line-clamp-2">{{ item.name }}</h3>
                      <div class="flex flex-wrap items-center gap-2 mb-4">
                        <span class="inline-flex items-center gap-1.5 bg-slate-100 text-slate-600 px-2 py-1.5 rounded-lg text-[11px] font-bold">
                          شناسه کالا: TJB-{{ String(item.id).substring(0, 4) }}
                        </span>
                        <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 px-2 py-1.5 rounded-lg text-[11px] font-bold">
                          موجود در انبار
                        </span>
                      </div>
                    </div>
                    
                    <!-- قیمت و تعداد -->
                    <div class="flex flex-wrap items-end justify-between gap-4 mt-auto">
                      
                      <!-- انتخاب تعداد -->
                      <div>
                        <span class="block text-[10px] font-bold text-slate-400 mb-1.5">تعداد درخواستی</span>
                        <div class="flex items-center bg-slate-50 border border-slate-200 rounded-xl p-1 w-fit">
                          <button @click="decreaseQty(item)" :class="['w-9 h-9 flex items-center justify-center rounded-lg transition-colors font-black text-lg', item.qty > (item.minOrder || 1) ? 'text-slate-600 hover:bg-white hover:text-blue-600 hover:shadow-sm' : 'text-slate-300 cursor-not-allowed']">-</button>
                          <input type="number" v-model="item.qty" @change="validateQty(item)" class="w-14 text-center bg-transparent font-black text-slate-800 outline-none text-base">
                          <button @click="increaseQty(item)" class="w-9 h-9 flex items-center justify-center rounded-lg text-slate-600 hover:bg-white hover:shadow-sm hover:text-blue-600 transition-colors font-black text-lg">+</button>
                        </div>
                        <p class="text-[10px] font-bold text-slate-400 mt-2">حداقل سفارش: {{ item.minOrder || 1 }} عدد</p>
                      </div>

                      <!-- قیمت نهایی ردیف -->
                      <div class="text-left bg-blue-50/30 px-4 py-2.5 rounded-xl border border-blue-100/50">
                        <span class="block text-[10px] font-bold text-slate-500 mb-1">قیمت واحد: {{ formatPrice(item.unitPrice) }}</span>
                        <div class="text-lg md:text-xl font-black text-blue-700">
                          {{ formatPrice(item.unitPrice * item.qty) }} <span class="text-xs font-bold text-slate-400">تومان</span>
                        </div>
                      </div>

                    </div>
                  </div>
                </div>
              </div>

            </div>
          </template>

          <!-- سبد خالی -->
          <div v-else class="bg-white rounded-[2rem] border border-slate-100 p-12 flex flex-col items-center justify-center text-center shadow-sm h-96">
            <div class="w-24 h-24 bg-slate-50 rounded-full flex items-center justify-center text-slate-300 mb-6">
              <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            </div>
            <h3 class="text-xl font-black text-slate-800 mb-2">سبد خرید شما خالی است</h3>
            <p class="text-sm font-medium text-slate-500 mb-8">برای ثبت سفارش عمده، ابتدا محصولی را به سبد خود اضافه کنید.</p>
            <router-link to="/category/all" class="bg-slate-900 text-white font-bold px-8 py-3.5 rounded-xl hover:bg-black transition-colors shadow-lg">
              مشاهده محصولات فروشگاه
            </router-link>
          </div>

        </div>

        <!-- ================= ستون چپ: باکس صورت‌حساب (سایدبار 4 ستون) ================= -->
        <div class="lg:col-span-4 space-y-6 lg:sticky top-28">
          
          <div class="bg-white rounded-[2rem] border border-slate-100 p-6 md:p-8 shadow-[0_15px_40px_rgb(0,0,0,0.05)] relative overflow-hidden">
            <!-- خط تزئینی بالا -->
            <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-blue-600 to-sky-400"></div>
            
            <h3 class="font-black text-slate-800 text-lg mb-6 border-b border-slate-100 pb-4">
              خلاصه صورت‌حساب
            </h3>
            
            <div class="space-y-4 text-sm font-medium text-slate-600 mb-8">
              <div class="flex justify-between items-center bg-slate-50 p-3 rounded-xl border border-slate-100">
                <span>ارزش کالاها ({{ cartItems.length }})</span>
                <span class="font-bold text-slate-800">{{ formatPrice(subTotal) }} تومان</span>
              </div>
              <div class="flex justify-between items-center text-emerald-600 px-3">
                <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg> سود خرید عمده</span>
                <span class="font-bold">{{ formatPrice(Math.round(subTotal * 0.12)) }} تومان</span>
              </div>
              <div class="flex justify-between items-center px-3 text-slate-500">
                <span>هزینه باربری</span>
                <span class="font-bold text-slate-800 text-xs bg-slate-100 px-2 py-1 rounded">محاسبه در مرحله بعد</span>
              </div>
            </div>

            <!-- جمع کل -->
            <div class="mb-8 relative border-t border-dashed border-slate-200 pt-6 mt-6">
              <div class="flex justify-between items-end">
                <span class="text-sm font-black text-slate-800">مبلغ قابل پرداخت:</span>
                <div class="text-left">
                  <span class="text-3xl font-black text-blue-700 tracking-tight block">{{ formatPrice(subTotal) }}</span>
                  <span class="text-[10px] font-bold text-slate-400 mt-1 block">تومان (شامل مالیات بر ارزش افزوده)</span>
                </div>
              </div>
            </div>

            <!-- دکمه‌های اکشن -->
            <div class="space-y-3">
              <button 
                :disabled="cartItems.length === 0"
                @click="$router.push('/checkout')" 
                class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgb(0,0,0,0.1)] transition-all hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-base"
              >
                تایید و ادامه خرید <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </button>
              
              <!-- دکمه صدور پیش فاکتور -->
              <button 
                :disabled="cartItems.length === 0"
                @click="showProforma = true" 
                class="w-full bg-white border border-slate-200 hover:border-blue-400 hover:text-blue-700 text-slate-600 font-bold py-3.5 rounded-xl transition-colors flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                صدور پیش‌فاکتور (PDF)
              </button>
            </div>
            
          </div>
        </div>

      </div>
    </div>

    <!-- ================= MODAL: پیش فاکتور رسمی ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="showProforma" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 sm:p-6" dir="rtl">
          
          <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm transition-opacity" @click="showProforma = false"></div>
          
          <div class="bg-white w-full max-w-4xl max-h-[90vh] overflow-y-auto rounded-3xl shadow-2xl relative z-10 print:max-h-none print:shadow-none print:w-full print:m-0 custom-scrollbar flex flex-col font-sans">
            
            <div class="p-8 md:p-12 flex-grow">
              
              <!-- هدر فاکتور -->
              <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b-2 border-slate-800 pb-6 mb-8 gap-6 print:border-black">
                <div class="flex items-center gap-4">
                  <div class="w-16 h-16 bg-slate-900 rounded-2xl flex items-center justify-center print:border print:border-black"><svg class="w-8 h-8 text-white print:text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg></div>
                  <div>
                    <h2 class="text-3xl font-black text-slate-800 tracking-tight">پیش‌فاکتور رسمی</h2>
                    <p class="text-sm font-bold text-slate-500 tracking-widest mt-1 uppercase">Proforma Invoice</p>
                  </div>
                </div>
                <div class="text-left text-sm font-medium text-slate-600 space-y-2 bg-slate-50 p-4 rounded-xl print:bg-transparent print:p-0">
                  <p><span class="font-black text-slate-800">شماره سند:</span> PRF-{{ Math.floor(Math.random() * 9000) + 1000 }}</p>
                  <p><span class="font-black text-slate-800">تاریخ صدور:</span> {{ new Date().toLocaleDateString('fa-IR') }}</p>
                </div>
              </div>

              <!-- هشدار مهم اعتبار -->
              <div class="bg-amber-50 border-2 border-dashed border-amber-300 rounded-2xl p-4 mb-8 flex items-start gap-4 print:border-amber-500">
                <div class="w-10 h-10 bg-amber-100 rounded-full flex items-center justify-center text-amber-600 shrink-0"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg></div>
                <div>
                  <h4 class="font-black text-amber-800 mb-1 text-base">اخطار اعتبار قیمت‌ها</h4>
                  <p class="text-sm font-bold text-amber-700 leading-relaxed text-justify">با توجه به نوسانات بازار عمده‌فروشی، مبالغ درج شده <span class="bg-amber-200 text-amber-900 px-2 py-0.5 rounded-md">تنها ۲۴ ساعت</span> از زمان صدور معتبر می‌باشد.</p>
                </div>
              </div>

              <!-- اطلاعات طرفین -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8 text-sm">
                <div class="border border-slate-200 rounded-2xl p-5 bg-slate-50 print:bg-white">
                  <h3 class="font-black text-slate-800 mb-4 text-base border-b border-slate-200 pb-2">فروشنده (تامین‌کننده)</h3>
                  <ul class="space-y-3 text-slate-600 font-medium">
                    <li><span class="font-black text-slate-800">پلتفرم:</span> عمده‌فروشی تاجربام</li>
                    <li><span class="font-black text-slate-800">تامین‌کنندگان:</span> {{ Object.keys(groupedCart).join('، ') }}</li>
                  </ul>
                </div>
                <div class="border border-slate-200 rounded-2xl p-5 bg-white">
                  <h3 class="font-black text-slate-800 mb-4 text-base border-b border-slate-200 pb-2">خریدار</h3>
                  <ul class="space-y-3 text-slate-600 font-medium">
                    <li><span class="font-black text-slate-800">نام:</span> {{ userName }}</li>
                    <li><span class="font-black text-slate-800">حساب:</span> {{ userRole }}</li>
                  </ul>
                </div>
              </div>

              <!-- جدول اقلام -->
              <div class="border border-slate-200 rounded-2xl overflow-hidden mb-8">
                <table class="w-full text-right text-sm">
                  <thead class="bg-slate-100 text-slate-700 font-black border-b border-slate-200">
                    <tr>
                      <th class="px-4 py-4 w-12 text-center">ردیف</th>
                      <th class="px-4 py-4">شرح کالا</th>
                      <th class="px-4 py-4 text-center">تعداد</th>
                      <th class="px-4 py-4">قیمت واحد (تومان)</th>
                      <th class="px-4 py-4 text-left">قیمت کل (تومان)</th>
                    </tr>
                  </thead>
                  <tbody class="font-bold text-slate-600 divide-y divide-slate-100">
                    <tr v-for="(item, index) in cartItems" :key="item.id" class="hover:bg-slate-50">
                      <td class="px-4 py-4 text-center">{{ index + 1 }}</td>
                      <td class="px-4 py-4 text-slate-800 leading-relaxed">{{ item.name }}</td>
                      <td class="px-4 py-4 text-center">
                        <span class="bg-slate-100 px-2 py-1 rounded">{{ item.qty }}</span>
                      </td>
                      <td class="px-4 py-4 font-mono">{{ formatPrice(item.unitPrice) }}</td>
                      <td class="px-4 py-4 font-mono text-slate-800 text-left">{{ formatPrice(item.qty * item.unitPrice) }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- جمع کل و امضا در یک ردیف -->
              <div class="flex flex-col-reverse md:flex-row justify-between items-end gap-10">
                <div class="flex gap-12 text-center font-bold text-slate-500 text-sm print:mb-10 w-full md:w-auto mt-8 md:mt-0">
                  <div>
                    <p class="mb-20 text-slate-800">مهر و امضای فروشنده (سیستمی)</p>
                    <div class="w-32 h-px bg-slate-300 mx-auto"></div>
                  </div>
                  <div>
                    <p class="mb-20 text-slate-800">مهر و امضای خریدار</p>
                    <div class="w-32 h-px bg-slate-300 mx-auto"></div>
                  </div>
                </div>

                <div class="w-full md:w-1/2 bg-slate-50 border border-slate-200 rounded-2xl p-6 space-y-4 text-sm font-bold print:border-black">
                  <div class="flex justify-between text-slate-600">
                    <span>جمع اقلام:</span>
                    <span class="font-mono">{{ formatPrice(subTotal) }} تومان</span>
                  </div>
                  <div class="flex justify-between text-slate-800 text-xl font-black border-t border-slate-200 pt-4 mt-2">
                    <span>مبلغ قابل پرداخت:</span>
                    <span class="font-mono text-blue-700 print:text-black">{{ formatPrice(subTotal) }} <span class="text-xs">تومان</span></span>
                  </div>
                </div>
              </div>
            </div>

            <!-- دکمه‌های اکشن مودال (مخفی در زمان پرینت) -->
            <div class="bg-slate-50 border-t border-slate-200 p-6 flex items-center justify-end gap-3 rounded-b-3xl print:hidden sticky bottom-0 z-20">
              <button @click="showProforma = false" class="px-6 py-3 rounded-xl font-bold text-slate-600 bg-white border border-slate-200 hover:bg-slate-100 hover:text-slate-900 transition-colors">بازگشت</button>
              <button onclick="window.print()" class="px-6 py-3 rounded-xl font-bold text-white bg-slate-900 hover:bg-black transition-colors shadow-md flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                چاپ / ذخیره PDF
              </button>
            </div>

          </div>
        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const showProforma = ref(false);
const cartItems = ref([]);
const userName = ref(localStorage.getItem('user_name') || 'کاربر مهمان');
const userRole = ref(localStorage.getItem('user_role') === 'buyer' ? 'خریدار عمده' : 'کاربر عادی');

// لود کردن محصولات از لوکال استوریج (سبد خرید واقعی)
const loadCart = () => {
  const savedCart = localStorage.getItem('tajerbam_cart');
  if (savedCart) {
    cartItems.value = JSON.parse(savedCart);
  } else {
    // داده‌های دمو اگر سبد کاملا خالی باشد (برای تست طراحی)
    cartItems.value = [];
  }
};

onMounted(() => {
  loadCart();
});

// ذخیره تغییرات در لوکال استوریج
watch(cartItems, (newVal) => {
  localStorage.setItem('tajerbam_cart', JSON.stringify(newVal));
  window.dispatchEvent(new Event('storage'));
}, { deep: true });

const removeItem = (id) => {
  cartItems.value = cartItems.value.filter(item => item.id !== id);
};

const increaseQty = (item) => {
  item.qty++;
};

const decreaseQty = (item) => {
  if (item.qty > (item.minOrder || 1)) {
    item.qty--;
  }
};

const validateQty = (item) => {
  const min = item.minOrder || 1;
  if (item.qty < min) {
    item.qty = min;
  }
};

const groupedCart = computed(() => {
  return cartItems.value.reduce((acc, item) => {
    const seller = item.seller || 'فروشنده معتمد';
    if (!acc[seller]) acc[seller] = [];
    acc[seller].push(item);
    return acc;
  }, {});
});

const subTotal = computed(() => {
  return cartItems.value.reduce((sum, item) => sum + (item.qty * item.unitPrice), 0);
});

const formatPrice = (price) => {
  if(!price) return 0;
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
</script>

<style>
.custom-scrollbar::-webkit-scrollbar { width: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: #f8fafc; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

body:has(.fixed.z-\[99999\]) {
  overflow: hidden;
}

@media print {
  body * { visibility: hidden !important; }
  .fixed.z-\[99999\], .fixed.z-\[99999\] * { visibility: visible !important; }
  .fixed.z-\[99999\] { 
    position: absolute; 
    left: 0; 
    top: 0; 
    width: 100%; 
    margin: 0; 
    padding: 0; 
    box-shadow: none; 
    background: transparent; 
  }
}
</style>