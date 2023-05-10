<template>
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <!-- Brand/logo -->
    <a class="navbar-brand">Mi Condominio</a>
    
    <!-- Links -->
    <ul class="navbar-nav">
        <li class="nav-item">
        <a class="nav-link" @click="showReservas()">Reservas</a>
        </li>
    </ul>
    </nav>
</template>

<script>
export default{
    name: 'Nav-bar',
    methods: {
    // Muestra el listado de reservas
    showReservas(){
        this.$emit('toggle-reservas')
    }
}
}
</script>