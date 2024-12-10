<template>
  <div
    class="product-item"
    @mouseover="hover = true"
    @mouseleave="hover = false"
  >
    <img :src="product.image_url" alt="Product Image" />
    <h2>{{ product.guitar_name }}</h2>
    <p>{{ product.description }}</p>
    <p>Цена: {{ product.price }} руб.</p>
    <p>Производитель: {{ product.manufacturer }}</p>
    <p>Страна происхождения: {{ product.country_of_origin }}</p>
    <p>Год производства: {{ product.year_of_production }}</p>
    <p v-if="product.in_stock">В наличии</p>
    <p v-else>Нет в наличии</p>
    <button @click="addToCart(product)" :disabled="!product.in_stock">
      Добавить в корзину
    </button>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "ProductItem",
  props: {
    product: Object,
  },
  data() {
    return {
      hover: false,
    };
  },
  methods: {
    ...mapActions(["addToCart"]),
  },
};
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
.product-item {
  width: 350px;
  border: 1px solid #ddd;
  border-radius: 20px;
  padding: 20px;
  text-align: center;
  transition: transform 0.3s ease;
  background-color: white;
}

.product-item:hover {
  transform: scale(0.9);
}

.product-item img {
  max-width: 100%;
  border-radius: 10px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:enabled {
  background-color: #0056b3;
}
</style>
