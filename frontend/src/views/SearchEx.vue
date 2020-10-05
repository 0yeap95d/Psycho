<template>
  <div
    v-infinite-scroll="loadMore"
    infinite-scroll-disabled="loading"
    infinite-scroll-distance="10"
    style="max-height: 1000px"
    class="overflow-y-auto"
  >
    <v-container fill-height fluid grid-list-xl>
      <v-layout justify-center wrap mt-5>
        <v-flex xs12 md8>
          <card title="맛집 검색">
            <v-form>
              <v-container py-0>
                <v-layout wrap>
                  <v-flex xs12 md12>
                    <v-text-field v-model="storeName" label="음식점 이름" />
                  </v-flex>
                  <v-flex xs12 text-center>
                    <v-btn
                      large
                      class="indigo white--text ma-5"
                      rounded
                      color="blue lighten-1"
                      @click="onSubmit"
                    >GO!</v-btn>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-form>
          </card>
          <v-divider class="mx-4" />
        </v-flex>

        <v-flex xs12 md8>
          <v-flex v-for="store in stores" :key="store.id" pa-4>
            <store-list-card
              :id="store.id"
              :name="store.name"
              :categories="store.categories"
              :address="store.address"
              :tel="store.tel"
            />
          </v-flex>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import Card from "@/components/Card";
import StoreListCard from "@/components/StoreListCard";
import { mapState, mapActions } from "vuex";
// import RequestApi from "../api/api"

export default {
  components: {
    Card,
    StoreListCard,
    // RequestApi,
  },
  data: () => ({
    storeName: "",
    loading: true,
    windowHeight: window.innerHeight,
  }),
  computed: {
    ...mapState({
      stores: state => state.data.storeSearchList,
      page: state => state.data.storeSearchPage
    })
  },
  methods: {
    ...mapActions("data", ["getStores"]),
    onSubmit: async function() {
      console.log("onSubmit");
      // const params = {
      //   name: this.storeName,
      //   page: 1,
      //   append: false
      // };
      // await this.getStores(params);
      // this.loading = false;
      // await RequestApi.requestStore(
      //   (res) => {
      //     console.log(res);
      //   },
      //   (error) => {
      //     console.log(error);
      //   }
      // )
    },
    loadMore: async function() {
      console.log("loadMore");
      this.loading = true;
      const params = {
        name: this.storeName,
        page: this.page,
        append: true
      };
      await this.getStores(params);
      setTimeout(() => {
        this.loading = false;
      }, 1000);
    }
  }
};
</script>
