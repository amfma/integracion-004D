import { createApp } from 'vue'
import {createRouter, createWebHashHistory} from 'vue-router'
import App from './App.vue'
// Impotación de componentes
import Reservas from './views/Reservas'

// Rutas
const routes = [
    {
        path: '/reservas', 
        component: Reservas,
        name: 'reservas'
    },
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