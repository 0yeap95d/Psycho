<template>
  <v-container fluid class="pa-0 search-container" fill-height>
    <v-layout column>
      <v-flex>
        <navbar></navbar>
      </v-flex>
      <v-flex>
        <v-layout row>

          <!-- 카카오 맵-->
          <v-flex class="map">
            <kakao-map :storeList="hotels"></kakao-map>
          </v-flex>

          <v-flex class="search">
            <v-layout column justify-center wrap mt-5>
                <!-- 검색 창 -->
                <v-flex xs12 md8>
                  <card title="맛집 검색">
                    <v-form>
                      <v-container py-0>
                        <v-layout wrap>
                          <v-flex xs12 md12>
                            <v-text-field label="음식점 이름" />
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

                <!-- 검색 결과 -->
                <v-flex
                  xs12 md8
                  v-infinite-scroll="loadMore"
                  infinite-scroll-disabled="loading"
                  infinite-scroll-distance="10"
                  style="max-height: 800px"
                  class="overflow-y-auto">

                  <v-flex v-for="hotel in hotels" :key="hotel.id" pa-4>
                    <store-list-card
                      :id="hotel.id"
                      :name="hotel.name"
                      :address="hotel.address1"
                      :tel="hotel.tel"
                    />
                  </v-flex>

                </v-flex>
            </v-layout>
          </v-flex>

          <v-flex
            v-infinite-scroll="loadMore"
            infinite-scroll-disabled="loading"
            infinite-scroll-distance="10"
            class="overflow-y-auto search">
            
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import KakaoMap from "@/components/KakaoMap";
import Navbar from "@/components/Search/Navbar";
import Card from "@/components/Card";
import StoreListCard from "@/components/StoreListCard";
import HotelApi from "@/api/HotelApi";
import StoreApi from "@/api/StoreApi";

export default {
  components: {
    KakaoMap,
    Navbar,
    Card,
    StoreListCard,
  },
  data: () => ({
    windowWidth: window.innerWidth,
    windowHeight: window.innerHeight,
    hotels: [],
  }),
  computed: {},
  methods: {
    onSubmit: async function() {
      console.log("onSubmit");
      await StoreApi.requestRecStore(
        (res) => {
          console.log(res);
        },
        (error) => {
          console.log(error);
        }
      )
      // await HotelApi.requestHotel(
      //   (res) => {
      //     this.hotels = res.data;
      //     console.log(this.hotels);
      //   },
      //   (error) => {
      //     console.log(error);
      //   }
      // )
    },

    loadMore: async function() {
      console.log("loadMore");
      // this.loading = true;
      // const params = {
      //   name: this.storeName,
      //   page: this.page,
      //   append: true
      // };
      // await this.getStores(params);
      // setTimeout(() => {
      //   this.loading = false;
      // }, 1000);
    }
  },
};
</script>

<style>
.search-container {
  width: 100%;
  margin: 0;
  padding: 0;
}
.map {
  width: 65%;
}
.search {
  width: 35%;
}
</style>
