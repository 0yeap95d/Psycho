import { Bar } from "vue-chartjs"
import CoronaApi from "../../api/CoronaApi"

export default {
  extends: Bar,
  data: () => ({
    chartdata: {
      labels: [],
      datasets: [
        {
          label: "누적 확진자",
          backgroundColor: "#111111",
          data: [],
        },
        {
          label: "누적 격리해제",
          backgroundColor: "#555555",
          data: [],
        },
        {
          label: "누적 사망자",
          backgroundColor: "#999999",
          data: [],
        },
      ],
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
    },
  }),
  computed() {
    // let data = {
    //   syear: 2020,
    //   smonth: 9,
    //   sday: 6,
    //   eyear: 2020,
    //   emonth: 9,
    //   eday: 6,
    // }
    // this.getDatasets(data)
    this.getDatasets(this.data)
  },
  props: ["data"],
  methods: {
    getDatasets: async function(data) {
      await CoronaApi.requestCorona(
        data,
        (res) => {
          this.chartdata.labels = []
          this.chartdata.datasets[0].data = []
          this.chartdata.datasets[1].data = []
          this.chartdata.datasets[2].data = []
          for (var i = 0; i < res.data.length; i++) {
            this.chartdata.labels.push(res.data[i].stateDt)
            this.chartdata.datasets[0].data.push(res.data[i].decideCnt)
            this.chartdata.datasets[1].data.push(res.data[i].clearCnt)
            this.chartdata.datasets[2].data.push(res.data[i].deathCnt)
          }
          this.renderChart(this.chartdata, this.options)
        },
        (error) => {
          console.log(error)
        }
      )
    },
  },
}
