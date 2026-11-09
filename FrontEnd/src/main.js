import 'vazirmatn/Vazirmatn-font-face.css'
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router' // اضافه شدن روتر
import App from './App.vue'

const app = createApp(App)

app.use(createPinia())
app.use(router) // فعال‌سازی روتر

app.mount('#app')