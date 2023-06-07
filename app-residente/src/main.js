import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
// Impotación de componentes
import Reservas from './views/Reservas'
import Deudas from '@/views/Deudas'
import Pago from '@/views/Pago'

// Rutas
const routes = [
    {
        path: '/reservas', 
        component: Reservas,
        name: 'reservas'
    },
    {
        path: '/deudas',
        component: Deudas,
        name: 'deudas'
    },
    {
        path: '/confirmacion_pago',
        component: Pago,
        name: '/confirmacion_pago'
    }
]
// Router
const router = createRouter({
    history: createWebHistory(),
    routes
})

// Instancia Vue
const app = createApp(App)
app.use(router)
app.mount('#app')