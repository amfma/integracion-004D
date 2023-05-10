<template>
    <div class="justify-content-start d-flex h1 ml-5 m-4 font-weight-bold">
        Reservas
    </div>
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
    <div class="striped-border">
            <button class="btn btn-primary" @click="showReservas()">Hacer Reserva</button>
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
                }
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
            }
        }
    }
</script>