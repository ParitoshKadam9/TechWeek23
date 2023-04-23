<template>
  <div class="login">
          <div class="loginText">Login</div>
                <input placeholder="Enter Username" v-model="u_name" />
                <input type="password" placeholder="Enter Password" v-model="pwd" />
                <div><button @click="login">Submit</button></div>
  
                <p>
                  <router-link to="signup" class="tag">New User? Sign Up </router-link>
                </p>
              </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: "LoginView",
  data() {
    return {
      u_name: "",
      pwd: "",
    };
  },
  methods: {
    ...mapActions({
      GetUsers: 'GetUsers',
      LogInUser: 'LogInUser'
    }),

    login() {
      this.LogInUser({ 'u_name': this.u_name, 'pwd': this.pwd })
      this.$router.push({ name: 'HomeView' })
    },
  },
  mounted() {
    this.GetUsers();
  }
};
</script>

<style scoped>
.login{
  color: white;
  margin-top: 20vh;
  display: flex;
  width: 70vh;
  flex-direction: column;
  align-items: center;
  background: rgb(176, 176, 31);
  padding: 3vh;
  padding-top: 7vh;
  border-radius:10px ;
  margin-left: auto;
  margin-RIGHT: auto;
}
.loginText{
  color: black;
  font-size: 4vh;
}
.login input {
  width: 40VH;
  height: 40px;
  display: block;
  padding-left: 20px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  margin-top: 20px;
  border: 1px solid rgb(0, 0, 0);
  border-radius: 5px;
  background: #393939;
  font-size: 2.2vh;
  color: white;
}
.login p{
  color: white;
}
.login button {
  width:20vh;
  height: 40px;
  border-radius: 5px;
  margin-left: auto;
  margin-right: auto;
  background:inherit;
  border: 1px solid rgb(0, 0, 0);
  color: black;
  font-size: 2.3vh;
  cursor: pointer;
}

.tag {
  text-decoration: none;
  color: black;
}

.login h1 {
  margin-top: 150px;
}

</style>
