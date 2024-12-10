<!-- src/views/ProductDetail.vue -->
<template>
  <div>
    <AppHeader />
    <h2>Детали продукта</h2>
    <!-- Контент страницы продукта -->
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

export default {
  name: "ProductDetail",
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>
