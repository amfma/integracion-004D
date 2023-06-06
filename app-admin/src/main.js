import { createApp } from 'vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import App from './App.vue'
// Importación de componentes
import Reservas from '@/views/Reservas'
import NuevaReserva from '@/views/NuevaReserva'

// Rutas
const routes = [
    {
        path: '/reservas', 
        component: Reservas,
        name: 'reservas'
    },
    {
        path: '/nueva_reserva',
        component: NuevaReserva,
        name: 'nueva_reserva'
    }
]
// Router
const router = createRouter({
    history: createWebHashHistory(),
    routes
})

// Instancia Vue
const app = createApp(App)
app.use(router)
app.mount('#app')