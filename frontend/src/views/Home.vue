<template>
  <v-container fluid class="pa-0" fill-height>
    <v-layout column>
      <v-flex>
        <!-- 캐러셀 -->
        <carousels />
      </v-flex>

      <v-flex>
        <!-- 코로나 현재 상태 -->
        <main-state />
      </v-flex>

      <v-flex>
        <!-- 페이지 소개 -->
        <introduce />
      </v-flex>

      <v-flex>
        <!-- 뉴스 카드 -->
        <news-area />
      </v-flex>
        
    </v-layout>
  </v-container>
</template>

<script>
import Carousels from '../components/Main/Carousels'
import MainState from '../components/Main/MainState'
import Introduce from '../components/Main/Introduce'
import NewsArea from '../components/Main/NewsArea'

export default {
  components: {
    Carousels,
    MainState,
    Introduce,
    NewsArea,
  }
};
</script>