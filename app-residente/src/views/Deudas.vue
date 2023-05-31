<template>
    <DeudasList/>
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
            gastos_comunes: [],
            multas: []
        }
    },
    methods:{
        // Obtener deudas (gastos comunes y multas)
        async fetchDeudas(id_condominio){
            const res = await fetch(`api/residente/espacios/${id_condominio}`)
            const data = await res.json()
            if (data.status == '200'){
                this.gastos_comunes = data.gastocomun
                this.multas = data.multa
            }
        },
    },
}
</script>