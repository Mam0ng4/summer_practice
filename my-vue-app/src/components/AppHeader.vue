<template>
  <header class="app-header">
    <router-link to="/">
      <img src="@/assets/logo1.png" alt="logo" class="logo" />
      <h1>STRING&SOUND</h1>
    </router-link>
    <nav>
      <router-link to="/">Главная страница</router-link>
      <router-link to="/cart">Корзина</router-link>
      <router-link to="/about">О нас</router-link>
    </nav>
    <div class="contact-info">
      <div class="email">📧 string_sound@gmail.com</div>
      <div class="phone">📞 +7 999-123-45-67</div>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
};
</script>

<style scoped>
.app-header {
  color: #ffe4b5;
  display: flex;
  align-items: center;
  background-color: #334f63;
  color: white;
  border-radius: 10px;
  position: fixed;
  top: 0;
  width: 97.3%;
  padding: 10px 20px;
  z-index: 1000;
  justify-content: space-between;
}
.logo-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: inherit;
}
.logo {
  height: 50px;
  margin-right: 10px;
}
nav {
  display: flex;
  gap: 20px;
}
nav a {
  color: #ffe4b5;
  text-decoration: none;
  font-size: 26px;
  font-weight: bolder;
}
.contact-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  font-size: 16px;
}
.email,
.phone {
  margin: 2px 0;
}
h1 {
  margin: 0;
  font-size: 24px;
  background-color: #1dbfbb;
  border-radius: 10px;
  color: #334f63;
}
@media (max-width: 768px) {
  .app-header {
    flex-direction: column;
    align-items: flex-start;
  }
  nav {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    margin-top: 10px;
  }
  .contact-info {
    align-items: flex-start;
    font-size: 14px;
  }
}
</style>
