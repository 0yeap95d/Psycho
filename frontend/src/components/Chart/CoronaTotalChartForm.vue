<template>
  <div id="ChartForm">
    <corona-total-chart :chart-data="ChartData" />
    <input id="startDate" v-model="startDate" type="date" />
    <input id="endDate" v-model="endDate" type="date" />
    <button @click="getChart">확인</button>
  </div>
</template>

<script>
import CoronaTotalChart from "./CoronaTotalChart";
import CoronaApi from "../../api/CoronaApi";

export default {
  components: {
    CoronaTotalChart,
  },
  data: () => {
    return {
      startDate: null,
      endDate: null,
      data: null,
      ChartData: {
        labels: [],
        datasets: [
          {
            label: "누적 확진자",
            backgroundColor: "#FF5555",
            data: [],
          },
          {
            label: "누적 격리해제",
            backgroundColor: "#55FF55",
            data: [],
          },
          {
            label: "누적 사망자",
            backgroundColor: "#5555FF",
            data: [],
          },
        ],
      },
    };
  },
  mounted() {
    // this.startDate = this.getFormatDate(new Date());
    // this.endDate = this.getFormatDate(new Date());
    this.startDate = this.getFormatDate(new Date("2020-07-01"));
    this.endDate = this.getFormatDate(new Date("2020-09-01"));
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
      this.getDatasets(this.data);
      this.getDatasets(this.data);
    },
    getDatasets(data) {
      CoronaApi.requestCorona(
        data,
        (res) => {
          this.ChartData.labels = [];
          this.ChartData.datasets[0].data = [];
          this.ChartData.datasets[1].data = [];
          this.ChartData.datasets[2].data = [];
          for (var i = 0; i < res.data.length; i++) {
            this.ChartData.labels.push(res.data[i].stateDt);
            this.ChartData.datasets[0].data.push(res.data[i].decideCnt);
            this.ChartData.datasets[1].data.push(res.data[i].clearCnt);
            this.ChartData.datasets[2].data.push(res.data[i].deathCnt);
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
    // getDatasets: async function (data) {
    //   await CoronaApi.requestCorona(
    //     data,
    //     (res) => {
    //       this.ChartData.labels = [];
    //       this.ChartData.datasets[0].data = [];
    //       this.ChartData.datasets[1].data = [];
    //       this.ChartData.datasets[2].data = [];
    //       for (var i = 0; i < res.data.length; i++) {
    //         this.ChartData.labels.push(res.data[i].stateDt);
    //         this.ChartData.datasets[0].data.push(res.data[i].decideCnt);
    //         this.ChartData.datasets[1].data.push(res.data[i].clearCnt);
    //         this.ChartData.datasets[2].data.push(res.data[i].deathCnt);
    //       }
    //     },
    //     (error) => {
    //       console.log(error);
    //     }
    //   );
    // },
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