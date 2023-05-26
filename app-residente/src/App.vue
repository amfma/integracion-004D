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

      this.fetchReservasEspacio(id_espacio).then((reservas) => {
        this.categorizaFechas(reservas)
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
    dateToString(fecha){
      let date = new Date(fecha)
      return date.toISOString().split('T')[0]
    },
    stringToDate(fecha){
      let parced = fecha.concat('T00:00:00')
      return new Date(parced)
    },
    // Categoriza la fecha de una reserva
    categorizaFechas(reservas){

      let no_disponibles = []
      let medio_dia = {}

      reservas.map((reserva)=>{
        const fecha = this.dateToString(reserva.fecha)
        const horario = reserva.horario_id
        
        if (fecha in medio_dia){
          delete medio_dia[fecha]
          no_disponibles.push(this.stringToDate(fecha))
        }else{
          medio_dia[fecha] = horario
        }
      })
      this.fechas_medio_dia = medio_dia
      this.fechas_no_disponibles = no_disponibles
    },
  },
  async created(){
    this.fetchEspacios("1")
  }
}
</script>