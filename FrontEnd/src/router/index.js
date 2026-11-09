import { createRouter, createWebHistory } from 'vue-router'
import { h } from 'vue'

// ================= 1. ایمپورت قالب‌های اصلی (Layouts) =================
import ShopLayout from '../layouts/ShopLayout.vue'
import PanelLayout from '../layouts/PanelLayout.vue'
import MarketerLayout from '../layouts/MarketerLayout.vue'
import BuyerLayout from '../layouts/BuyerLayout.vue'
import AdminLayout from '../layouts/AdminLayout.vue'

// کامپوننت جایگزین برای صفحاتی که هنوز ساخته نشده‌اند
const DummyView = { setup() { return () => h('div', { class: 'p-8 text-center font-black text-2xl text-slate-400 mt-20' }, 'این صفحه به زودی در دسترس خواهد بود...') } }

// ================= 2. پیکربندی مسیرها (Routes) =================
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    else return { top: 0, behavior: 'smooth' }
  },
  routes: [
    // ---------------- مسیرهای فروشگاه (Shop) ----------------
    {
      path: '/',
      component: ShopLayout,
      children: [
        { path: '', name: 'home', component: () => import('../views/shop/HomeView.vue').catch(() => DummyView) },
        { path: 'product/:id', name: 'product', component: () => import('../views/shop/ProductView.vue').catch(() => DummyView) },
        { path: 'category/:slug', name: 'category', component: () => import('../views/shop/CategoryView.vue').catch(() => DummyView) },
        { path: 'cart', name: 'cart', component: () => import('../views/shop/CartView.vue').catch(() => DummyView) },
        { path: 'checkout', name: 'checkout', component: () => import('../views/shop/CheckoutView.vue').catch(() => DummyView) }
      ]
    },

    // ---------------- مسیر احراز هویت (Auth) ----------------
    { 
      path: '/login', 
      name: 'login', 
      component: () => import('../views/auth/LoginView.vue').catch(() => DummyView) 
    },

    // ---------------- مسیرهای پنل فروشندگان (Seller Panel) ----------------
    {
      path: '/panel',
      component: PanelLayout,
      children: [
        { path: '', name: 'dashboard', component: () => import('../views/panel/DashboardHome.vue').catch(() => DummyView) },
        { path: 'add-product', name: 'add-product', component: () => import('../views/panel/AddProduct.vue').catch(() => DummyView) },
        { path: 'products', name: 'product-list', component: () => import('../views/panel/ProductList.vue').catch(() => DummyView) },
        { path: 'orders', name: 'order-list', component: () => import('../views/panel/OrderList.vue').catch(() => DummyView) },
        { path: 'plans', name: 'plans', component: () => import('../views/panel/PlansView.vue').catch(() => DummyView) },
        { path: 'requests', name: 'purchase-requests', component: () => import('../views/panel/RequestsView.vue').catch(() => DummyView) },
        { path: 'marketing', name: 'smart-marketing', component: () => import('../views/panel/SmartMarketing.vue').catch(() => DummyView) }
      ]
    },

    // ---------------- مسیرهای پنل بازاریابان (Marketer Panel) ----------------
    {
      path: '/marketer',
      component: MarketerLayout,
      children: [
        { path: '', name: 'marketer-dashboard', component: () => import('../views/marketer/MarketerDashboard.vue').catch(() => DummyView) },
        { path: 'plans', name: 'marketer-plans', component: () => import('../views/marketer/MarketerPlans.vue').catch(() => DummyView) },
        { path: 'requests', name: 'marketer-requests', component: () => import('../views/marketer/MarketerRequests.vue').catch(() => DummyView) },
        { path: 'cart', name: 'marketer-cart', component: () => import('../views/marketer/MarketerCart.vue').catch(() => DummyView) },
        { path: 'products', name: 'marketer-products', component: () => import('../views/marketer/MarketerProducts.vue').catch(() => DummyView) },
        { path: 'links', name: 'marketer-links', component: () => import('../views/marketer/MarketerLinks.vue').catch(() => DummyView) },
        { path: 'wallet', name: 'marketer-wallet', component: () => import('../views/marketer/MarketerWallet.vue').catch(() => DummyView) }
      ]
    },

    // ---------------- مسیرهای پنل خریداران (Buyer Panel) ----------------
    {
      path: '/buyer',
      component: BuyerLayout,
      children: [
        { path: '', name: 'buyer-dashboard', component: () => import('../views/buyer/BuyerDashboard.vue').catch(() => DummyView) },
        { path: 'orders', name: 'buyer-orders', component: () => import('../views/buyer/BuyerOrders.vue').catch(() => DummyView) },
        { path: 'rfq', name: 'buyer-rfq', component: () => import('../views/buyer/BuyerRFQ.vue').catch(() => DummyView) },
        { path: 'wallet', name: 'buyer-wallet', component: () => import('../views/buyer/BuyerWallet.vue').catch(() => DummyView) },
        { path: 'favorites', name: 'buyer-favorites', component: () => import('../views/buyer/BuyerFavorites.vue').catch(() => DummyView) }
      ]
    },

    // ---------------- مسیرهای سوپر ادمین (Admin Panel) ----------------
    {
       path: '/admin',
      component: AdminLayout,
      children: [
        { path: '', name: 'admin-dashboard', component: () => import('../views/admin/AdminDashboard.vue').catch(() => DummyView) },
        { path: 'categories', name: 'admin-categories', component: () => import('../views/admin/AdminCategories.vue').catch(() => DummyView) },
        { path: 'users', name: 'admin-users', component: () => import('../views/admin/AdminUsers.vue').catch(() => DummyView) },
        { path: 'products', name: 'admin-products', component: () => import('../views/admin/AdminProducts.vue').catch(() => DummyView) },
        { path: 'finance', name: 'admin-finance', component: () => import('../views/admin/AdminFinance.vue').catch(() => DummyView) },
        { path: 'accounting', name: 'admin-accounting', component: () => import('../views/admin/AdminAccounting.vue').catch(() => DummyView) },
        { path: 'inventory', name: 'admin-inventory', component: () => import('../views/admin/AdminInventory.vue').catch(() => DummyView) },
        { path: 'orders', name: 'admin-orders', component: () => import('../views/admin/AdminOrders.vue').catch(() => DummyView) },
        { path: 'rfq', name: 'admin-rfq', component: () => import('../views/admin/AdminRFQ.vue').catch(() => DummyView) },
        { path: 'settings', name: 'admin-settings', component: () => import('../views/admin/AdminSettings.vue').catch(() => DummyView) },
        { path: 'notifications', name: 'admin-notifications', component: () => import('../views/admin/AdminNotifications.vue').catch(() => DummyView) },
        { path: 'cms', name: 'admin-cms', component: () => import('../views/admin/AdminCMS.vue').catch(() => DummyView) }
      ]
    },

    // ---------------- صفحه 404 برای آدرس‌های اشتباه ----------------
    { path: '/:pathMatch(.*)*', redirect: '/' }
  ]
})

// ================= 3. نگهبان امنیتی مسیرها (Route Guard) =================
router.beforeEach((to, from, next) => {
  // 1. ریست سخت (Hard Reset): اگر کلمه logout را زد، کل مرورگر را جارو کن!
  if (to.path === '/logout') {
    localStorage.clear();
    sessionStorage.clear();
    return next('/login');
  }

  // خواندن اطلاعات از حافظه
  const token = localStorage.getItem('access_token') || localStorage.getItem('tajerbam_token');
  const role = localStorage.getItem('user_role');

  // لیست مسیرهای نیازمند لاگین
  const protectedRoutes = ['/admin', '/panel', '/marketer', '/buyer'];
  const isProtected = protectedRoutes.some(route => to.path.startsWith(route));

  // 2. تلاش برای ورود به پنل‌ها بدون توکن
  if (isProtected && !token) {
    return next('/login');
  } 
  
  // 3. تلاش برای باز کردن صفحه لاگین در حالی که توکن داریم
  if (to.path === '/login' && token) {
    if (!role) {
      // کشف تله توکن فاسد! توکن هست ولی رول نیست. حافظه را پاک کن و اجازه بده صفحه لاگین باز شود.
      localStorage.clear();
      return next();
    }
    
    // اگر نقش سالم است، او را به پنل خودش بفرست
    if (role === 'admin') return next('/admin');
    if (role === 'seller') return next('/panel');
    if (role === 'marketer') return next('/marketer');
    return next('/buyer'); 
  } 

  // 4. مسیر عادی و بدون مشکل
  next();
})

export default router