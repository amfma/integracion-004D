<template>
    <div class="mb-3 bg-secondary p-2 rounded text-dark">
        <div class="text-capitalize">{{ residente.nombres }} {{ residente.apellidos }} | rut: {{ rut }}</div>
    </div>
</template>

<script>

export default{
    props:{
        residente:{
            type: Object,
            required: true,
        }
    },
    computed:{
        rut(){
            if (!this.residente.rut){
                return ''
            }else{
                return this.formatearRut(this.residente.rut)
            }
        }
    },
    methods:{
        formatearRut(rut){
            rut = rut.replace(/[^0-9]/g, '').replace(/^(\d{1,2})(\d{3})(\d{3})(\w{1})$/, '$1.$2.$3-$4')
            return rut
        },
    }
}
</script>