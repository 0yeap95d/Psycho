import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  data:() => ({
    chartData: {
    datasets: [
      {
        label: 'red1',
        backgroundColor: '#ff0000',
        data: [40, 20, 30]
      },
      {
        label: 'red2',
        backgroundColor: '#000000',
        data: [40, 15, 30]
      },
      {
        label: 'red3',
        backgroundColor: '#ff00dd',
        data: [40, 5, 5]
      }
    ],
    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
  }
}),
  props: ['options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}