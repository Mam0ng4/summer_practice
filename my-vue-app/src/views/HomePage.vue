<template>
  <div>
    <AppHeader />
    <main class="home-page">
      <p1>Добро пожаловать в</p1>
      <p>STRING&SOUND SHOP</p>
      <ProductList :products="sortedProducts" />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import ProductList from "../components/ProductList.vue";

export default {
  name: "HomePage",
  components: {
    AppHeader,
    AppFooter,
    ProductList,
  },
  data() {
    return {
      products: [], // Ваши товары из базы данных
      sortedProducts: [], // Отсортированные товары
    };
  },
  methods: {
    sortByPrice() {
      this.sortedProducts = this.products
        .slice()
        .sort((a, b) => a.price - b.price);
    },
    sortByAlphabet() {
      this.sortedProducts = this.products
        .slice()
        .sort((a, b) => a.name.localeCompare(b.name));
    },
  },
  mounted() {
    // Загрузка товаров из базы данных (вы можете использовать AJAX запрос или какой-либо другой метод для получения данных)
    this.products = [
      // Ваши товары из базы данных
    ];
    this.sortedProducts = [...this.products]; // Инициализация отсортированных товаров
  },
};
</script>

<style scoped>
.home-page {
  padding: 20px;
  text-align: center;
}
p {
  font-size: 48px;
  font-weight: bold;
}
p1 {
  font-size: 34px;
  font-weight: bold;
}
.sort-buttons {
  margin: 20px 0;
}
.sort-buttons button {
  padding: 10px 20px;
  margin: 5px;
  font-size: 16px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
}
.sort-buttons button:hover {
  background-color: #0056b3;
}
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}
.product-item {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  transition: transform 0.3s;
}
.product-item:hover {
  transform: scale(1.05);
}
.product-item img {
  width: 100px;
  height: auto;
  border-radius: 10px;
}
@media (max-width: 768px) {
  .product-item {
    width: 100%;
  }
}
</style>
