<template>
    <div class="boxx">
        <div class="form">
        <div class="QuestionID">
                       Question ID :  #{{ qid }}
                    </div>
                    <div class="answer">
                        <textarea class="anserInput" placeholder="Type Answer here" v-model="this.value"></textarea>
                    </div>
                    <div class="Submit" @click="handleSubmit()">
                        Submit
                    </div>
                    </div>
                </div>
</template>
<script scoped>
export default {
    name: "AddAnswer",
    props: {
        qid: Number
    },
    data() {
        return {
            value: ''
        }
    },
    methods: {
        handleSubmit() {
            let formData = {
                'value': this.value,
                'uid': this.$store.state.user.uid,
                'qid': this.qid
            }
            this.$store.dispatch('CreateAnswer', formData)
        }
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    .boxx{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .form{
        width: 90vh;
        height: 45vh;
        display: flex;
        border-radius: 5px;
        flex-direction: column;
        align-items: center;
        background: rgb(176, 176, 31);
    }
    textarea {
  width: 80vh;
  height: 25vh;
  margin-top: 2vh;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #303030;
  border-radius: 4px;
  background-color: #303030;
  font-size: 2.2vh;
  color: white;
  resize: none;
}
    .QuestionID{
        font-size: 3vh;
        font-family: 'Montserrat', sans-serif;
        margin-top: 5vh;
    }
    .Submit{
        margin-top: 2vh;
        width: fit-content;
        height: fit-content;
        padding: 1vh;
        font-size: 2.4vh;
        background: rgb(176, 176, 31);
        color: black;
        border: 1px solid black;
        cursor: pointer;
        border-radius: 5px;        font-family: 'Montserrat', sans-serif;
        transition: 0.1s;
    }
    .Submit:hover{
        background: #404040;
        color: rgb(176, 176, 31);
    }
</style>