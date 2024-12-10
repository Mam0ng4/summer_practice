<!-- src/views/ShoppingCart.vue -->
<template>
  <div>
    <AppHeader />
    <h2>Корзина</h2>
    <!-- Контент корзины -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from '../components/AppHeader.vue';
import AppFooter from '../components/AppFooter.vue';

export default {
  name: 'ShoppingCart',
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>