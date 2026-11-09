<template>
  <div class="space-y-6 max-w-[1400px] mx-auto pb-16 font-sans text-slate-800 relative" dir="rtl">
    
    <!-- ================= هدر صفحه و تب‌ها ================= -->
    <div class="bg-white p-6 md:p-10 rounded-[2.5rem] border border-slate-100 shadow-[0_8px_30px_rgb(0,0,0,0.03)] flex flex-col md:flex-row items-start md:items-center justify-between gap-6 relative overflow-hidden">
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-emerald-100 rounded-full mix-blend-multiply opacity-50 blur-[70px] pointer-events-none"></div>
      
      <div class="flex items-center gap-6 relative z-10">
        <div class="w-16 h-16 md:w-20 md:h-20 bg-gradient-to-br from-emerald-400 to-teal-600 rounded-[1.5rem] flex items-center justify-center text-white shadow-lg shadow-emerald-500/30 shrink-0 border border-emerald-300">
          <svg class="w-8 h-8 md:w-10 md:h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"></path></svg>
        </div>
        <div>
          <h1 class="text-2xl md:text-3xl font-black text-slate-800 tracking-tight mb-2">ارتباطات و همکاری B2B</h1>
          <p class="text-sm font-bold text-slate-500 max-w-lg leading-relaxed">تامین‌کنندگان قدرتمند بیابید، درخواست نمایندگی فروش بفرستید یا به پیشنهادات همکاری پاسخ دهید.</p>
        </div>
      </div>
      
      <!-- تب‌های جابجایی -->
      <div class="relative z-10 flex bg-slate-50 p-2 rounded-2xl border border-slate-200 w-full md:w-auto shadow-inner">
        <button @click="activeTab = 'search'" :class="['flex-1 md:flex-none px-6 py-3.5 rounded-xl text-sm font-black transition-all', activeTab === 'search' ? 'bg-white text-emerald-600 shadow-sm border border-slate-100' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-100']">
          جستجوی تامین‌کننده
        </button>
        <button @click="activeTab = 'received'" :class="['flex-1 md:flex-none px-6 py-3.5 rounded-xl text-sm font-black transition-all flex items-center justify-center gap-2', activeTab === 'received' ? 'bg-white text-emerald-600 shadow-sm border border-slate-100' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-100']">
          صندوق پیشنهادات
          <span class="bg-rose-500 text-white text-[10px] px-2 py-0.5 rounded-md shadow-sm">۲ جدید</span>
        </button>
      </div>
    </div>

    <!-- ================= تب 1: جستجوی تامین‌کنندگان ================= -->
    <div v-if="activeTab === 'search'" class="animate-fade-in space-y-8 relative z-10">
      
      <!-- نوار جستجو پیشرفته -->
      <div class="bg-white p-5 rounded-[2rem] border border-slate-100 shadow-sm flex flex-col md:flex-row gap-4 relative z-10">
        <div class="relative w-full md:flex-grow">
          <input type="text" v-model="searchQuery" placeholder="نام فروشنده، دسته‌بندی یا کلمه کلیدی کالا..." class="w-full bg-slate-50 border-2 border-slate-100 hover:border-emerald-200 text-sm font-black text-slate-800 px-5 py-4 pr-14 rounded-2xl focus:bg-white focus:border-emerald-500 outline-none transition-all shadow-sm">
          <svg class="w-6 h-6 text-slate-400 absolute right-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        <select class="w-full md:w-64 bg-slate-50 border-2 border-slate-100 hover:border-emerald-200 text-sm font-bold text-slate-700 px-5 py-4 rounded-2xl outline-none focus:bg-white focus:border-emerald-500 cursor-pointer shadow-sm transition-all">
          <option value="all">همه دسته‌بندی‌ها</option>
          <option value="digital">کالای دیجیتال</option>
          <option value="home">لوازم خانگی</option>
          <option value="tools">ابزارآلات صنعتی</option>
        </select>
      </div>

      <!-- لیست تامین‌کنندگان -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative min-h-[300px]">
        
        <div v-if="isLoadingSellers" class="absolute inset-0 flex justify-center py-20 z-20">
          <svg class="w-10 h-10 text-emerald-500 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        </div>

        <div v-for="seller in filteredSellers" :key="seller.id" class="bg-white rounded-[2.5rem] border border-slate-200/60 p-6 md:p-8 shadow-sm hover:shadow-[0_25px_50px_-12px_rgba(16,185,129,0.15)] hover:border-emerald-300 transition-all duration-300 flex flex-col group relative overflow-hidden">
          
          <div class="absolute top-0 right-0 w-1.5 h-full bg-emerald-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

          <div class="flex items-start gap-5 mb-6">
            <div class="w-16 h-16 bg-slate-50 rounded-[1.2rem] flex items-center justify-center font-black text-2xl text-slate-400 border border-slate-100 group-hover:bg-emerald-50 group-hover:text-emerald-600 group-hover:border-emerald-200 transition-all shadow-sm shrink-0">
              {{ seller.name.charAt(0) }}
            </div>
            <div>
              <h3 class="font-black text-slate-800 text-lg group-hover:text-emerald-700 transition-colors mb-1.5">{{ seller.name }}</h3>
              <p class="text-[11px] font-bold text-slate-500 bg-slate-100 border border-slate-200 px-2.5 py-1 rounded-lg w-fit">{{ seller.category }}</p>
            </div>
          </div>

          <div class="text-xs font-medium text-slate-600 mb-8 flex-grow leading-relaxed bg-slate-50/50 p-4 rounded-2xl border border-slate-100">
            <span class="font-black text-slate-400 block mb-2">کلمات کلیدی محصولات:</span> 
            <div class="flex flex-wrap gap-2">
              <span v-for="kw in seller.keywords" :key="kw" class="bg-white border border-slate-200 px-2 py-1 rounded-md text-[10px] text-slate-500">{{ kw }}</span>
            </div>
          </div>

          <button @click="openActionModal('send_request', seller)" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl shadow-[0_10px_20px_rgba(0,0,0,0.15)] transition-all hover:-translate-y-1 text-sm flex items-center justify-center gap-2">
            ارسال درخواست نمایندگی فروش
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
        </div>
        
        <div v-if="!isLoadingSellers && filteredSellers.length === 0" class="col-span-full py-12 text-center text-slate-400 font-bold">
          فروشنده‌ای با این مشخصات یافت نشد.
        </div>
      </div>
    </div>

    <!-- ================= تب 2: درخواست‌های دریافتی ================= -->
    <div v-if="activeTab === 'received'" class="animate-fade-in grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative z-10">
      
      <div v-for="req in requests" :key="req.id" class="bg-white rounded-[2.5rem] border border-slate-200/60 p-6 md:p-8 shadow-sm hover:shadow-[0_25px_50px_-12px_rgba(16,185,129,0.15)] hover:border-emerald-300 transition-all duration-300 flex flex-col group relative overflow-hidden">
        
        <div class="absolute top-0 right-0 w-full h-1.5 bg-gradient-to-r from-emerald-400 to-teal-500 transform scale-x-0 group-hover:scale-x-100 transition-transform origin-right duration-500"></div>

        <div class="flex justify-between items-start mb-6">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 bg-slate-50 rounded-[1.2rem] flex items-center justify-center font-black text-2xl text-slate-400 border border-slate-100 group-hover:bg-emerald-50 group-hover:border-emerald-200 group-hover:text-emerald-600 transition-all shadow-sm">
              {{ req.seller.charAt(0) }}
            </div>
            <div>
              <h3 class="font-black text-slate-800 text-lg group-hover:text-emerald-700 transition-colors mb-1">{{ req.seller }}</h3>
              <p class="text-[11px] font-bold text-slate-500 bg-slate-50 border border-slate-200 px-2 py-0.5 rounded-lg">{{ req.category }}</p>
            </div>
          </div>
        </div>

        <div class="bg-emerald-50/50 border border-emerald-200/60 rounded-2xl p-5 mb-8 flex-grow shadow-inner">
          <div class="flex items-center justify-between mb-4 border-b border-emerald-100/60 pb-4">
            <span class="text-xs font-black text-slate-600">پیشنهاد پورسانت:</span>
            <span class="bg-gradient-to-r from-emerald-500 to-teal-500 text-white text-sm font-black px-4 py-1.5 rounded-xl shadow-md">{{ req.commission }}٪ سود</span>
          </div>
          <p class="text-[11px] font-bold text-slate-700 leading-relaxed text-justify relative">
            <span class="absolute -top-3 -right-2 text-2xl text-emerald-200 font-serif">"</span>
            {{ req.message }}
          </p>
        </div>

        <div class="flex gap-3 mt-auto">
          <button @click="openActionModal('accept_request', req)" class="flex-1 bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-black py-3.5 rounded-xl shadow-[0_10px_20px_rgba(16,185,129,0.3)] transition-all hover:-translate-y-1 text-sm flex items-center justify-center gap-2">
            تایید و شروع همکاری
          </button>
          <button @click="openActionModal('chat', req)" class="w-14 bg-white border-2 border-slate-200 text-slate-500 hover:text-emerald-600 hover:border-emerald-400 hover:bg-emerald-50 font-bold py-3.5 rounded-xl transition-all flex items-center justify-center tooltip shadow-sm" title="شروع مذاکره در چت">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
          </button>
        </div>
      </div>

    </div>

    <!-- ================= MODAL: Paywall یا ارتقا پلن ================= -->
    <Teleport to="body">
      <transition enter-active-class="transition duration-400 ease-out" enter-from-class="opacity-0 scale-95 translate-y-4" enter-to-class="opacity-100 scale-100 translate-y-0" leave-active-class="transition duration-300 ease-in" leave-from-class="opacity-100 scale-100 translate-y-0" leave-to-class="opacity-0 scale-95 translate-y-4">
        <div v-if="actionModal.show" class="fixed inset-0 z-[99999] flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md" dir="rtl">
          
          <div class="bg-white w-full max-w-md rounded-[3rem] shadow-2xl relative overflow-hidden border border-white/20">
            <!-- افکت‌های پس‌زمینه مودال -->
            <div class="absolute top-0 right-0 w-full h-3 bg-gradient-to-r from-amber-400 to-orange-500 z-10"></div>
            <div class="absolute -right-16 -top-16 w-64 h-64 bg-amber-400 rounded-full mix-blend-screen filter blur-[70px] opacity-30 pointer-events-none"></div>
            
            <button @click="actionModal.show = false" class="absolute top-6 left-6 z-20 w-10 h-10 bg-slate-50 hover:bg-red-50 text-slate-400 hover:text-red-500 rounded-full flex items-center justify-center transition-colors border border-slate-100">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>

            <div class="p-8 md:p-10 pb-6 text-center relative z-10">
              <div class="w-24 h-24 bg-gradient-to-tr from-amber-100 to-orange-100 rounded-[2rem] flex items-center justify-center mx-auto mb-6 shadow-inner border border-amber-200">
                <svg class="w-12 h-12 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              </div>
              <h2 class="text-2xl font-black text-slate-800 mb-3 tracking-tight">پرداخت هزینه عملیات</h2>
              <p class="text-slate-500 font-bold text-sm leading-relaxed px-2">
                شما در حال حاضر پلن VIP (شریک تجاری) ندارید. برای {{ actionModal.title }} می‌توانید هزینه این تک عملیات را بپردازید یا با ارتقاء حساب خود، نامحدود از این قابلیت استفاده کنید.
              </p>
            </div>

            <div class="p-6 md:p-8 bg-slate-50/90 border-t border-slate-100 space-y-5">
              <!-- گزینه 1: پرداخت موردی -->
              <label class="block border-2 border-amber-200 bg-amber-50/50 rounded-2xl p-5 cursor-pointer hover:border-amber-400 hover:bg-amber-100/50 transition-colors relative group">
                <div class="flex justify-between items-center mb-1">
                  <span class="font-black text-slate-800 text-sm">پرداخت هزینه {{ actionModal.title }}</span>
                  <span class="font-black text-amber-600 text-lg tracking-tight">۴۹,۰۰۰ <span class="text-[10px]">تومان</span></span>
                </div>
                <button @click="payForAction" class="w-full mt-4 bg-amber-500 hover:bg-amber-600 text-white text-sm font-black py-4 rounded-xl shadow-[0_8px_20px_rgba(245,158,11,0.3)] transition-all group-hover:-translate-y-0.5 flex items-center justify-center gap-2">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
                  پرداخت و انجام آنی عملیات
                </button>
              </label>

              <div class="flex items-center gap-4 py-2">
                <div class="h-px bg-slate-300 flex-1"></div>
                <span class="text-[11px] font-black text-slate-400 bg-slate-100 px-3 py-1 rounded-full">پیشنهاد فوق‌العاده</span>
                <div class="h-px bg-slate-300 flex-1"></div>
              </div>

              <!-- گزینه 2: ارتقا پلن -->
              <button @click="$router.push('/marketer/plans')" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4.5 rounded-2xl shadow-[0_10px_20px_rgba(0,0,0,0.2)] transition-all hover:-translate-y-1 flex items-center justify-center gap-2 text-sm">
                خرید پلن VIP (دسترسی کامل و نامحدود)
                <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </button>
            </div>
          </div>

        </div>
      </transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const API_BASE_URL = 'https://tajerbam.com';
const token = localStorage.getItem('tajerbam_token');

const activeTab = ref('search');
const hasActivePlan = ref(false); // بررسی VIP بودن

const isLoadingSellers = ref(false);
const allSellers = ref([]);
const requests = ref([]);

const fetchSellersAndRequests = async () => {
  isLoadingSellers.value = true;
  try {
    // در واقعیت این مسیر به اندپوینت سرچ و ریکوئست‌ها متصل می‌شود.
    // به دلیل اینکه API مارکتر به صورت کامل در پایتون قبلی تعریف نشده بود، Mock می‌کنیم.
    setTimeout(() => {
      allSellers.value = [
        { id: 101, name: 'رایان تکرو', category: 'کالای دیجیتال', keywords: ['لپ‌تاپ', 'موس', 'کیبورد'] },
        { id: 102, name: 'دیجیتال شاپ مرکزی', category: 'کالای دیجیتال', keywords: ['گوشی موبایل', 'مانیتور', 'تبلت'] },
        { id: 103, name: 'ابزارآلات صنعتی پیشرو', category: 'ابزارآلات', keywords: ['دریل', 'فرز', 'جعبه ابزار'] },
        { id: 104, name: 'پخش لوازم خانگی امید', category: 'لوازم خانگی', keywords: ['یخچال', 'جاروبرقی', 'مخلوط‌کن'] },
      ];
      
      requests.value = [
        { id: 1, seller: 'شرکت رایان گستر', category: 'تامین‌کننده کالای دیجیتال', commission: 12, message: 'سلام، ما تولیدکننده مستقیم هستیم و محصولاتمون حاشیه سود بالایی داره. مایلیم فروش آنلاینمون رو با این پورسانت ویژه به شما و تیمتون بسپاریم.' },
        { id: 2, seller: 'پخش عمده ابزارآلات صنعتی', category: 'واردکننده مستقیم', commission: 15, message: 'با توجه به فروش‌های موفق اخیر شما، ما آمادگی خود را برای اعطای نمایندگی فروش محصولات ابزارآلات خود با ۱۵٪ کمیسیون خالص اعلام می‌کنیم.' },
      ];
      isLoadingSellers.value = false;
    }, 600);
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  fetchSellersAndRequests();
});

const searchQuery = ref('');
const filteredSellers = computed(() => {
  if (!searchQuery.value) return allSellers.value;
  return allSellers.value.filter(s => 
    s.name.includes(searchQuery.value) || 
    s.category.includes(searchQuery.value) || 
    s.keywords.some(k => k.includes(searchQuery.value))
  );
});

// منطق مودال پرداخت موردی
const actionModal = ref({ show: false, title: '', data: null });

const openActionModal = (actionType, data) => {
  if (hasActivePlan.value) {
    alert("عملیات با موفقیت انجام شد (حساب شما VIP است).");
    return;
  }
  
  let title = '';
  if(actionType === 'send_request') title = 'ارسال درخواست همکاری';
  if(actionType === 'accept_request') title = 'تایید درخواست همکاری';
  if(actionType === 'chat') title = 'باز کردن چت اختصاصی B2B';

  actionModal.value = { show: true, title, data };
};

const payForAction = () => {
  alert(`مبلغ با موفقیت پرداخت شد و عملیات "${actionModal.value.title}" انجام گردید.`);
  actionModal.value.show = false;
};
</script>

<style scoped>
.animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
body:has(.fixed.z-\[99999\]) { overflow: hidden; }
</style>