<template>
    <ReservasList :reservas="reservas" 
      @delete-reserva="delReserva"
      @search-reserva="fetchReserva"
      @clear-search="fetchReservas"
    />
</template>

<script>
import ReservasList from '@/components/ReservasList.vue';

export default{
    name: 'ReservasView',
    components:{
        ReservasList,
    },
    data(){
        return{
            reservas: [],
        }
    },
    methods:{
        //Obtener reservas
        async fetchReservas(){
            const res = await fetch('api/admin/reservas')
            const data = await res.json()
            console.log(data)
            this.reservas = data
        },
        //Eliminar reserva
        async delReserva(id){
            const requestOptions = {
                method: 'DELETE',
                headers: { 'Content-Type' : 'application/json'}
            }
            await fetch(`api/admin/reservas/del/${id}`, requestOptions)
            this.fetchReservas()
        },
        //Obtener reserva
        async fetchReserva(id){
        console.log(id)
        const res = await fetch(`api/admin/reservas/${id}`)
        const data = await res.json()
        this.reservas = [data]
        },
    },
    async created() {
        this.fetchReservas()
    }
}
</script>