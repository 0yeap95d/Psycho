<template>
  <v-container fluid class="pa-0 search-container" fill-height>
    <v-layout column>
      <v-flex>
        <navbar></navbar>
      </v-flex>
      <v-flex>
        <v-layout row>
          <v-flex xs8 class="Map">
            <kakao-map></kakao-map>
          </v-flex>

          <v-flex xs4 style="background-color: #fce8e8;">
            <!-- 들어가야 하는 정보: 성별, 나이, 필요없는 기타 정보 -->
            <div class="container">
              <form @submit.prevent="submitForm">
                <img src="../assets/location.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectCity">
                  <option disabled value="">도시입력</option>
                  <option>서울특별시</option><option>부산광역시</option>
                  <option>대구광역시</option><option>인천광역시</option>
                  <option>광주광역시</option><option>대전광역시</option>
                  <option>울산광역시</option><option>세종특별자치시</option>
                  <option>경기도</option><option>강원도</option>
                  <option>충청북도</option><option>충청남도</option>
                  <option>전라북도</option><option>전라남도</option>
                  <option>경상북도</option><option>경상남도</option>
                  <option>제주특별자치도</option>
                  </select>
                </span>
                <img src="../assets/age.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectAge">
                  <option disabled value="">나이입력</option>
                  <option>10대</option>
                  <option>20대</option>
                  <option>30대</option>
                  <option>40대</option>
                  <option>50대</option>
                  <option>60대</option>
                  <option>70대</option>
                  <option>80대</option>
                  <option>90대</option>
                  </select>
                </span>
                <img src="../assets/sex.png" height="17px" width="17px">&nbsp;
                <span class="Info">
                  <select v-model="selectSex">
                  <option disabled value="">성별입력</option>
                  <option>남자</option>
                  <option>여자</option>
                  </select>
                </span>
                <!-- <button type="submit">추천을 받아볼까나..?</button> -->
                
              </form>
            </div>
            <!--  -->
            <card>
            <v-form>
              <v-container py-0>
                <v-layout wrap>
                  <v-flex xs12 md12>
                    <div md6 style="text-align: center; font-family:Maple; font-size:17pt;">
                      당신은?!&nbsp;{{ selectCity }}&nbsp;{{ selectAge }}&nbsp;{{ selectSex }}
                    </div>
                  </v-flex>
                  <br><br>
                  <v-flex xs12 text-center>
                    <!-- <v-btn
                      rounded
                      text color="#f08c8c"
                      @click="onSubmit"
                    >내가 가야만 한다면 이 글을 눌러서 추천</v-btn> -->
                    <div v-if="this.selectCity==='' || this.selectAge==='' || this.selectSex===''">
                        <div style="background-color: #f08c8c; padding:10px; 
                        border-radius: 10px; color: white; font-family:Maple; font-size:20pt;">
                        선택해야 추천받을 수 있어~</div> 
                    </div>
                    <div v-else> 
                        <button type="submit" style="background-color: #f08c8c; padding:10px; 
                        border-radius: 10px; color: white; font-family:Maple; font-size:20pt; outline:none;">
                        추천을 받아볼까나..?</button>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-form>
          </card>
          <v-divider class="mx-4" />
          <!-- 장식용 -->
          <v-list three-line style="max-height: calc(100vh - 280px);background-color: #fce8e8" class="overflow-y-auto">
          <v-list-item v-for="n in 50" :key="n">
          <v-card style="width:100%;">
            <v-card-text class="text-center">
              <p class="display-1 font-weight-bold">식당{{n}}</p>
              <p class="subtitle-1 font-italic">맛있는 밥집, 맛있는 술집</p>
            </v-card-text>
            <v-footer color="white">
              <v-col class="text-center">
                <span class="grey--text caption font-italic">부산광역시 동구 수정동 / 📞 051-xxx-xxxx</span>
              </v-col>
            </v-footer>
          </v-card>
          </v-list-item>
          </v-list>
          <!-- 장식용 -->
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

export default {
  components: {
    KakaoMap,
    Navbar,
    Card
  },
  data: () => ({
    selectSex: "",
    selectAge: "",
    selectCity: ""
  }),
  computed: {},
  methods: {},
};
</script>

<style>
@font-face { 
    font-family: 'Maple'; 
    src: url(../assets/font/Maplestory_Bold.ttf) format('truetype')
		,url(../assets/font/Maplestory_Light.ttf) format('truetype'); 
}
body{-ms-overflow-style:none; }
body::-webkit-scrollbar { display:none; }
select:focus {
  outline: none;
	box-shadow: none;
}
option {
  text-align: center;
}
select {
  width: 25%;
  color: #505050;
  font-family: "Maple";
  text-align: center;
  margin: 0 auto;
}
.search-container {
  width: 100%;
  margin: 0;
  padding: 0;
}
.Map {
  width: 50%;
}
</style>
