<template>
  <div class="min-h-screen bg-slate-900 flex items-center justify-center p-4 relative overflow-hidden font-sans" dir="rtl">
    
<!-- ================= پس‌زمینه متحرک ================= -->
<div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
  <div class="absolute top-[-10%] -left-10 w-[500px] h-[500px] bg-blue-600/40 rounded-full mix-blend-screen filter blur-[100px] animate-blob"></div>
  <div class="absolute top-[20%] -right-20 w-[600px] h-[600px] bg-purple-600/30 rounded-full mix-blend-screen filter blur-[120px] animate-blob animation-delay-2000"></div>
  <div class="absolute -bottom-32 left-[20%] w-[500px] h-[500px] bg-emerald-600/20 rounded-full mix-blend-screen filter blur-[100px] animate-blob animation-delay-4000"></div>
</div>

<!-- ================= کارت اصلی ورود و ثبت‌نام ================= -->
<div class="w-full relative z-10 transition-all duration-500" :class="step === 3 ? 'max-w-[500px]' : 'max-w-[420px]'">
  
  <div class="text-center mb-8">
    <div class="w-16 h-16 bg-white rounded-2xl flex items-center justify-center shadow-[0_0_40px_rgba(255,255,255,0.2)] mx-auto mb-4 border-2 border-white/20">
      <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
    </div>
    <h1 class="text-3xl font-black text-white tracking-tight">پلتفرم تاجربام</h1>
    <p class="text-blue-200 text-sm font-bold mt-2">مرکز تجارت و خرید و فروش عمده B2B</p>
  </div>

  <div class="bg-white/95 backdrop-blur-2xl rounded-[2.5rem] p-8 md:p-10 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.5)] border border-white/40 overflow-hidden relative min-h-[400px]">
    
    <!-- نوار پیشرفت بالا -->
    <div class="absolute top-0 left-0 h-1.5 bg-slate-100 w-full">
      <div class="h-full bg-blue-600 transition-all duration-700 ease-out" :style="`width: ${step === 1 ? '33%' : step === 2 ? '66%' : '100%'}`"></div>
    </div>

    <transition name="slide-fade" mode="out-in">
      
      <!-- ================= مرحله 1: دریافت شماره موبایل ================= -->
      <div v-if="step === 1" key="step1" class="h-full flex flex-col justify-center mt-4">
        <div class="mb-8">
          <h2 class="text-2xl font-black text-slate-800 mb-2">ورود / ثبت‌نام</h2>
          <p class="text-sm font-bold text-slate-500 leading-relaxed">برای ورود به پنل کاربری یا ثبت‌نام، لطفا شماره موبایل خود را وارد کنید.</p>
        </div>

        <form @submit.prevent="sendOTP" class="space-y-6">
          <div>
            <label class="block text-xs font-black text-slate-700 mb-2">شماره موبایل</label>
            <div class="relative flex items-center">
              <span class="absolute left-4 text-slate-400 font-bold font-mono" dir="ltr">+98</span>
              <input 
                type="tel" 
                v-model="phoneNumber" 
                placeholder="09123456789" 
                dir="ltr"
                class="w-full bg-slate-50 border-2 border-slate-200 text-lg font-black text-slate-800 py-4 pl-14 pr-4 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all"
                :class="{'border-red-400 focus:border-red-500 focus:ring-red-50': phoneError}"
                maxlength="11"
                autofocus
              >
            </div>
            <p v-if="phoneError" class="text-xs font-bold text-red-500 mt-2 flex items-center gap-1 leading-relaxed">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              {{ phoneErrorMessage }}
            </p>
          </div>

          <button 
            type="submit" 
            :disabled="isLoading || !phoneNumber" 
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-black py-4 rounded-2xl shadow-lg shadow-blue-500/30 transition-all hover:-translate-y-0.5 disabled:opacity-70 disabled:hover:translate-y-0 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-base"
          >
            <svg v-if="isLoading" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            <template v-else>
              دریافت کد تایید
              <svg class="w-5 h-5 rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </template>
          </button>
        </form>
      </div>

      <!-- ================= مرحله 2: وارد کردن کد تایید (OTP) ================= -->
      <div v-else-if="step === 2" key="step2" class="h-full flex flex-col justify-center mt-4">
        <button @click="goBack" class="w-10 h-10 bg-slate-50 border border-slate-200 rounded-full flex items-center justify-center text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors mb-6 absolute top-8 left-8">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        </button>

        <div class="mb-8 pr-2">
          <h2 class="text-2xl font-black text-slate-800 mb-2">کد تایید را وارد کنید</h2>
          <p class="text-sm font-bold text-slate-500 leading-relaxed">
            کد ۵ رقمی ارسال شده به شماره <span class="font-mono text-blue-600 mx-1" dir="ltr">{{ phoneNumber }}</span> را وارد کنید.
          </p>
        </div>

        <form @submit.prevent="verifyOTP" class="space-y-8">
          <div class="flex justify-between gap-2" dir="ltr">
            <input 
              v-for="(digit, index) in 5" 
              :key="index"
              ref="otpInputsRef"
              type="text" 
              inputmode="numeric"
              maxlength="1"
              v-model="otpDigits[index]"
              @input="handleOtpInput($event, index)"
              @keydown.delete="handleOtpDelete($event, index)"
              class="w-12 h-14 sm:w-14 sm:h-16 bg-slate-50 border-2 border-slate-200 text-2xl font-black text-center text-slate-800 rounded-2xl outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-50 transition-all shadow-sm"
            >
          </div>
          <p v-if="otpError" class="text-xs font-bold text-red-500 text-center -mt-4 leading-relaxed">{{ otpErrorMessage }}</p>

          <div class="space-y-4">
            <button 
              type="submit" 
              :disabled="isLoading || !isOtpComplete" 
              class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-2xl shadow-lg shadow-slate-900/20 transition-all hover:-translate-y-0.5 disabled:opacity-70 flex items-center justify-center gap-2 text-base"
            >
              <svg v-if="isLoading" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              تایید و ورود
            </button>
            <div class="text-center">
              <p v-if="timer > 0" class="text-xs font-bold text-slate-500 flex items-center justify-center gap-1.5">
                <svg class="w-4 h-4 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                ارسال مجدد کد تا <span class="font-mono text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded">{{ formattedTimer }}</span>
              </p>
              <button v-else @click="resendOTP" type="button" class="text-xs font-black text-blue-600 hover:text-blue-800 transition-colors">
                ارسال مجدد کد تایید
              </button>
            </div>
          </div>
        </form>
      </div>

      <!-- ================= مرحله 3: پروفایل کاربری ================= -->
      <div v-else-if="step === 3" key="step3" class="h-full flex flex-col justify-start mt-2">
        <div class="mb-6 shrink-0 border-b border-slate-100 pb-4">
          <h2 class="text-2xl font-black text-slate-800 mb-2">تکمیل پروفایل سازمانی</h2>
          <p class="text-sm font-bold text-slate-500 leading-relaxed">لطفاً نقش خود را در پلتفرم تاجربام انتخاب کرده و اطلاعات مرتبط را وارد کنید.</p>
        </div>

        <form @submit.prevent="completeRegistration" class="space-y-6 overflow-y-auto custom-scrollbar pr-2 pb-4 max-h-[55vh]">
          
          <!-- انتخاب نقش -->
          <div>
            <label class="block text-xs font-black text-slate-700 mb-3">نقش کاربری <span class="text-red-500">*</span></label>
            <div class="grid grid-cols-3 gap-3">
              <label class="relative border-2 rounded-2xl p-3 cursor-pointer transition-all hover:bg-slate-50 flex flex-col items-center text-center gap-2" :class="userInfo.role === 'buyer' ? 'border-blue-500 bg-blue-50/40 shadow-sm' : 'border-slate-100'">
                <input type="radio" v-model="userInfo.role" value="buyer" class="sr-only">
                <div class="w-10 h-10 rounded-full flex items-center justify-center transition-colors" :class="userInfo.role === 'buyer' ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-100 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg></div>
                <span class="font-black text-[11px]" :class="userInfo.role === 'buyer' ? 'text-blue-700' : 'text-slate-600'">خریدار عمده</span>
              </label>

              <label class="relative border-2 rounded-2xl p-3 cursor-pointer transition-all hover:bg-slate-50 flex flex-col items-center text-center gap-2" :class="userInfo.role === 'seller' ? 'border-emerald-500 bg-emerald-50/40 shadow-sm' : 'border-slate-100'">
                <input type="radio" v-model="userInfo.role" value="seller" class="sr-only">
                <div class="w-10 h-10 rounded-full flex items-center justify-center transition-colors" :class="userInfo.role === 'seller' ? 'bg-emerald-500 text-white shadow-md' : 'bg-slate-100 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m3-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg></div>
                <span class="font-black text-[11px]" :class="userInfo.role === 'seller' ? 'text-emerald-700' : 'text-slate-600'">تامین‌کننده</span>
              </label>

              <label class="relative border-2 rounded-2xl p-3 cursor-pointer transition-all hover:bg-slate-50 flex flex-col items-center text-center gap-2" :class="userInfo.role === 'marketer' ? 'border-purple-500 bg-purple-50/40 shadow-sm' : 'border-slate-100'">
                <input type="radio" v-model="userInfo.role" value="marketer" class="sr-only">
                <div class="w-10 h-10 rounded-full flex items-center justify-center transition-colors" :class="userInfo.role === 'marketer' ? 'bg-purple-600 text-white shadow-md' : 'bg-slate-100 text-slate-400'"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"></path></svg></div>
                <span class="font-black text-[11px]" :class="userInfo.role === 'marketer' ? 'text-purple-700' : 'text-slate-600'">بازاریاب</span>
              </label>
            </div>
          </div>

          <!-- فیلدهای پویا بر اساس نقش انتخاب شده -->
          <div class="space-y-4">
            
            <!-- نام اصلی -->
            <div>
              <label class="block text-xs font-black text-slate-700 mb-2">
                {{ userInfo.role === 'buyer' ? 'نام و نام خانوادگی نماینده خرید' : userInfo.role === 'seller' ? 'نام و نام خانوادگی صاحب جواز' : 'نام و نام خانوادگی کامل' }}
                <span class="text-red-500">*</span>
              </label>
              <input type="text" v-model="userInfo.fullName" required class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 px-4 rounded-xl outline-none focus:bg-white focus:border-blue-500">
            </div>

            <!-- خریدار -->
            <template v-if="userInfo.role === 'buyer'">
              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">نام شرکت / سازمان (اختیاری)</label>
                <input type="text" v-model="userInfo.companyName" placeholder="مثال: کارخانجات پارس" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 px-4 rounded-xl outline-none focus:bg-white focus:border-blue-500">
              </div>
              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">شناسه ملی حقوقی (جهت فاکتور رسمی)</label>
                <input type="text" v-model="userInfo.nationalId" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 px-4 rounded-xl outline-none focus:bg-white focus:border-blue-500">
              </div>
            </template>

            <!-- تامین‌کننده -->
            <template v-if="userInfo.role === 'seller'">
              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">نام فروشگاه / برند <span class="text-red-500">*</span></label>
                <input type="text" v-model="userInfo.storeName" placeholder="نام کسب و کار شما" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 px-4 rounded-xl outline-none focus:bg-white focus:border-blue-500">
              </div>
              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">شماره جواز / ثبت شرکت</label>
                <input type="text" v-model="userInfo.licenseNumber" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 px-4 rounded-xl outline-none focus:bg-white focus:border-blue-500">
              </div>
            </template>

            <!-- بازاریاب -->
            <template v-if="userInfo.role === 'marketer'">
              <div>
                <label class="block text-xs font-black text-slate-700 mb-2">شماره شبا بانکی (جهت واریز پورسانت) <span class="text-red-500">*</span></label>
                <div class="relative flex items-center">
                  <span class="absolute left-4 text-slate-400 font-bold font-mono" dir="ltr">IR</span>
                  <input type="text" v-model="userInfo.shebaNumber" class="w-full bg-slate-50 border-2 border-slate-200 text-sm font-bold py-3.5 pl-12 pr-4 rounded-xl outline-none focus:bg-white focus:border-blue-500" placeholder="0000000000000000000000" dir="ltr">
                </div>
              </div>
            </template>
          </div>

          <div class="pt-2 shrink-0">
            <button type="submit" :disabled="isRegistering || !isFormValid" class="w-full bg-slate-900 hover:bg-black text-white font-black py-4 rounded-xl shadow-lg transition-all disabled:opacity-50 flex items-center justify-center gap-2">
              <svg v-if="isRegistering" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              تایید اطلاعات و ورود به داشبورد
            </button>
          </div>
        </form>
      </div>
    </transition>
  </div>
</div>

  </div>
</template>

<script setup>
import { ref, computed, nextTick, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// تنظیم آدرس صحیح سرور پایتون بر روی پورت local
const API_BASE_URL = 'https://tajerbam.com';

const step = ref(1);
const isLoading = ref(false);
const isRegistering = ref(false);

const phoneNumber = ref('');
const phoneError = ref(false);
const phoneErrorMessage = ref('');

const otpDigits = ref(['', '', '', '', '']);
const otpInputsRef = ref([]);
const otpError = ref(false);
const otpErrorMessage = ref('');

const userInfo = ref({
  fullName: '',
  role: 'buyer', 
  companyName: '',
  nationalId: '',
  storeName: '',
  licenseNumber: '',
  shebaNumber: ''
});

const isFormValid = computed(() => {
  if (!userInfo.value.fullName) return false;
  if (userInfo.value.role === 'seller' && !userInfo.value.storeName) return false;
  if (userInfo.value.role === 'marketer' && !userInfo.value.shebaNumber) return false;
  return true; 
});

const sendOTP = async () => {
  const regex = /^09\d{9}$/;
  if (!regex.test(phoneNumber.value)) {
    phoneError.value = true;
    phoneErrorMessage.value = 'شماره موبایل وارد شده معتبر نیست.';
    return;
  }
  
  phoneError.value = false;
  isLoading.value = true;
  
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/send-otp`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone: phoneNumber.value })
    });
    
    if (!response.ok) {
      throw new Error('خطا در ارتباط با سرور.');
    }
    
    step.value = 2;
    startTimer();
    nextTick(() => { if(otpInputsRef.value[0]) otpInputsRef.value[0].focus(); });
  } catch (error) {
    // Fallback: حتی اگر سرور آفلاین باشد، جهت تست وارد مرحله ۲ می‌شود
    step.value = 2;
    startTimer();
    nextTick(() => { if(otpInputsRef.value[0]) otpInputsRef.value[0].focus(); });
  } finally {
    isLoading.value = false;
  }
};

const isOtpComplete = computed(() => otpDigits.value.every(d => d !== ''));

const handleOtpInput = (e, index) => {
  const val = e.target.value;
  if (!/^\d*$/.test(val)) { otpDigits.value[index] = ''; return; }
  otpError.value = false;
  if (val && index < 4) nextTick(() => { otpInputsRef.value[index + 1].focus(); });
  if (isOtpComplete.value && index === 4) verifyOTP();
};

const handleOtpDelete = (e, index) => {
  if (!otpDigits.value[index] && index > 0) otpInputsRef.value[index - 1].focus();
};

const routeUserByRole = (role) => {
  const target = role ? role.toLowerCase() : 'seller';
  
  if (target === 'buyer') router.push('/buyer');
  else if (target === 'marketer') router.push('/marketer');
  else if (target === 'admin') router.push('/admin');
  else router.push('/panel'); // دیفالت فروشنده
};

const verifyOTP = async () => {
  if (!isOtpComplete.value) return;
  const finalCode = otpDigits.value.join('');
  isLoading.value = true;
  otpError.value = false;
  
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/verify-otp`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone: phoneNumber.value, code: finalCode })
    });

    if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData.detail || 'کد وارد شده اشتباه است یا منقضی شده.');
    }
    
    const data = await response.json();
    
    if (data.access_token) {
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('tajerbam_token', data.access_token);
    }
    
    const isNewUser = 
        data.is_new === true || 
        String(data.is_new).toLowerCase() === 'true' || 
        data.full_name === 'کاربر جدید' || 
        !data.full_name || 
        data.full_name.trim() === '';

    if (!isNewUser && data.user_role) {
      localStorage.setItem('user_role', data.user_role);
      localStorage.setItem('user_name', data.full_name);
      localStorage.setItem('full_name', data.full_name);
      routeUserByRole(data.user_role);
    } else {
      step.value = 3;
    }
  } catch (error) {
    otpError.value = true;
    otpErrorMessage.value = error.message || 'کد تایید وارد شده اشتباه است.';
    otpDigits.value = ['', '', '', '', ''];
    if(otpInputsRef.value[0]) otpInputsRef.value[0].focus();
  } finally {
    isLoading.value = false;
  }
};

const completeRegistration = async () => {
  isRegistering.value = true;
  try {
    const token = localStorage.getItem('access_token') || 'test-token';
    const response = await fetch(`${API_BASE_URL}/api/auth/update-profile`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json', 
        'Authorization': `Bearer ${token}` 
      },
      body: JSON.stringify({ 
        full_name: userInfo.value.fullName, 
        role: userInfo.value.role,
        company_name: userInfo.value.companyName,
        national_id: userInfo.value.nationalId,
        store_name: userInfo.value.storeName,
        license_number: userInfo.value.licenseNumber,
        sheba_number: userInfo.value.shebaNumber
      })
    });

    if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData.detail || "ثبت اطلاعات با خطا مواجه شد.");
    }
    
    const data = await response.json();
    
    if (data.access_token) {
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('tajerbam_token', data.access_token);
    }
    
    localStorage.setItem('user_role', userInfo.value.role);
    localStorage.setItem('user_name', userInfo.value.fullName);
    localStorage.setItem('full_name', userInfo.value.fullName);
    
    routeUserByRole(userInfo.value.role);

  } catch (error) {
    // Fallback logic for offline test
    localStorage.setItem('user_role', userInfo.value.role);
    localStorage.setItem('user_name', userInfo.value.fullName);
    localStorage.setItem('full_name', userInfo.value.fullName);
    routeUserByRole(userInfo.value.role);
  } finally {
    isRegistering.value = false;
  }
};

const goBack = () => { step.value = 1; otpDigits.value = ['', '', '', '', '']; stopTimer(); };

const timer = ref(120);
let timerInterval = null;
const startTimer = () => { timer.value = 120; clearInterval(timerInterval); timerInterval = setInterval(() => { if (timer.value > 0) timer.value--; else stopTimer(); }, 1000); };
const stopTimer = () => clearInterval(timerInterval);
const resendOTP = () => { sendOTP(); otpDigits.value = ['', '', '', '', '']; };
const formattedTimer = computed(() => `${Math.floor(timer.value / 60).toString().padStart(2, '0')}:${(timer.value % 60).toString().padStart(2, '0')}`);

onUnmounted(() => stopTimer());
</script>

<style scoped>
@keyframes blob { 0% { transform: translate(0px, 0px) scale(1); } 33% { transform: translate(30px, -50px) scale(1.1); } 66% { transform: translate(-20px, 20px) scale(0.9); } 100% { transform: translate(0px, 0px) scale(1); } }
.animate-blob { animation: blob 7s infinite; }
.animation-delay-2000 { animation-delay: 2s; }
.animation-delay-4000 { animation-delay: 4s; }

.slide-fade-enter-active { transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); }
.slide-fade-leave-active { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.slide-fade-enter-from { opacity: 0; transform: translateX(-30px); }
.slide-fade-leave-to { opacity: 0; transform: translateX(30px); }

.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 4px; }
</style>