<template>
  <div>
    <AppHeader />
    <main class="cart-page">
      <h1>Корзина</h1>
      <div v-if="cart.length > 0">
        <div v-for="item in cart" :key="item.guitar_id" class="cart-item">
          <img :src="item.image_url" :alt="item.guitar_name" />
          <div>
            <h2>{{ item.guitar_name }}</h2>
            <p>Цена: {{ formatPrice(item.price) }} руб.</p>
            <button @click="removeFromCart(item.guitar_name)">Удалить</button>
          </div>
        </div>
        <h2>Итоговая сумма: {{ totalPrice.toFixed(2) }} руб.</h2>
        <button @click="clearCart">Очистить корзину</button>
        <form @submit.prevent="submitOrder">
          <h3>Оформление заказа</h3>
          <div>
            <label for="firstName">Имя:</label>
            <input
              type="text"
              id="firstName"
              v-model="orderForm.first_name"
              required
            />
          </div>
          <div>
            <label for="lastName">Фамилия:</label>
            <input
              type="text"
              id="lastName"
              v-model="orderForm.last_name"
              required
            />
          </div>
          <div>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="orderForm.email" required />
          </div>
          <button type="submit">Оформить заказ</button>
        </form>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      </div>
      <div v-else>
        <p>Ваша корзина пуста.</p>
      </div>
    </main>
    <AppFooter />
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue"; // Исправление пути

export default {
  name: "CartPage",
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      orderForm: {
        first_name: "",
        last_name: "",
        email: "",
      },
      errorMessage: "",
    };
  },
  computed: {
    ...mapState(["cart"]),
    totalPrice() {
      return this.cart.reduce(
        (total, item) => total + parseFloat(item.price),
        0
      );
    },
  },
  methods: {
    ...mapMutations(["removeFromCart", "clearCart"]),
    removeFromCart(guitarName) {
      this.$store.commit("removeFromCart", guitarName);
    },
    clearCart() {
      this.$store.commit("clearCart");
    },
    formatPrice(price) {
      return parseFloat(price).toFixed(2);
    },
    async submitOrder() {
      const orderData = {
        first_name: this.orderForm.first_name,
        last_name: this.orderForm.last_name,
        email: this.orderForm.email,
        total_price: this.totalPrice,
        items: this.cart.map((item) => ({
          guitar_id: item.guitar_id,
          quantity: 1,
        })),
      };
      try {
        const response = await axios.post(
          "http://localhost:8000/simple_orders/",
          orderData
        );
        console.log("Order created:", response.data);
        this.clearCart();
        this.errorMessage = "";
        // Редирект на страницу успешного заказа
        this.$router.push("/order-success");
      } catch (error) {
        console.error("Error creating order:", error.response.data);
        this.errorMessage = `Заказ успешно создан`;
      }
    },
  },
};
</script>

<style scoped>
.cart-page {
  padding: 20px;
}
.cart-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  justify-content: center;

  padding: 10px;
  border-radius: 10px;
  width: 100%;
}
.cart-item img {
  width: 80px;
  height: auto;
  margin-right: 20px;
  border-radius: 10px;
}
.item-details {
  flex-grow: 1;
}
.item-details h2 {
  font-size: 1.2em;
  margin: 0 0 10px;
}
.item-details p {
  margin: 0 0 10px;
}
.clear-cart,
.submit-order {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 20px 0;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}
.clear-cart:hover,
.submit-order:hover {
  background-color: #0056b3;
}
form {
  margin-top: 20px;
}
form div {
  margin-bottom: 10px;
}
form label {
  display: block;
  margin-bottom: 5px;
}
form input {
  width: calc(35% - 20px);
  padding: 10px;
  border: 3px solid #ddd;
  border-radius: 10px;
}
.error-message {
  color: red;
  margin-top: 10px;
}
button {
  font-size: 18px;
  border-radius: 10px;
  transition: transform 0.3s ease;
}
button:hover {
  transform: scale(1.05);
}
@media (max-width: 768px) {
  .cart-item {
    flex-direction: column;
    align-items: center;
  }
  .cart-item img {
    width: 100%;
    margin-bottom: 10px;
  }
  .item-details {
    text-align: center;
  }
}
</style>
