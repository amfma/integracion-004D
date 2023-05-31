<template>
    <tr>
        <td>{{ multa.concepto }}</td>
        <td>{{ monto }}</td>
    </tr>
</template>

<script>
export default{
    name: 'DeudaMulta',
    props:{
        multa: Object,
    },
    computed:{
        monto(){
            if(!this.multa.monto){
                return ''
            }else{
                return Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP'}).format(this.multa.monto)
            }
        }
    },
}
</script>