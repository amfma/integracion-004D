<template>
    <div v-if="estado_pago.response_status < 2 && estado_pago.response_status >=0">
        <PagoResumen
        :estado_pago="estado_pago"
        />
    </div>
    <div v-else>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                <div class="card-body text-center">
                    <h4 class="card-title">Pago no realizado</h4>
                    <p class="card-text">Ah ocurrido un error, no se ha efectuado la transacción</p>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import PagoResumen from '@/components/PagoResumen.vue'

export default{
    name: 'PagoView',
    components:{
        PagoResumen
    },
    data(){
        return{
            estado_pago: {},
        }
    },
    methods:{
        // consultar estado del pago
        async confirmaPago(token){
            const res = await fetch(`api/residente/confirma_pago/${token}`)
            const data = await res.json()
            this.estado_pago = data
            console.log(this.estado_pago.response_status)
        }
    },
    created(){
        if (this.$route.query.token_ws){
            this.confirmaPago(this.$route.query.token_ws)
            console.log(this.$route.query.token_ws)
        }
    }
}
</script>