<template>
    <div class="justify-content-center d-flex border m-5 p-5">
        <form @submit="addReserva">
        <div class="form-group">
            <label for="espacio_comun_id">Espacio común</label>
            <select name="espacio_comun_id" id="espacio_comun_id" class="form-control" v-model="espacio_comun_id">
                <option value=1>Picina</option>
                <option value=2>Quincho</option>
                <option value=3>Sala de eventos</option>
            </select>
        </div>
        <div class="form-group">
            <label for="horario_id">Horario</label>
            <select name="horario" id="horario_id" class="form-control" v-model="horario_id">
                <option value=1>AM</option>
                <option value=2>PM</option>
            </select>
        </div>
        <div class="form-check-inline">
            <label class="form-check-label">
                <input type="checkbox" class="form-check-input" value="1" v-model="pagado">Pagado
            </label>
        </div>
        <div class="form-group">
            <label for="fecha">Fecha</label>
            <input type="date" class="form-control" id="fecha" v-model="fecha">
        </div>
        <div class="form-group">
            <label for="rut">Rut residente</label>
            <input type="text" class="form-control" id="rut" v-model="residente_rut">
        </div>
        <button type="submit" class="btn btn-primary">Crear</button>
        <button type="button" class="btn btn-danger ml-2" @click="showReservas()">Volver</button>
    </form>
    </div>
</template>

<script>
    export default{
        name: "AddReservas",
        data(){
            return {
                espacio_comun_id: '',
                horario_id: '',
                pagado: 0,
                fecha: '',
                residente_rut: '',
            }      
        },
        methods:{
            addReserva(e){
                e.preventDefault()

                // Validaciones
                if(!this.residente_rut){
                    alert('Ingrese el rut del residente')
                    return
                }

                // Nueva reserva
                const newReserva = {
                    espacio_comun_id: this.espacio_comun_id,
                    horario_id: this.horario_id,
                    pagado: this.pagado,
                    fecha: this.fecha,
                    rut: this.residente_rut
                }
                this.$emit('new-reserva', newReserva)

                // Limpieza del formulario
                this.espacio_comun_id = '',
                this.horario_id = '',
                this.pagado = 0,
                this.fecha = '',
                this.residente_rut = ''
            },
            showReservas(){
            this.$emit('toggle-reservas')
            }
        }
    }
</script>