import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  data: () => ({
    chartdata: {
      labels: ['January', 'February', 'April', 'May', 'June'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: ['#f87979','#f87900','#d10101','#f80101','#f82222'],
          data: [40, 35, 30, 20, 55]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}