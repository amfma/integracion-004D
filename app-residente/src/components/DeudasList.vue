<template>
    <div class="justify-content-start d-flex h1 mt-5 mb-4 font-weight-bold">
        Deudas
    </div>
    <!-- Lista Deudas -->
    <div v-if="deudas[0]" class="d-flex justify-content-center">
        
    <table class="table table-striped border">
        <thead>
            <th>Concepto</th>
            <th>Fecha Emisión</th>
            <th>Fecha Vencimiento</th>
            <th>Monto</th>
        </thead>
        <tbody :key="deuda.id" v-for="deuda in deudas">
            <DeudaItem
                :deuda="deuda"
            />
        </tbody>
    </table>
    </div>
    <div class="row justify-content-center mt-5" v-else>
        <h3>No se han encontrado resultados</h3>
    </div>
    <!-- Barra pago -->
    <div class="row mb-2 mt-1">
        <div class="col ml-1 striped-border">
            <button class="btn btn-success">Pagar</button>
        </div>
        <div class="col col-auto">
            <InfoResidente
            :residente="residente"
            />
        </div>
    </div>
</template>

<script>
import DeudaItem from './DeudaItem.vue';
import InfoResidente from './infoResidente.vue';

export  default {
    name: 'DeudasList',
    props:{
        deudas: Array,
        residente: Object,
    },
    components:{
        DeudaItem,
        InfoResidente,
    },
}
</script>