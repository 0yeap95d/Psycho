<template>
  <div id="ChartForm">
    <corona-total-chart v-bind:data="data" />
    <input id="startDate" v-model="startDate" type="date" />
    <input id="endDate" v-model="endDate" type="date" />
    <button @click="getChart">확인</button>
  </div>
</template>

<script>
import CoronaTotalChart from "./CoronaTotalChart";

export default {
  components: {
    CoronaTotalChart,
  },
  data: () => {
    return {
      startDate: null,
      endDate: null,
      data: null,
    };
  },
  mounted() {
    this.startDate = this.getFormatDate(new Date());
    this.endDate = this.getFormatDate(new Date());
    this.getChart();
  },
  methods: {
    getFormatDate(date) {
      var year = date.getFullYear();
      var month = 1 + date.getMonth();
      month = month >= 10 ? month : "0" + month;
      var day = date.getDate();
      day = day >= 10 ? day : "0" + day;
      return year + "-" + month + "-" + day;
    },
    getChart() {
      let s = this.startDate.split("-");
      let e = this.endDate.split("-");
      this.data = {
        syear: s[0] * 1,
        smonth: s[1] * 1,
        sday: s[2] * 1,
        eyear: e[0] * 1,
        emonth: e[1] * 1,
        eday: e[2] * 1,
      };
      console.log(this.data);
    },
  },
};
/*
요청 json 형식
{
    "syear": 2020, //시작년도
    "smonth": 9, //시작월
    "sday": 4, //시작일
    "eyear": 2020, //끝년도
    "emonth": 9, //끝월
    "eday": 4, //끝일
}
*/
</script>

<style scoped>
#ChartForm {
  border: 1px solid gray;
}
</style>