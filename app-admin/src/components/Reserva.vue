<template>
    <tr>
        <td>{{ reserva.id }}</td>
        <td>{{ espacios[reserva.espacio_comun_id] }}</td>
        <td>{{ estados[reserva.estado_id] }}</td>
        <td>{{ parsear(reserva.fecha) }}</td>
        <td>{{ horarios[reserva.horario_id] }}</td>
        <td>{{ pagado[reserva.pagado] }}</td>
        <td>{{ reserva.residente_rut }}</td>
        <td><button type="button" class="btn btn-danger" @click="$emit('delete-reserva', reserva.id)">Anular</button></td>
        <td><button type="button" class="btn btn-info">Editar</button></td>
    </tr>
</template>

<script>
export default {
    name: 'ReservaR',
    props: {
        reserva: Object
    },
    methods: {
        parsear(fecha){
                let date = new Date(fecha)
                return date.toISOString().split('T')[0]
            },
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
        }
    }
}
</script>