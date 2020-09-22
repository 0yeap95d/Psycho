<template>
  <v-container class="mt-5" fill-height>

    <v-flex class="md8">
      <KakaoMap></KakaoMap>
    </v-flex>

    <v-flex>
      <v-card-text class="text-center">
      <p class="display-3 pa-2">🍜</p>
      <p class="display-2 pa-5">코딩도 식후경</p>
      <v-btn large color="blue lighten-1 white--text ma-5" rounded to="/search">검색하기</v-btn>
      </v-card-text>
      <Graph></Graph>
      <Graph></Graph>
    </v-flex>
    
    
  </v-container>
</template>

<script>
import KakaoMap from '../components/KakaoMap'
import Graph from '../components/Graph'
export default {
  components: { 
    KakaoMap,
    Graph,
  }
};
</script>