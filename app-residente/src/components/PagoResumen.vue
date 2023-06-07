<template>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body text-center">
            <h4 class="card-title">Pago confirmado</h4>
            <p class="card-text">¡El pago ha sido confirmado con éxito</p>
            <p class="card-text">Monto cancelado {{ estado_pago.amount }}</p>
            <p class="card-text">Orden de compra: {{ estado_pago.buy_order }}</p>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default{
    props:{
        estado_pago: Object,
    }
}
</script>

<style>
.card {
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-top: 50px;
  padding: 20px;
}
</style>
