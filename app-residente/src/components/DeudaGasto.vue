<template>
    <tr>
        <td>Gasto Común</td>
        <td>{{ monto }}</td>
    </tr>
</template>

<script>
export default{
    name: 'DeudaGasto',
    props:{
        gasto_comun: Object,
    },
    computed:{
        monto(){
            if(!this.gasto_comun.monto){
                return ''
            }else{
                return Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP'}).format(this.gasto_comun.monto)
            }
        }
    },
}
</script>