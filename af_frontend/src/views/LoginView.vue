<template>
  <div class="login">
          <div class="text">Login</div>
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

<style>
.login{
  color: white;
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
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
.login p{
  color: white;
}
.login button {
  width: 320px;
  height: 40px;
  margin-left: auto;
  margin-right: auto;
  background: steelblue;
  border-color: 1px solid steelblue;
  color: white;
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
