<template>
    <div class="all">
        <div class="CommunityHeader">
                                                <div class="name">{{ this.$store.state.community.title }}</div>
                                                <div class="id">#{{ this.$store.state.community.description }}</div>
                                            </div>
                                        </div>
                                        <!-- <AddCommunity/> -->
                                        <div class="questions">
                                            <div class="upper">
                                                <div class="QuestionHeader">Questions :</div>
                                                <div class="listQuestions" v-for="question in this.$store.state.question.questions" :key="question.id">
                                                    <div v-if="question.cid == this.$store.state.community.cid">
                                                        <RouterLink to="/question" @click="this.$store.commit('setNewViewQuestion', question.id)">
                                                            <QuestionBox v-bind:question="question.value" v-bind:date="question.created" v-bind:likes="question.likes" :qid="question.id"/>
                                                        </RouterLink>
                                            
                                                    </div>
                                                </div>

                                            </div>
                                            <div class="CreateCommunity">
                                                    <div class="button" @click="this.addq = !this.addq">+ Ask a Question</div>
                                                    <div v-if="addq" >
                                                        <AddQuestion></AddQuestion> 
                                                    </div>
                                                </div>
                                        </div>
</template>
<script>
// import AddCommunity from "@/components/AddCommunity.vue";
import AddQuestion from '@/components/AddQuestion.vue'
import { mapActions } from "vuex";
import QuestionBox from "../components/QuestionBox.vue";
export default {
    name: "CommunityView",
    components: {
        AddQuestion,
        QuestionBox
    },
    data() {
        return {
            addq: false
        };
    },
    methods: {
        ...mapActions({
            GetQuestions: 'GetQuestions'
        })
    },
    mounted() {
        this.GetQuestions();
    }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    .all{
        margin-left: auto;
        margin-right: auto;
        /* width: 100vh; */
    }
    .QuestionHeader{
        font-size: 3.2vh;
        margin-top:5vh ;
        border-bottom: 1px solid rgb(176, 176, 31);
        width: fit-content;
        color: gray;
        margin-bottom: 2vh;
    }
    .questions{
    margin-left: auto;
    margin-right: auto;
transform: translateX(-5vh);
        width: 130vh;
display: flex;
flex-direction: column;
justify-content: center;
        /* align-items: center; */
    }
    .CommunityHeader{
        width: 130vh;
        margin-top: 2vh;
        height: 15vh;
        margin-left: auto;
        margin-right: auto;
        background: rgb(176, 176, 31);
        border-radius: 5px;
        display: flex;
        flex-direction: row;
        align-items :end;
        justify-content: space-between;
        padding: 5vh;
        cursor: pointer;
        color: Black;
        transition: 0.1s;
    }
    .button {
    min-width: 20vh;
    cursor: pointer;
    padding: 1.5vh;
    color: white;
    font-size: 2.5vh;
    margin-top: 5vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 5vh;
    border-radius: 5px;
    justify-content: center;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background: rgb(176, 176, 31);
    transition: 0.1s ease-in;
}
    .name{
        font-size: 6vh;
    }
    .id{
        margin: 0 5vh 0 0 ;
            font-family: 'Montserrat', sans-serif;
    }
</style>