<template>
  <div class="container-fluid">
    <AddReserva :espacios="espacios"
    :fechas_medio_dia="fechas_medio_dia"
    :fechas_no_disponibles="fechas_no_disponibles"
    @list-fechas="ListFechas"
    @add-reserva="AddReserva"
    />
  </div>
</template>

<script>
import AddReserva from './components/AddReserva.vue';

export default {
  name: 'App',
  components: {
    AddReserva,
  },
  data(){
    return{
      espacios: [],
      fechas_medio_dia: {}, // fecha con reservas solo am o pm
      fechas_no_disponibles: [], // fecha con reservas am y pm
    }
  },
  methods:{
    //Obtener espacios comunes
    async fetchEspacios(id_condominio){
      const res = await fetch(`api/residente/espacios/${id_condominio}`)
      const data = await res.json()
      this.espacios = data
    },
    // Retorna reservas de espacio comun
    async fetchReservasEspacio(id_espacio){
      const res = await fetch(`api/residente/reservas/${id_espacio}`)
      const data = await res.json()
      this.reservas = data
      return data
    },
    // Obtiene las fechas de las reservas
    ListFechas(id_espacio){
      // reestablece listas de fechas
      this.fechas_medio_dia = {}
      this.fechas_no_disponibles = []
      // Obtiene reservas y categoriza las fechas
      this.fetchReservasEspacio(id_espacio).then((reservas) => {
        reservas.map(r => this.categorizaFechas(r))
      })
    },
    async AddReserva(reserva){
      const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(reserva)
      }
      const res = await fetch('api/residente/reservar', requestOptions)
      if(res.status == 200){
        alert('Reserva exitosa')
      }else{
        alert('No se ha podido realizar la operación')
      }
    },
    parsear(fecha){
      let date = new Date(fecha)
      return date.toLocaleDateString()
    },
    // Categoriza la fecha de una reserva
    categorizaFechas(reserva){
      let fecha = this.parsear(reserva.fecha)
      let horario = reserva.horario_id
      
      if (fecha in this.fechas_medio_dia){
        delete this.fechas_medio_dia[fecha]
        this.fechas_no_disponibles.push(new Date(fecha))
      }else{
        this.fechas_medio_dia[fecha] = horario
      }
    },
  },
  async created(){
    this.fetchEspacios("1")
  }
}
</script>