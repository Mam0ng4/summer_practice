import { createStore } from "vuex";

export default createStore({
  state: {
    cart: [],
  },
  mutations: {
    ADD_TO_CART(state, product) {
      state.cart.push(product);
    },
    clearCart(state) {
      state.cart = [];
    },
    removeFromCart(state, guitarName) {
      state.cart = state.cart.filter((item) => item.guitar_name !== guitarName);
    },
  },
  actions: {
    addToCart({ commit }, product) {
      commit("ADD_TO_CART", product);
    },
  },
  getters: {
    cartItems: (state) => state.cart,
    cartTotal: (state) =>
      state.cart.reduce((total, item) => total + item.price, 0),
  },
});
