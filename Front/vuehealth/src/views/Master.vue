<template>
    <!-- Section Header -->
    <header-section></header-section>


    <router-view></router-view>

    <!-- Section Header -->
    <footer-section></footer-section> 
</template>

<script>
import HeaderSection from '../components/frontend/Header.vue'
import FooterSection from '../components/frontend/Footer.vue'

export default {
  name: 'Master',
  // Composants enfants
  components:{
    HeaderSection, FooterSection
  },
}
</script>
  
<style lang="scss" scoped>
</style>
