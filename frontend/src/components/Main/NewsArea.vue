<template>
  <v-card class="pa-5">
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :display="3"
      :width="windowWidth - 300"
      :height="windowHeight"
    >
      <slide v-for="(slide, i) in slides" :key="i" :index="i">
        <figure>
          <v-layout column>
            <v-flex class="news-publisher">네이버 뉴스</v-flex>
            <v-divider class="mx-6 black"></v-divider>
            <v-layout row>

                <v-flex xs6>
                  <v-layout column>
                  <v-flex class="news-title">日 지바롯데, 코로나19 집단 감염…선수 8명 등 13명 확진(종합)</v-flex>
                  <img class="MainArticle" src="https://picsum.photos/1920/1080?random"/>
                  <div class="news-contents">일본프로야구 지바 롯데 말린스에서 신종 코로나바이러스 감염증(코로나19)이 확산하고 있다. 일본 스포츠전문매체 '닛칸스포츠'는 6일 내야수 도리타니 다카시를 포함해 지바 롯데에서 총 11명의 코로나19 신규...</div>
                  </v-layout>
                </v-flex>
                <v-flex xs6>
                  <v-layout column>
                  <div class="Article2">
                  <img class="SubArticle" src="https://picsum.photos/1920/1080?random" align="left"/>
                  <span class="Sub-title">코로나19 신규 확진자 75명…엿새째 두 자릿수</span>
                  <div class="Sub-contents">5일 코로나19 신규 확진자가 75명 발생해 엿새째 두 자릿수를 유지했다. 중앙방역대책본부(방대본)는 이날 0시 기준으로 코로나19 국내 발생 신규 확진자는 66명, 국외유입 사례는 9명이라고 밝혔다. 이에 따른...</div>
                  </div>
                  <div class="Article2">
                  <img class="SubArticle" src="https://picsum.photos/1920/1080?random" align="left" />
                  <span class="Sub-title">'코로나 대출' 받은 소상공인, 셋 중 한명은 끼워팔기 당해</span>
                  <div class="Sub-contents">현행법 안 어기는 선에서 신용카드·보험 등 끼워팔아 전북·우리·하나은행, 끼워팔기 비율 50% 웃돌기도 시중은행이 신종 코로나 바이러스 감염증(코로나19) 사태로 어려움을 겪는 소상공인에게 대출을 하면서...</div>
                  </div>
                  </v-layout>
                </v-flex>
              
            </v-layout>
            
          </v-layout>
          <figcaption>
            (샌프란시스코=연합뉴스) 정성호 특파원
          </figcaption>
        </figure>
      </slide>
    </carousel-3d>
  </v-card>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  data() {
    return {
      windowWidth: window.innerWidth,
      windowHeight: window.innerHeight,
      slides: 7,
    };
  },
  components: {
    Carousel3d,
    Slide,
  },
};
</script>

<style>
.carousel-3d-container figure {
  margin: 0;
  height: 80%;
}

.carousel-3d-container figure .MainArticle {
  width: 85%;
  height: 350px;
  float: left;
  margin: 20px auto;
} 

.carousel-3d-container figure .SubArticle {
  width: 40%;
  height: 200px;
  float: left;
  margin: 10px 20px;
} 

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  text-align: right;
  box-sizing: border-box;
}

.carousel-3d-slide {
  max-height: 98%;
  background-color: #f0f0f0;
  box-shadow: 10px 10px 0px #e0e0e0,
            10.5px 9.5px 0px black,
            9.5px 10.5px 0px black;
  }

.news-publisher {
  font-size: 30px;
  margin: 20px;
}

.news-title {
  text-align: center;
  font-size: 20px;
  margin: 10px;
}

.Sub-title {
  text-align: center;
  font-size: 15pt;
  width: 150px;
  margin-top: 20px;
}

.news-contents {
  font-size: 12pt;
  margin: 20px 30px;
}
.Sub-contents {
  font-size: 12pt;
  margin-top: 30px;
}
.Article2 {
  padding: 20px 30px 40px 0;
}
</style>
