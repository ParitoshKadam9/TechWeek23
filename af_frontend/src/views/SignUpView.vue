<template>
  <div class="signup">
    <div class="SignupText">SignUp</div>
    <input type="text" placeholder="Enter BITSID" v-model="bits_id" required />
    <input
      type="text"
      placeholder="Enter Username"
      v-model="username"
      required
    />
    <input
      type="password"
      placeholder="Enter Password"
      v-model="password"
      required
    />
    <input
      type="text"
      placeholder="Enter Full Name"
      v-model="full_name"
      required
    />
      <input
        type="email"
        placeholder="Enter Email"
        v-model="email"
        required
      />
      <div>
      <button @click="Signup">Sign Up</button>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  name: "SignUpView",
  data() {
    return {
      bits_id: "",
      username: "",
      password: "",
      full_name: "",
      email: "",
    };
  },
  methods: {
    ...mapActions({
      SignUpUser: 'SignUpUser'
    }),

    Signup() {
      this.SignUpUser({
        'bits_id': this.bits_id,
        'u_name': this.username,
        'pwd': this.password,
        'full_name': this.full_name,
        'email': this.email
      })
      this.$router.push({ name: 'HomeView' })
    },
  },
};
</script>

<style>
.SignupText{
    color: black;
  font-size: 4vh;
}
.signup input {
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

.signup button {
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

.signup h1 {
  margin-top: 150px;
}

.signup{
  color: white;
  margin-top: 8vh;
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
</style>
