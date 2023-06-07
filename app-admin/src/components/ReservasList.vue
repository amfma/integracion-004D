<template>
    <div class="justify-content-start d-flex h1 mt-5 mb-5 font-weight-bold">
        Reservas
    </div>
    <!-- Barra de busqueda -->
    <div class="row mb-2 mt-3">
        <div class="col ml-1 striped-border">
            <router-link :to="{ name: 'nueva_reserva' }">
                <button class="btn btn-success">
                        Nueva Reserva
                </button>
            </router-link>
        </div>
        <div class="col col-auto">
            <form class="form-inline" @submit="searchReserva">
                <label for="reserva_id">Buscar por id:</label>
                <input type="number" min=1 v-model="reserva_id" class="form-control ml-2" id="reserva_id">
                <button type="submit" class="btn btn-primary ml-2 mr-1">Buscar</button>
                <button type="button" class="btn btn-danger ml-2" @click="clearSearch">Limpiar</button>
            </form>
        </div>
    </div>
    <!-- Lista reservas -->
    <div v-if="reservas[0]" class="d-flex justify-content-center">
        
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
            <Reserva
                @delete-reserva="anular"
                :reserva="reserva"
            />
        </tbody>
    </table>  
    </div>
    <div class="row justify-content-center mt-5" v-else>
        <h3>No se han encontrado resultados</h3>
    </div>
</template>

<script>
    import Reserva from './Reserva.vue'

    export default {
        name: 'ListReservas',
        props: {
            reservas: Array,
        },
        data(){
            return{
                reserva_id: 0,
            }
        },
        methods: {
            anular(id){
                this.$emit('delete-reserva', id)
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
            },
            clearSearch(){
                this.reserva_id = 0
                this.$emit('clear-search')
            },
        },
        components:{
            Reserva,
        }
    }
</script>