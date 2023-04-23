<template>
    <div class="boxx">
        <div class="form">
            <div class="header">Add Question</div>
            <div class="title"><input class="communityTitle" placeholder="Question Title" v-model="title" /></div>
            <div class="answer">
                <textarea class="anserInput" placeholder="Your Question here" v-model="value"></textarea>
            </div>
            <div class="Submit" @click="handleSubmit()">
                Submit
            </div>
        </div>

    </div>
</template>
<script>
import { mapActions } from 'vuex';

export default {
    name: "AddQuestion",
    data() {
        return {
            value: "",
            title: '',
        }
    },
    methods: {
        ...mapActions({
            CreateQuestion: 'CreateQuestion'
        }),
        handleSubmit() {
            let formData = {
                'uid': this.$store.state.user.uid,
                'title': this.title,
                'value': this.value,
                'cid': this.$store.state.community.cid
            }
            this.CreateQuestion(formData)
        }
    }
}
</script>
<style scoped>
.header {
    font-size: 3vh;
    color: black;
    margin-bottom: 2vh;
}

.communityTitle {
    border: 1px solid gray;
    border-radius: 5px;
    background-color: #303030;
    color: gray;
    font-size: 2.5vh;
    height: 3vh;
    width: 76vh;
    padding: 10px;
    font-size: 2.6vh;
    /* margin-top: 10vh; */
    transition: 0.2s;
}

.boxx {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.form {
    width: 90vh;
    height: 55vh;
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

.QuestionID {
    font-size: 3vh;
    font-family: 'Montserrat', sans-serif;
    margin-top: 5vh;
}

.Submit {
    margin-top: 2vh;
    width: fit-content;
    height: fit-content;
    padding: 1vh;
    font-size: 2.4vh;
    background: rgb(176, 176, 31);
    color: black;
    border: 1px solid black;
    cursor: pointer;
    border-radius: 5px;
    font-family: 'Montserrat', sans-serif;
    transition: 0.1s;
}

.Submit:hover {
    background: #404040;
    color: rgb(176, 176, 31);
}
</style>