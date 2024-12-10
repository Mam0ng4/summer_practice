import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import ProductDetail from "../views/ProductDetail.vue";
import CartPage from "../views/CartPage.vue";
import AboutUs from "../views/AboutUs.vue";

const routes = [
  { path: "/", name: "HomePage", component: HomePage },
  { path: "/product/:id", name: "ProductDetail", component: ProductDetail },
  {
    path: "/cart",
    name: "CartPage",
    component: CartPage,
    props: (route) => ({ cart: route.params.cart }),
  },
  { path: "/about", name: "AboutUs", component: AboutUs },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
