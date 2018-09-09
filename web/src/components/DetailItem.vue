<template>
    <div class="detail-item" :style="`background: ${color}`">
        <div class="item-left-bg">
            <div class="item-icon">
            <img :src="icon" alt="icon"/>
            </div>
            <div class="item-content" >
            <div class="item-title">{{title}}</div>
            <div class="item-data">休息比：90%</div>
            </div>
        </div>

        <div class="item-desc">
            <!-- <img src="@/assets/img/right-water.png" alt=""> -->
            <div class="up-desc">{{updesc}}</div>
            <div class="down-desc">{{downdesc}}</div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DetailItem",
    data() {
        return {}
    },
    props: {
        title: String,
        color: String,
        icon: String,
        updesc: String,
        downdesc: String
    }
}
</script>

<style lang="stylus" scoped>
.detail-item {
    margin: 10px auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 90%;
    height:60px;
    box-shadow:0px 2px 4px 0px rgba(0,0,0,0.1);
    border-radius:10px;
    overflow: hidden;
    color: white;
    .item-left-bg {
      background: rgba(255,255,255,0.3);
      width : 65%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 100%;
      box-shadow:0px 2px 4px 0px rgba(0,0,0,0.1);
      border-radius:10px;
      padding: 0 5%;
    }
    .item-icon {
      width: 17%;
      img{
        width: 100%;
        height: auto;
      }
    }
    .item-content {
      width: 70%
    }
    .item-desc {
      width: 35%;
      img{
        width: 100%;
        height: 100%;
      }
      div{
        color: white;
        &.up-desc{
          top: 25%;
        }
        &.down-desc{
          bottom: 25%;
        }
      }
    }
  }
</style>

