<template>
  <v-container fluid class="pa-0" fill-height>
    <v-layout column>
      <v-flex>
        <!-- 캐러셀 -->
        <Carousels></Carousels>
      </v-flex>

      <v-flex class="green lighten-3 pa-5">
        <!-- 전일 대비 동향 -->
        <v-layout column class="white lighten-4 pa-5" fill-height>
          
          <v-flex>
            전일 대비 동향
          </v-flex>

          <v-flex text-center class="white lighten-4 pa-5">
            <v-layout row>
              <v-flex><v-spacer /></v-flex>
              <v-flex><testCard></testCard></v-flex>
              <v-flex><testCard></testCard></v-flex>
              <v-flex><testCard></testCard></v-flex>
              <v-flex><testCard></testCard></v-flex>
              <v-flex><v-spacer /></v-flex>
            </v-layout>
            
          </v-flex>
        </v-layout>
      </v-flex>

      <v-flex>
        <v-parallax
          dark
          src="https://picsum.photos/1920/1080?random"
        >
          <v-row
            align="center"
            justify="center"
          >
            <v-col class="text-center" cols="12">
              <h1 class="display-1 font-weight-thin mb-4">Vuetify.js</h1>
              <h4 class="subheading">Build your application today!</h4>
            </v-col>
          </v-row>
        </v-parallax>
      </v-flex>

      <v-flex class="ma-10">
        <v-layout row>
          <v-flex>
            <v-spacer />
          </v-flex>

          <v-flex>
            <!-- 뉴스 카드 리스트 -->
            뉴스
            <v-divider class="mb-5" ></v-divider>
            <news-card></news-card>
            <news-card></news-card>
            <news-card></news-card>
            <news-card></news-card>
          </v-flex>
          <v-divider class="mx-4" vertical></v-divider>
          <v-flex>
            <!-- 코로나 관련 통계 차트 -->
            차트
            <v-divider class="mb-5" ></v-divider>
            <RandomChart></RandomChart>
            <RandomChart></RandomChart>
            <RandomChart></RandomChart>
          </v-flex>
          <v-flex>
            <v-spacer />
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex>
          <word-cloud></word-cloud>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// import KakaoMap from '../components/KakaoMap'
import Carousels from '../components/Carousels'
import NewsCard from '../components/NewsCard'
import Graph from '../components/Graph'
import Search from './Search'
import RandomChart from '../components/Chart/RandomChart'
import testCard from '../components/testCard'
import WordCloud from '../components/WordCloud'

export default {
  components: {
    Carousels,
    NewsCard,
    // KakaoMap,
    Graph,
    Search,
    RandomChart,
    testCard,
    WordCloud,
  }
};
</script>