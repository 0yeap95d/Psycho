import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: ['options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}