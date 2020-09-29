<template>
  <v-container fluid class="pa-0" fill-height>
    <v-layout column>
      <v-flex>
        <navbar></navbar>
      </v-flex>
      <v-flex>
        <v-layout row>
          <v-flex class="Map">
            <kakao-map></kakao-map>
          </v-flex>

          <v-flex>
            <span>hello world</span>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import KakaoMap from "@/components/KakaoMap";
import Navbar from "@/components/Search/Navbar";

export default {
  components: {
    KakaoMap,
    Navbar,
  },
  data: () => ({
    windowWidth: window.innerWidth,
  }),
  computed: {},
  methods: {},
};
</script>

<style>
.container {
  width: 100%;
  margin: 0;
  padding: 0;
}
.Map {
  width: 50%;
}
</style>
