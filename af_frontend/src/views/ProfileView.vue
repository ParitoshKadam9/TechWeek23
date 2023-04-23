<template>
                                                    <div class="profile">
                                                      <img src="../assets/profile.png" />
                                                      <div class="all">
                                                          <div class="row"><h3 >User Name: {{ this.$store.state.user.u_name }}</h3></div>
                                                          <div class="row"><h3 > BITS ID:{{ this.$store.state.user.bits_id }}</h3></div>
                                                            <div class="row"><h3 > Full Name: {{ this.$store.state.user.full_name }}</h3></div>
                                                          <div class="row"><h3 >Date Created: {{ this.$store.state.user.created }}</h3></div>
        
                                                      </div>
                                                    </div>
  </template>
  
<script>
export default {
    name: "ProfileView",
};
</script>
  
<style>
img {
    border-radius: 50%;
    size: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 10%;
    margin-top: 50px;
}

.all {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
}

.row {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    color: white;
}

.row button {
    background-color: yellow;
    padding: 10px 70px 10px 70px;
    border-radius: 10px;
    cursor: pointer;
}

.row1 {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 20vh
}
</style>