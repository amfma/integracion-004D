<template>
    <DeudasList
    :deudas="this.deudas"
    :residente="this.residente"
    />
</template>

<script>
import DeudasList from '@/components/DeudasList.vue';

export default {
    name: 'DeudasView',
    components: {
        DeudasList
    },
    data(){
        return{
            deudas: [],
            residente: {}
        }
    },
    methods:{
        // Obtener deudas (gastos comunes y multas)
        async fetchDeudas(id_condominio){
            const res = await fetch(`api/residente/deudas/${id_condominio}`)
            if (res.status === 200){
                const data = await res.json()
                this.deudas = data
            }
        },
        // Obtener residente
        async fetchResidente(rut){
            const res = await fetch(`api/residente/residente/${rut}`)
            const data = await res.json()
            this.residente = data
        },
    },
    async created(){
        this.fetchDeudas('1')
        this.fetchResidente('11111111-1')
    }
}
</script>