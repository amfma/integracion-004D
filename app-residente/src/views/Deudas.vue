<template>
    <div class="justify-content-start d-flex h1 mt-5 mb-4 font-weight-bold">
        Deudas
    </div>
    <DeudasList
    :deudas="this.deudas"
    @generar-pago="generarPago"
    />
    <!-- Barra superior-->
    <div class="row mt-1 justify-content-start">
        <div class="col col-auto">
            <infoResidente
            :residente="residente"
            />
        </div>
    </div>
</template>

<script>
import DeudasList from '@/components/DeudasList.vue';
import infoResidente from '@/components/infoResidente.vue';

export default {
    name: 'DeudasView',
    components: {
        DeudasList,
        infoResidente,
    },
    data(){
        return{
            deudas: [],
            residente: {}
        }
    },
    methods:{
        // Obtener deudas (gastos comunes y multas)
        async fetchDeudas(id_condominio){
            const res = await fetch(`api/residente/deudas/${id_condominio}`)
            if (res.status === 200){
                const data = await res.json()
                this.deudas = data
            }
        },
        // Obtener residente
        async fetchResidente(rut){
            const res = await fetch(`api/residente/residente/${rut}`)
            const data = await res.json()
            this.residente = data
        },
        //Inicia un nuevo pago
        async generarPago(porPagar){
            const nuevo_pago = {
                deudas: JSON.parse(JSON.stringify(porPagar)),
                rut: this.residente.rut
            }
            console.log(JSON.stringify(nuevo_pago))
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type' : 'application/json'},
                body: JSON.stringify(nuevo_pago)
            }
            const res = await fetch('/api/residente/pago', requestOptions)

            if(res.status == 200){
                const data = await res.json()
                console.log(data)
                // redireccion a webpay
                window.location.href = `${data.url}?token_ws=${data.token}`;
            }else{
                alert('No se ha podido realizar la operación')
            }
        }
    },
    async created(){
        this.fetchDeudas('1')
        this.fetchResidente('11111111-1')
    }
}
</script>