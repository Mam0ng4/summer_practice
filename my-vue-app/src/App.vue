<template>
  <div id="app">
    <AppHeader />
    <main>
      <router-view :cart="cart" @add-to-cart="addToCart" />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      cart: [],
    };
  },
  methods: {
    addToCart(product) {
      this.cart.push(product);
    },
  },
};
</script>

<style>
body {
  background-color: #ffe4b5;
}

#app {
  background-color: #ffe4b5;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 90px;
  margin-bottom: 90px;
}
</style>
