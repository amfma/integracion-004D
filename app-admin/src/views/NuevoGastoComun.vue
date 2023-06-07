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
        async addGasto(nuevo_gasto){
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type' : 'application/json'},
                body: JSON.stringify(nuevo_gasto)
            }
            const res = await fetch('api/admin/gastos_comunes', requestOptions)
            if(res.status == 200){
                alert('Gasto común ingresado con exito')
            }else{
                alert('No se ha podido realizar la operación')
            }
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