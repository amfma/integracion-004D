<template>
<div class="justify-content-center d-flex border m-5 p-5">
    <form @submit="addGasto">
        <div class="justify-content-start h3 mb-3 mt-4">
            Añadir nuevo gasto
        </div>
        <div v-if="condominios[0]">
            <div class="form-group">
                <label for="condominio_id">Condominio</label>
                <select id="condominio_id" class="form-control" v-model="condominio_id">
                    <option 
                        :key="condominio.id" 
                        v-for="condominio in condominios" 
                        :value="condominio.id">{{ condominio.nombre }}
                    </option>
                </select>
            </div>
            <div class="form-group">
                <label for="monto">Monto a Prorratear</label>
                <input type="text" id="monto" class="form-control" 
                    v-model="monto"
                    @input="montoFormat($event.target.value)"
                />
            </div>
            <button type="submit" class="btn btn-primary">Añadir</button>
        </div>
        <div v-else>
            <div class="h4">No hay condominios registrados</div>
        </div>
    </form>
</div>
</template>

<script>

export default{
    name: 'CondominiosSelect',
    props:{
        condominios: Array,
    },
    data(){
        return{
            condominio_id: 0,
            monto: '$0',
        }
    },
    methods:{
        addGasto(){
            const monto = this.numericFormat(this.monto)
            const condominio_id = this.condominio_id
            //Verificaciones
            if(!this.condominios.find(c => c.id === condominio_id)){
                alert('Ingrese un condominio válido')
            }else if(isNaN(monto)){
                alert('Ingrese un monto válido')
            }else if(monto < 1){
                alert('ingrese un monto mayor a 0')
            }else if(monto >= 2**64){
                alert('El monto supera el máximo aceptado')
            }else{
                // generar nuevo gasto
                const nuevo_gasto = {
                    monto: monto,
                    condominio_id: condominio_id
                }
                this.$emit('add-gasto', nuevo_gasto)

                // limpiar formulario
                this.monto = '$0'
                this.condominio_id = 0
            }
        },
        montoFormat(value){
            const monto = value.replace(/[^0-9]/g, '')
            const monto_formateado = this.currencyFormat(monto)
            this.monto = monto_formateado
        },
        numericFormat(value){
            return parseInt(value.replace(/[^0-9]/g, ''))
        },
        currencyFormat(number){
            const format = {
                style: 'currency',
                currency: 'CLP'
            }
            return Intl.NumberFormat('es-CL', format).format(number)
        }
    },
}
</script>