<template>
  <div class="spisok">
    <select v-model="selectedSort" @change="sortProducts">
      <option value="price_asc">Цена (по возрастанию)</option>
      <option value="price_desc">Цена (по убыванию)</option>
      <option value="alphabet_asc">Алфавит (A-Z)</option>
      <option value="alphabet_desc">Алфавит (Z-A)</option>
    </select>
    <div class="product-list">
      <ProductItem
        v-for="product in sortedProducts"
        :key="product.guitar_id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductItem from "./ProductItem.vue";

export default {
  name: "ProductList",
  components: {
    ProductItem,
  },
  data() {
    return {
      products: [],
      sortedProducts: [],
      selectedSort: "price_asc",
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get("http://localhost:8000/guitars/");
        this.products = response.data;
        this.sortProducts();
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    },
    sortProducts() {
      switch (this.selectedSort) {
        case "price_asc":
          this.sortedProducts = [...this.products].sort(
            (a, b) => a.price - b.price
          );
          break;
        case "price_desc":
          this.sortedProducts = [...this.products].sort(
            (a, b) => b.price - a.price
          );
          break;
        case "alphabet_asc":
          this.sortedProducts = [...this.products].sort((a, b) =>
            a.guitar_name.localeCompare(b.guitar_name)
          );
          break;
        case "alphabet_desc":
          this.sortedProducts = [...this.products].sort((a, b) =>
            b.guitar_name.localeCompare(a.guitar_name)
          );
          break;
        default:
          this.sortedProducts = [...this.products];
          break;
      }
    },
  },
};
</script>

<style scoped>
select {
  transition: transform 0.3s ease;
  background-color: #ffe4b5;
  border-radius: 20px;
  font-size: 20px;
  border-width: 4px;
  border-color: #2c3e50;
}
select:hover {
  transform: scale(1.1);
}
.product-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
</style>
