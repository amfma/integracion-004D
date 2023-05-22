<template>
    <div class="justify-content-center d-flex border m-5 p-5">
        <form>
            <!-- Selección espacio común -->
            <div class="form-group">
                <label for="espacio_comun_id">Espacio común</label>
                <select id="espacio_comun_id" class="form-control" v-model="espacio_comun_id" @change="cargarOpciones">
                    <option :key="espacio.id" v-for="espacio in espacios" :value="espacio.id">{{ espacio.descripcion }}</option>
                </select>
            </div>
            <!-- Selección fecha-->
            <div class="form-group">
                <label for="fecha">Fecha</label>
                <Datepicker 
                v-model="fecha" 
                :lowerLimit="today" 
                :disabledDates="{dates: fechas_no_disponibles}" 
                :disabled="datepicker_disabled"
                @update:modelValue="cargarHorarios()"/>
            </div>
            <!-- Selección horario -->
            <div class="form-group">
                <label for="horario_id">Horario</label>
                <select name="horario" id="horario_id" class="form-control" v-model="horario_id" :disabled="horario_disabled" >
                    <option value=1 :disabled="!horarioDisponible(1)">AM</option>
                    <option value=2 :disabled="!horarioDisponible(2)">PM</option>
                </select>
            </div>
            <!-- Precio -->
            <div class="mb-2">
                Precio: {{ precio }}
            </div>
            <button type="submit" class="btn btn-primary">Reservar</button>
        </form>
    </div>
</template>

<script>
import Datepicker from 'vue3-datepicker'

export default{
    name: 'addReserva',
    props:{
        espacios: Array,
        fechas_medio_dia: Object,
        fechas_no_disponibles: Array,
    },
    components:{
        Datepicker
    },
    data(){
        return{
            espacio_comun_id: '',
            horario_id: '',
            fecha: new Date(),
            today: new Date(),
            precio: 0,
            horario_disponible: [
                {id: 1, disponible: false},
                {id: 2, disponible: false},
            ],
            horario_disabled: true,
            datepicker_disabled: true,
        }
    },
    methods:{
        // Carga opciones que dependen del espacio común
        cargarOpciones(){
            // Obtiene fechas de reservas
            this.$emit('list-fechas', this.espacio_comun_id)

            // Obtiene el precio
            const espacio_comun = this.espacios.find(e => e.id === this.espacio_comun_id)
            const precio = espacio_comun.precio
            if (!precio){
                this.precio = 0
            }else{
                this.precio = precio
            }
            //Reestablece fecha
            this.fecha = new Date()
            // Recarga horarios disponibles
            this.cargarHorarios()
            //Desbloquea el date picker
            this.datepicker_disabled = false
        },
        // Bloquea horarios no disponibles para la fecha
        cargarHorarios(){
            const fecha = this.fecha.toLocaleDateString()
            const id_horario = this.fechas_medio_dia[fecha]
            // establece si el horario está disponible para la fecha
            if(id_horario){
                this.horario_disponible = this.horario_disponible
                .map(({id, disponible}) => {
                    if (id_horario === id){
                        disponible = false
                        return {id: id, disponible: disponible}
                    }else{
                        disponible = true
                        return {id: id, disponible: disponible}
                    }
                })
            }else{
                this.horario_disponible = this.horario_disponible
                .map(({id})=>({id: id, disponible: true}))
            }
            //Desbloquea el select de horario
            this.horario_disabled = false
        },
        // Retorna si el horario esta disponible o no
        horarioDisponible(id){
            const horario = this.horario_disponible.find(horario => horario.id === id)
            return horario.disponible
        }
    },

}
</script>