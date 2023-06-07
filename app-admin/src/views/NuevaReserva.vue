<template>
    <AddReservas 
    @new-reserva="addReserva"
    />
</template>

<script>
import AddReservas from '@/components/AddReservas.vue';

export default{
    name: 'NuevaReservaView',
    components:{
        AddReservas
    },
    methods:{
        //Crear reserva
        async addReserva(reserva){
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type' : 'application/json'},
                body: JSON.stringify(reserva)
            }
            const res = await fetch('api/admin/reservas', requestOptions)
            if(res.status == 200){
                alert('Reserva ingresada con exito')
            }else{
                alert('No se ha podido realizar la operación')
            }
        },
    },
}

</script>