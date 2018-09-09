<template>
    <div :id="chartsName" style="width: 150px;height:150px;">

    </div>
</template>

<script>
import echarts from 'echarts'
export default {
  props:{
      chartsName: String,
      score: Number
  },
  computed: {
    color () {
      if (this.score >= 75 ) return '#096DD9';
      else if (this.score >= 50) return '#389E0D'
      else if (this.score >= 25) return '#D48806'
      else return '#A8061A'
    }
  },
  mounted() {
    const charts = echarts.init(document.getElementById(this.chartsName));
    var option = {
      series: [
        {
          name:'得分',
          type:'pie',
          radius: ['50%', '70%'],
          avoidLabelOverlap: false,
          color: [`${this.color}55`,`${this.color}FF`],
          label: {
              normal: {
                  show: true,
                  position: 'center',
                  fontSize: '26',
              }
          },
          labelLine: {
              normal: {
                  show: false
              }
          },
          data:[
              {value:100-this.score},
              {value:this.score, name:`${this.score}分`},
          ]
        }
      ]
    };
    charts.setOption(option);
  }
}
</script>
