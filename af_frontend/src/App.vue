<template>
  <div class="Headers">
    <div class="header">Ni69ers</div>
  </div>
<!-- <LandingPage/> -->
<CommunitiesBox/>
<CommunitiesBox/>
</template>
    
<script>
let x = document.cookies
console.log(x) 
import CommunitiesBox from './components/CommunitiesBox.vue';
// import LandingPage from './components/LandingPage.vue';
export default {
  components: {
    // LandingPage
    CommunitiesBox
  }
}
   
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.Headers{
width: 100vw;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
}
.header{
  font-size: 3vh;
font-family: 'Montserrat', sans-serif;  color: gray;
  margin-top: 2vh;
}

body{
  background: rgb(36, 36, 36);
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  overflow-y: auto;
}
/* width */
::-webkit-scrollbar {
  width: 7px;
}

/* Track */
::-webkit-scrollbar-track {
  background: rgb(49, 49, 49); 
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #606060; 
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555; 
}

.login input {
  width: 300px;
  height: 40px;
  display: block;
  padding-left: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  margin-top: 20px;
  border: 1px solid steelblue;
}

.login button {
  width: 320px;
  height: 40px;
  background: steelblue;
  border-color: 1px solid steelblue;
  color: white;
  cursor: pointer;
}
</style>
