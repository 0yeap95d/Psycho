<template>
  <v-app-bar color="white" id="app-toolbar" elevation="0">
    <v-spacer v-if="!responsive" />

    <v-toolbar-title @click="goSearchPage('home')">싸이코</v-toolbar-title>
    <div v-if="!responsive" class="ml-5 mt-1">싸우자 이기자 코로나</div>

    <v-spacer />

    <v-app-bar-nav-icon
      v-if="responsive"
      @click.stop="onClickDrawer"
    ></v-app-bar-nav-icon>

    <v-layout v-if="!responsive" justify-end>
      <v-menu>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="gray"
            depressed
            width="300px"
            left
            v-bind="attrs"
            v-on="on"
          >
            {{ searchItem }}
          </v-btn>
        </template>

        <v-list>
          <v-list-item v-for="(item, i) in items" :key="i">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn text color="gray" @click="goSearchPage('search')">
        <span>지도 검색</span>
      </v-btn>

      <v-btn text color="gray" @click="goSearchPage('statistic')">
        <span>해시태그</span>
      </v-btn>
    </v-layout>

    <v-spacer v-if="!responsive" />
  </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  data: () => ({
    responsive: false,
    searchItem: "",
    interval: {},
    items: [
      { title: "COVID-19" },
      { title: "무섭다" },
      { title: "언제끝나" },
      { title: "Amazing 2020" },
      { title: "COVID-19" },
      { title: "무섭다 무섭다 무섭다 무섭다" },
      { title: "언제끝나" },
      { title: "Amazing 2020" },
      { title: "COVID-19" },
      { title: "무섭다" },
      { title: "언제끝나" },
      { title: "Amazing 2020" },
    ],
  }),
  computed: {
    ...mapState("app", ["drawer"]),
  },
  mounted() {
    this.onResponsiveInverted();
    this.changeSearchItem();
    window.addEventListener("resize", this.onResponsiveInverted);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResponsiveInverted);
  },

  methods: {
    ...mapMutations("app", ["setDrawer"]),
    onClickDrawer() {
      this.setDrawer(!this.drawer);
    },
    onResponsiveInverted() {
      if (window.innerWidth < 900) {
        this.responsive = true;
      } else {
        this.responsive = false;
      }
    },
    changeSearchItem() {
      let itemNum = 1;
      this.interval = setInterval(() => {
        if (itemNum === 11) {
          return (itemNum = 1);
        }
        let word = this.items[itemNum].title;
        if (word.length > 8) word = word.slice(0, 8) + "...";

        // console.log(word);

        this.searchItem = itemNum + ". " + word;
        itemNum += 1;
      }, 2000);
    },
    goSearchPage(page) {
      this.$router.push(page);
    },
  },
};
</script>
