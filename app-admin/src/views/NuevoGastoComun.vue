<template>
    <AddGastoComun
    :condominios="condominios"
    @add-gasto="addGasto"
    />
</template>

<script>
import AddGastoComun from '@/components/AddGastoComun.vue';

export default{
    name: 'NuevoGastoComun',
    components:{
        AddGastoComun,
    },
    data(){
        return {
            condominios: [],
        }
    },
    methods:{
        // Genera nuevo gasto comun
        addGasto(nuevo_gasto){
            // temporal
            console.log(nuevo_gasto)
        },
        // Obtiene lista de condominios
        async fetchCondominios(){
            const res = await fetch(`api/admin/condominios`)
            const data = await res.json()
            this.condominios = data
        }
    },
    async created() {
        this.fetchCondominios()
    }
}
</script>