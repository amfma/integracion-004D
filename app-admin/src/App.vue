<template>
  <NavBar @toggle-reservas="toggleReservas()" />
  <div class="container">
    <div v-if="showReservas">
      <Reservas :reservas="reservas" 
      @delete-reserva="delReserva"  
      @toggle-reservas="toggleReservas()" 
      @search-reserva="fetchReserva"
      @clear-search="updateReservas"
      />
    </div>
    <div v-if="!showReservas">
      <AddReservas @new-reserva="addReserva" @toggle-reservas="toggleReservas()"/>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import Reservas from './components/Reservas.vue';
import AddReservas from './components/AddReservas.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    Reservas,
    AddReservas,
  },
  data() {
    return {
      reservas: [],
      showReservas: true,
    }
  },
  methods:{
    //Boton formulario
    toggleReservas(){
      this.showReservas = !this.showReservas
      this.updateReservas()
    },
    //Obtener reservas
    async fetchReservas(){
      const res = await fetch('api/admin/reservas')
      const data = await res.json()
      console.log(data)
      return data
    },
    //Obtener reserva
    async fetchReserva(id){
      console.log(id)
      const res = await fetch(`api/admin/reservas/${id}`)
      const data = await res.json()
      this.reservas = [data]
    },
    //Eliminar reserva
    async delReserva(id){
      const requestOptions = {
        method: 'DELETE',
        headers: { 'Content-Type' : 'application/json'}
      }
      await fetch(`api/admin/reservas/del/${id}`, requestOptions)
      this.updateReservas()
    },
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
      this.updateReservas()
    },
    //Actualizar lista de reservas
    async updateReservas(){
      this.reservas = await this.fetchReservas()
    }
  },
  async created() {
    this.updateReservas()
  }
}
</script>
