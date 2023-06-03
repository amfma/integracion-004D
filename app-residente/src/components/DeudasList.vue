<template>
    <!-- Lista Deudas -->
    <div v-if="deudas[0]" class="d-flex justify-content-center">
        
    <table class="table table-striped border">
        <thead>
            <th>Concepto</th>
            <th>Fecha Emisión</th>
            <th>Fecha Vencimiento</th>
            <th>Monto</th>
            <!-- Checkbox selecciona todo -->
            <th>
                <label class="custom-control custom-checkbox">
                    <input 
                    type="checkbox" 
                    class="form-check-input"
                    @change="checkAll($event)"
                    >Seleccionar todo
                </label>
            </th>
        </thead>
        <tbody>
            <!-- Deudas -->
            <DeudaItem
                v-for="deuda in deudas"
                :key="deuda.id" 
                :deuda="deuda"
                :allChecked="this.allChecked"
                @selecciona-deuda="seleccionaDeuda"
            />
            <tr>
                <td></td><td></td><td></td>
                <!-- Total -->
                <td>{{ this.currencyFormat(total) }}</td>
                <td>
                    <div class="col striped-border">
                        <button class="btn btn-success">Pagar</button>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
    </div>
    <div class="row justify-content-center mt-5" v-else>
        <h3>No se han encontrado resultados</h3>
    </div>
</template>

<script>
import DeudaItem from './DeudaItem.vue';

export  default {
    name: 'DeudasList',
    props:{
        deudas: Array,
        residente: Object,
    },
    components:{
        DeudaItem,
    },
    data(){
        return{
            total: 0,
            allChecked: false,
            porPagar: []
        }
    },
    methods:{
        //agrega o quita deudas del total y la lista porPagar
        seleccionaDeuda(checked, monto, id){
            if(checked){
                this.total += monto
                this.porPagar.push(id)
            }else{
                this.total -= monto
                const index = this.porPagar.indexOf(id, 0)
                if (index > -1){
                    this.porPagar.splice(index, 1)
                }
            }
        },
        // selecciona o deselecciona todas las deudas
        checkAll(event){
            this.allChecked = event.target.checked
        },
        currencyFormat(number){
            const format = {
                style: 'currency',
                currency: 'CLP'
            }
            return Intl.NumberFormat('es-CL', format).format(number)
        }
    }
}
</script>