import { createApp } from 'vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import App from './App.vue'
// Importación de componentes
import Reservas from '@/views/Reservas'
import NuevaReserva from '@/views/NuevaReserva'
import NuevoGastoComun from '@/views/NuevoGastoComun'

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
    },
    {
        path: '/nuevo_gasto',
        component: NuevoGastoComun,
        name: 'nuevo_gasto'
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