<template>
    <div class="justify-content-start d-flex h1 mt-5 mb-5 font-weight-bold">
        Reservas
    </div>
    <!-- Barra de busqueda -->
    <div class="row mb-2 mt-3">
        <div class="col ml-1 striped-border">
            <button class="btn btn-success" @click="showReservas()">Nueva Reserva</button>
        </div>
        <div class="col col-auto">
            <form class="form-inline" @submit="searchReserva">
                <label for="reserva_id">Buscar por id:</label>
                <input type="number" v-model="reserva_id" class="form-control ml-2" id="reserva_id">
                <button type="submit" class="btn btn-primary ml-2 mr-1">Buscar</button>
            </form>
        </div>
    </div>
    <!-- Lista reservas -->
    <div class="d-flex justify-content-center">
        
    <table class="table table-striped border">
        <thead>
            <th>Id</th>
            <th>Espacio común</th>
            <th>Estado</th>
            <th>Fecha</th>
            <th>Horario</th>
            <th>Pagado</th>
            <th>Rut residente</th>
        </thead>
        <tbody :key="reserva.id" v-for="reserva in reservas">
            <tr>
                <td>{{ reserva.id }}</td>
                <td>{{ espacios[reserva.espacio_comun_id] }}</td>
                <td>{{ estados[reserva.estado_id] }}</td>
                <td>{{ parsear(reserva.fecha) }}</td>
                <td>{{ horarios[reserva.horario_id] }}</td>
                <td>{{ pagado[reserva.pagado] }}</td>
                <td>{{ reserva.residente_rut }}</td>
                <td><button type="button" class="btn btn-danger" @click="anular(reserva.id)">Anular</button></td>
                <td><button type="button" class="btn btn-info">Editar</button></td>
            </tr>  
        </tbody>
    </table>  
    </div>
    <div class="">
            
    </div>
</template>

<script>
    export default {
        name: 'ListReservas',
        props: {
            reservas: Array,
        },
        data(){
            return{
                estados: {
                    1:'Activo',
                    2:'Anulado',
                },
                horarios: {
                    1: 'AM',
                    2: 'PM'
                },
                espacios: {
                    1: 'Piscina',
                    2: 'Quincho',
                    3: 'Sala de Eventos'
                },
                pagado: {
                    0: 'No',
                    1: 'Si'
                },
                reserva_id: 0,
            }
        },
        methods: {
            anular(id){
                this.$emit('delete-reserva', id)
            },
            parsear(fecha){
                let date = new Date(fecha)
                return date.toLocaleDateString()
            },
            showReservas(){
            this.$emit('toggle-reservas')
            },
            searchReserva(e){
                e.preventDefault()
                // Validación
                if (this.reserva_id < 0){
                    alert('Ingrese un id válido')
                    return
                }

                const id = this.reserva_id
                this.$emit('search-reserva', id)
            }
        }
    }
</script>