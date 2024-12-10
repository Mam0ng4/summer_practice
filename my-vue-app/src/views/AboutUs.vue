<template>
  <AppHeader />
  <main class="about">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card class="text-card">
            <h1>О нас</h1>
            <div class="text-row">
              <v-card-text class="text-block">
                <p>
                  Добро пожаловать в STRING&SOUND SHOP! Мы специализируемся на
                  продаже музыкальных инструментов и аксессуаров. Наша цель —
                  предоставить клиентам качественные товары и профессиональное
                  обслуживание. Мы предлагаем широкий ассортимент гитар,
                  барабанов, укулеле, синтезаторов, аксессуаров и других
                  музыкальных инструментов.
                </p>
              </v-card-text>
              <v-card-text class="text-block">
                <p>
                  В нашем магазине вы найдете как инструменты для начинающих,
                  так и для профессионалов. Наши консультанты всегда готовы
                  помочь вам с выбором инструмента и ответить на все ваши
                  вопросы.
                </p>
              </v-card-text>
            </div>
            <v-card-text class="text-center">
              <p>Спасибо, что выбрали STRING&SOUND SHOP!</p>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </main>
  <AppFooter />
</template>

<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
export default {
  name: "AboutUs",
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style scoped>
.about {
  padding: 20px;
}
.text-card {
  padding: 20px;
}
.text-row {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 20px;
}
.text-block {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-size: 22px;
}
.text-center {
  padding: 20px;
  border-radius: 10px;
  font-size: 22px;
  text-align: center;
}
@media (min-width: 769px) {
  .text-row {
    flex-direction: row;
    justify-content: space-between;
  }
  .text-block {
    width: 48%;
  }
  .text-center {
    width: 100%;
  }
}
</style>
