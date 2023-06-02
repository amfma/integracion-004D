<template>
    <tr>
        <td>{{ deuda.concepto }}</td>
        <td>{{ fecha_emision }}</td>
        <td>{{ fecha_vencimiento }}</td>
        <td>{{ monto }}</td>
    </tr>
</template>

<script>

export default{
    name: 'DeudaItem',
    props:{
        deuda: Object,
    },
    computed:{
        monto(){
            if(!this.deuda.monto){
                return ''
            }else{
                return Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP'}).format(this.deuda.monto)
            }
        },
        fecha_emision(){
            if(!this.deuda.fecha_emision){
                return ''
            }else{
                return this.dateToString(this.deuda.fecha_emision)
            }
        },
        fecha_vencimiento(){
            if(!this.deuda.fecha_vencimiento){
                return ''
            }else{
                return this.dateToString(this.deuda.fecha_vencimiento)
            }
        },
    },
    methods:{
        // Formateo de fecha a string
        dateToString(fecha){
            let date = new Date(fecha)
            return date.toISOString().split('T')[0]
        },
    }
}
</script>