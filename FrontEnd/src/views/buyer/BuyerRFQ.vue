<template>
  <div class="space-y-8 max-w-[1400px] mx-auto pb-20 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- Ultra-Premium Header -->
    <div class="bg-gradient-to-br from-white to-slate-50 p-8 md:p-10 rounded-[2.5rem] border border-slate-100 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)] flex flex-col lg:flex-row items-start lg:items-center justify-between gap-8 relative overflow-hidden z-10">
      
      <!-- Ambient Glow Effects -->
      <div class="absolute -right-32 -top-32 w-96 h-96 bg-violet-200/50 rounded-full mix-blend-multiply opacity-50 blur-[80px] pointer-events-none"></div>
      <div class="absolute -left-20 -bottom-20 w-72 h-72 bg-fuchsia-100/50 rounded-full mix-blend-multiply opacity-50 blur-[60px] pointer-events-none"></div>
      
      <div class="relative z-10 flex items-center gap-6">
        <div class="w-16 h-16 bg-gradient-to-tr from-violet-600 to-fuchsia-600 rounded-2xl flex items-center justify-center shadow-[0_10px_25px_rgba(139,92,246,0.4)] text-white">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg>
        </div>
        <div>
          <h1 class="text-3xl font-black text-slate-800 mb-1 tracking-tight">استعلام قیمت سازمانی (RFQ)</h1>
          <p class="text-sm font-bold text-slate-500">درخواست خرید خود را ثبت کنید تا فروشندگان VIP پیشنهادات رقابتی خود را ارسال کنند.</p>
        </div>
      </div>

      <!-- Segmented Control Tabs -->
      <div class="flex bg-slate-100/80 backdrop-blur-xl p-1.5 rounded-2xl border border-slate-200/60 relative z-10 w-full lg:w-auto shadow-inner">
        <button @click="activeTab = 'new'" :class="['flex-1 lg:flex-none px-8 py-3.5 rounded-xl text-sm font-black transition-all duration-300 relative', activeTab === 'new' ? 'bg-white text-violet-600 shadow-[0_4px_15px_rgba(0,0,0,0.05)]' : 'text-slate-500 hover:text-slate-800']">
          ثبت استعلام جدید
        </button>
        <button @click="activeTab = 'list'" :class="['flex-1 lg:flex-none px-8 py-3.5 rounded-xl text-sm font-black transition-all duration-300 relative flex items-center justify-center gap-2', activeTab === 'list' ? 'bg-white text-violet-600 shadow-[0_4px_15px_rgba(0,0,0,0.05)]' : 'text-slate-500 hover:text-slate-800']">
          پیگیری پیشنهادات
          <span class="absolute -top-2 -right-2 bg-gradient-to-r from-fuchsia-500 to-rose-500 text-white text-[10px] px-2 py-0.5 rounded-lg shadow-sm border border-white">جدید</span>
        </button>
      </div>
    </div>

    <!-- Tab 1: New RFQ Form -->
    <div v-if="activeTab === 'new'" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start relative z-10 animate-fade-in">
      
      <!-- Main Form Area -->
      <div class="lg:col-span-8 space-y-6">
        
        <!-- AI Banner -->
        <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-100 rounded-[2rem] p-6 flex items-start md:items-center gap-4 shadow-sm">
          <div class="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center text-blue-500 shrink-0">
             <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          </div>
          <div>
            <h4 class="text-sm font-black text-slate-800 mb-1">سیستم هوشمند تشخیص دسته‌بندی</h4>
            <p class="text-xs font-bold text-slate-500">دسته‌بندی کالاها به صورت خودکار بر اساس نام کالای وارد شده تنظیم می‌شود تا به بهترین فروشندگان متصل شوید.</p>
          </div>
        </div>

        <div class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_-10px_rgba(0,0,0,0.04)] p-6 md:p-10">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-8 pb-6 border-b border-slate-100 gap-4">
            <h2 class="text-xl font-black text-slate-800 flex items-center gap-3">
              <span class="w-3 h-3 rounded-full bg-violet-500 shadow-[0_0_10px_rgba(139,92,246,0.5)]"></span> اقلام مورد نیاز
            </h2>
            <button @click="addRfqItem" class="text-xs font-black text-violet-600 bg-violet-50 border border-violet-100 hover:bg-violet-600 hover:text-white px-5 py-3 rounded-xl transition-all shadow-sm flex items-center justify-center gap-2 group">
              <svg class="w-4 h-4 transition-transform group-hover:rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg> افزودن کالای جدید
            </button>
          </div>

          <transition-group name="list" tag="div" class="space-y-4">
            <div v-for="(item, index) in rfqForm.items" :key="item.id" class="bg-slate-50/50 border-2 border-slate-100/80 rounded-2xl p-6 relative group transition-all hover:border-violet-300 hover:bg-white focus-within:bg-white focus-within:border-violet-400 focus-within:shadow-[0_10px_30px_rgba(139,92,246,0.1)]">
              
              <button v-if="rfqForm.items.length > 1" @click="removeRfqItem(index)" class="absolute top-4 left-4 w-8 h-8 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-400 hover:text-red-500 hover:border-red-200 hover:bg-red-50 transition-all shadow-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
              </button>

              <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-end pr-10 md:pr-0">
                <div class="md:col-span-8 relative">
                  <label class="block text-[11px] font-black text-slate-500 uppercase tracking-widest mb-2 ml-1">نام دقیق کالا یا مدل</label>
                  <input type="text" v-model="item.name" placeholder="مثلاً: لپ‌تاپ ایسوس مدل X1502ZA" class="w-full bg-white border border-slate-200 text-sm font-black text-slate-800 px-5 py-4 rounded-xl outline-none focus:border-violet-500 focus:ring-4 focus:ring-violet-50 transition-all shadow-sm">
                </div>
                <div class="md:col-span-4 relative">
                  <label class="block text-[11px] font-black text-slate-500 uppercase tracking-widest mb-2 ml-1">تعداد درخواستی</label>
                  <div class="relative">
                    <input type="number" v-model="item.qty" placeholder="0" class="w-full bg-white border border-slate-200 text-base font-black text-center text-slate-800 py-4 rounded-xl outline-none focus:border-violet-500 focus:ring-4 focus:ring-violet-50 transition-all shadow-sm">
                    <span class="absolute left-4 top-1/2 -translate-y-1/2 text-xs font-bold text-slate-400 pointer-events-none">عدد</span>
                  </div>
                </div>
              </div>
            </div>
          </transition-group>
        </div>
        
        <div class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_-10px_rgba(0,0,0,0.04)] p-6 md:p-10">
           <label class="block text-sm font-black text-slate-800 mb-4">توضیحات تکمیلی و شروط خاص (اختیاری)</label>
           <textarea v-model="rfqForm.note" rows="4" placeholder="مثلاً: نیاز به فاکتور رسمی با ارزش افزوده، گارانتی شرکتی ۱۸ ماهه، تحویل در محل کارخانه و..." class="w-full bg-slate-50/50 border-2 border-slate-100/80 text-sm font-medium text-slate-800 p-6 rounded-2xl outline-none focus:bg-white focus:border-violet-400 focus:ring-4 focus:ring-violet-50 transition-all resize-none shadow-sm leading-relaxed"></textarea>
        </div>
      </div>

      <!-- Sidebar Settings -->
      <div class="lg:col-span-4 space-y-6 lg:sticky top-28">
        <div class="bg-slate-900 rounded-[2.5rem] p-8 text-white shadow-[0_20px_50px_-10px_rgba(15,23,42,0.6)] relative overflow-hidden border border-slate-800">
          <!-- Glass Highlights -->
          <div class="absolute right-0 top-0 w-full h-1/2 bg-gradient-to-br from-violet-600/20 to-transparent pointer-events-none"></div>
          <div class="absolute -left-10 -bottom-10 w-40 h-40 bg-fuchsia-600 rounded-full mix-blend-screen filter blur-[60px] opacity-30 pointer-events-none"></div>
          
          <h3 class="font-black text-xl mb-6 relative z-10 border-b border-slate-800 pb-5">تنظیمات نهایی استعلام</h3>
          
          <div class="space-y-6 relative z-10">
            <div>
              <label class="block text-[10px] font-black text-slate-400 uppercase tracking-widest mb-2 ml-1">سقف بودجه کل (تومان)</label>
              <div class="relative">
                <input type="text" v-model="rfqForm.targetBudget" placeholder="توافقی" class="w-full bg-slate-800/50 border border-slate-700 hover:bg-slate-800 focus:bg-slate-800 text-lg font-black text-white px-5 py-4 rounded-xl outline-none focus:border-violet-500 focus:ring-4 focus:ring-violet-500/20 transition-all text-left" dir="ltr">
              </div>
            </div>

            <!-- Custom Toggle -->
            <label class="flex items-start justify-between cursor-pointer group bg-slate-800/40 p-5 rounded-2xl border border-slate-700/50 hover:bg-slate-800 transition-colors">
              <div class="flex flex-col pr-2">
                <span class="font-black text-white text-sm">ارسال به فروشندگان VIP</span>
                <span class="text-[10px] text-slate-400 mt-1 leading-relaxed">فقط تامین‌کنندگان تایید شده با نماد اعتماد و تضمین کیفیت پیشنهاد ارسال کنند.</span>
              </div>
              <div class="relative shrink-0 mt-1">
                <input type="checkbox" checked class="sr-only peer">
                <div class="w-11 h-6 bg-slate-700 peer-focus:outline-none rounded-full peer peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:right-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-violet-500"></div>
              </div>
            </label>
          </div>

          <button @click="submitRfq" :disabled="isSubmitting" class="w-full mt-8 bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-500 hover:to-indigo-500 text-white font-black py-4.5 rounded-2xl shadow-[0_10px_30px_rgba(124,58,237,0.4)] transition-all hover:-translate-y-1 relative z-10 flex items-center justify-center gap-3 text-base disabled:opacity-50 disabled:transform-none">
            <svg v-if="isSubmitting" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path></svg>
            {{ isSubmitting ? 'در حال ارسال به شبکه...' : 'ارسال درخواست (رایگان)' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Tab 2: RFQ List & Quotes -->
    <div v-if="activeTab === 'list'" class="animate-fade-in space-y-6 relative z-10">
      
      <div v-if="isLoadingRfqs" class="flex flex-col items-center justify-center py-20">
        <div class="relative w-20 h-20">
          <div class="absolute inset-0 border-4 border-slate-100 rounded-full"></div>
          <div class="absolute inset-0 border-4 border-violet-600 rounded-full border-t-transparent animate-spin"></div>
        </div>
        <p class="text-sm font-black text-slate-400 mt-4 animate-pulse">در حال بروزرسانی پیشنهادات...</p>
      </div>

      <div v-else v-for="rfq in myRfqs" :key="rfq.id" class="bg-white rounded-[2.5rem] border border-slate-100 shadow-[0_10px_40px_-10px_rgba(0,0,0,0.04)] overflow-hidden transition-all duration-300" :class="{'ring-2 ring-violet-500/20 shadow-[0_15px_50px_-10px_rgba(139,92,246,0.15)]': rfq.expanded}">
        
        <!-- Accordion Header -->
        <div class="p-6 md:p-8 flex flex-col md:flex-row md:items-center justify-between gap-6 cursor-pointer hover:bg-slate-50/50 transition-colors" @click="rfq.expanded = !rfq.expanded">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 bg-slate-50 border border-slate-200 rounded-2xl flex items-center justify-center shrink-0">
              <svg class="w-6 h-6 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            </div>
            <div>
              <h3 class="font-black text-slate-800 text-lg md:text-xl mb-1">{{ rfq.title }}</h3>
              <p class="text-xs font-bold text-slate-500 line-clamp-1">{{ rfq.description }}</p>
            </div>
          </div>
          
          <div class="flex items-center gap-4 shrink-0">
            <div class="bg-gradient-to-r from-violet-50 to-fuchsia-50 border border-violet-100 text-violet-700 text-xs font-black px-4 py-2.5 rounded-xl flex items-center gap-2 shadow-sm">
              <span class="w-2 h-2 rounded-full bg-violet-500 animate-pulse"></span>
              {{ rfq.quotes.length }} پیشنهاد دریافت شده
            </div>
            <button class="w-10 h-10 bg-white border-2 border-slate-100 rounded-xl flex items-center justify-center text-slate-400 transition-transform duration-300" :class="{'rotate-180 bg-slate-50 border-slate-200 text-slate-600': rfq.expanded}">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </button>
          </div>
        </div>

        <!-- Accordion Body (Quotes List) -->
        <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 -translate-y-4" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-4">
          <div v-if="rfq.expanded" class="p-6 md:p-8 bg-slate-50/50 border-t border-slate-100">
            
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div v-for="quote in rfq.quotes" :key="quote.id" class="bg-white border-2 border-slate-100 rounded-[2rem] p-6 md:p-8 hover:border-violet-400 hover:shadow-[0_15px_40px_-10px_rgba(139,92,246,0.15)] transition-all duration-300 relative group">
                
                <!-- Premium Seller Info -->
                <div class="flex justify-between items-start mb-8 pb-6 border-b border-slate-100 border-dashed">
                  <div class="flex items-center gap-4">
                    <div class="w-14 h-14 bg-gradient-to-br from-slate-100 to-slate-200 rounded-2xl flex items-center justify-center font-black text-2xl text-slate-400 shadow-inner border border-white">{{ quote.seller.charAt(0) }}</div>
                    <div>
                      <h5 class="font-black text-slate-800 text-lg mb-1">{{ quote.seller }}</h5>
                      <span class="text-[10px] font-black text-emerald-700 bg-emerald-50 border border-emerald-100 px-2.5 py-1 rounded-md inline-flex items-center gap-1"><svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg> فروشنده وریفای شده</span>
                    </div>
                  </div>
                  <div class="text-left bg-slate-50 px-5 py-3 rounded-2xl border border-slate-200">
                    <span class="block text-[10px] font-black text-slate-400 mb-1 uppercase tracking-widest">قیمت کل</span>
                    <span class="font-black text-indigo-600 text-xl tracking-tight">{{ formatPrice(quote.price) }} <span class="text-[10px]">تومان</span></span>
                  </div>
                </div>
                
                <!-- Notes & AI -->
                <div class="space-y-4 mb-8">
                  <div class="bg-slate-50 border border-slate-100 p-4 rounded-xl text-sm font-bold text-slate-600 leading-relaxed">
                    "{{ quote.note || 'پیشنهاد با بهترین کیفیت و در اسرع وقت ارسال می‌شود.' }}"
                  </div>
                  
                  <div v-if="quote.ai_score > 0" class="flex items-center gap-3 bg-blue-50/50 border border-blue-100 p-3 rounded-xl">
                    <div class="w-8 h-8 rounded-lg bg-blue-100 text-blue-600 flex items-center justify-center shrink-0"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg></div>
                    <div class="flex-1">
                      <div class="flex items-center justify-between mb-1">
                        <span class="text-[10px] font-black text-blue-800 uppercase tracking-wider">ارزیابی هوش مصنوعی تاجربام</span>
                        <span class="text-xs font-black text-blue-600">{{ quote.ai_score }}/10</span>
                      </div>
                      <div class="h-1.5 w-full bg-blue-100 rounded-full overflow-hidden">
                        <div class="h-full bg-blue-500 rounded-full" :style="`width: ${quote.ai_score * 10}%`"></div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Action Buttons -->
                <div class="flex gap-3">
                  <button @click="acceptQuote(rfq.id, quote.id)" :disabled="isAccepting" class="flex-1 bg-slate-900 hover:bg-slate-800 text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(15,23,42,0.15)] transition-all hover:-translate-y-1 text-sm flex items-center justify-center gap-2 disabled:opacity-50 disabled:transform-none">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> 
                    تایید و صدور فاکتور
                  </button>
                </div>
              </div>

              <!-- Empty State for Quotes -->
              <div v-if="rfq.quotes.length === 0" class="col-span-full py-16 flex flex-col items-center justify-center text-center">
                <div class="w-16 h-16 bg-white border border-slate-200 rounded-full flex items-center justify-center text-slate-300 mb-4 shadow-sm">
                  <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <h4 class="font-black text-slate-800 mb-1">در انتظار بررسی فروشندگان</h4>
                <p class="text-xs font-bold text-slate-500">به محض ثبت پیشنهاد جدید از سوی تامین‌کنندگان، پیامک دریافت خواهید کرد.</p>
              </div>
            </div>

          </div>
        </transition>

      </div>
      
      <div v-if="!isLoadingRfqs && myRfqs.length === 0" class="bg-white border border-slate-200 border-dashed rounded-[2.5rem] py-24 flex flex-col items-center justify-center text-center">
        <h3 class="text-xl font-black text-slate-800 mb-2">هنوز استعلامی ثبت نکرده‌اید</h3>
        <p class="text-sm font-bold text-slate-500 mb-6">اولین لیست نیازهای خود را ثبت کنید تا رقابت فروشندگان آغاز شود.</p>
        <button @click="activeTab = 'new'" class="bg-violet-100 text-violet-700 font-black px-6 py-3 rounded-xl hover:bg-violet-200 transition-colors text-sm">ثبت استعلام جدید</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';

const API_BASE = 'https://tajerbam.com';
const token = localStorage.getItem('access_token') || 'test-token';

const activeTab = ref('new');
const isSubmitting = ref(false);
const isLoadingRfqs = ref(false);
const isAccepting = ref(false);

const rfqForm = ref({
  items: [{ id: 1, name: '', qty: null }],
  note: '',
  targetBudget: ''
});

const myRfqs = ref([]);

const formatPrice = (price) => {
  return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : '۰';
};

const addRfqItem = () => { rfqForm.value.items.push({ id: Date.now(), name: '', qty: null }); };
const removeRfqItem = (index) => { rfqForm.value.items.splice(index, 1); };

const fetchRfqs = async () => {
  try {
    isLoadingRfqs.value = true;
    const response = await fetch(`${API_BASE}/api/buyer/rfqs`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (response.ok) {
      const data = await response.json();
      myRfqs.value = data.rfqs.map(r => ({ ...r, expanded: false }));
    }
  } catch (error) {
    console.error("Error fetching RFQs:", error);
  } finally {
    isLoadingRfqs.value = false;
  }
};

const submitRfq = async () => {
  if(!rfqForm.value.items[0].name) { alert("وارد کردن نام حداقل یک کالا الزامی است."); return; }
  
  const totalQty = rfqForm.value.items.reduce((sum, it) => sum + Number(it.qty || 1), 0);
  const description = rfqForm.value.items.map(i => `${i.name} (${i.qty} عدد)`).join(' | ') + '\n' + rfqForm.value.note;
  
  const payload = {
    title: `استعلام خرید ${rfqForm.value.items.length} قلم کالا`,
    qty: totalQty,
    description: description,
    target_price: Number(rfqForm.value.targetBudget) || 0
  };

  try {
    isSubmitting.value = true;
    const response = await fetch(`${API_BASE}/rfq/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify(payload)
    });
    
    if(response.ok) {
      alert('استعلام قدرتمند شما با موفقیت در شبکه B2B تاجربام ثبت شد!');
      // Reset form
      rfqForm.value = { items: [{ id: 1, name: '', qty: null }], note: '', targetBudget: '' };
      activeTab.value = 'list';
      fetchRfqs();
    }
  } catch (error) {
    console.error("Error creating RFQ:", error);
  } finally {
    isSubmitting.value = false;
  }
};

const acceptQuote = async (rfqIdStr, quoteId) => {
  const rfqId = rfqIdStr.split('-').pop(); 
  try {
    isAccepting.value = true;
    const response = await fetch(`${API_BASE}/api/buyer/rfqs/${rfqId}/accept`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
      body: JSON.stringify({ quote_id: quoteId })
    });
    
    if (response.ok) {
      alert("قرارداد تنظیم شد! فاکتور نهایی در بخش سفارشات (Orders) قابل پیگیری و پرداخت می‌باشد.");
      fetchRfqs();
    }
  } catch(error) {
    console.error("Error accepting quote", error);
  } finally {
    isAccepting.value = false;
  }
};

watch(activeTab, (newTab) => {
  if (newTab === 'list') fetchRfqs();
});

onMounted(() => {
  if (activeTab.value === 'list') fetchRfqs();
});
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateX(30px) scale(0.95); }
</style>