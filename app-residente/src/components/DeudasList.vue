<template>
    <div class="justify-content-start d-flex h1 mt-5 mb-4 font-weight-bold">
        Deudas
    </div>
    <!-- Lista Deudas -->
    <div v-if="gastos_comunes[0] || multas[0]" class="d-flex justify-content-center">
        
    <table class="table table-striped border">
        <thead>
            <th>Concepto</th>
            <th>Monto</th>
        </thead>
        <tbody :key="multa.id" v-for="multa in multas">
            <DeudaMulta
                :multa="multa"
            />
        </tbody>
        <tbody :key="gasto_comun.id" v-for="gasto_comun in gastos_comunes">
            <DeudaGasto
                :gasto_comun="gasto_comun"
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
import DeudaGasto from './DeudaGasto.vue';
import DeudaMulta from './DeudaMulta.vue';
import InfoResidente from './infoResidente.vue';

export  default {
    name: 'DeudasList',
    props:{
        gastos_comunes: Array,
        multas: Array,
        residente: Object,
    },
    components:{
    DeudaGasto,
    DeudaMulta,
    InfoResidente,
}
}
</script>