<template>
    <option value="{{ espacio.id }}">{{ espacio.descripcion }}</option>
</template>

<script>

export default{
    name: 'EspacioE',
    props:{
        espacio: Object,
    },
}
</script>